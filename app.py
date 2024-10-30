from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here

    answer = "Make your calculations cutie."
    amount_needed = request.form.get('amount')
    rate = request.form.get('rate')
    repayment_years = request.form.get('years')

    if amount_needed and rate and repayment_years:

        try:
            periodic_rate = (1 + float(rate) / 100) ** (1/12) - 1
            c = float(amount_needed)
            t = float(periodic_rate)
            n = float(repayment_years)*12

            monthly_payment = ( c * t * pow( 1 + t, n ) ) / ( pow( 1 + t, n) - 1 )
            total_interest = monthly_payment * n - c
            total_coast = c + total_interest


            answer = (f"If you need ${c:,} with an interest rate of {rate}% and a repayment term of {repayment_years} years : <br><br>"
                      f"Your <b>monthly payment</b> will be ${monthly_payment:,.2f}. <br> "
                      f"The total <b>interest</b> on your loan will be ${total_interest:,.2f}. <br> "
                      f"In <b>total</b>, your loan will cost you <span>${total_coast:,.2f}</span>.")
        except ValueError:
            answer = "Please enter only numbers."

    else:
        answer = 'Please fill out every fields'



    return render_template('home.html',
                           answer=answer)


if __name__ == '__main__':
    app.run()
