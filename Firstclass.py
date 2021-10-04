from typing import Collection
import time
import random as rd

new_black=10
# print(new_black)
# print(type(new_black))

# float_me=0.5
# print(float_me,type(float_me))

# stringify="We had a down pour in Lagos 2 days ago"
# print(stringify,type(stringify))

# my_verdict=True
# print(my_verdict,type(my_verdict))

# random_stuff= ['music',"sports",True,99.9]
# print(random_stuff,type(random_stuff))

# Random_tuple= ('music',"sports",True,99.9)
# print(Random_tuple,type(Random_tuple))

# Random_curly= {'music',"sports",True,99.9,"music"}
# print(Random_curly,type(Random_curly))

# my_info={
#     "name":"Adam",
#     "gender":"male",
#     "age":12
# }
# print(my_info, type(my_info))


# data types str,bool,int,float

#1 convert string to integer
# word="15"
# number=int(word)
# print(number,type(number))
# works

#2 convert integer to string
# digit=10
# w_ord=str(digit)
# print(w_ord,type(w_ord))
# works

#3 convert string to bool
# Word="pawn"
# convert=bool(Word)
# print(convert,type(convert))
# works

# 4 convert bool to string
# c_onvert= True
# W_ord= str(c_onvert)
# print(W_ord,type(W_ord))
# works

#5 convert string to float
# Wo_rd="queen"
# dec_no=float(Wo_rd)
# print(dec_no,type(dec_no))
# failed

# 6 convert float to string
# Dec_no= 0.1
# Wor_d=str(Dec_no)
# print(Wor_d,type(Wor_d))
# works

#7 convert bool to integer
# Co_nvert= True
# num= int(Co_nvert)
# print(num, type(num))
# works

# 8 convert integer to bool
# Num= 10
# DEC_no= bool(Num)
# print(DEC_no,type(DEC_no))
# works

#9 convert bool to float
# DE_Cno= False
# con_Vert=float(DE_Cno)
# print(con_Vert,type(con_Vert))
# works

#10 convert int to float
# Num_ber=10
# Con_Vert=float(Num_ber)
# print(Con_Vert,type(Con_Vert))
# works

# 11 convert float to int
# COn_Vert= 0.1
# Num_Ber= int(COn_Vert)
# print(Num_Ber,type(Num_Ber))
# works

# 12 convert float to bool
# decimal_NO=0.1
# Convert_num= bool(decimal_NO)
# print(Convert_num,type(Convert_num))
# works


# data structures tuple,lists,set,dict,

# 1 convert tuple to list
# ARR= ("Bishop","G8",16)
# convert_ARR= list(ARR)
# print(convert_ARR,type(convert_ARR))
# works

# 2 convert list to tuple
# Arr=["Checkmate","pawn"]
# convert_Arr=tuple(Arr)
# print(convert_Arr,type(convert_Arr))
# works

# 3 convert tuple to set
# ARr=("pretty","natural",0.1)
# convert_ARr= set(ARr)
# print(convert_ARr,type(convert_ARr))
# works

# 4 convert set to tuple
# aRR= {"e1g5","castling",True}
# convert_aRR= tuple(aRR)
# print(convert_aRR,type(convert_aRR))
# works

# 5 convert tuple to dict
# I_E= ("Promtion","Pin","Stale")
# convert_IE= dict(I_E)
# print(convert_IE,type(convert_IE))
# failed

# # 6 convert dict to tuple
# Eg= {"Item":"Pen", "Color":"White"}
# convert_eg=tuple(Eg)
# print(convert_eg,type(convert_eg))
# works

# 7 convert list to set
# E_g= ["time","leg",0.1]
# convertE_g= set(E_g)
# print(convertE_g,type(convertE_g))
# works

# 8 convert set to list 
# EG_= {"Stand","Stair"}
# convert_EG= list(EG_)
# print(convert_EG,type(convert_EG))
# works

