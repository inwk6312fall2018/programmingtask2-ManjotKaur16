import pandas as pd    #panda module for read and write .CSV file
counter_assault=0
counter_robbery=0
user=pd.read_csv("crime.csv")   #it will read the file
a=user["RUCR_EXT_D"]             #this will read particular column in file
for word in a:
    if word == "ASSAULT":
        counter_assault += 1
    elif word == "ROBBERY":
        counter_robbery += 1
data={"Crime Type":["ASSAULT","ROBBERY"], "Crime ID":[1430,2142], "Crime Count":[counter_assault,counter_robbery]}
new_CSV=pd.DataFrame(data,columns=["Crime Type","Crime ID","Crime Count"])
print(new_CSV)
new_CSV.to_csv("crime1.csv")     #saving final result in to crime1 file



