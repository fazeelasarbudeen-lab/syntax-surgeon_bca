
from flask import Flask, render_template, request
from code_detector import detect_code
from syntax_checker import check_syntax
from formatter import format_code
from chatbot import chat_response

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    formatted = ""
    response = ""

    if request.method == "POST":
        user_input = request.form["message"]

        if detect_code(user_input):
            valid, error = check_syntax(user_input)

            if valid:
                result = "Syntax is correct"
            else:
                result = "Syntax Error: " + error

            formatted = format_code(user_input)

        response = chat_response(user_input)

    return render_template("index.html",
                           result=result,
                           formatted=formatted,
                           response=response)

if __name__ == "__main__":
    app.run(debug=True)
