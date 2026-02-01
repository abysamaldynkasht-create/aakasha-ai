from bot.faq import faq_data
from bot.gemini_api import ask_gemini

def get_reply(user_text):
    """
    يقرر مصدر الرد بناءً على مدخلات المستخدم.
    """
    # تحويل النص لـ lowercase (اختياري) وتجهيزه
    user_text = user_text.strip()

    # 1. البحث في قاعدة بيانات الأسئلة الشائعة (FAQ)
    # بنجرب نبحث عن النص كما هو
    if user_text in faq_data:
        return faq_data[user_text]
    
    # 2. إذا لم يجد إجابة في الـ FAQ، نستخدم Gemini API
    try:
        gemini_response = ask_gemini(user_text)
        return gemini_response
    except Exception as e:
        return f"عذراً يا Akasha AI، واجهت مشكلة في التفكير: {str(e)}"