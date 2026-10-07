import google.generativeai as genai

# Gemini API ကို ချိတ်ဆက်ခြင်း (API Key ထည့်ရန်)
GOOGLE_API_KEY = "Ab8RN6KMzlcuV87qZWIaJWdeNOGH_9L3YSbSInNyRL0OdWVCGw"
genai.configure(api_key=GOOGLE_API_KEY)

def generate_burmese_recap(movie_synopsis):
    """
    ရုပ်ရှင်ဇာတ်လမ်းအနှစ်ချုပ်ကို အခြေခံ၍ မြန်မာဇာတ်ညွှန်းထုတ်ပေးခြင်း
    """
    prompt = f"""
    အောက်ပါ ရုပ်ရှင်ဇာတ်လမ်းအနှစ်ချုပ်ကို အခြေခံ၍ Movie Recap (ရုပ်ရှင်ပြန်လည်သုံးသပ်ချက်) ဗီဒီယိုများတွင် အသုံးပြုရန် စိတ်ဝင်စားစရာကောင်းသော အသံထွက်ဟန်ဖြင့် မြန်မာလို ဇာတ်ညွှန်းတစ်ခုကို ရေးသားပေးပါ။
    
    ဇာတ်လမ်းအနှစ်ချုပ်: {movie_synopsis}
    """
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
