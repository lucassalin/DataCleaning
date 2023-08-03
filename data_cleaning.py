import pandas as pd
import numpy as np

def clean_phone_number(x):
	x = pd.Series(str(x).strip()).replace('\D', '', regex=True).values[0]

	if len(x) != 10:
		return np.nan
	else:
		return x[0:3] + '-' + x[3:6] + '-' + x[6:10]

df = pd.read_excel("/Users/lucas/Downloads/CustomerCallList.xlsx")

df = df.drop_duplicates()
df = df.drop(columns="Not_Useful_Column")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

df["Phone_Number"] = df["Phone_Number"].apply(clean_phone_number)

replacements = {"N/a": "", "N": "No", "Y": "Yes"}
df["Address"] = df["Address"].replace(replacements)
df["Paying Customer"] = df["Paying Customer"].replace(replacements)
df["Do_Not_Contact"] = df["Do_Not_Contact"].replace(replacements)

df["Do_Not_Contact"] = df["Do_Not_Contact"].fillna("?")

df = df.dropna(subset=["Phone_Number"])

df = df.rename(columns={"First_Name": "First name",
						"Last_Name": "Last name",
						"Phone_Number": "Phone Number",
						"Do_Not_Contact": "Do not contact"})

print(df)
