from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#main route that displays the form.
@app.route('/')
def index ():
    return render_template("index.html")

#post route that displays form submission results
@app.route('/result', methods= ['POST'])
def survey_results():
    print("*"*50)
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['favoritelanguage']
    comment_from_form = request.form['comment']
    return render_template("result.html", name_on_survey=name_from_form, location_on_survey=location_from_form, language_on_survey=language_from_form, comment_on_survey=comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)