# 9 convert list to dict 
# run= ["one","two","three"]
# convert_run=dict(run)
# print(convert_run,type(convert_run))
# failed

# 10 convert set to dict
# Run= {"four ","five","hey"}
# convert_Run= dict(Run)
# print(convert_Run,type(convert_Run))
# failed

#11 dict to list
# r_un= {"name":"Val","age":19,"status":"single"}
# conver_trun= list(r_un)
# print(conver_trun,type(conver_trun))
# works

# 12 dict to set
# R_un= {"name":"Val","age":19,"status":"single"}
# convert_R= set(R_un)
# print(convert_R,type(convert_R))
# # works


#  Arithmetic
# my_mod= 33%4
# print(my_mod)

# my_quot=33//4
# print(my_quot)

# r_power= 5**4
# print(r_power)

# # comparison ooperators
first_num=67
secon_num=41

# nb float and integer arent considered


# quick_check= first_num==secon_num
# print(quick_check)

# quick_check= first_num !=secon_num
# print(quick_check)

quick_check= first_num =secon_num
# print(quick_check)

# feedback = (first_num<23) or (secon_num>first_num)
# print(feedback)

# feedback = (first_num%2==0) or (secon_num>first_num)
# print(feedback)

# feedback = ((first_num%2 !=0) or (secon_num>first_num)) and (secon_num==40)
# print(feedback)

# members  operations

# career= "she is a model"
# ouptu="m" in career
# ptu="mo" in career
# uptu="ml" in career
scores=[34,34,54,45]
# check= 34 in scores
# print(ouptu,ptu,uptu,check)

# first_phrase= "Hello"
# second_phrase="there, welcome"
# dull_sent= first_phrase+  " " + second_phrase
# print(dull_sent)

career= "She is a model who lives in california"
# desire_char= career[::2],career[5]
# print(desire_char)

age_limit= 10
# # report_template= "You cant gain access until you are ..{}.. years old".format(age_limit)
# report_template= f"You cant gain access until you are ..{age_limit}.. years old"

# print(report_template)

# Escape character
# source_of_income= 'the nation\'s curde oil'
# print(source_of_income)

# title method affects first charcater
first_cap= career.title()
# upper method affects all characters
fir_stcap= career.upper()
# print(fir_stcap,first_cap)

# endwith method
q_search=career.startswith("she"), career.endswith("model")
# .find method gives you -1
toSearch= career.find(" ")
# .index method gives you a value error
to_search= career.index("She")
# print(to_search)

#  a split string returns a list
trans_list= career.split(" ! ")
# print(trans_list)

# replace method
new_career= career.replace("california","Texas")
# print(new_career)

# strip method
trimmed= career.strip("she")
# print(trimmed)

# LIST
r_stuff= ["six",5,True,"pawn",7,"ten"]
# print(r_stuff[2])

# r_stuff[1]=10
# print(r_stuff)

r_stuff[2 : 5: 2]=[4,6]
# print(r_stuff)
# count method
# coutn_water= r_stuff.count("pawn")
# print(coutn_water)

r_stuff.extend(scores)
# print(r_stuff)

r_stuff.append("Check")
# print(r_stuff)

bac_list= r_stuff.copy()
# print(bac_list)

r_stuff.insert(0,"awesome")
# print(r_stuff)

# scores.sort()
# print(scores)

#  SETS
grocery_cart1={"Bread","Oranges","Jam","Fruit","Juice","Eggs","Butter","Cookies"}
grocery_cart2={"Eggs","Yam","Grapes","Cookies","Apple","Carrot","Bread","Ice cream"}


grocery_cart2.discard("Yam")
# .discard removes an item
grocery_cart2.add("Yoghurt")
# .add() adds an item
mergedcart= grocery_cart1.union(grocery_cart2)
#union unifies two sets and assigns to a new variable

# grocery_cart1.update(grocery_cart2)

backUP_CART1= grocery_cart1.copy()
backUP_CART2= grocery_cart2.copy()

