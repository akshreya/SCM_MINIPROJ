from ML_Prepare import prepare_data
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# get cleaned data
data = prepare_data()

# features + target
X = data[['days']]
y = data['quantity']

# train model
model = LinearRegression()
model.fit(X, y)

# predict next 30 days
future_days = list(range(data['days'].max()+1, data['days'].max()+31))
future_df = pd.DataFrame({'days': future_days})
predictions = model.predict(future_df)

# plot
plt.figure(figsize=(10,5))
plt.plot(data['days'], y, label='Actual Demand')
plt.plot(future_days, predictions, label='Predicted Demand', linestyle='--')
plt.xlabel('Days')
plt.ylabel('Quantity')
plt.title('Demand Forecast')
plt.legend()
plt.tight_layout()
plt.show()
print("Predicted demand for next 30 days:")
print(predictions)
input("Press Enter to close...")
