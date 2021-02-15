import requests_with_caching
import json


def get_movies_from_tastedive(name):
        base_url = 'https://tastedive.com/api/similar'
        params = {}
        params['q'] = name
        params['type'] = 'movies'
        params['limit'] = 5
        tastedive_req = requests_with_caching.get(base_url, params=params)
        return tastedive_req.json()
    

def extract_movie_titles(d):
    titles = d['Similar']['Results']
    new_lst = []
    for title in titles:
        new_lst.append(title['Name'])
    return new_lst
        
        
def get_related_titles(lst):
    n_l = []
    for i in lst:
        n_l.append(extract_movie_titles(get_movies_from_tastedive(i)))
    nn_l = []
    for u in n_l:
        for j in u:
            if j not in nn_l:
                nn_l.append(j)
    return nn_l
    
def get_movie_data(title):
    base_url = 'http://www.omdbapi.com/'
    dict_param = {}
    dict_param['t'] = title
    dict_param['r'] = 'json'
    r = requests_with_caching.get(base_url, params=dict_param)
    return r.json()
    
def get_movie_rating(d):
    ratings = d['Ratings']
    for i in ratings:
        if i['Source'] == 'Rotten Tomatoes':
            b = i['Value']
            return int(b[:-1])
        
    return 0

def get_sorted_recommendations(lst):
    new_lst = get_related_titles(lst)
    recom = {}
    for i in new_lst:
        recom[i] = get_movie_rating(get_movie_data(i))
    return [i[0] for i in sorted(recom.items(), key=lambda x: (x[1], x[0]), reverse = True)]
        

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

