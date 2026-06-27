from flask import Blueprint, request, jsonify

from core.research.research_service import ResearchService

research_bp = Blueprint(
    "research",
    __name__
)

research_service = ResearchService()


@research_bp.route("/research", methods=["POST"])
def research():

    try:

        data = request.json

        topic = data.get("topic")

        if not topic:
            return jsonify({
                "success": False,
                "message": "Topic is required"
            }), 400

        result = research_service.research(topic)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500