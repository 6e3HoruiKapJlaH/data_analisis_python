import numpy as np

def main():
    k = generate_arrays()
    acessing_elements(k[0], -1)
    testing_arithmetics()
    test_csv()
    selection_subarrays(k[0], 1, 3)




def generate_arrays():
    arr1 = np.array([1,2,6])
    arr2 = np.array([[1,4,5],[1,8,0]])
    arr3 = np.zeros((4,5))
    arr4 = np.linspace(1, 5, 5, dtype=int)
    arr5 = np.random.randint(1,1000, (5,5))
    return arr1, arr2, arr3, arr4, arr5


def acessing_elements(array, first, second=None):
    if second:
        try:
            print(array[first][second])   
        except:
            print(f"Elements {first} and/or {second} are out of range of array")
    else:
        try:
            print(array[first])   
        except:
            print(f"Element {first} are out of range of array")

def selection_subarrays(array,start, stop,  start1 = None, stop1 = None):
    if start1 and stop1:
        try:
            print(array[start:stop, start1:stop1])   
        except:
            print(f"Elements {start}, {stop} and/or {start1}, {stop1}  are out of range of array")    
    else:
        try:
            print(array[start:stop])   
        except:
            print(f"Elements {start} and/or {stop}  are out of range of array")    
        
            
def testing_arithmetics():   
    a = np.zeros(4)
    a+=14
    print(a)
    a/=2
    print(a)
    a-=1
    print(a)
    a%=4
    print(a)
    
    
    import functools
    list = [i for i in range(1, 20)]
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(lambda a, b: a+b, list))
    
    
    import itertools
    arr = [4, 2, 6, 9, 10, 0, 3, -9]
    res = itertools.accumulate(arr, max)
    print([i for i in res])
    
    
    first = np.ones(3)
    second = np.linspace(1, 5, 3, dtype=int)
    print(np.add.outer(first, second))
    
    
    
def test_csv():
    import pandas as pd
    data = pd.read_csv('iris.csv')
    data.shape
    print(data['petal_width'].describe(percentiles=[.25, .75]))
    sepal_l, sepal_w, petal_l, petal_w, class_iris = np.array(data['sepal_length']), np.array(data['sepal_width']), np.array(data['petal_length']), np.array(data['petal_width']), np.array(data['class'])
    
    """ print(f"Max petal width = {np.max(petal_w)}")
    print(f"Min petal width = {np.min(petal_w)}")  
    print(f"Mean petal width = {np.mean(petal_w)}")  
    print(f"Variance petal width = {np.var(petal_w)}")  
    print(f"Standart deviation petal width = {np.std(petal_w)}")  
    print(f"Median petal width = {np.median(petal_w)}")  
    print(f"25 percentil petal width = {np.percentile(petal_w, 25)}")  
    print(f"75 percentil petal width = {np.percentile(petal_w, 75)}")   """
    

    
if __name__ == "__main__":
    main()