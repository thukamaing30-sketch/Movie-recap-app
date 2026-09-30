import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Movie Recap Generator")
st.title("🎬 Movie Recap ဖန်တီးပေးမည်")

# Render မှ API Key ကို တိုက်ရိုက်ယူခြင်း
openai_api_key = os.environ.get("OPENAI_API_KEY")

uploaded_file = st.file_uploader("ဇာတ်ကား ဗီဒီယိုဖိုင်ကို တင်ပါ (MP4 format)", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)

if st.button("🚀 Movie Recap စတင်ဖန်တီးမည်"):
    if not openai_api_key:
        st.error("ကျေးဇူးပြု၍ Render ၏ Environment Variables ထဲတွင် OpenAI API Key ထည့်သွင်းပါ။")
    else:
        with st.spinner("AI မှ ဇာတ်ညွှန်းရေးနေပြီ..."):
            try:
                client = OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional movie recap scriptwriter."},
                        {"role": "user", "content": "ဒီဗီဒီယိုအတွက် ဇာတ်လမ်းအကျဉ်း ဇာတ်ညွှန်း ရေးပေးပါ။"}
                    ]
                )
                st.success("ဇာတ်ညွှန်း အောင်မြင်စွာ ထွက်ရှိလာပါပြီ!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"အမှားအယွင်းရှိနေပါသည်။ {e}")