cart1_only= grocery_cart1.difference(grocery_cart2)
#  a.differenve(b) gives you items that are unique to the first set

# grocery_cart2.difference_update(grocery_cart1)
# a.differenec_update(b) it does the difference then update a with that difference

common_groce=grocery_cart1.intersection(grocery_cart1)
# intersection() the common difference
# backUP_CART1.intersection_update(backUP_CART2)
# intersection_update, updates cart1 with items in common

taking_out_duplicates= grocery_cart1.symmetric_difference(grocery_cart2)
# symmetric difference, does a,diff(b) and reverse, hence giving you a joint set with unique values from a and unique values from b
grocery_cart1.symmetric_difference_update(grocery_cart2)

grocery_cart1.pop()

# print(taking_out_duplicates)
# print(common_groce)
# print(cart1_only)
#  print(mergedcart)
# print(grocery_cart1)
# print(grocery_cart2)
# print(backUP_CART1)



# ###DICTIONARY
# cust_info= {
#     "Name":["Mike Aubentraut","Uzor Chuks","Tom Whiteside","Mary Jane"],
#     "Gender":["Male","Male","Male","Female"],
#     "Age":[22,29,34,18],
#     "Nationality":["American","Nigerian","Canadian","Jamaican"]
# }

# all_names=cust_info["Name"]
# # access values usnig keys

# # .get does the same thing
# ex=cust_info.get("Nationality")

# # print(ex)
# # print(all_names)

# all_keys=cust_info.keys()
# all_val=cust_info.values()
# # .keys returns all keys in dict, .values returns all values in dict.
# all_entries=cust_info.items()
# # 
# # print(all_entries)
# # print(all_val)

# cust_info.update({"occupation":["Actor","Banker","Footballer","Experience Engineer"]})

# cust_info.pop("Age")
# cust_info.clear()
# # print(cust_info)

# #### BILT IN FUNCTIONS

# get_data= input(" Enter intgers here ")
# # to have access to the integers
# con_list= get_data.split(" ")
# to convert/change entries to proper integers

# con_list[0]=int(con_list[0])
# con_list[1]=int(con_list[1])
# con_list[2]=int(con_list[2])
# con_list[3]=int(con_list[3])
# con_list[4]=int(con_list[4])

# new_list=list(set(con_list))
# new_list.sort()

# output=new_list[-2]

# print(output)


# zip
f_list=["high","low","middle"]
s_list=[1,2,3]

zipped_objs=zip(f_list,s_list)

# print(list(zipped_objs))
#  if one list is longer than the other the joint list stops at the length of the smaller list 

modifier= lambda a : a.upper()
output= modifier("voice")
# print(output)

scores=[68,72,83,91]
updgraded_scores=map(lambda a:a+2,scores)
output=list(updgraded_scores)
# print(output)

num=[20,31,45,60,10,77]
my_sieve= filter(lambda a: a%2, num)
output=list(my_sieve)
# print(output)

rand_words= ["Emmanuel","Pizza","Corece","Smooth","Laptop","Screen"]
retain_e=filter(lambda a: "e" in a, rand_words)
output=list(retain_e)
# print(output)

my_sequence= range(10,25)
# print(list(my_sequence))

# print("hello")
# time.sleep(8)
# print("Done")
rd.seed(99)
rand_words= ["Emmanuel","Pizza","Corece","Smooth","Laptop","Screen"]



# rd.shuffle(rand_words)
rand_pick=rd.choice(rand_words)
# selected_items= rd.sample(rand_words,   3)

feedback= rd.randrange(14,44,2)
# print(feedback)

# Date time
from datetime import datetime as dt 
cu_date_and_time= dt.now()
current_year= dt.now().year
output=cu_date_and_time.strftime("%B %A")
# print(output)


ch_day= "25/12/2012"
conv_data= dt.strptime(ch_day,"%d/%m/%Y")
# print(conv_data.date())

