import os
import google.generativeai as genai

# قراءة المفتاح من إعدادات السيرفر بشكل سري (Environment Variable)
# تأكد إنك سميت المتغير في Render باسم GEMINI_API_KEY
API_KEY = os.environ.get("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("⚠️ تحذير: لم يتم العثور على مفتاح API. تأكد من ضبط GEMINI_API_KEY في إعدادات Render.")

def get_working_model():
    """بتفتش الموديل الشغال في حسابك عشان نتفادى خطأ 404"""
    try:
        if not API_KEY:
            return None
            
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # الأولوية لـ flash لأنه سريع
        for m in available_models:
            if 'gemini-1.5-flash' in m:
                return m
        return available_models[0] if available_models else None
    except Exception as e:
        print(f"خطأ أثناء جلب الموديلات: {e}")
        return "models/gemini-1.5-flash" # خيار احتياطي

# نختار الموديل المتاح
selected_model_name = get_working_model()

if selected_model_name:
    model = genai.GenerativeModel(selected_model_name)
    print(f"--- تم الربط بنجاح باستخدام موديل: {selected_model_name} ---")
else:
    model = None
    print("--- للأسف ما لقيت أي موديل متاح أو المفتاح غير مضبوط ---")

def ask_gemini(prompt):
    if not model:
        return "عذراً يا Akasha AI، نظام الذكاء الاصطناعي غير متصل حالياً. تأكد من إعدادات المفتاح السري."
        
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"حصل خطأ أثناء معالجة الطلب: {str(e)}"