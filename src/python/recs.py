import numpy as np
import pandas as pd
import math
# from collections import Counter
# from sklearn.model_selection import train_test_split
import operator
import sys

print("working")

def age_group(age):
    if 17<= int(age) <=22:
        return 'G1'
    elif 23<= int(age) <=27:
        return 'G2'
    elif 28<= int(age) <=33:
        return 'G3'
    elif 34<= int(age) <=40:
        return 'G4'
    elif 41<= int(age) <=50:
        return 'G5'
    elif 51<= int(age) <=60:
        return 'G6'
    elif 61<= int(age) <=70:
        return 'G7'
    elif 71<= int(age) <=80:
        return 'G8'
    elif 81<= int(age) <=90:
        return 'G9'

def get_age_sim(u1, df, data):
    if df.loc[u1]['Age'] == data[0]:
        return 1
    return 0

def get_occupation_sim(u1, df, data):
    if df.loc[u1]['Occupation'] == data[1]:
        return 1
    return 0

def get_gender_sim(u1, df, data):
    if df.loc[u1]['Gender'] == data[2]:
        return 1
    return 0

def get_location_sim(u1, distance_df, data):
    u1_loc = df.loc[u1]['Locality ']
    u2_loc = data[3]
    u1_distance = list(distance_df[u1_loc])
    u2_distance = list(distance_df[u2_loc])
    
    sumxx, sumyy, sumxy = 0, 0, 0
    
    for i in range(len(u1_distance)):
        x = u1_distance[i]
        y = u2_distance[i]
        
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
        
    return sumxy/math.sqrt(sumxx*sumyy)

def create_sim_array(df, data):
    sim_dic = {}
    for i in range(len(df)):
        occ_age_gen_sim = get_age_sim(i,df, data) * get_occupation_sim(i,df, data) * get_gender_sim(i,df, data)
        location_sim = get_location_sim(i, distance_df, data)

        sim_dic[df.iloc[i]['userId']] = occ_age_gen_sim * location_sim
        
    sorted_dic = sorted(sim_dic.items(), key=operator.itemgetter(1), reverse=True)
                
    return sorted_dic

def get_sim_user(data, k):
    data[0] = age_group(data[0])
    sim_dic = create_sim_array(df, data)
    arr = []
    for i in range(k):
        arr.append(sim_dic[i][0])
        
    return arr

distance_df = pd.DataFrame()

distance_df[' '] ='ND,ED,WD,SD'.split(',') 

distance_df['ND'] = [0, 35, 25, 48]
distance_df['ED'] = [35, 0, 40, 26]
distance_df['WD'] = [25, 40, 0, 33]
distance_df['SD'] = [48, 25, 32, 0]

df = pd.DataFrame()
df['userId'] = range(1,11)

df['Occupation'] = 's,s,j,s,j,j,s,s,j,s'.split(',')

df['Age'] = [18, 23, 30, 21, 27, 26, 21, 20, 32, 23]
df['Gender'] = 'm,f,m,m,f,m,f,m,m,m'.split(',')
df['Locality '] = 'ND,SD,ND,WD,ND,ED,ED,SD,WD,ND'.split(',')


df['Age'] = df['Age'].apply(age_group)

print(get_sim_user(sys.argv[1:], 5))