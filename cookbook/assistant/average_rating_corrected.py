import pandas as pd

# Function to calculate the average rating
def calculate_average_rating(url):
    # Reading the data from the provided URL
    data = pd.read_csv(url)
    # Calculating the average
    average_rating = data['Rating'].mean()
    return average_rating

if __name__ == "__main__":
    url = "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
    average_rating = calculate_average_rating(url)
    print(average_rating)