import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Movie Recap Generator")
st.title("🎬 YouTube Movie Recap မြန်မာလို ဘာသာပြန်မည်")

gemini_api_key = os.environ.get("GEMINI_API_KEY")

# ဗီဒီယိုဖိုင် တင်ရန်
uploaded_file = st.file_uploader("YouTube မှ ဒေါင်းလုပ်လုပ်ထားသော ဗီဒီယိုဖိုင်ကို တင်ပါ (MP4 format)", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    # ယာယီဖိုင်အဖြစ် သိမ်းဆည်းရန်
    video_path = "temp_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

if st.button("🚀 ဗီဒီယိုကို မြန်မာလို ဘာသာပြန်ပြီး ဇာတ်ညွှန်းထုတ်မည်"):
    if not gemini_api_key:
        st.error("ကျေးဇူးပြု၍ Render ၏ Environment Variables ထဲတွင် GEMINI_API_KEY ထည့်သွင်းပါ။")
    elif uploaded_file is None:
        st.error("ကျေးဇူးပြု၍ ပထမဆုံး ဗီဒီယိုဖိုင် တင်ပေးပါ။")
    else:
        with st.spinner("AI မှ ဗီဒီယိုကို ဖတ်ရှု၍ မြန်မာလို ဘာသာပြန်နေပါပြီ... ခဏစောင့်ပေးပါ..."):
            try:
                genai.configure(api_key=gemini_api_key)
                
                # Gemini သို့ ဗီဒီယိုဖိုင်ကို Upload လုပ်ခြင်း
                st.info("ဗီဒီယိုဖိုင်ကို AI ဆီသို့ ပို့ဆောင်နေပါပြီ...")
                video_file = genai.upload_file(path=video_path)
                
                # ဖိုင်အဆင်သင့်ဖြစ်သည်အထိ စောင့်ဆိုင်းခြင်း
                import time
                while video_file.state.name == "PROCESSING":
                    time.sleep(2)
                    video_file = genai.get_file(video_file.name)
                
                if video_file.state.name == "FAILED":
                    raise ValueError("ဗီဒီယိုဖိုင် လုပ်ဆောင်မှု မအောင်မြင်ပါ။")
                
                # အလုပ်လုပ်မည့် မော်ဒယ်ကို ရွေးချယ်ခြင်း
                models_to_try = ["gemini-3.8-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
                response = None
                success = False
                
                prompt = (
                    "You are a professional movie recap scriptwriter and translator. "
                    "ဒီဗီဒီယိုဖိုင်ထဲက အကြောင်းအရာများကို အစအဆုံး နားထောင်/ကြည့်ရှုပြီး "
                    "ပရိသတ် စိတ်ဝင်စားမယ့် ပုံစံမျိုးနဲ့ မြန်မာလို အသေးစိတ် ဇာတ်လမ်းအကျဉ်း (Movie Recap) ဇာတ်ညွှန်း ရေးပေးပါ။ "
                    "ဘာသာပြန်ဆိုရာတွင် သဘာဝကျပြီး နားထောင်လို့ကောင်းအောင် ရေးပေးပါ။"
                )
                
                for m_name in models_to_try:
                    try:
                        model = genai.GenerativeModel(m_name)
                        response = model.generate_content([video_file, prompt])
                        success = True
                        break
                    except Exception:
                        continue
                
                if success and response:
                    st.success("✨ မြန်မာလို ဇာတ်ညွှန်းနှင့် ဘာသာပြန် အောင်မြင်စွာ ထွက်ရှိလာပါပြီ!")
                    st.write(response.text)
                else:
                    st.error("ဇာတ်ညွှန်းထုတ်ယူရာတွင် အမှားအယွင်းရှိသွားပါသည်။")
                    
                # ယာယီဖိုင်ကို ဖျက်ရန်
                if os.path.exists(video_path):
                    os.remove(video_path)
                    
            except Exception as e:
                st.error(f"အမှားအယွင်းရှိနေပါသည်။ {e}")
