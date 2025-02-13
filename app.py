from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Change this to a strong, random key

# Define the correct password
CORRECT_PASSWORD = "kashishbestgirl@120203"

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html') 

# Route for flower.html
@app.route('/flower')
def flower():
    return render_template('flower.html')  # Render the flower page

@app.route('/flower2')
def flower2():
    return render_template('flower2.html')  # Render the flower page


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
            return render_template("index.html", error="Incorrect password!")  # Show error message
    
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

@app.route('/note1')
def note1():
    return render_template('note1.html')

@app.route('/note2')
def note2():
    return render_template('note2.html')

@app.route('/note3')
def note3():
    return render_template('note3.html')

@app.route('/note4')
def note4():
    return render_template('note4.html')

@app.route('/note5')
def note5():
    return render_template('note5.html')

@app.route('/note6')
def note6():
    return render_template('note6.html')

@app.route('/note7')
def note7():
    return render_template('note7.html')

@app.route('/note8')
def note8():
    return render_template('note8.html')

@app.route('/note9')
def note9():
    return render_template('note9.html')

@app.route('/note10')
def note10():
    return render_template('note10.html')

@app.route('/note11')
def note11():
    return render_template('note11.html')

@app.route('/note12')
def note12():
    return render_template('note12.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/v1')
def v1():
    return render_template('v1.html')

@app.route('/v2')
def v2():
    return render_template('v2.html')


if __name__ == "__main__":
    app.run(debug=True)
