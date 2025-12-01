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
print(df.describe())#Descriptive Statistical Analysis
print(f"Shape: {df.shape}")
print(f"Columns:{df.columns}")
'''
For accessing a column (selecting)
column=df["Columnname"]
or column=df["col1","col2",........]

Filtering Rows based on condition
Single Condition
filtered_rows=df[df["Salary"]>50000]
Multiple Conditions
filtered_rows=df[df["Column"]>value & df["Salary"]>50000]
'''
print(df[(df["Feature_1"]>20) &(df['Feature_2']>35)])#place multiple conditions in tuple
print(df[(df["Feature_1"]>20) |(df['Feature_2']>35)])
#to add a new column df['columnname']=somedata
df['Feature_Hi']=df['Feature_1']*0.1

'''
.loc[rowindex,columnname]used to acess and modify a specific cell
df.insert(loc,'Columnname',somedata)
'''
df.insert(5,"Feature_Hello","hello")
print(df)
df.loc[0,'Feature_1']=46
print(df)
df.drop(columns=['Feature_1'],inplace=True)#this is used to delete a column and in the main file i.e inplace=True
print(df)
#isnull() 
print(df.isnull().sum())
#dropna(axis,implace=True)#removes the roww(axis=0) and colum(axis=0) where there is null
print(df.dropna(axis=0,inplace=True))
#fillna(value,inplace)
#df.fillna(0,inplace=True)
'''
Interpolation
preserves data intergrity
smooth trends
avoid data loss
used to fill missing values based on trend
'''
print(df)
df.interpolate(method='linear',axis=0)
print(df)
#Sorting
print(df.sort_values(by="Feature_2",ascending=False,inplace=True))#sorting in descending order