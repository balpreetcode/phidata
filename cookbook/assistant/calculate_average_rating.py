import pandas as pd

# Function to calculate the average rating of movies
def calculate_average_rating(file_path):
    # Read the movie data
    movies = pd.read_csv(file_path)

    # Calculate the average rating
    average_rating = movies['Rating'].mean()

    return average_rating

if __name__ == "__main__":
    # The path to the IMDB movie data
    file_path = './IMDB-Movie-Data.csv'
    # Calculate and print the average rating
    average_rating = calculate_average_rating(file_path)
    print(f'The average rating of movies is: {average_rating}')