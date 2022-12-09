import pandas as pd
import matplotlib.pyplot as plt

def main():
    path = "StudentsPerformance.csv"
    parse_data(path)
    

def parse_data(path):
    data = pd.read_csv(path)
    
    data["race/ethnicity"].value_counts().plot(kind = "bar").set_title("Number of Students in Each race")
    plt.show()

    data.groupby("race/ethnicity").max().plot(kind = "bar").set_title("Max Math")
    plt.show()
    
    
    
if __name__ == "__main__":
    main()