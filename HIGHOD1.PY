def add(data):
    return data+2
def prod(data):
    return data*2
def main_fun(function1,function2, number_list):
    result_sum=0
    for num in number_list:
        if(num%3==0):
            result_sum=result_sum+function1(num)
        else:
            result_sum=result_sum+function2(num)
    return result_sum
number_list=[1,3,5,6]
print(main_fun(add, prod, number_list))PythonCopy
 15

 25

 28




Your answer is Right



As per this option, 25 is the value returned from main_fun() in line 5.
Execution starts from line 13 where number_list is initialized with [1,3,5,6]
Line 14 invokes main_fun() by passing functions add, prod and number_list
Inside the function, for all the numbers in number_list which are divisible by 3, add() is invoked by passing that number and result is added to result_sum. For all the remaining numbers, prod() is invoked by passing each of the those numbers and result is added to result_sum.
Thus for values 1 and 5, prod() is invoked and for values 3 and 6 add() is invoked resulting in value of result_sum as 
2 + 10 + 5 + 8 -> 25.
Hence this is the answer.
