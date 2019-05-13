def create_largest_number(number_list):
    result=''
    number=list(sorted(number_list,reverse=True))
    for i in number:
        result+=str(i)
    
    return int(result)
        
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
