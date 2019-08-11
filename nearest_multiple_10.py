def nearest(n):
  a=(n//10)*10
  b=a+10
  return(a if n-a>b-n else b)
n=int(input(" "))
print(nearest(n))  
