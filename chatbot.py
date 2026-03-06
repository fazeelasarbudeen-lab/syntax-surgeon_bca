
def chat_response(text):
    if "python" in text.lower():
        return "Python is widely used for AI, web development, and automation."
    elif "error" in text.lower():
        return "Syntax errors usually happen due to missing brackets or indentation."
    else:
        return "I am Syntax Surgeon. I can help analyze Python code and explain errors."
