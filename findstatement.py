def check_value(message,num):
    msg=message[:num]
    return len(msg)

#function call statement
print("Result:", result)PythonCopy

result=check_value(‘Infosys’,3)

result=check_value(4,'Infosys‘)

result=check_value('Infosys',len('Infosys'))

result=check_value('Infosys',4)

result=check_value('Infosys',5)



Your answer is Right



In this option, function check_value() is invoked by passing a string ('Infosys') followed by an integer(4).
Inside the function, line 2, assigns the value 'Info' to msg thereby returning 4 to the calling block.
Hence this is the answer.
