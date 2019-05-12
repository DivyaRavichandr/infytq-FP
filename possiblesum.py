def find_pairs_of_numbers(num_list,n):
    count=0
    for i in range(0,s):
        for j in range(i+1,s):
            if(num_list[i]+num_list[j]==n):
                count+=1
    return count        

num_list=[1, 2, 4, 5, 6]
s=len(num_list)
n=6
print(find_pairs_of_numbers(num_list,n))
