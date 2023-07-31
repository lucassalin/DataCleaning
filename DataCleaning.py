import pandas as pd
import numpy as np

df = pd.read_excel("/Users/lucas/Downloads/CustomerCallList.xlsx")

df = df.drop_duplicates()
df = df.drop(columns="Not_Useful_Column")

df["Last_Name"] = df["Last_Name"].str.strip("123._/")

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x).strip())
df["Phone_Number"] = df["Phone_Number"].str.replace('\D', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x if len(x) == 10 else "")
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x if x == "" else x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Address"] = df["Address"].replace("N/a", "")

df["Paying Customer"] = df["Paying Customer"].replace("N/a", "")
df["Paying Customer"] = df["Paying Customer"].replace("N", "No")
df["Paying Customer"] = df["Paying Customer"].replace("Y", "Yes")

df["Do_Not_Contact"] = df["Do_Not_Contact"].fillna("?")
df["Do_Not_Contact"] = df["Do_Not_Contact"].replace("N", "No")
df["Do_Not_Contact"] = df["Do_Not_Contact"].replace("Y", "Yes")

df["Phone_Number"].replace("", np.nan, inplace=True)
df = df.dropna(subset=["Phone_Number"])

df = df.rename(columns={"First_Name": "First name",
                        "Last_Name": "Last name",
                        "Phone_Number": "Phone Number",
                        "Do_Not_Contact": "Do not contact"})

print(df)
