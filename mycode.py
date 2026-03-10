import pandas as pd
import os

data={"Name":['Sandip','ABC','Sssa'],
"Roll":[1,10,45],
"City":['Kol','Chennnai','Kol']}

df=pd.DataFrame(data)

data_dir="data"

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
filepath=os.path.join(data_dir,'sample_data.csv')
df.to_csv(filepath,index=True)
print("hii")



