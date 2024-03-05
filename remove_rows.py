import pandas as pd

# WORKING OUTPUT

filter_strings = ["MCDONALD'S"]

file_name = 'Anthony_TRANSACTIONS_2022.csv'
input_df = pd.read_csv(f'~/Documents/Taxes_2022/{file_name}') # INPUT
output_df = f'~/Documents/Taxes_2022/1_{file_name}'

def filter_and_save_csv(filter_strings, input_df, output_df):
    # Read the CSV file into a DataFrame

    # Remove selected strings from the DataFrame
    filtered_df = input_df[input_df.apply(lambda row: row.astype(str).str.contains('|'.join(filter_strings), case=False).any(), axis=1)]

    # Save the cleaned DataFrame to a new CSV file
    filtered_df.to_csv(output_df, index=False)


filter_and_save_csv(filter_strings, input_df, output_df)


# keywords_to_remove = ['B@H', 'from']
# "MCDONALD'S", 'Wix.Com' ,  'MURPHY',  'ADOBE',  'JERSEY',  'GOOGLE' 'DAWN',  'APPLE',  'CHATGPT',  'SPOTIFY',  'WHATABURGER',  "McDonald's",  'WESTLAKE',  'RAISING CANES',  'TACO BELL',  "THAI EXPRESS",  "KUM&GO",  'Microsoft',  'CULVERS',  'CENEX'
# keywords_to_remove = ['RoundUp', 'WAL-MART', 'Wal-Mart Super', 'Nintendo' 'prime video', 'payment', 'samsclub', 'AMZN', 'ONLYFANS', 'aldi', 'deposit', 'maxmoney', 'paypal', 'patreon', 'square', 'funimation', 'subscribestar', 'B@H', 'london', 'steam', 'humblebundle', 'fort l', 'capital one', 'mobile pmt', 'cvs', 'COXHEALTHSYSTEM', 'WALGREENS', 'savings', 'nintendo', 'petco']
# keyword_to_filter = ['MURPHY',"KUM&GO",  'CENEX', 'LOWES' , 'DEPOT', 'amazon', 'VZWRLSS', 'AMZR']