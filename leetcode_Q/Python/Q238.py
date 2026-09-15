class solution:
  def productexceptself(self,nums):
    ans=[1]* len(nums)

    #prefix product
    ans[0]=1
    for i in range(1,len(nums)):
      ans[i]=ans[i-1] * nums[i-1]

    #suffix product
    suffix=1
    for i in range(len(nums)-2,-1,-1):
      suffix=suffix*nums[i+1]
      ans[i]=ans[i]*suffix

    return ans


nums=list(map(int,input().split()))
obj=solution()
result=obj.productexceptself(nums)
print(result)