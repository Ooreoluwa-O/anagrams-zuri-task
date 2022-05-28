# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_length(string1, string2):
    string1_word = len(string1)
    string2_word = len(string2)

    if string1_word == string2_word:
     return True
    else:
     return False
print(find_length("toaster", "rotates"))


def find_anagram(string1, string2):
    # [assignment] Add your code here
    string1_anagram = sorted(string1)
    string2_anagram = sorted(string2)
    if string1_anagram == string2_anagram:
     return True
    else: 
     return False
print(find_anagram("toaster","rotates"))



