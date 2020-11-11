import pandas as pd

melbourne_file_path = './melb_data.csv'
#read data & store in DF
melbourne_data = pd.read_csv(melbourne_file_path)
#print summary of data
print(melbourne_data.describe())
    #count shows # of rows w/ non-missing values

#SELECTING DATA FOR MODELING (3 of 7) ---------------------

melbourne_data.columns

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#subsetting data:
#1: Dot notation, which we use to select the "prediction target"
#2: Selecting with a column list, which we use to select the "features"

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
X.describe()
X.head()

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))



#EXERCISE (3.5 out of 7) ------------------------------------

#this shows the same thing:
melbourne_data.Price
melbourne_data['Price']

#MODEL VALIDATION (4 of 7) --------------------------------
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)


from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

melbourne_model_2 = DecisionTreeRegressor()
melbourne_model_2.fit(train_X, train_y)

val_predictions = melbourne_model_2.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
