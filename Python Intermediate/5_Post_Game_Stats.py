listwithdict=[
{'name':'ABC','position':'12','jerseynum':'02'},
{'name':'DEF','position':'18','jerseynum':'08'},
{'name':'GHI','position':'16','jerseynum':'06'}]  # list of dictionaries
for player in listwithdict:
  print(f'Position of Player = {player["position"]} \n')

list1=[{'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2},
{"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3}]
for i in listwithdict:
  if i['name']=='ABC':
    i['position']=13
# 1st way to update
print("After the Upadate : ")
print(listwithdict[0])
# 2nd  way to Update 
list1[0]["yards_gained"]+=50
print(list1[0]["yards_gained"])
# Calculate AVG Statistics
#print(len(list1))

l=len(list1)
sum1=0
sum2=0
for i in list1:
  sum1+=i["yards_gained"]
  sum2+=i["touchdowns"]

result1=sum1/l
result2=sum2/l
print("Average Yards Gained:", int(result1))
print("Average Touchdowns:", result2)


