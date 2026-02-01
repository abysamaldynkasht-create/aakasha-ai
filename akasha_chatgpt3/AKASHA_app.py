from flask import Flask, render_template, request, jsonify
# استدعاء الموجه (router) من مجلد bot
from bot.router import smart_reply 

app = Flask(__name__)

@app.route('/')
def index():
    # بيفتح صفحة النجوم والدردشة اللي عملناها
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        user_message = data.get("message")
        
        # الربط الحقيقي: بنرسل الرسالة لملف الراوتر في مجلد bot
        bot_response = smart_reply(user_message)
        
        return jsonify({"reply": bot_response})
    except Exception as e:
        return jsonify({"reply": f"عذراً يا Akasha AI، حصل خطأ: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)