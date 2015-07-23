class Dic:
    def __init__(self, list):
        self._list = list

    def matches(self, word):
        return word in self._list

    def score(self, words):
        count = 0
        for word in words:
            if word in self._list:
                count += 1
        return [count, len(self._list)]
