def sum_all(function, data):
    result_sum=0;
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum
 #Remove pass and write the logic here


list_of_nos= [100,200,300,500,1040]

greater =lambda x : x>10 #Write the lambda expression for question1

divide = lambda x : ((x%10==0) and (x<=100))#Write the lambda expression for question2

range_of_values = lambda x : (25<=x<=50)#Write the lambda expression for question3


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
