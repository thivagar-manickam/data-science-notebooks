import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class HousePricePrediction:
    def __init__(self, train_x, train_y):
        self.train_x = train_x
        self.train_y = train_y
    
    def fit(self):
        self.scaler = StandardScaler().fit(self.train_x)
        train_x_scaled = self.scale()
        self.model = LinearRegression().fit(train_x_scaled.values, self.train_y)
        return self
        
    def scale(self, data=None):
        if data is None:
            data = self.train_x
        scaler = self.scaler
        data_scaled = scaler.transform(data)
        df_scaled_data = pd.DataFrame(data_scaled, columns=data.columns, index=data.index)
        return df_scaled_data