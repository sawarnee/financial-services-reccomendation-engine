import numpy as np
import pandas as pd
import math
import operator
import sys

print("working!!")

df = pd.read_csv('C:/Users/kaka/Documents/NetBeansProjects/minor/src/python/newExpenditure Survey (3).csv')
df['userId'] = range(len(df['Age']))
distance_df = pd.read_csv('C:/Users/kaka/Documents/NetBeansProjects/minor/src/python/distance_matrix.csv')
main_df = df[['userId', 'Occupation', 'Age', 'Gender','Locality ']].copy()

offline_df = df[['userId', 'clothes (offline)', 'groceries (offline)', 'cosmetics (offline)',
       'medicines (offline)', 'breakfast, lunch or dinner ',
       'Rate your shopping from 1 to 5 (offline)']]

online_df = df[['userId', 'clothes (online)',
       'groceries (online)', 'cosmetics (online)', 'medicines (online)',
       'food items (online)', 'Rate your shopping from 1 to 5 (online)']]

expense_df = df[['userId', 'Monthly income', 'Monthly expenses: [Clothes and other wearables]',
       'Monthly expenses: [Groceries (all food items and drinks)]',
       'Monthly expenses: [Cosmetics]',
       'Monthly expenses: [Phone and internet usage (data/wifi)]',
       'Monthly expenses: [Movies]',
       'Monthly expenses: [Dinners and other outings]',
       'Monthly expenses: [Medicines and health checkup]',
       'Monthly expenses: [Sports activities and sports items]',
       'Monthly expenses: [Transportation]',
       'Monthly expenses: [Any other that is not mentioned]',
       'Yearly expenses: [Travel and tourism]',
       'Yearly expenses: [Home items (bed sheets, crockery etc)]',
       'Yearly expenses: [Gadgets and technology (Mobile, TV, Computer etc)]',
       'Yearly expenses: [Birthday parties and other functions]',
       'Yearly expenses: [Any other not mentioned above]']]

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
    sim_dic = create_sim_array(main_df, data)
    arr = []
    for i in range(k):
        arr.append(sim_dic[i][0])
        
    return arr

main_df['Age'] = main_df['Age'].apply(age_group)

user_data = sys.argv[1:]
# print(user_data)
user_data[0] = age_group(user_data[0])
user_data[-1] = ' '.join(x for x in user_data[-1].split('_'))

sim_users = get_sim_user(user_data, 5)

offline_shops = []
offline_shops_4 = []
online_websites = []
online_websites_4 = []
for i in sim_users:
    if offline_df.loc[i]['Rate your shopping from 1 to 5 (offline)'] == 5:
        offline_shops.append(i)
    elif offline_df.loc[i]['Rate your shopping from 1 to 5 (offline)'] == 4:
        offline_shops_4.append(i)
        
    if online_df.loc[i]['Rate your shopping from 1 to 5 (online)'] == 5:
        online_websites.append(i)
    elif online_df.loc[i]['Rate your shopping from 1 to 5 (online)'] == 4:
        online_websites_4.append(i)
        
for i in offline_shops_4:
    offline_shops.append(i)
    
for i in online_websites_4:
    online_websites.append(i)
        
# print('offline shops: {}, online websites: {}'.format(offline_shops, online_websites))


offline_shop_names = {'Clothes':set(), 'Groceries':set(), 'Cosmetics':set(), 'Medicines':set(), 'Food':set()}
online_websites_names = {'Clothes':set(), 'Groceries':set(), 'Cosmetics':set(), 'Medicines':set(), 'Food':set()}

for i in offline_shops:
    offline_shop_names['Clothes'].add(offline_df.loc[i]['clothes (offline)'])
    offline_shop_names['Groceries'].add(offline_df.loc[i]['groceries (offline)'])
    offline_shop_names['Cosmetics'].add(offline_df.loc[i]['cosmetics (offline)'])
    offline_shop_names['Medicines'].add(offline_df.loc[i]['medicines (offline)'])
    offline_shop_names['Food'].add(offline_df.loc[i]['breakfast, lunch or dinner '])
print('**************************** OFFLINE SHOPS **************************') 
print()
for i in offline_shop_names:
    print(i, offline_shop_names[i])
    print()
    print('------------------------------------------------------------------')
    

for i in online_websites:
    online_websites_names['Clothes'].add(online_df.loc[i]['clothes (online)'])
    online_websites_names['Groceries'].add(online_df.loc[i]['groceries (online)'])
    online_websites_names['Cosmetics'].add(online_df.loc[i]['cosmetics (online)'])
    online_websites_names['Medicines'].add(online_df.loc[i]['medicines (online)'])
    online_websites_names['Food'].add(online_df.loc[i]['food items (online)'])
print('**************************** ONLINE SHOPS **************************')
print()
for i in online_websites_names:
    print(i, online_websites_names[i])
    print()
    print('-------------------------------------------------------------')