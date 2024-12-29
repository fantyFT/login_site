from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Правильные учетные данные пользователя
VALID_USERNAME = "fanty"
VALID_PASSWORD = "ft"

@app.route("/", methods=["GET", "POST"])
def login():
  error = None
  if request.method == "POST":
      username = request.form["username"]
      password = request.form["password"]

      if username == VALID_USERNAME and password == VALID_PASSWORD:
          return redirect(url_for("welcome", username=username))
      else:
        error = "Invalid username or password. Please try again."
  return render_template("login.html", error=error)


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)