from flask import Blueprint, request, jsonify

from core.resume.resume_analyzer import ResumeAnalyzer

resume_bp = Blueprint(
    "resume",
    __name__
)

analyzer = ResumeAnalyzer()


@resume_bp.route(
    "/resume/analyze",
    methods=["POST"]
)
def analyze_resume():

    try:

        data = request.json

        resume_text = data.get(
            "resume_text"
        )

        result = analyzer.analyze(
            resume_text
        )

        return jsonify({
            "success": True,
            "analysis": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500