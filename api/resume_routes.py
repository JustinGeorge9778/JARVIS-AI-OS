from flask import Blueprint
from flask import request
from flask import jsonify

import os

from core.resume.resume_service import ResumeService

resume_bp = Blueprint(
    "resume",
    __name__
)

resume_service = ResumeService()

UPLOAD_FOLDER = "uploads"


@resume_bp.route(
    "/resume/upload",
    methods=["POST"]
)
def upload_resume():

    try:

        if "file" not in request.files:

            return jsonify({
                "success": False,
                "message": "No file uploaded"
            }), 400

        file = request.files["file"]

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(file_path)

        analysis = resume_service.analyze_resume(
            file_path
        )

        return jsonify({
            "success": True,
            "filename": file.filename,
            "analysis": analysis
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500