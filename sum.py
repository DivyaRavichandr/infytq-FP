def fun(n):
   stack = Stack(100)
   while (n > 0):
       stack.push(n%10)
       n =int (n/10)
   result=0
   while (not stack.is_empty()):
       result+=stack.pop()
   return result
