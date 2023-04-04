from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():

    if request.method == "GET":
        return render_template("form.html", min=0, max=1000)

    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return render_template("form3.html", guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return render_template("form2.html", guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run()


