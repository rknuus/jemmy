class DicError(Exception):
    pass


class Dic:
    def __init__(self, list):
        if len(list) is 0:
            raise DicError('Word list must not be empty')
        self._list = list

    def matches(self, word):
        return word in self._list

    def score(self, words):
        count = 0
        for word in words:
            if word in self._list:
                count += 1
        return 100 * count // len(self._list)
