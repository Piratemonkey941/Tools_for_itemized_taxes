import pandas as pd

# WORKING FILTERS THEN REMOVES ROWS WITH KEYWORDS
filter_strings = ["MCDONALD'S", 'MCDONALDS']

fileName = 'Anthony_TRANSACTIONS_2022.csv'
input_df = pd.read_csv(f'~/Documents/Taxes_2022/{fileName}') # INPUT
output_df = '{fileName}'
# output_df = f'~/Documents/Taxes_2022/1_{fileName}'

def filter_and_remove(filter_strings, input_df):
    filtered_df = input_df[~input_df.apply(lambda row: row.astype(str).str.contains('|'.join(filter_strings), case=False).any(), axis=1)]

    filtered_df.to_csv('cleaned_output.csv', index=False) # change depending on filter


def filter_and_save_csv(filter_strings, input_df, output_df):
    filtered_df = input_df[input_df.apply(lambda row: row.astype(str).str.contains('|'.join(filter_strings), case=False).any(), axis=1)]

    filtered_df.to_csv(output_df, index=False)


filter_and_remove(filter_strings, input_df)
filter_and_save_csv(filter_strings, input_df, output_df)
