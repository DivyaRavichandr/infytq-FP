def create_largest_number(number_list):
    largest_number=0
    largest_number1=0
    largest_number2=0
    largest_number=sorted(number_list,reverse=True)
    largest_number1=str(largest_number).strip('[]')
    largest_number2=str(largest_number1).strip(",")
    return largest_number2
    


largest_number=create_largest_number(number_list=[23,45,67])
print(largest_number2)
