from flask import Flask, request, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route and methods for the game
@app.route("/", methods=["GET", "POST"])
def guess_the_number():

    # If the request method is GET, display the form to the user with a default range of 0-1000
    if request.method == "GET":
        return render_template("form.html", min=0, max=1000)

    # If the request method is POST, retrieve the form data and update the range based on user feedback
    else:
        # Retrieve the minumum and maximum number from the form
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))

        # Retrieve the user's feedback and current guess from the form
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        # Update the range based on the user's feedback
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            # If the user correctly guesses the number, display a winning message
            return render_template("form3.html", guess=guess)

        # Make a new guess based on the updated range
        guess = (max_number - min_number) // 2 + min_number

        # Display the updated form to the user with the new guess and range
        return render_template("form2.html", guess=guess, min=min_number, max=max_number)


# Start the Flask application
if __name__ == '__main__':
    app.run()


