def factorial(number):
    i=1
    f=1
   
    
    while(i<=number and number!=0):
        f=f*i
        i=i+1
    return f    


def find_strong_numbers(num_list):
    list1=[]
    for num in num_list:
        
        sum1=0
        temp=num
        while(num):
            number=num%10
            f=factorial(number)
            sum1=sum1+f
            num=num//10
        if(sum1==temp and temp!=0):
            list1.append(temp)
        
    return list1

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
