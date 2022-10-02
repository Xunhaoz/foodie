from calendar import month
import json
from pickle import APPEND
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/<username>")
def hello(username):
    return render_template('index.html', username=username)


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
                           
@app.route("/advanced_purchase/<username>")
def display_advanced_purchase(username):
    return render_template('advanced_purchase.html', username=username)

@app.route("/menu/<username>")
def display_menu(username):
    return render_template('food_menu.html', username=username)

@app.route("/customerMessage/<username>")
def display_cutomerMessage(username):
    return render_template('customerMessage.html', username=username)

@app.route("/customerService/<username>")
def display_customerService(username):
    return render_template('customerService.html', username=username)

@app.route("/memberRegistering/<username>")
def display_memberRegistering(username):
    return render_template('memberRegistering.html', username=username)

@app.route("/personalInfo/<username>")
def display_personalInfo(username):
    return render_template('personalInfo.html', username=username)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/Private_Collection/<username>")
def Private_Collection(username):
    return render_template('Private_Collection.html', username=username) 

@app.route("/PersonalOrder/<username>")
def PersonalOrder(username):
    return render_template('PersonalOrder.html', username=username)     

@app.route("/CloseOrder/<username>")
def CloseOrder(username):
    return render_template('CloseOrder.html', username=username)

@app.route("/loginSuccess/<username>")
def login_success(username):
    return render_template('loginSuccess.html', username=username)

@app.route("/deposit/<username>")
def deposit(username):
    return render_template('deposit.html', username=username)


@app.route("/confirmOrder/<username>")
def confirm_order(username):
    return render_template('confirmOrder.html', username=username)


@app.route("/splitBill/<username>")
def split_bill(username):
    return render_template('splitBill.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
