# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TPGc9u0RJQPZdPjGK7PbNZlz6WSrRfzh
"""

import pickle
import numpy as np
import pandas as pd



user = pd.read_csv("Users.csv" , encoding='latin-1')
book = pd.read_csv("Books.csv", encoding='latin-1')
area = pd.read_csv("Ratings.csv", encoding='latin-1')

# Adding Pickle File
adult = pd.read_pickle('age_adult.pkl')
child = pd.read_pickle('age_child.pkl')
young = pd.read_pickle('age_young.pkl')
other = pd.read_pickle('age_other.pkl')
elder = pd.read_pickle('age_elder.pkl')
teen = pd.read_pickle('age_teen.pkl')
usa = pd.read_pickle('area_usa.pkl')
canada = pd.read_pickle('area_canada.pkl')
uk = pd.read_pickle('area_uk.pkl')
australia = pd.read_pickle('area_australia.pkl')
germany = pd.read_pickle('area_germany.pkl')
others = pd.read_pickle('area_others.pkl')

# New
new_adult = pd.read_pickle('new_adult.pkl')
new_child = pd.read_pickle('new_children.pkl')
new_young = pd.read_pickle('new_youngster.pkl')
new_other = pd.read_pickle('new_other.pkl')
new_elder = pd.read_pickle('new_elder.pkl')
new_teen = pd.read_pickle('new_youngster.pkl')
new_usa = pd.read_pickle('new_usa.pkl')
new_canada = pd.read_pickle('new_canada.pkl')
new_uk = pd.read_pickle('new_uk.pkl')
new_spain = pd.read_pickle('new_spain.pkl')
new_germany = pd.read_pickle('new_germany.pkl')
new_others = pd.read_pickle('new_others.pkl')

user

def create_result(s,x):
    ISBN = []
    rating = []

    for i in s[s['user-2'] == x].loc[:,'user-1']:
        for j in area[(area['User-ID'] == i)].index:
            k = area.loc[j,'ISBN']
            l = area.loc[j,'Book-Rating']
            ISBN.append(k)
            rating.append(l)

    result = pd.DataFrame(
        {
            'ISBN' : ISBN,
            'rating' : rating
        }
    )

    return result

def get_ISBN(x):
    d = []
    for i in area[(area['User-ID'] == x)].loc[:,'ISBN'].values:
        d.append(i)

    return d

def drop(a,b):

    drop = []

    for i in range(len(a)):
        for j in b:
            c = a.loc[i,'ISBN']
            if c == j:
                drop.append(i)

    return drop

def fillter_ISBN(x, y):

    x.drop(index=y, inplace= True)
    x.drop_duplicates(inplace=True)

    return x

def set_name(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Book-Title'].values[0]

def set_Author(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Book-Author'].values[0]

def set_Publisher(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Publisher'].values[0]

def set_Image(x):
    if book[book['ISBN'] == x].shape[0] == 0:
        return np.nan
    else:
        return book[book['ISBN'] == x].loc[:,'Image-URL-L'].values[0]

def predect(similarity,ISBN):

    o = create_result(similarity,ISBN)
    k = get_ISBN(ISBN)
    n = drop(o,k)
    e = fillter_ISBN(o,n)
    e = e.sort_values(by='rating', ascending= False).head(75)
    e['name'] = e['ISBN'].apply(lambda x: set_name(x))
    e['auther'] = e['ISBN'].apply(lambda x: set_Author(x))
    e['publisher'] = e['ISBN'].apply(lambda x: set_Publisher(x))
    e['image'] = e['ISBN'].apply(lambda x: set_Image(x))
    e.dropna(inplace=True)

    return e.sort_values(by='rating', ascending= False).head(5)

def get_detail(x):
    area = user[user['User_Id'] == x].loc[:,'area'].values[0]
    age = user[user['User_Id'] == x].loc[:,'age'].values[0]
    u_type = user[user['User_Id'] == x].loc[:,'type'].values[0]

    return area,age,u_type

user

def pred_age(user_id):

    age = get_detail(user_id)[1]
    type = get_detail(user_id)[2]

    try:

        if type == 'old':
            if age == 'Adult':
                df_age = predect(adult,user_id)
            elif age == 'other':
                df_age = predect(other,user_id)
            elif age == 'Youngster':
                df_age = predect(young,user_id)
            elif age == 'Teenager':
                df_age = predect(teen,user_id)
            elif age == 'Elder':
                df_age = predect(elder,user_id)
            elif age == 'Children':
                df_age = predect(child,user_id)

        elif type == 'new':
            if age == 'Adult':
                df_age = new_adult
            elif age == 'other':
                df_age = new_other
            elif age == 'Youngster':
                df_age = new_young
            elif age == 'Teenager':
                df_age = new_teen
            elif age == 'Elder':
                df_age = new_elder
            elif age == 'Children':
                df_age = new_child

    except:
        if age == 'Adult':
            df_age = new_adult
        elif age == 'other':
            df_age = new_other
        elif age == 'Youngster':
            df_age = new_young
        elif age == 'Teenager':
            df_age = new_teen
        elif age == 'Elder':
            df_age = new_elder
        elif age == 'Children':
            df_age = new_child

    if df_age.shape[0] == 0:
        if age == 'Adult':
            df_age = new_adult
        elif age == 'other':
            df_age = new_other
        elif age == 'Youngster':
            df_age = new_young
        elif age == 'Teenager':
            df_age = new_teen
        elif age == 'Elder':
            df_age = new_elder
        elif age == 'Children':
            df_age = new_child
    return df_age

new_adult = pd.read_pickle('new_adult.pkl')
new_child = pd.read_pickle('new_children.pkl')
new_young = pd.read_pickle('new_youngster.pkl')
new_other = pd.read_pickle('new_other.pkl')
new_elder = pd.read_pickle('new_elder.pkl')
new_teen = pd.read_pickle('new_youngster.pkl')
new_usa = pd.read_pickle('new_usa.pkl')
new_canada = pd.read_pickle('new_canada.pkl')
new_uk = pd.read_pickle('new_uk.pkl')
new_spain = pd.read_pickle('new_spain.pkl')
new_germany = pd.read_pickle('new_germany.pkl')
new_others

def pred_area(user_id):

    area = get_detail(user_id)[0]
    type = get_detail(user_id)[2]

    if type == 'old':
        if area == 'usa':
            return predect(usa,user_id)
        elif area == 'other':
            return predect(others,user_id)
        elif area == 'canada':
            return predect(canada,user_id)
        elif area == 'unitedkingdom':
            return predect(uk,user_id)
        elif area == 'germany':
            return predect(germany,user_id)
        elif area == 'australia':
            return predect(australia,user_id)

    elif type == 'new':
        if area == 'usa':
            return new_usa
        elif area == 'canada':
            return new_canada
        elif area == 'unitedkingdom':
            return new_uk
        elif area == 'germany':
            return new_germany
        elif area == 'australia':
            return new_spain
        elif area == 'other':
            return new_others

def if_area_empty(x,user_id):

    area = get_detail(user_id)[0]

    if x.shape[0] == 0:
        if area == 'usa':
            x = new_usa
        elif area == 'canada':
            x = new_canada
        elif area == 'unitedkingdom':
            x = new_uk
        elif area == 'germany':
            x = new_germany
        elif area == 'australia':
            x = new_spain
        elif area == 'other':
            x = new_others

    else:
        return x

    return x

get_detail(278857)

create_result(usa,278857)

usa

usa[usa['user-2'] == 278857]

predect(usa,278857)

149084 , 88122

a = pred_area(152)
if_area_empty(a,152)

a



b = pred_age(1)

b

book.head()

new['Country'].value_counts()

new_other = new.iloc[[0,26,34,36,42],:]

new_others