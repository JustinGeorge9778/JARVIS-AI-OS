class ATSScorer:

    def score(self, resume_text):

        score = 70

        if "python" in resume_text.lower():
            score += 10

        if "machine learning" in resume_text.lower():
            score += 10

        return min(score, 100)