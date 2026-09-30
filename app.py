import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Movie Recap Generator")
st.title("🎬 Movie Recap ဖန်တီးပေးမည်")

gemini_api_key = os.environ.get("GEMINI_API_KEY")

uploaded_file = st.file_uploader("ဇာတ်ကား ဗီဒီယိုဖိုင်ကို တင်ပါ (MP4 format)", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)

if st.button("🚀 Movie Recap စတင်ဖန်တီးမည်"):
    if not gemini_api_key:
        st.error("ကျေးဇူးပြု၍ Render ၏ Environment Variables ထဲတွင် GEMINI_API_KEY ထည့်သွင်းပါ။")
    else:
        with st.spinner("AI မှ ဇာတ်ညွှန်းရေးနေပြီ..."):
            try:
                genai.configure(api_key=gemini_api_key)
                
                # အဆင်ပြေနိုင်မယ့် မော်ဒယ်နာမည်များကို စာရင်းပြုစုထားခြင်း
                models_to_try = ["gemini-3.8-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-pro"]
                response = None
                success = False
                last_error = None
                
                for m_name in models_to_try:
                    try:
                        model = genai.GenerativeModel(m_name)
                        response = model.generate_content("You are a professional movie recap scriptwriter. ဒီဗီဒီယိုအတွက် ဇာတ်လမ်းအကျဉ်း ဇာတ်ညွှန်း ရေးပေးပါ။")
                        success = True
                        break
                    except Exception as err:
                        last_error = err
                        continue
                
                if success and response:
                    st.success("ဇာတ်ညွှန်း အောင်မြင်စွာ ထွက်ရှိလာပါပြီ!")
                    st.write(response.text)
                else:
                    st.error(f"အမှားအယွင်းရှိနေပါသည်။ မော်ဒယ်များအားလုံး ချိတ်ဆက်၍ မရပါ: {last_error}")
                    
            except Exception as e:
                st.error(f"အမှားအယွင်းရှိနေပါသည်။ {e}")
