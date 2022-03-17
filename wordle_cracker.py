# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 03:15:42 2022

@author: Haris.Mallick
"""

from english_words import english_words_lower_alpha_set

print(len(english_words_lower_alpha_set)) #25463 words

# file = open('English_words.txt') #only use this file once code is optimised. Has 10x more words!
##Append every 6-letter word in English to an array

six_letter_list = []

# for line in file:
#     word = line.strip()
#     if len(word) == 6:
#         six_letter_list.append(word)

for word in english_words_lower_alpha_set:
    if len(word) == 6:
        six_letter_list.append(word)
        
print(len(six_letter_list)) #29874 6-letter words from .txt; 3909 from english_words
#print(six_letter_list)

# all_letters = [
#     'a','b','c', 'd','e', 'f', 'g', 'h', 'i', 'k', 'l', 'm','n','o','p','r','s','t',
#     'u', 'v','w','x','y','z'
#     ]

#ignore j and q -- least used letters in english language

## Append words with all unique letters to a new array (except j, q)
unique_letter_words = []
i = 0

while i < len(six_letter_list):
    
    x = six_letter_list[i]
    x_ascii_sort = sorted(x)    #create an array of letters in x, sorted based on ASCII
    dups = False
    j_q_check = False
    
    for ii in range(len(x_ascii_sort)-1):
        if x_ascii_sort[ii] == x_ascii_sort[ii+1]:
            dups = True
    
    for letter in x_ascii_sort:
        if letter == 'j' or letter == 'q':
            j_q_check = True
        
    if dups == False and j_q_check == False:
        unique_letter_words.append(x)
        # for letter in x:
        #     all_letters.remove(letter)
                
    i += 1
        
        
print(len(unique_letter_words))    #1847 words (13308 from the text file)    
#print(unique_letter_words)

##Nested for loops to identify word combos using unique letters each and covering 24 of 26 English letters

letter_coverage = []
for word in unique_letter_words:
    temp_list = []
    temp_list.append(word)
    
    for i in range(len(unique_letter_words)-1):
        temp_list.append(unique_letter_words[i])
        concat_string = ''.join(temp_list)
        concat_sorted = sorted(concat_string)
        dups = False
        for ii in range(len(concat_sorted)-1):
            if concat_sorted[ii] == concat_sorted[ii+1]:
                dups = True
                
        if dups == True:
            temp_list.pop()
            
        if len(temp_list) == 3: #setting this variable to 4, ie, 4-unique-lettered words returns empty list
            letter_coverage.append(temp_list)
            break
        
        i += 1

print(letter_coverage)

########## Tried recursive to make code faster ###########
#Error: Kernel restart

# def recur_search(arr, j=0):
#     letter_coverage = []
#     if j < len(arr):
#         #letter_coverage = []
#         temp_list = []
#         temp_list.append(arr[j])
        
#         for i in range(len(arr)-1):
#             temp_list.append(arr[i])
#             concat_string = ''.join(temp_list)
#             concat_sorted = sorted(concat_string)
#             dups = False
#             for ii in range(len(concat_sorted)-1):
#                 if concat_sorted[ii] == concat_sorted[ii+1]:
#                     dups = True
                    
#             if dups == True:
#                 temp_list.pop()
                
#             if len(temp_list) == 3:
#                 letter_coverage.append(temp_list)
#                 break
            
#             i += 1
            
#         recur_search(arr, j=j+1)
#     return letter_coverage

# word_search = recur_search(unique_letter_words)    
# print(word_search)
# print(len(word_search)) #315 combinations with j and q; 281 combinations without j and q


####### Random stuff to test Python functionality ##########

## This code is returning an empty list when searching for 4 words with unique letters
## Code working when searching for 3 words. This means we can find 6 letter words with 18 unique letters
## But cannot find 6-letter words with 24 unique letters.
## Might be worth trying another english word library with more words.

# st = 'roger'#'haris' 'roger'
# dups = False
# st_ascii = sorted(st)
# #the sorted() is generally used to sort a given list of elements of the same type.
# #for strings, they are arranged in ascending order of their ascii value.
# print(st_ascii)
# for i in range(len(st_ascii)-1):
#     if st_ascii[i] == st_ascii[i+1]:
#         dups = True
        
# if dups == True:
#     print(f'There are duplicate letters in {st}')

# else:
#     print(f'{st} has unique letters')

# test = set()
# test.add('a')
# test.add('z')
# print(test)

# test = ['haris', 'mallick', 'abda']
# test.pop()
# print(test)
# test2 = ''.join(test)
# print(test2)
# test3 = sorted(test2)
# print(test3)
# abc = []
# abc.append(test)
# print(abc)



# def test_func():
#     test_list = []
#     for num in range(10):
#         #print(num)
#         test_list.append(num)
#     return test_list

# x = test_func()
# print(x)















