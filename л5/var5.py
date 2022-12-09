import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv("Amazon.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index(keys='Date', inplace=True)

    second_task(data)

def first_task(data):
    data['Close'].plot()
    plt.show()

    data.loc['2018-01-01':'2018-12-31', ['Close']].plot()
    plt.show()

    data.loc['2020-01-01':'2020-02-01', ['Close']].plot()
    plt.show()

    data.loc['2016-12-01':'2018-03-01', ['Close']].plot()
    plt.show()

    data.loc['2016-01-01':'2018-01-01', ['Close']].plot()
    plt.show()


def second_task(data):
    data.loc['2016-01-01':'2016-12-31', ['High']].resample('D').max().plot()
    plt.show()
    
    data.loc[:, ['High']].resample('D').max().plot()
    plt.show()
    
    data.loc['2019-03-01':'2019-05-31', ['High']].resample('W').max().plot()
    plt.show()
    
    data.loc['2018-03-01':'2018-05-31', ['High']].pct_change().plot()
    plt.show()
    
    data.loc['2017-01-01':'2017-12-31', ['High']].rolling(window=60).mean().plot()
    plt.show()

if __name__ == "__main__":
    main()
