class Solution:
  def kidswithcandies(self,candies,extracandies):
    maximum=max(candies)
    answer=[]
    for candy in candies:
      if candy+extracandies>=maximum:
        answer.append(True)
      else:
        answer.append(False)
    return answer






#main part
candies=list(map(int,input().split()))   # by default .split() separetes the input wherever there is whitespace,especially spaces
extracandies=int(input())
#object create
obj=Solution()
ans=obj.kidswithcandies(candies,extracandies)
print(ans)
