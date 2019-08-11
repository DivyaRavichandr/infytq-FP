def sum_naturalnum(num):
  sum=0
  while(num!=0):
    sum+=num
    num-=1
  return sum
num=int(input())
print(sum_naturalnum(num))    
