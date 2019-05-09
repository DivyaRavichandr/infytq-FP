count=0
def find_winner_of_the_day(*match_tuple):
    for i in find_winner_of_the_day:
        if i==x:
            count+=1
            i=i+1
            
    
    

#Invoke the function with each of the print statements given below
#find_winner_of_the_day=("Team1","Team2","Team1")

find_winner_of_the_day=("Team1","Team2","Team2","Team1","Team2")
x=max(find_winner_of_the_day,key=find_winner_of_the_day.count)
if x=="Team1":
  print("Team1")
else:
  print("Team2")
