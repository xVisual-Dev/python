import math
welcome = '''
Hello this my game 

i'm NP owner this project

'''
print(welcome)
stock = ["1", "1", "3", "4", "5", "6", "3", "2", "1", "1", "5", "6"]
redsock = [x for x in stock if x == "1"]
bluesock = [x for x in stock if x =="2"]
yellowsock = [x for x in stock if x =="3"]
blacksock = [x for x in stock if x =="4"]
whitsock = [x for x in stock if x =="5"]
other = [x for x in stock if x == "6"]

print("Pair Red sock is " ,math.floor(len(redsock))/2)
print("Pair Blue is ",math.floor(len(bluesock))/2)
print(stock[0:4])
print('"Do Not Do this"')