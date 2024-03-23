# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('C:\\Users\\Admin\\Desktop\\prog\\python\\traffic.csv')

# Print the dataset
print(df)

# Convert 'DateTime' to datetime format if it's not
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extract features from 'DateTime'
df['hour'] = df['DateTime'].dt.hour
df['day'] = df['DateTime'].dt.day
df['month'] = df['DateTime'].dt.month
df['year'] = df['DateTime'].dt.year

# Now drop the original 'DateTime' column
df = df.drop(columns=['DateTime'])

# Selecting features and target variable
X = df.drop(columns=['Vehicles']) # assuming 'Vehicles' is your target variable
y = df['Vehicles']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the Decision Tree model
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

# Predicting traffic volume for test data
dt_predictions = dt_model.predict(X_test)

# Calculating Mean Absolute Error for the model
dt_mae = mean_absolute_error(y_test, dt_predictions)

# Calculating Root Mean Squared Error for the model
dt_rmse = mean_squared_error(y_test, dt_predictions, squared=False)

# Calculating R-squared for the model
dt_r2 = r2_score(y_test, dt_predictions)

print(f'Decision Tree MAE: {dt_mae}')
print(f'Decision Tree RMSE: {dt_rmse}')
print(f'Decision Tree R-squared: {dt_r2}')
