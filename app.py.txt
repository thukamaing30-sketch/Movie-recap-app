import streamlit as st
import openai
import os
from pathlib import Path

# App ရဲ့ ခေါင်းစဉ်နှင့် ပုံစံ
st.set_page_title_co = st.set_page_config(page_title="AI Movie Recap Generator", layout="centered")

st.title("🎬 AI Movie Recap & Voiceover Generator")
st.write("ဗီဒီယိုဖိုင် သို့မဟုတ် ဇာတ်လမ်းအချက်အလက်ကို ထည့်သွင်းရုံဖြင့် AI က ဇာတ်ညွှန်းနှင့် အသံထွက်ကို အလိုအလျောက် ဖန်တီးပေးမည်။")

# API Keys ထည့်သွင်းရန် နေရာ (Sidebar ဘက်တွင် ထည့်ရန်)
st.sidebar.header("🔑 API Keys ထည့်ရန်")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
elevenlabs_api_key = st.sidebar.text_input("ElevenLabs API Key", type="password")

# အသုံးပြုသူ တင်မည့် နေရာ
uploaded_file = st.file_uploader("ဇာတ်ကား ဗီဒီယိုဖိုင်ကို တင်ပါ (MP4 format)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("🚀 Movie Recap စတင်ဖန်တီးမည်"):
        if not openai_api_key:
            st.error("ကျေးဇူးပြု၍ OpenAI API Key ကို အရင်ထည့်ပါ။")
        else:
            with st.spinner("AI မှ ဇာတ်လမ်းကို စစ်ဆေးနေသည်... ဇာတ်ညွှန်းရေးနေပါပြီ။"):
                try:
                    # OpenAI API ချိတ်ဆက်ခြင်း
                    client = openai.OpenAI(api_key=openai_api_key)
                    
                    # AI ကနေ ဇာတ်ညွှန်းထုတ်ပေးခြင်း (Mock prompt for demonstration)
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a professional movie recap scriptwriter for TikTok and YouTube. Write an engaging, fast-paced recap script."},
                            {"role": "user", "content": "ဒီဗီဒီယိုအတွက် စိတ်ဝင်စားစရာကောင်းတဲ့ TikTok Movie Recap ဇာတ်ညွှန်းတစ်ခုကို မြန်မာလို ရေးပေးပါ။"}
                        ]
                    )
                    
                    script_result = response.choices[0].message.content
                    
                    st.success("ဇာတ်ညွှန်း အောင်မြင်စွာ ထွက်ရှိလာပါပြီ!")
                    st.subheader("📝 ထွက်လာသော ဇာတ်ညွှန်း (Script):")
                    st.write(script_result)
                    
                except Exception as e:
                    st.error(f"အမှားအယွင်းရှိနေပါသည်: {e}")
