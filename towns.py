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

