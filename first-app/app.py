import pandas as pd

# Load csv into data frame
df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()
print(df)