import pandas as pd

df=pd.read_csv("data/original.csv", encoding='latin_1')

df2=pd.DataFrame()

df2[['before','after']] = df['text'].str.split('6', expand=True)



df2['before'] = df2['before'].str.strip(r" 1. |1) | (1) ")
df2['before'] = df2['before'].str.split(r"\d.", expand=False)

df2['after'] = df2['after'].str.strip(r" 6. |6) | (6) ")
df2['after'] = df2['after'].str.split(r"\d.", expand=False)
'''
for i in range(60):
    beforeLen=len(df2['before'][i])
    afterLen=len(df2['after'][i])
    if(beforeLen!=afterLen):
        print("index: %i, beforeLen: %i, afterLen: %i"%(i,beforeLen,afterLen))
        print(df2['before'][i])
        print(df2['after'][i])
'''
#print(df2['after'])
df2=df2.explode(['before','after'])

print(df2)

df2.to_csv('data/modData.csv')
df2['before'].to_csv('data/before_unclustered.csv')
df2['after'].to_csv('data/after_unclustered.csv')





    
