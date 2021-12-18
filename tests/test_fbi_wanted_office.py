import pytest

# main function
def fbi_wanted_office(field_offices = None):
    ''' This function allows you to search for all FBI wanted people by administrative region.
    Parameter
    ----------
    field_offices : string
      A lowercase city names without space.
      Could be one of: 'losangeles', 'phoenix', 'pittsburgh','washingtondc'..., or None.

    Returns
    -------
    Pandas.Dataframe
    The information of the FBI wanted people in the administrative region.
    '''
    import requests
    import json
    import os
    import pandas as pd
    from requests.exceptions import HTTPError

    office_options = ['saltlakecity', 'losangeles', 'phoenix', 'pittsburgh', 'sanjuan',
                      'albuquerque', 'houston', 'honolulu', 'tampa', 'chicago',
                      'louisville', 'sacramento', 'washingtondc', 'detroit',
                      'lasvegas', 'columbia', 'philadelphia', 'jacksonville', 'miami',
                      'cleveland', 'richmond', 'newhaven', 'seattle', 'cincinnati',
                      'portland', 'dallas', 'boston', 'minneapolis', 'newark',
                      'sanfrancisco', 'newyork', 'omaha', 'atlanta', 'albany',
                      'kansascity', 'denver', 'mobile', 'buffalo', 'elpaso',
                      'littlerock', 'sandiego', 'milwaukee', 'baltimore', 'neworleans',
                      'charlotte', 'indianapolis', 'oklahomacity', 'norfolk', 'stlouis',
                      'knoxville', 'birmingham', 'springfield', 'memphis', 'jackson',
                      'sanantonio', None]
    
    if field_offices not in office_options:
        raise ValueError("City name not found")

    # experiment
    params_test = {'field_offices': field_offices}
    
    try:
        response_example  = requests.get('https://api.fbi.gov/wanted/v1/list', params = params_test)
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Other error: {err}')
    
    # request for all the data from multiple pages
    df_all = pd.DataFrame()
    for i in range(1,51):
        params={'field_offices': field_offices,
                'page': i}
#         print(i)
        response  = requests.get('https://api.fbi.gov/wanted/v1/list', params = params)
#         print(response.status_code)
        data = json.loads(response.content)
        df = pd.DataFrame.from_dict(data['items'], orient='columns')
        df['name'] = pd.Series([i.lower().split(" -", 1)[0].title() for i in df['title']])
        # select some columns of meaningful information 
        vars = ['name', 'status', 'sex', 'nationality', 'race', 'hair', 'eyes', 'height_max', 'height_min', 'scars_and_marks',
                'dates_of_birth_used', 'place_of_birth', 'occupations', 'languages', 'aliases', 
                'subjects', 'field_offices', 'url', 'reward_max', 'warning_message']
        df = df[vars]
#         print(len(df))
        df_all = df_all.append(df)
#         print(len(df_all))
        if len(df) < 20:
            break
            
#     display(df_all)
    print(f"{len(df_all)} records retrieved.") 
    
    # tranform the 2 columns to series (was a column of list objects)
    # 1) 'subjects'
    sub = []
    for s in df['subjects']:
        if s is not None:
            s = s[0]
            sub.append(s)
    df_all['subjects'] = pd.Series(sub)
    # 2) 'field_offices'
    fos = []
    for fo in df['field_offices']:
        if fo is not None:
            fo = fo[0]
            fos.append(fo)
    df_all['field_offices'] = pd.Series(fos) 
    return df_all

# test function
def test_fbi_wanted_office(field_offices = None):
    import pandas as pd
    from pandas.testing import assert_frame_equal # <-- for testing dataframes
    import pickle 
    with open('data/test_office.pkl', 'rb') as file:    
        expected = pickle.load(file)
    
    actual = fbi_wanted_office(field_offices = "honolulu")
    assert_frame_equal(expected, actual)
