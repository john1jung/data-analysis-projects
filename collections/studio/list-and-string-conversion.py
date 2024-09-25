proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
print("," in proto_list1)


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
list1_split =  proto_list1.split(',')
print(list1_split)

list1_split.reverse()
print(list1_split)

joined1 = ",".join(list1_split)
print(joined1)
  
# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
list2_split = proto_list2.split(';')
print(list2_split)

list2_split.sort()
print(list2_split)

alpha2 = ",".join(list2_split)
print(alpha2)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
list3_split = proto_list3.split()
print(list3_split)

list3_split.sort(reverse = True)
print(list3_split)

reverse_alpha3 = ",".join(list3_split)
print(reverse_alpha3)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “codeb”, making sure that the extra spaces are NOT part of the final string.
list4_split = proto_list4.split(', ')
print(list4_split)

list4_split.reverse()
print(list4_split)

joined4 = ','.join(list4_split)
print(joined4)



