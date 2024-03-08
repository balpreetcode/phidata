import pandas as pd

# Load the data
url = 'https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv'
data = pd.read_csv(url)

# Calculate the average rating
average_rating = data['Rating'].mean()

# Print the average rating
print('The average rating of movies is:', average_rating)

if __name__ == '__main__':
    average_rating