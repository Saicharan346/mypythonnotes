import pandas as pd  # This line is essential!

# Read the CSV file
#df = pd.read_csv("smpledata.csv")
df=pd.read_excel("smpledata.xlsx")
# Print the DataFrame
print(df)
data={'name':['Sai','Charan','Tej'],'marks':[12,13,13]}
bf=pd.DataFrame(data)
print(bf)
df.to_csv('output.csv')