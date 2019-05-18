res1=' '
res2=' '
def even(data):
    for i in sample_data:
        if i%2==0:
            res1=res1[i]
    return res1

def odd(data):
    for i in sample_data:
        if i%2!=0:
            res2=res2[i]
    return res2
    
def sum_of_numbers(list_of_num,filter_func=None):
    result_sum=0
    for num in sample_data:
        result_sum=result_sum+num
            
    return result_sum
    if num not in sample_data:
        result_sum=result_sum+num
    return result_sum    
        
    

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
