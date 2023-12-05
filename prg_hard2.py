def shortest_palindrome(s):
    #Function to check if a string is palindrome
    def is_palindrome(str):
        return str == str[::-1]
    #string to find the longest palindrome suffix
    for x in range(len(s), 0, -1):
        if is_palindrome(s[:x]):
            #string needs to be added in front to form a palindrome
            return s[x:][::-1] + s
#input from the user
a= input("Enter a string: ")
#obtain shortest palindrome
res = shortest_palindrome(a)
#print the result
print("Shortest palindrome:", res)
