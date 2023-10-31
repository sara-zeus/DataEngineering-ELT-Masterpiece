#%%

import pandas as pd

def read():
    towns=[]
    state=" "

    with open("university_towns.txt", mode="r") as file:
        for line in file: 
            if "[edit]" in line:
                state= line.strip()
            else:
                towns.append([state,line])
            
                       
    return pd.DataFrame(towns, columns=["state","town"])

towns= read()
towns.to_csv("towns.csv")

#%% 
import pandas as pd

def read():
    return pd.read_csv("towns.csv", index_col=0).assign(
        state= lambda df: df.loc[:,"state"].str.removesuffix("[edit]"), 
        town= lambda df: df.loc[:,"town"].str.extract(r"(.+) \(.*") 
    )


towns=read() 

# %%
 