from flask import Flask
from api.research_routes import research_bp
from api.chat_routes import chat_bp
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(
    chat_bp,
    url_prefix="/api"
)
app.register_blueprint(
    research_bp,
    url_prefix="/api"
)
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "JARVIS AI OS",
        "version": "1.0.0"
    })

@app.route("/")
def home():
    return "JARVIS AI OS Running"

if __name__ == "__main__":
    app.run(
        debug=True
    )