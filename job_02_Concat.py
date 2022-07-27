import pandas as pd
import glob
df = pd.DataFrame()
data_paths = glob.glob('./wanted/clear_data/*')

for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
df.to_csv('./wanted/clear_data/All_clear_data.csv', index=False)