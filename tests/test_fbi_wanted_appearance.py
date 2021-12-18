import pytest

# main function
def fbi_wanted_appearance(eyes = None, hair = None, race = None):
    ''' This function allows you to search for all FBI wanted people by appearance and administrative region.
    Parameters
    ----------
    eyes : string
      The eye color of the suspect.
      Could be: 'brown', 'blond', 'black', or None.
    hair : string
      The hair color of the suspect.
      Could be: 'brown', 'green', 'blue', 'black' or None.
    race : string
      Race of the suspect.
      Could be one of: 'hispanic', 'native', 'white', 'black', 'asian' or None.

    Returns
    -------
    Pandas.Dataframe
    The information of the FBI wanted people with described looks.
    '''
    import requests
    import json
    import os
    import pandas as pd
    from requests.exceptions import HTTPError

    eyes_options = ['brown', 'green', 'blue', 'hazel', 'dark', 'black','', None]
    if eyes not in eyes_options:
        raise ValueError("Invalid eye color. Expecting one of 'brown', 'green', 'blue', 'hazel', 'dark', 'black' or None.")
    
    hair_options = ['brown', 'blond', 'black', 'gray','bald', '', None]
    if hair not in hair_options:
        raise ValueError("Invalid hair type. Expecting one of 'brown', 'blond', 'black', 'gray', 'bald' or None.")
    
    race_options = ['white', 'hispanic', 'native', 'black', 'asian', '', None]
    if race not in race_options:
        raise ValueError("Invalid type. Expecting one of 'white', 'hispanic', 'native', 'black', 'asian' or None.")
    
    # experiment
    params_test = {'hair': hair,
                   'eyes' : eyes,
                   'race': race}
    try:
        response_example  = requests.get('https://api.fbi.gov/wanted/v1/list', params = params_test)
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Other error: {err}')
    
    # request for all the data from multiple pages
    df_all = pd.DataFrame()
    for i in range(1,51):
        params={'hair': hair,
                'eyes' : eyes,
                'race': race,
                'page': i}
#         print(i)
        response  = requests.get('https://api.fbi.gov/wanted/v1/list', params = params)
#         print(response.status_code)
        data = json.loads(response.content)
        df = pd.DataFrame.from_dict(data['items'], orient='columns')
        # select some columns of meaningful information 
        df['name'] = pd.Series([i.lower().split(" -", 1)[0].title() for i in df['title']])
#         vars = ['uid', 'name', 'status', 
#             'sex', 'nationality', 'race', 'hair', 'eyes', 'height_max', 'height_min', 'scars_and_marks',
#             'dates_of_birth_used', 'place_of_birth', 'occupations', 'languages', 'aliases', 
#             'subjects', 'field_offices', 'description', 'additional_information', 'remarks', 'caution',
#             'url', 'modified', 'reward_max', 'warning_message']
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
    # 3) 'occupations'
    lo = []
    for o in df['occupations']:
        if o is not None:
            o = o[0]
            lo.append(o)
    df_all['occupations'] = pd.Series(lo) 
    # 4) 'aliases'
    la = []
    for a in df['aliases']:
        if a is not None:
            a = a[0]
            la.append(a)
    df_all['aliases'] = pd.Series(la) 
    
    
    return df_all




# test function
# def test_fbi_wanted_appearance():
#     import pandas as pd
#     from pandas.testing import assert_frame_equal # <-- for testing dataframes
#     eyes = "brown"
#     hair = "blond"
#     race = "white"
    
#     import pickle 
#     with open('data/test_appearance.pkl', 'rb') as file:    
#         expected = pickle.load(file)
    
#     actual = fbi_wanted_appearance(eyes = "brown", hair = "blond", race = "white")
#     assert_frame_equal(expected, actual)

def test_fbi_wanted_appearance():
    import pandas as pd
    from pandas.testing import assert_frame_equal # <-- for testing dataframes
    eyes = "brown"
    hair = "blond"
    race = "white"
    
    import os
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_data_url = os.path.join(directory, 'data/test_appearance.pkl')
    import pickle 
    with open(test_data_url, 'rb') as file:    
        expected = pickle.load(file)
    
    actual = fbi_wanted_appearance(eyes = "brown", hair = "blond", race = "white")
    assert_frame_equal(expected, actual)

