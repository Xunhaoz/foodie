from calendar import month
import json
from pickle import APPEND
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/personal/<username>")
def get_personal_budget(username, method=['GET']):
    report_month = request.values.get('month')

    with open('static/src/purchase_analysis.json', encoding="utf-8") as f:
        pie_data = json.load(f)[str(report_month)]
        option_values = []
        money_values = []
        for k, v in pie_data.items():
            option_values.append(k)
            money_values.append(v)

    return render_template('personal.html',
                           username=username,
                           report_month=report_month,
                           option_values=option_values,
                           money_values=money_values,
                           sum_of_money=sum(money_values)
                           )

@app.route("/advanced_purchase")
def display_advanced_purchase():
    return render_template('advanced_purchase.html')

@app.route("/menu")
def display_menu():
    return render_template('food_menu.html')

@app.route("/customerMessage.html")
def display_cutomerMessage():
    return render_template('customerMessage.html')

@app.route("/customerService")
def display_customerService():
    return render_template('customerService.html')

@app.route("/memberRegistering")
def display_memberRegistering():
    return render_template('memberRegistering.html')

@app.route("/personalInfo")
def display_personalInfo():
    return render_template('personalInfo.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
