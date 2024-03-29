import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from ISLP.models import summarize
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def linearRegression(dir: str):
    # Combine all records
    dfs = list()
    
    for filename in os.listdir(dir):
        if filename.endswith(".csv"):
            # Read each CSV file into a DataFrame
            filepath = os.path.join(dir, filename)
            df = pd.read_csv(filepath)
            dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    all_records = pd.concat(dfs, ignore_index=True)
    
    del dfs
    
    y = all_records["gain/loss"]
    X = all_records[all_records.columns.drop(["gain/loss", "buy_lag3_return", "buy_lag4_return"])]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=300)
    
    slr_model = sm.OLS(y_train, X_train)
    result = slr_model.fit()
    print(summarize(result))
    
    prediction = result.predict(X_test)
    mse = mean_squared_error(y_test, prediction)
    print(mse)
    rmse = np.sqrt(mse)
    print(rmse)
    
    print(pd.concat([y_test, prediction], axis=1).to_string())
    

if __name__ == "__main__":
    linearRegression("results")