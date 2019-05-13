ef find_duplicates(list_of_numbers):
    list_of_duplicates=[]
    #start writing your code here
    for i in range(a):
        for j in range(0,a):
            if i==j:
                list_of_duplicates.append(i)
    return list_of_duplicates            

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
a=len(list_of_numbers)
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
