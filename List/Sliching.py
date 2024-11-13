nums = [i for i in range(10)] #list comprehension
print(nums)

first_num = nums[0:5] #0 to 4 print
last_num = nums[5:]   #5 to last
arr = nums[:]          #whole in sliching
odd_num = nums[1::2]   #odd print
print(first_num)
print(last_num)
print(arr)
print(odd_num)
revers_num = nums[-1::-1]       #reverse
#or reverse_num = nums[::-1]
print(revers_num)