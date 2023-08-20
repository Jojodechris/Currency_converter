from flask import Flask, redirect, render_template, request,flash,session, url_for
from forex_python.converter import CurrencyCodes
import json

app = Flask(__name__)

import requests
from currency import is_value_in_array


# Set the secret key in the Flask app configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = "jojo237"


@app.route('/')
def home_page():

    from_currency = request.args.get('Convertfrom')
    to_currency = request.args.get('Convertto')
    amount = request.args.get('Convertamount')

    #  # Store form data in session
    # session['from_currency'] = from_currency
    # session['to_currency'] = to_currency
    # session['amount'] = amount

    # # Retrieve form data from session to pre-fill the form fields
    # from_currency = session.get('from_currency', '')
    # to_currency = session.get('to_currency', '')
    # amount = session.get('amount', '')

    
    return render_template("index.html", from_currency="", to_currency= "", amount=amount)
  

@app.route('/result', methods=['GET', 'POST'])
def result_page():
    if request.method == 'POST':
        from_currency = request.form.get('Convertfrom')
        to_currency = request.form.get('Convertto')
        amount = request.form.get('Convertamount')

        has_error = False

        url1="https://api.exchangerate.host/latest"
        response1=requests.get(url1)
        data1 = response1.json()
        # parsed_data = json.loads(data1)
        # Extract currency codes
        currency_codes = list(data1['rates'].keys())



        try:
            # if len(from_currency) ==0:
            if from_currency not in currency_codes:
                raise ValueError("From Currency cannot be empty!")
                # return render_template('index.html', from_currency=from_currency)
        except ValueError:
            flash('Please enter a valid code currency in "converting from" ', 'error')
            # session["from_currency"]= from_currency
            has_error = True

        # return render_template('index.html', from_currency=from_currency)

        try:
            # if len(to_currency) == 0:
            if to_currency not in currency_codes:
                raise ValueError("To Currency cannot be empty!")
                # return render_template('index.html', to_currency=to_currency)
        except ValueError:
            flash('Please enter a valid code currency in "converting to" ', 'error')
            # session["to_currency"]= to_currency
            has_error = True

        # return render_template('index.html', to_currency=to_currency)



        try:
            amount = float(amount)
            if amount <= 0 or amount is None:
                raise ValueError("Amount must be a positive number")
        except ValueError:
            flash('Please enter a valid amount', 'error')
            # session["amount"]= amount
            has_error = True


        if has_error:
            session["amount"]= amount
            session["from_currency"]= from_currency
            session["to_currency"]= to_currency
            # return redirect('/')
            return render_template('index.html',from_currency=session.get('from_currency'), to_currency= session.get('to_currency'), amount=session.get('amount'))


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
                return render_template("result.html", rate_value=rate_value, amount=amount, result=rounded_result, symbols=symbols)
            else:
                flash('Invalid currency code', 'error')
        else:
            flash('Invalid currency code or API error', 'error')

    # # Clear the form data from the session
    # session.pop('from_currency', None)
    # session.pop('to_currency', None)
    # session.pop('amount', None)


    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)




 
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



 

