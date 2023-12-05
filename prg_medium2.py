def find_major_elements(nums):
    #Check if the input list is empty, if so, return an empty list
    if not nums:
        return []
    #Initialize an empty dictionary to store element counts
    count = {}
    #Iterate through the list and update the element counts dictionary
    for num in nums:
        count[num] = count.get(num, 0) + 1
    #Initialize a list to store the major elements
    k = []
    #Iterate through the element counts dictionary and find elements appearing more than ⌊ n/3 ⌋ times
    number = len(nums) // 3
    for num, count in count.items():
        if count > number:
            k.append(num)
    # Return the final result
    return k
#Get user input as a list
user_in = input("input: ")
nums = eval(user_in)
#Find the major elements
k = find_major_elements(nums)
#Print the result
print("Elements appearing more than ⌊ n/3 ⌋ times:", k)
