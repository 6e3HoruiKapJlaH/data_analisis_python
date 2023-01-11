import pandas as pd
import  numpy as np

data = pd.read_json("Version 5.json", orient='records')

data.columns = ["ID","Warehouse_block","Shipment_method","Calls_to_customer_support","Customer_rating","Product_cost","Previous_purchases","Product_importance","Gender","Discount_offered","Weight_in_grams","Delivered_on_Time"]
data['ID'] = data['ID'].astype(int)
data['Warehouse_block'] = data['Warehouse_block'].astype('category')
data['Shipment_method'] = data['Shipment_method'].astype('category')
data['Calls_to_customer_support'] = data['Calls_to_customer_support'].astype(int)
data['Customer_rating'] = data['Customer_rating'].astype(int)
data['Product_cost'] = data['Product_cost'].astype(float)
data['Previous_purchases'] = data['Previous_purchases'].astype(int)
data['Product_importance'] = data['Product_importance'].astype('category')

def clear_data(data):
    data = data.replace('?', np.nan)
    data = data.dropna()
    data = data.reset_index(drop=True)



    #Sorting and reordering data
    data = data.sort_values(by=['ID'], ascending=True)

    #Duplicate data processing
    data = data.drop_duplicates(subset=['ID'], keep='first')

    #Filter to the desired subset of data

    #Save the data to a new file
    data.to_json("Version 6.json", orient='records')