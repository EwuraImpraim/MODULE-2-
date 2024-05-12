import pandas as pd 

def insight(filepath):
    df = pd.read_csv(filepath)
    
    hot_technologies = df[df["Hot Technology"] == "Y"]
    
    hot_examples = hot_technologies['Example'].unique()
    
    print("SKILLS OF HOT TECHNOLOGIES:")
    for example in hot_examples:
        print(example)
    
insight("Technology.csv")
    


