#a function to detect a palindrome
def is_palindrome(k) :
  return k == k[: : - 1]

#K will be the input
k = 'food'
ans = is_palindrome(k)
if ans :
	print ('Yes')
else :
	print ('No')
  
