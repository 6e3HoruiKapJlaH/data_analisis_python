import numpy as np
import pandas as pd
import copy

def main():
    table = 'Budget.csv'
    parsing(table)    


def parsing(table_name):
    data = pd.read_csv(table_name)
    food_spend, fuel_cost, cloth_spend, alc_spend, transport_cost, other_spends, totexp, income, age_oldest, number_of_children =  np.array(data['wfood']), np.array(data['wfuel']), np.array(data['wcloth']), np.array(data['walc']), np.array(data['wtrans']), np.array(['wother']), np.array(data['totexp']), np.array(data['income']), np.array(data['age']), np.array(data['children'])
    
    select_array(fuel_cost)
    print("")
    change_dataframe(copy.deepcopy(data))
    print("")
    test_column(copy.deepcopy(data))
    print("")
    
   
   
def select_array(arr):
    a = pd.Series(arr)
    sub_arr = a[5:10]
    sub_arr.index=["A", "B", "C", "D", "E"]
    print("loc:\n", sub_arr.loc["A":"C"])
    print("iloc:\n", sub_arr.iloc[2:5])
    

def change_dataframe(df):
    df.insert(9, 'total profit', df['income']-df['totexp'])
    new_df = df.append({
        'food':'0.1111',
        'wfuel' : '0.222',
        'wcloth' : '0.111',
        'walc':'0',
        'wtrans': '0.001',
        'wother':'0.1212',
        'totexp':'150',
        'income':'100',
        'age':'40',
        'children':1}, ignore_index=True)
    df = df.drop(df.index[1:200])
    del df['children']   
    
    
def test_column(df):
    from tabulate import tabulate
    df.set_index(['wfood'])
    print(tabulate(df.describe(include='all'), headers = 'keys', tablefmt = 'psql'))   
    #change datatype of column to string
    df['wfood'] = df['wfood'].astype(str)
    #Group data by one of the columns, apply several aggregating functions, select a subarray according to certain characteristics
    print(tabulate(df.groupby('wfood')['wfood'].agg(['count', 'min', 'max']).loc['0.1':'0.2'], headers = 'keys', tablefmt = 'psql'))


def merging_dataframes(df):
    df2 = pd.DataFrame(index=df.index)
    df2['food and fuel'] = df['wfood'] + df['wfuel']
    #Merge two dataframes
    df3 = pd.merge(df, df2, left_index=True, right_index=True)
    
    df4 = pd.DataFrame(index=df.index)
    df4['numbers of family'] = np.random.randint(2, 10, size=len(df4))
    #Merge two dataframes
    df5 = pd.merge(df3, df4, left_index=True, right_index=True)


   
if __name__ == "__main__":
    main()