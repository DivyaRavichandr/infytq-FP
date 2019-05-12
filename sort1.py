list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count=0 
    for i in list_of_marks:
        if i>=12:
            count=count+1
            find_more_than_average=(count/10)*100
    return find_more_than_average        

def sort_marks():
    sort_marks=list(sorted(list_of_marks))
    return sort_marks
def generate_frequency():
    list1=[ ]
    i=0
    for i in sort_marks:
        if i<=25:
            sort_marks.insert( i,1)
            i+=1
        else:
            sort_marks.insert(i,0)
    return list1  
    

print(find_more_than_average())
print(sort_marks())
print(generate_frequency())
