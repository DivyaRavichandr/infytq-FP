def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    valid=0

    #Start writing your code here
    i=0
    for i in range(heads+1):
        j=heads-i
        if (2*i+4*j)==legs:
            chicken_count=i
            rabbit_count=j
            valid=1
    if valid==1:
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)
       
          
solve(38,131)
