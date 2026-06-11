from flask import Blueprint, request, jsonify
from core.gemini.gemini_client import GeminiClient
from core.memory.conversation_manager import ConversationManager
from config.logging_config import logger
chat_bp = Blueprint("chat", __name__)

gemini = GeminiClient()

memory = ConversationManager()
@chat_bp.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.json

        prompt = data.get("message")

        logger.info(f"User Query: {prompt}")

        response = gemini.ask(prompt)

        logger.info("Gemini response generated successfully")

        memory.save_conversation(
            prompt,
            response
        )

        logger.info("Conversation saved to database")

        return jsonify({
            "success": True,
            "response": response
        })

    except Exception as e:

        logger.error(f"Error: {str(e)}")

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500