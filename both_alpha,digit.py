def alpha_digit(a):
  letter_falg=False
  number_flag=False
  for i in a:
    if i.isalpha():
      letter_flag=True
    if i.isdigit():
      number_flag=True
  return letter_flag and number_flag
a=input()
print(alpha_digit(a))  
