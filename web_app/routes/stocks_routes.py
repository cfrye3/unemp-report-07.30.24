
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.stocks import fetch_stocks_csv, format_usd

stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form: --> based on row 10 in stocks_form.html
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    print("REQUEST DATA:", request_data)

    symbol = request_data.get("symbol") or "NFLX" # get specified symbol or use default, pass through data fetching funciton

    try:
        df = fetch_stocks_csv(symbol=symbol) # fetch_stocks_csv found in row 15 of stocks.py
        latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("stocks_dashboard.html", # now passing symbol data through new stocks dashboard
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/stocks/form")


#
# API ROUTES
#

@stocks_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_csv(symbol=symbol)
        data = df.to_dict("records") # convert dataframe to list of dict
        return {"symbol": symbol, "data": data}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404