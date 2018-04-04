def twoSum(nums, target):
        i = 0
        j = len(nums) - 1
        while(i < j):
            if (nums[i] + nums[j] == target):
                return [nums[i], nums[j]]
            elif(nums[i] + nums[j] < target):
                i += 1
            else:
                j -= 1
        return []

x = [1, 2, 5, 8, 10]
target = 10

result = twoSum(x, target)
print("result", result)
