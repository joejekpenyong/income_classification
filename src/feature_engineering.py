import pandas as pd
import numpy as np

def map_workclass(data):
    mapping = {
        " Not in universe": "Other",
        " Self-employed-not incorporated": "Self-employed",
        " Private": "Private",
        " Local government": "Government",
        " Federal government": "Government",
        " Self-employed-incorporated": "Self-employed",
        " State government": "Government",
        " Never worked": "Never worked",
        " Without pay": "Other"
    }
    
    # Map the values in the column to the new values
    data['workclass'] = data['workclass'].map(mapping) 
    return(data)


def map_education(data):
    mapping = {
        " High school graduate": "HSD and some college",
        " Some college but no degree": "HSD and some college",
        " 10th grade": "No high school diploma",
        " Masters degree(MA MS MEng MEd MSW MBA)": "Postgraduate degree",
        " Associates degree-academic program": "HSD and some college",
        " 12th grade no diploma": "No high school diploma",
        " Prof school degree (MD DDS DVM LLB JD)": "Postgraduate degree", 
        " 11th grade": "No high school diploma",
        " 9th grade": "No high school diploma",
        " Bachelors degree(BA AB BS)": "College degree",
        " Less than 1st grade": "No high school diploma",
        " 7th and 8th grade": "No high school diploma",
        " Associates degree-occup /vocational": "HSD and some college",
        " 5th or 6th grade": "No high school diploma",
        " Doctorate degree(PhD EdD)": "Postgraduate degree",
        " 1st 2nd 3rd or 4th grade": "No high school diploma",
        " Children": "No high school diploma"
    }
    
    # Map the values in the column to the new values
    data['education'] = data['education'].map(mapping) 
    return(data)


def map_hispanic(data):
    mapping = {
        ' All other': "Not Hispanic",
        ' Do not know': np.nan,
        ' Central or South American': "Hispanic",
        ' Mexican (Mexicano)': "Hispanic",
        ' Mexican-American': "Hispanic",
        ' Other Spanish': "Hispanic",
        ' Puerto Rican': "Hispanic",
        ' Cuban': "Hispanic",
        ' Chicano': "Hispanic",
        ' NA': np.nan
    }
    
    # Map the values in the column to the new values
    data['hispanic_origin'] = data['hispanic_origin'].map(mapping) 
    return(data)


def map_tax_filer_status(data):
    mapping = {
        ' Nonfiler': 'Nonfiler',
        ' Head of household': 'Head of household',
        ' Joint both under 65': 'Joint',
        ' Joint both 65+': 'Joint',
        ' Single': 'Single',
        ' Joint one under 65 & one 65+': 'Joint'
    }
    
    # Map the values in the column to the new values
    data['tax_filer_status'] = data['tax_filer_status'].map(mapping) 
    return(data)



def map_household_summary(data):
    mapping = {
        ' Other relative of householder': 'Other', 
        ' Householder': 'Householder',
        ' Child 18 or older': 'Child',
        ' Child under 18 never married': 'Child',
        ' Spouse of householder': 'Spouse of householder',
        ' Nonrelative of householder': 'Other',
        ' Group Quarters- Secondary individual': 'Other',
        ' Child under 18 ever married': 'Child'
    }
    
    # Map the values in the column to the new values
    data['household_summary'] = data['household_summary'].map(mapping) 
    return(data)



def map_father_country(data):
    mapping = {
        ' United-States': 'United States',
        ' Mexico': 'Mexico'        
    }
    
    # Map the values in the column to the new values
    data['father_country'] = data['father_country'].map(mapping).fillna('Other')
    return(data)


def map_mother_country(data):
    mapping = {
        ' United-States': 'United States',
        ' Mexico': 'Mexico'        
    }
    
    # Map the values in the column to the new values
    data['mother_country'] = data['mother_country'].map(mapping).fillna('Other')
    return(data)


def map_self_country(data):
    mapping = {
        ' United-States': 'United States',
        ' Mexico': 'Mexico'        
    }
    
    # Map the values in the column to the new values
    data['self_country'] = data['self_country'].map(mapping).fillna('Other')
    return(data)


def map_emp_status(data):
    mapping = {
        ' Not in labor force': 'Not in labor force',
        ' Children or Armed Forces': 'Children or Armed Forces',
        ' Full-time schedules': 'Full-time',
        ' Unemployed full-time': 'Unemployed',
        ' Unemployed part- time': 'Unemployed',
        ' PT for non-econ reasons usually FT': 'Part-time',
        ' PT for econ reasons usually PT': 'Part-time',
        ' PT for econ reasons usually FT': 'Part-time'
    }
    
    # Map the values in the column to the new values
    data['emp_status'] = data['emp_status'].map(mapping).fillna('Other')
    return(data)

def drop_duplicates(data):
    return(data.drop_duplicates())

