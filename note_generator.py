def generate_notes(topic):
    notes = {
        "python":
        """
        Python is a high-level programming language.

        Key Points:
        - Easy syntax
        - Used in AI, ML and web development
        - Supports object-oriented programming
        """,

        "machine learning":
        """
        Machine Learning allows computers to learn from data.
        """
    }

    topic = topic.lower()

    if topic in notes:
        return notes[topic]

    else:
        return "Topic not found"