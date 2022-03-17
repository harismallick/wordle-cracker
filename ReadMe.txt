Here's a link to the 6-letter wordle game:
https://www.wordle2.in/

The game gives you six attempts to guess the 6-letter word of the day.
There are 26 letters in the English alphabet, which means in theory, you should be able to cover 24 of the letters in 4 6-letter words.

The aim of this programme is to parse through every word in the english language and generate a list of 6-letter words, where every letter in the word is unique.
Once such a list is achieved, identify 4 words, each containing different letters of the English alphabet. The programme should output this subarray(s) of 4 words.

Please see the attached python file for my take on solving this problem.

Current Issue: I can only get the code to output 3-word subarrays, each containing unique letters. When I set the condition to find a 4-word subarray, the code outputs an empty array.
I believe that this is probably happening because all the vowels are being used in the first 3-words (18-letters). As its near impossible to have 6-letter words without
vowels, I'm guessing no new words meeting my strict no repeat letter criteria are being found.

Potential solution: Restricting the word search such that each word only contains one vowel. {a,e,i,o,u} once a word is found with only one letter from this set, delete that letter from set
and continue the search. Do this until 4 words with unique 6 letters are found.

Time complexity: The current version of my code is O(n^3). If there's a way making it faster, please let me know.

Any other ideas on tackling this algorithmic challenge would be greatly appreciated :)
