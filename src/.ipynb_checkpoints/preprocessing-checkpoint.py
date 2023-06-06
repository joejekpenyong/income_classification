import pandas as pd

def load_data(filepath):
    # Assign column names
    colnames = [
        "age", "workclass", "industry_code", "occupation_code", "education", "wage_ph",
        "educ_last_wk", "marital_status", "maj_ind_code", "maj_occ_code", "race",
        "hispanic_origin", "sex", "union_member", "unemp_type", "emp_status", "capgain",
        "caploss", "stock_div", "tax_filer_status", "region_prev_res", "state_prev_res",
        "household_details", "household_summary", "instance_weight", "migration_msa",
        "migration_reg", "migration_within_reg", "live_here_year_ago", "migration_sunbelt",
        "employer_size", "presence_of_parents", "father_country", "mother_country",
        "self_country", "citizenship", "own_business", "vet_quest", "vet_benefit",
        "weeks_worked", "year", "income"
    ]

    # Load data with specified column names
    data = pd.read_csv(filepath, header=None, names=colnames)

    return data

    

def drop_columns(df, cols_to_drop):
    """
    Drops the specified columns from the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame.
        cols_to_drop (list): List of column names to be dropped.
    
    Returns:
        pd.DataFrame: The DataFrame with specified columns dropped.
    """
    return df.drop(cols_to_drop, axis=1)


def drop_children(data):
    newdata = data[data["age"] >= 15]
    return newdata



def get_missing_columns(df):
    missing_columns = df.columns[df.isnull().any()]
    missing_count = df[missing_columns].isnull().sum()
    return missing_count