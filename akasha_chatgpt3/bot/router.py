from bot.chat_logic import get_reply

def smart_reply(message):
    """
    يستلم الرسالة من AKASHA_app.py ويوجهها للمنطق.
    """
    if not message:
        return "من فضلك أرسل رسالة واضحة."
    
    # استدعاء المنطق للحصول على الرد
    response = get_reply(message)
    return response