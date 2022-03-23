import pandas as pd
from sklearn.model_selection import train_test_split
from housePricePredictor import HousePricePrediction as HousePricePredictor
import joblib

if __name__ == "__main__":
    url = "house_price.csv"
    house_df = pd.read_csv(url)
    target_column = "price"
    input_col = ['bedrooms', 'bathrooms', 'sqft_living', 'view', 'grade', 'sqft_above', 'sqft_living15']
    train_x, test_x, train_y, test_y = train_test_split(
        house_df[input_col], house_df[target_column], test_size=0.2, random_state=1
    )
    model_obj = HousePricePredictor(train_x, train_y).fit()
    test_x_scaled = model_obj.scale(test_x)
    test_y_pred = model_obj.model.predict(test_x_scaled.values)
    joblib.dump(model_obj, "model.joblib")