import re
from autocorrect import spell


class SpellCorrect(object):

    @staticmethod
    def correct_word(word):
        return spell(word)

    @staticmethod
    def correct_sentence(text):
        tokens = re.split(r'\s+', text)
        return ' '.join([spell(token) for token in tokens])


if __name__ == '__main__':
    assert 'something' == SpellCorrect.correct_word('somthing')
    assert 'India plays cricket very well' == SpellCorrect.correct_sentence(
        'Indai plays crickt very well')
