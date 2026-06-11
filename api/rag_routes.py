from flask import Blueprint, request, jsonify
from flask import Response
import json

from core.rag.rag_service import RAGService

rag_bp = Blueprint(
    "rag",
    __name__
)

rag_service = RAGService()


@rag_bp.route("/rag/ask", methods=["POST"])
def ask_document():

    try:

        data = request.json

        question = data.get("question")

        if not question:

            return jsonify({
                "success": False,
                "message": "Question is required"
            }), 400

        answer = rag_service.ask(
            question
        )

        response = {
            "success": True,
            "question": question,
            "answer": answer
        }

        return Response(
            json.dumps(response, indent=4),
            mimetype="application/json"
        )

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500