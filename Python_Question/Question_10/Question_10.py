"""Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
paragraph, and return their respective count as a dictionary.
Note -
1. Write code comments wherever required for code
2. You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
"""

# import all required liberaries
from string import punctuation
from nltk import pos_tag, word_tokenize
import unittest


class GrammarCheck:
    """
    A class for performing part-of-speech analysis on a given phrase.

    Attributes:
        phrase (str): The input phrase to analyze.

    Methods:
        pos_dict(): Performs part-of-speech analysis on the phrase and returns a dictionary 
        with counts for nouns, pronouns, verbs, and adjectives.
    """

    def __init__(self, phrase) -> None:
        """
        Initialize the GrammarCheck object with a given phrase.

        Args:
            phrase (str): The input phrase to analyze.
        """
        self.phrase = phrase

    def pos_dict(self):
        """
        Perform part-of-speech analysis on the phrase.

        Returns:
            dict: A dictionary containing the counts of nouns, pronouns, verbs, and adjectives in the phrase.
        """
        try:
            test_pharse = self.__clean_pharse()

            # Tokenize the phrase into individual words
            words = word_tokenize(test_pharse)

            # Perform part-of-speech tagging
            tag_words = pos_tag(words)

            # noun word
            nouns = [word for word, pos in tag_words if pos in [
                'NN', 'NNS', 'NNP', 'NNPS']]
            # pronoun word
            pronouns = [word for word,
                        pos in tag_words if pos in ['PRP', 'WP']]
            # verb
            verbs = [word for word, pos in tag_words if pos in [
                'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
            # adjective
            adjectives = [word for word,
                          pos in tag_words if pos in ['JJ', 'JJR', 'JJS']]

            pos_counts = {"nouns": len(nouns),
                          "pronouns": len(pronouns),
                          "verbs": len(verbs),
                          "adjectives": len(adjectives)}
            return pos_counts

        except Exception as e:
            print(e)

    def __clean_pharse(self) -> str:
        """
        Clean the phrase by converting it to lowercase and removing punctuation.

        Returns:
            str: The cleaned version of the input phrase.
        """
        lower_phrase = self.phrase.lower()
        for ele in lower_phrase:
            if ele in punctuation:
                lower_phrase = lower_phrase.replace(ele, "")
        return lower_phrase


class GrammarCheckTestCase(unittest.TestCase):
    def test_case1(self):
        phrase = "Beautiful sunny day with Apples oranges bananas"
        # This pharse only contian noun and adjective word
        pos_count = GrammarCheck(phrase)
        result = pos_count.pos_dict()
        self.assertEqual(result["nouns"], 4)
        self.assertEqual(result["pronouns"], 0)
        self.assertEqual(result["verbs"], 0)
        self.assertEqual(result["adjectives"], 2)

    def test_case3(self):
        phrase = "The cat jumps, ran, will run, is running, has jumped, and will be jumping."
        # This pharse contain all the verbs forms
        pos_count = GrammarCheck(phrase)
        result = pos_count.pos_dict()
        self.assertEqual(result["nouns"], 2)
        self.assertEqual(result["pronouns"], 0)
        self.assertEqual(result["verbs"], 8)
        self.assertEqual(result["adjectives"], 0)

    def test_case2(self):
        phrase = """The quick brown fox jumps over the lazy dog. 
            It was a bright and sunny day! The dog, named Max, barked loudly at the squirrel. 
            'Stop!' shouted the owner. The squirrel quickly ran up the tree, escaping the 
            dog's reach. Max wagged his tail happily."""
        pos_count = GrammarCheck(phrase)
        result = pos_count.pos_dict()
        self.assertEqual(result["nouns"], 12)
        self.assertEqual(result["pronouns"], 2)
        self.assertEqual(result["verbs"], 9)
        self.assertEqual(result["adjectives"], 5)


if __name__ == "__main__":
    unittest.main()
