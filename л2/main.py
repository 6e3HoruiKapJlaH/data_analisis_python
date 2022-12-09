import numpy as np

def main():
    table = 'Budget.csv'
    parsing(table)    


def parsing(table_name):
    import pandas as pd
    data = pd.read_csv(table_name)
    food_spend, fuel_cost, cloth_spend, alc_spend, transport_cost, other_spends, totexp, income, age_oldest, number_of_children =  np.array(data['wfood']), np.array(data['wfuel']), np.array(data['wcloth']), np.array(data['walc']), np.array(data['wtrans']), np.array(['wother']), np.array(data['totexp']), np.array(data['income']), np.array(data['age']), np.array(data['children'])
   
    calc_average_age(age_oldest)
    print("")
    check_normal_distibution(cloth_spend)
    print("")
    check_correlation(number_of_children, alc_spend)
    print("")
    test_hypo(food_spend, number_of_children)


def calc_average_age(arr):
    avg = np.average(arr)
    print(f'The average age of oldest in the family = {avg} ')
    
    rmsd = np.sqrt(np.var(arr))
    print(f'The root mean square deviation age of oldest in the family = {rmsd} ')
    
    
def check_normal_distibution(data):
    from scipy.stats import shapiro
    stat, p = shapiro(data)
    
    print(f"stat = {stat}, p value = {p}")
    if(p>0.05):
        print("Not a Gaussian distibution")
    else:
        print("It`s a Gaussian distibution")



def check_correlation(data1, data2):
    from scipy.stats import pearsonr
    corr, p  = pearsonr(data1, data2)
    print(f"correlation coefficient = {corr}, p value = {p}")
    if(p>0.05):
        print("Not a correlation")
    else:
        print("It`s a correlation")

def test_hypo(waste, childrens):
    import scipy.stats as stats
    class1 = [j for i,j in enumerate(waste) if childrens[i]==1]
    class2 = [j for i,j in enumerate(waste) if childrens[i]==2]
    print(stats.ttest_ind(a=class1, b=class2, equal_var=True))    
    
if __name__ == "__main__":
    main()