import pandas as pd

def calculate_average_rating(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Calculate the average movie rating
    average_rating = df['Rating'].mean()
    return average_rating

if __name__ == "__main__":
    file_path = "./IMDB-Movie-Data.csv"
    average = calculate_average_rating(file_path)
    print(f"The average movie rating is: {average:.2f}")