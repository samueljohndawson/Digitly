import random
import operator

ops = ['+', '-', '*', '/']
nums = [1, 2, 3, 4, 5]

ops_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

# shuffle the operators and numbers
random.shuffle(ops)
random.shuffle(nums)

print(nums[0])
print(ops[0])
print(nums[1])
print(ops[1])
print(nums[2])
print(ops[2])
print(nums[3])
print(ops[3])
print(nums[4])


ans = nums[0]
for i in range(len(nums)-1):
    ans = ops_dict[ops[i]](ans, nums[i+1])

print(ans)


# Manual method
# answer = ops_dict[ops[0]](nums[0], nums[1])
# answer = ops_dict[ops[1]](answer, nums[2])
# answer = ops_dict[ops[2]](answer, nums[3])
# answer = ops_dict[ops[3]](answer, nums[4])

# print(answer)

