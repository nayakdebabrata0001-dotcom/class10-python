def sum_of_list(nums):
    total = 0
    for n in nums:
        total = total + n
    return total


print(sum_of_list([1,2,3,4]))

def find_max(nums):
    max_num=nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num
    
    
print(find_max([5,7,3,9,39]))


def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
        
table(7)
