"""
Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.

Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input - string = “write write write all the number from from from 1 to 100”
Example output - 5
Explanation - From the given string we can note that the most frequent words are “write” and “from” and
the maximum value of both the values is “write” and its corresponding length is 5
"""
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

import unittest


class Solution1:
    """
    This class takes a string that contains a sentence or paragraph which has few exact words.
    We have to count the occurrence of each word in the given line and return the length of that 
    word with the maximum number of occurrences.

    exmaple:- 
    string = “write write write all the number from from from 1 to 100”
    same word are write and from 
    output = 5 (write had max lenght)
    """

    def __init__(self, string):
        self.string = string

    def counts_word_frequency(self,):
        """
        This class method give dictionary which has word as a key and value as 
        its number of occurence in input string.

        Returns:
            dict: {key : word, value : number of occurence}
        """
        try:
            punc = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
            for ele in self.string:
                if ele in punc:
                    self.string = self.string.replace(ele, "")

            words = self.string.lower().split()
            freq = {}

            for word in words:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

            return freq

        except Exception as e:
            print("Error Occured in ", e)

    def len_max_freq_word(self, max_length=0, max_word="") -> int:
        """
        This mehtod gives the lenght of the word which has maximum occurenece.

        Args:
            max_length (int, optional): maximum strting length of word. Defaults to 0.
            max_word (str, optional): the word which has highest occurence. Defaults to "".

        Returns:
            int: the lenght of word which has highest occurence in given stirng.
        """
        freq = self.counts_word_frequency()
        for word, count in freq.items():
            if count > max_length:
                max_length = count
                max_word = word
        return len(max_word)


# Unittesting in python
class Solution1TestCase(unittest.TestCase):
    def test_case1(self):
        s = """Hi, I am Prathmesh Jagtap Jagtap from FSDS batch november 2021. Interest in 
            learning data science, data Analysis, data visualization,
            data cleaning, data science, and machine learning, deep learning, computer vision."""
        lenght = Solution1(s)
        output = lenght.len_max_freq_word()
        self.assertEqual(output, 4)
        # Explanation : In Test_case1 word "data" has maximumm frequency count and the lenght of this word is 4.

    def test_case2(self):
        s = """In the world of programming, the best way to learn is through practice. Take, for example, 
            coding challenges and problem-solving exercises. These provide an excellent opportunity to apply 
            your knowledge and improve your skills. By attempting various coding problems, you can gain 
            hands-on experience and deepen your understanding of different algorithms and data structures. 
            For instance, you might encounter an example where you need to implement a binary search tree or optimize 
            an algorithm for better time complexity. The more you practice, the better you become. So, don't hesitate to 
            take on coding examples, solve problems, and enhance your programming abilities."""
        lenght = Solution1(s)
        output = lenght.len_max_freq_word()
        self.assertEqual(output, 3)
        # Explanation : In Test_case2, the word "you" appear 5 times, thats why our progrma output 3 for the word "you".


if __name__ == '__main__':
    unittest.main()
