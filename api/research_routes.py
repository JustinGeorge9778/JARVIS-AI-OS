from flask import Blueprint, request, jsonify

from core.research.report_generator import ReportGenerator

research_bp = Blueprint(
    "research",
    __name__
)

report_generator = ReportGenerator()


@research_bp.route("/research", methods=["POST"])
def research():

    data = request.json

    topic = data.get("topic")

    report = report_generator.generate_report(
        topic
    )

    return jsonify({
        "success": True,
        "topic": topic,
        "report": report
    })