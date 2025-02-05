from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Change this to a strong, random key

# Define the correct password
CORRECT_PASSWORD = "143"

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html') 

# Route for flower.html
@app.route('/flower')
def flower():
    return render_template('flower.html')  # Render the flower page
@app.route('/note')
def note():
    return render_template('note.html')  # Ensure note.html exists

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')  # Ensure gallery.html exists

@app.route("/", methods=["GET", "POST"])
def password_page():
    if request.method == "POST":
        entered_password = request.form.get("password")
        if entered_password == CORRECT_PASSWORD:
            session["authenticated"] = True  # Set session variable
            return redirect(url_for("home"))  # Redirect to home if correct
        else:
            return render_template("pass.html", error="Incorrect password!")  # Show error message
    
    return render_template("pass.html")

@app.route("/home.html")
def home():
    if not session.get("authenticated"):  # Check if user is authenticated
        return redirect(url_for("password_page"))  # Redirect if not logged in
    return render_template("home.html")  # Show home page if authenticated


@app.route("/logout")
def logout():
    session.pop("authenticated", None)  # Remove session
    return redirect(url_for("password_page"))

if __name__ == "__main__":
    app.run(debug=True)
