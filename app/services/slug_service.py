import re


class SlugService:

    @staticmethod
    def generate(text: str) -> str:
        text = text.strip().lower()

        text = re.sub(r"[\s_]+", "-", text)
        text = re.sub(r"[^a-z0-9\-]", "", text)
        text = re.sub(r"-+", "-", text)

        return text