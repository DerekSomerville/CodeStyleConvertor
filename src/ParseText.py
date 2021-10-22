import re
from src.Case import *

class ParseText:

    def is_word_break(self, char):
        return not char.isalnum()

    def can_convert_word(self,word):
        found = True
        if word[0:6] == "assert":
            found = False
        if word in ["sqlExp"]:
            found = False
        return found

    def convert(self, text):
        word = ""
        new_text = ""
        for char in text:
            if self.is_word_break(char):
                if is_pascal_case(word) and self.can_convert_word(word):
                    word = self.to_snake_case(word)
                new_text += word
                word = ""
                new_text += char
            else:
                word += char
        if is_pascal_case(word):
            word = self.to_snake_case(word)
        new_text += word
        return new_text

    def to_snake_case(self, name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
