# 1. This function allows you search for all FBI wanted people information by appearance features.

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
    import numpy as np
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
        df['name'] = pd.Series([i.lower().split(" -", 1)[0].title() for i in df['title']])
        # select some columns of meaningful information 
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


# 2. This function allows you search for all FBI wanted people information by administrative region (city name).
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
        raise ValueError("City name not found. Expect a lowercase city names without space.")

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
    return df_all


# 3. This function allows you download the posters of the FBI wanted people by appearance features.

def fbi_poster_appearance(eyes = None, hair = None, race = None):
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
    
    # 1. get urls
    import requests
    import json
#     import os
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
        # keep only the id, name and url
        vars = ['uid', 'title', 'url']
        df = df[vars]
        df_all = df_all.append(df)
        if len(df) < 20:
            break
    
    # 2. download posters
    from urllib.request import urlretrieve
    import re
    url_list = [f"{url}/@@download.pdf" for url in df_all['url']]
    n = len(url_list)
    for url in url_list:
        poster_data = requests.get(url).content
        pattern = r'[a-z]+-{0}[a-z]+[a-z]+-[a-z]+'
        name_list = re.findall(pattern, url)
        name = '_'.join(re.findall(pattern, url))
#         print(name)

        with open(f"{name}.pdf", 'wb') as handler:
            handler.write(poster_data)
    print(f"Download completed. {n} posters downloaded.")