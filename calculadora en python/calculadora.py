from flask import Flask, render_template, request

calculadora = Flask(__name__)

@calculadora.route("/", methods=["GET", "POST"])
def calcular():
    result = ""
    screen_content = ""
    if request.method == "POST":
        button = request.form.get("button")
        screen_content = request.form.get("screen", "")
        if button == "all-clear":
            screen_content = ""
        elif button == "=":
            try:
                # Evalúa la expresión de manera segura usando eval()
                result = str(eval(screen_content))
                screen_content = result
            except Exception as e:
                screen_content = "Error"
        else:
            screen_content += button
    return render_template("index.html", result=screen_content)

if __name__ == "__main__":
    calculadora.run(debug=True)




