# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
print(text[0:12])

# # 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[-12:-1])

# # 3. Print a slice of the middle 12 characters from 'text'.
print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.
# max_index = len(word)-1
# for index in range(max_index, -1, -1):
#    print(word[index])

# 1. Print 1 letter per line. (JJ solutions)
x=-1
for index in range(len(word)):
    print(word[x])
    x-=1

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
good = 'good'
new_word = ''
it = 0
for letter in good:
   new_word += good[-1+it]
   it -= 1
print( new_word)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
new_word = ''
it = 0
for letter in word:
   new_word += word[-1+it]
   it -= 1
print( new_word, ' | ', word)

# LC solutions ##
# 1
# max_index = len(word)-1
# for index in range(max_index, -1, -1):
#    print(word[index])

# # 2
# new_word = ""
# for index in range(max_index, -1, -1):
#    new_word += word[index]

# print(new_word)