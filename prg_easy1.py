def length_of_last_word(x):
  #Split the input string into a list of words

  words = x.split()
 #Check if the list of words is empty

  if not words:
    #If the list is empty, return 0
    return 0
  
  #Return the length of the last word in the list of words
  return len(words[-1])

#Get user input
x= input("Enter a string: ")

#Call the length_of_last_word function with the input string as an argument
result = length_of_last_word(x)

#Print the result, indicating the length of the last word in the input string
print("The length of the last word is:", result)
