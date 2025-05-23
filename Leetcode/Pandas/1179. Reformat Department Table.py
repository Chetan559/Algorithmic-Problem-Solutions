import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    pivot_df = department.pivot(index='id', columns='month', values='revenue')
    all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    pivot_df = pivot_df.reindex(columns=all_months)

    pivot_df.columns = [f"{month}_Revenue" for month in pivot_df.columns]
    
    result = pivot_df.reset_index()

    return result
