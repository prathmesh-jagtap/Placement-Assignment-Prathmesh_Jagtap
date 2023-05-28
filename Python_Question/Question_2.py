"""
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO
"""
import unittest

class Solution2:
    """
    This class takes string as input and gives the valid string which has same frequency or 
    one more or less than tha given frequencies, but as a given condiction which only convert one letter.
    """
    def __init__(self, string):
        self.string = string
        
    def freq_count(self):
        """This class method take string and convert it into dictionary which has letter as key 
        and its number of occurence as value.

        Returns:
        dict: {key:letter, value:frequency of letter}
        """
        letters = list(self.string)
        freq = {}
        
        for letter in letters:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
                
        return freq
    
    def isValidString(self) -> str:
        """It takes the dictionary from the freq_count function and checks the condition whether a string is valid or not;
        It checks whether the frequency of each letter is equal or any one of the letter's frequencies is less or 
        more than the other letter's frequency, if this condition matches then return YES if not return NO.

        Returns:
            str: YES (if condition match) otherwise, NO
        """
        try:
            freq = self.freq_count()
            counts = list(freq.values())
            
            max_freq_count = counts.count(max(counts))
            min_freq_count = counts.count(min(counts))

            if max(counts) == min(counts) or (max(counts) == min(counts) + 1 and \
                                              (max_freq_count == 1 or min_freq_count == 1)):
                return "YES"
            
            else :
                return "NO"
            
        except Exception as e:
            print(e)


# Unittesting in python
class Solution2TestCase(unittest.TestCase):
    def test_case1(self):
        s = "abc"
        check = Solution2(s)
        self.assertEqual(check.isValidString(), "YES")
        # Explanation : In Test_case1 each letter has same frequency count.

    def test_case2(self):
        s = "abcc"
        check = Solution2(s)
        self.assertEqual(check.isValidString(), "YES")
        # Explanation : In Test_case2, as per condtition we can remove one 'c' from given string.
        
    def test_case3(self):
        s = "aabbcd"
        check = Solution2(s)
        self.assertEqual(check.isValidString(), "NO")
        # Explanation : In Test_case3, as per condtition there is two character has same frequencies only amd we only 
        # remove one character from given string.
        
    def test_case4(self):
        s = "abcdefghhgfedecba"
        check = Solution2(s)
        self.assertEqual(check.isValidString(), "YES")
        # Explanation : In Test_case4, all character in given string is twice except 'e' which occurs 3 times, so 
        # we can remove one instance of 'e' which makes it valid string.
    

if __name__ == '__main__':
    unittest.main()
