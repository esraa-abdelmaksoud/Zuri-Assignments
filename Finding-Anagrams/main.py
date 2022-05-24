# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    dict1, dict2 = {}, {}

    if len(word1) != len(word2):
        return False

    else:
        for c1, c2 in zip (word1, word2):
            if c1 in dict1.keys():
                dict1[c1] += 1
            else:
                dict1[c1] = 1

            if c2 in dict2.keys():
                dict2[c2] += 1
            else:
                dict2[c2] = 1

        return sorted(dict1) == sorted(dict2)