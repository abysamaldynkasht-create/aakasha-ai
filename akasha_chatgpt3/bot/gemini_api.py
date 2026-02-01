import google.generativeai as genai

# خت مفتاحك هنا
API_KEY = "AIzaSyAUoTRa6HdtZ2VoK4u-0sryfu-ql6yNSwg"
genai.configure(api_key=API_KEY)

def get_working_model():
    """بتفتش الموديل الشغال في حسابك عشان نتفادى خطأ 404"""
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # الأولية لـ flash لأنه سريع، لو مافي بنشيل أي واحد شغال
    for m in available_models:
        if 'gemini-1.5-flash' in m:
            return m
    return available_models[0] if available_models else None

# نختار الموديل المتاح
selected_model_name = get_working_model()

if selected_model_name:
    model = genai.GenerativeModel(selected_model_name)
    print(f"--- تم الربط بنجاح باستخدام موديل: {selected_model_name} ---")
else:
    print("--- للأسف ما لقيت أي موديل متاح في حسابك ---")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"حصل خطأ: {str(e)}"