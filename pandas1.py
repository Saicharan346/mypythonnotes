import pandas as pd  # This line is essential!

# Read the CSV file
#df = pd.read_csv("smpledata.csv")
df=pd.read_excel("smpledata.xlsx")
# Print the DataFrame
print(df)
data={'name':['Sai','Charan','Tej'],'marks':[12,13,13]}
bf=pd.DataFrame(data)
print(bf)
bf.to_csv('output.csv',index=False)
'''
head() if not entered any number in () default 5 first five rows
tail() if not entered any number in () default 5 last five rows
'''
print(df.head(5))
'''
info() -method
1-no of rows and columns
2-coulmn name
3-int64,float64 object
4-non null count
5-memory usage of the dataset
'''
print(df.info())