notable_days= ["15/1/2021","14/2/2021","1/4/2021","29/5/2021","1/8/2021","25/12/2021"]
formt_days = map(lambda days: dt.strptime(days, "%d/%m/%Y").date(), notable_days)
# print(list(formt_days))

ids = ["Emmanuel","Pizza","Corece","Smooth","Laptop","Screen"]
retain_no= filter(lambda a: len(a)>=7,ids)
new=(list(retain_no))
output=bool(new)
# if new == True:
    # print("yes")
# else:
#    print("nope")

# get_data= input("Enter data:")
# if len(set(get_data))!=len(get_data):
    # print("there are dups")
# else:
        # print("nope no dups")


#  #### LOOPS 
# cracker = 0          
# while (cracker < 5):
#     if cracker==3:
#         print("Here is my ride outta the lopop")
#         break
#     else:     
#         print("cracker is less than five")
#     cracker+=1


###  GUESS GAME
# get_data= input("enter two integers here: ")
# # converted_list= get_data.split(" ")
# #converting to integers
# converted_list[0]= int(converted_list[0])
# converted_list[1]=int(converted_list[1])
# # randomly selecting an integer within the range
# random_integer= rd.randrange(converted_list[0],converted_list[1])
#time to guess
# while True:
#     user_guess= input("enter your integer: ")
#     if random_integer==int(user_guess):
#         print("You guess right")
#         break
#     elif int(user_guess) < random_integer:
#         print("guess to loo... try again")
#     elif int(user_guess) > random_integer:
#         print("guess too high.. try again")
#     else:
#         pass

##for Loop
new_word="Universe"
# for a in new_word:
    # print("home for all")

new_list=["Pop","Rock","country"]
# for item in new_list:
#     print(item)

scores= [68,90,78,71,83]
# for num in scores:
#     if num %2 ==0 :
#         print(f"{num} is an even number")
#     elif num%2 !=0:
#         print("{} is an odd number".format(num))
#     else:
#             pass

cust_info= {
    "Name":["Mike Aubentraut","Uzor Chuks","Tom Whiteside","Mary Jane"],
    "Gender":["Male","Male","Male","Female"],
    "Age":[22,29,34,18],
    "Nationality":["American","Nigerian","Canadian","Jamaican"]
}

for entry in cust_info.items():
    # print(entry)
    # print("\n")

    continents= ["Africa","Asia","North America","South America","Europe","Antartica","Australia"]
    countries=["Morocco","China","USA","Argentina","Croatia","Eskimo"]

    zipped_obj= zip(continents,countries)
    # for entry in zipped_obj:
        # print (entry)

    # for country_name, continent_name in zipped_obj:
        # print(country_name, continent_name)

# get_data=input("Enter integers here: ")
# con_list=get_data.split(" ")
# converting to integer
# for num in range(len(con_list)):
#     con_list[num]=int(con_list[num])
    
# for x in range(len(con_list)):
#     con_list[x] *= 1.1
#      conlist[x]= round(con_list[x],2)
# print(con_list)

# new_list=map(lambda a: int(a), con_list)
# output=list(map(lambda a:round (a*1.1,2),new_list))

# print(output)


# 2 - level nested loop
starters=["It's ","They are","They all are"]
nouns=["car","country","lady"]
adjectives=["fast","beautiful","awesome"]

# for qualifier in adjectives:
#     for word in nouns:
        # print(qualifier,word)

# for beginners in starters:
#     for qualifier in adjectives:
#         for word in nouns:
#             print(beginners,qualifier,word)
#     print("\n")




##List comprehenesion

scores=[60,62,77,64,57,66,91]
# updgraded_scores=[num+3 for num in scores]
# print(updgraded_scores)
# new_upgrade= [num + 3 for num in scores if num%2 == 0]
# print(new_upgrade)

new_list=[("Awesome",12),("Zebra",2),("Dawn",9),("new",4)]
sorted_list=sorted(new_list,key=lambda a : a[1])
# print(sorted_list)