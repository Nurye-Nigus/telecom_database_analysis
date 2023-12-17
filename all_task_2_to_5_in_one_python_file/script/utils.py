# Define utility functions (replace with actual implementations)
def percent_missing(df):
    return df.isnull().mean() * 100

def format_float(value):
    return f"{value:.2f}"

def find_agg(df, column):
    return df.groupby(column).agg({'some_column': 'mean'})

def missing_values_table(df):
    return pd.DataFrame({
        'Column': df.columns,
        'Missing %': percent_missing(df)
    })

def convert_bytes_to_megabytes(bytes_value):
    return bytes_value / (1024 ** 2)

def fix_missing_ffill(df):
    return df.ffill()

def fix_missing_bfill(df):
    return df.bfill()