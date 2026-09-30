import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Movie Recap Generator")
st.title("🎬 Movie Recap ဖန်တီးပေးမည်")

# Render မှ Gemini API Key ကို ယူခြင်း
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
                
                # မော်ဒယ်အမည်ကို အမှန်ကန်ဆုံး ခေါ်ယူခြင်း
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                response = model.generate_content("You are a professional movie recap scriptwriter. ဒီဗီဒီယိုအတွက် ဇာတ်လမ်းအကျဉ်း ဇာတ်ညွှန်း ရေးပေးပါ။")
                
                st.success("ဇာတ်ညွှန်း အောင်မြင်စွာ ထွက်ရှိလာပါပြီ!")
                st.write(response.text)
            except Exception as e:
                st.error(f"အမှားအယွင်းရှိနေပါသည်။ {e}")
