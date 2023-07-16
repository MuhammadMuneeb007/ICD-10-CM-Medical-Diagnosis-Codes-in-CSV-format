import os
import pandas as pd

def merge_csv_files(directory):
    merged_df = pd.DataFrame()
    for filename in allfiles:
        if filename.endswith('.csv'):
            #file_path = os.path.join(directory, filename)
            df = pd.read_csv(filename)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    return merged_df

# Example usage
allfiles = []
for loop in range(0,3000,50):
    allfiles.append("ICDCodes"+str(loop)+".csv")

merged_data = merge_csv_files(allfiles)
merged_data = merged_data.drop_duplicates()
merged_data.to_csv("ICDCodesALL.csv")
print(len(merged_data))
