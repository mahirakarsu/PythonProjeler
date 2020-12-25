from array import array

def array_sum(nums_arr):
    sum_n =0
    for n in nums_arr:
        sum_n += n

    return sum_n


nums = array("b",[1,2,3,4,5])
print("original array : " , nums)

print(type(nums))

nums_arr = list(map(int,nums))

print(type(nums_arr))

result = array_sum(nums_arr)
print("sum of all elements of the said array: " , result)