def fun(n):
   aqueue = Queue(100)
   for num in range(1, n+1):
       aqueue.enqueue(num)
   result=1
   while (not(aqueue.is_empty())):
       num = aqueue.dequeue()
       result*=num
   print(result)
