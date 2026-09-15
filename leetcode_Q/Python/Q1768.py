#method  1
"""
from itertools import zip_longest
class solution:
  def merge(self,word1,word2):
    merge="".join(c1+c2  for c1,c2 in zip_longest(word1,word2,fillvalue=""))
    return merge
  
    


#main part
word1=input("enter word 1 complete:")
word2=input("enter word 2 complete:")
obj=solution() #obj create
result=obj.merge(word1,word2)
print(result)

#method  2

class solution:
  def merge(self,word1,word2):
    result=""
    for i in range (max(len(word1),len(word2))):
      if i<len(word1):
        result=result+word1[i]
      if i<len(word2):
        result=result+word2[i]
    return result
  
word1=input("enter word 1 complete:")
word2=input("enter word 2 complete:")
obj=solution() #obj create
ans=obj.merge(word1,word2)
print(ans)
"""

#method 3
class solution:
  def merge(self,word1,word2):
    result=""
    i=0
    j=0
    while(i<len(word1) or j<len(word2)):
      if i<len(word1):
        result=result+word1[i]
        i=i+1
      if j<len(word2):
        result=result+word2[j]
        j=j+1

    return result
word1=input("enter word 1 complete:")
word2=input("enter word 2 complete:")
obj=solution() #obj create
ans=obj.merge(word1,word2)
print(ans)
