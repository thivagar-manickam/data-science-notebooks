import flask
import pandas as pd
import joblib
import locale  # Module used for formatting the predicted price to US dollar format

model_obj = joblib.load("model.joblib")

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return flask.render_template("home.html")


@app.route("/response", methods=["POST"])
def predictHousePrice():
    noOfBedroom = int(flask.request.form.get("bedrooms"))
    noOfBathroom = float(flask.request.form.get("bathrooms"))
    view = int(flask.request.form.get("view"))
    grade = int(flask.request.form.get("grade"))
    sqftLiving = int(flask.request.form.get("sqftLiving"))
    sqftAbove = int(flask.request.form.get("sqftAbove"))
    sqft15 = int(flask.request.form.get("sqft15"))

    house_details = {
        "bedrooms": noOfBedroom,
        "bathrooms": noOfBathroom,
        "sqft_living": sqftLiving,
        "view": view,
        "grade": grade,
        "sqft_above": sqftAbove,
        "sqft_living15": sqft15,
    }

    house_df = pd.DataFrame([house_details])
    df_scaled = model_obj.scale(house_df)
    house_price = model_obj.model.predict(df_scaled.values)[0]

    # Code to format the predicted price value to US Dollar
    locale.setlocale(locale.LC_ALL, "en_US.utf-8")
    house_price = locale.currency(round(house_price, 3), grouping=True)

    return flask.render_template(
        "response.html", houseInput=house_details, price=house_price
    )


if __name__ == "__main__":
    app.run(host="localhost", port=3600)
