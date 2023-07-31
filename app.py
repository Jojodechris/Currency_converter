# app.py file

from flask import Flask, redirect, render_template, request,flash
from forex_python.converter import CurrencyCodes

app = Flask(__name__)

import requests
from currency import is_value_in_array 

import os

# Generate a secret key (you can use any method to generate a secret key)
secret_key = os.urandom(24)

# Set the secret key in the Flask app configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key



@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/result')
def result_page():
    from_currency = request.args.get('Convertfrom')
    to_currency = request.args.get('Convertto')
    amount = request.args.get('Convertamount')

    # Input validation for amount
    try:
        amount = float(amount)
        if amount <= 0 or amount is None :
            raise ValueError("Amount must be a positive number")
    except ValueError:
        # Flash message for invalid amount
        flash('Please enter a valid amount', 'error')
        return redirect("/")

    url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get("success", False):
        rate_value = data["info"].get("rate")
        if rate_value is not None:
            c = CurrencyCodes()
            result = rate_value * amount
            rounded_result = round(result, 2)
            symbols = c.get_symbol(to_currency)
            # Check if both the amount and the currency are valid
            return render_template("result.html", rate_value=rate_value, amount=amount, result=rounded_result, symbols=symbols)
        else:
            # Handle case when rate_value is None
            flash('Invalid currency code', 'error')
    else:
        # Check for invalid currency code or API error
        flash('Invalid currency code or API error', 'error')

    return redirect("/")




 
    # url2 ="https://api.exchangerate.host/base"
    # response2 = requests.get(url2)
    # data2 = response2.json()
    # rates_dict = data2["rates"]
    # # Create an array with the keys of the "rates" dictionary
    # rates_keys_array = list(rates_dict.keys())

    # result_From = is_value_in_array(rates_keys_array,from_currency)
    # result_To = is_value_in_array(rates_keys_array,to_currency)
    # if result_From and result_To == True :
    #     return render_template("result.html",  result=result)
    # else:
    #      flash('Invalid currency codes or API error', 'error')
    # return  redirect("/")
        

if __name__ == "__main__":
    app.run(debug=True)



 

