from flask import Flask, request
app = Flask(__name__)
courses = [
    "Python Programming",
    "Web Development",
    "Machine Learning",
    "Database Management",
    "Cloud Computing"
]
registrations = []
@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        course = request.form.get("course", "").strip()
        if not name or course not in courses:
            message = "Please enter a name and select a valid course."
        else:
            registrations.append({
                "name": name,
                "course": course
            })
            message = "Course registration successful!"
    options = "".join(
        f'<option value="{course}">{course}</option>'
        for course in courses
    )
    records = "".join(
        f'<li>{item["name"]} - {item["course"]}</li>'
        for item in registrations
    )
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Course Registration</title>
    </head>
    <body>
        <h2>Online Student Course Registration</h2>
        <p>{message}</p>
        <form method="POST">
            Student Name:
            <input type="text" name="name" required>
            <br><br>
            Select Course:
            <select name="course" required>
                <option value="">Choose a course</option>
                {options}
            </select>
            <br><br>
            <button type="submit">Register</button>
        </form>
        <h3>Registered Students</h3>
        <ul>{records}</ul>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)
