from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def main_page():
    return render_template('htmldoc.html')

@app.route("/converted", methods=["POST"])
def converted():
    starting_temp = request.form["temp1"]
    starting_degree = request.form["degree1"]
    ending_degree = request.form["degree2"]
    try:
        starting_temp = float(request.form["temp1"])
        if starting_degree == "Celsius" and ending_degree == "Fahrenheit":
            return str((starting_temp * 1.8) + 32)
        if starting_degree == "Fahrenheit" and ending_degree == "Celsius":
            return str((starting_temp - 32) * 1.8)
        if starting_degree == "Celsius" and ending_degree == "Kelvin":
            return str(starting_temp + 273.15)
        if starting_degree == "Kelvin" and ending_degree == "Celsius":
            return str(starting_temp - 273.15)
        if starting_degree == "Fahrenheit" and ending_degree == "Kelvin":
            return str((starting_temp - 32)* 1.8 + 273.15)
        if starting_degree == "Kelvin" and ending_degree == "Fahrenheit":
            return str((starting_temp - 273.15)* 1.8 + 32)
        if starting_degree == "Celsius" and ending_degree == "Celsius":
            return str(starting_temp) + " Y'alls stupik"
        if starting_degree == "Fahrenheit" and ending_degree == "Fahrenheit":
            return str(starting_temp) + " Y'alls stupik"
        if starting_degree == "Kelvin" and ending_degree == "Kelvin":
            return str(starting_temp) + " Y'alls stupik"
    except ValueError:
        return "Please input a number, not letters(Y'alls REALLY dumb)"
app.run()
