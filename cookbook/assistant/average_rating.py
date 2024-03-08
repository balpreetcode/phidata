import pandas as pd

def calculate_average_rating(file_path):
    df = pd.read_csv(file_path)
    average_rating = df['Rating'].mean()
    return average_rating

if __name__ == "__main__":
    average = calculate_average_rating('./IMDB-Movie-Data.csv')
    print(f'The average rating of movies is: {average:.2f}')