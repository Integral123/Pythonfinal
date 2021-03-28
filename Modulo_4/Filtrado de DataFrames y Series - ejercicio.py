import pandas as pd
airbnb = pd.read_csv("./data/pandas/airbnb.csv")
airbnb.head()
#1:c
df=airbnb[(airbnb['reviews'] > 10) & (airbnb['overall_satisfaction'] > 4)]
df=df.set_index("reviews")
df.head()
#2:c
ns = airbnb [ (airbnb['room_id'] == 97503) | (airbnb['room_id'] == 90387) ]
ns
#3:c
ns = airbnb [(airbnb['price'] < 50) & (airbnb['price'] < 50) & (airbnb['room_type'] == "Shared room")]
ns