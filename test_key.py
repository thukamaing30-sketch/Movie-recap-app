import google.generativeai as genai

# ကိုယ့်ရဲ့ API Key ကို ဒီနေရာမှာ " " အထဲသို့ ထည့်ပေးပါ
GOOGLE_API_KEY = "Ab8RN6KMzlcuV87qZWIaJWdeNOGH_9L3YSbSInNyRL0OdWVCGw"

# API Key ချိတ်ဆက်ခြင်း
genai.configure(api_key=GOOGLE_API_KEY)

try:
    # Gemini မော်ဒယ်ကို ခေါ်ပြီး စမ်းသပ်ခြင်း
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hello! Say 'API Key works successfully' if you receive this.")
    
    print("ရလဒ် - ", response.text)
    print("အောင်မြင်ပါသည်! သင့်ရဲ့ API Key အလုပ်လုပ်နေပါပြီ။")

except Exception as e:
    print("အမှားအယွင်း ဖြစ်ပေါ်နေပါသည် - ", e)
