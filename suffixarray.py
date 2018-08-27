class Suffixarray(object):
    def __init__(self, word):
        self.word = word
        self.word_sa = []
        for i in range(len(word)):
            self.word_sa.append(word[i:])
        self.word_sa_sorted = sorted(self.word_sa)

    def find_shortest(self, word):
        """Zwraca najkrótszy podłańcuch rozpoczynający się od słowa word lub zwraca None"""
        shortest, position = self.find(word, True)
        return shortest

    def find_longest(self, word):
        """Zwraca najdłuższy podłańcuch rozpoczynający się od słowa word lub zwraca None"""
        longest, position = self.find(word, False)
        return longest

    def find_all(self, word):
        """Zwraca posortowaną listę słów rozpoczynających się od słowa word lub zwraca None"""
        shortest, position = self.find(word, True)
        if shortest is None:
            return None
        all_words = []
        for w in self.word_sa_sorted[position:]:
            if w[:len(word)] == word:
                all_words.append(w)
            else:
                break
        return all_words

    def find(self, word, shortest=True):
        """Jeśli shortest=False, zwraca najdłuższy podłańcuch rozpoczynający się od słowa word oraz pozycję
        tego podłańcucha na liście posortowanej word_sa_sorted. Jeśli shortest=True (domyślnie), zwraca najkrótszy
        podłańcuch i jego pozycję."""
        low = 0
        high = len(self.word_sa_sorted) - 1
        mid = (high - low) // 2
        word_len = None
        word_value = None
        word_position = None
        while low <= high:
            mid_item = self.word_sa_sorted[mid]
            if word == mid_item[:len(word)]:
                if word_len is None:
                    word_len = len(mid_item)
                if shortest is True and len(mid_item) <= word_len:
                    word_len = len(mid_item)
                    word_value = mid_item
                    word_position = mid
                    high = mid - 1
                elif shortest is False and len(mid_item) >= word_len:
                    word_len = len(mid_item)
                    word_value = mid_item
                    word_position = mid
                    low = mid + 1
                else:
                    high = mid - 1
            elif word < mid_item[:len(word)]:
                high = mid - 1
            else:
                low = mid + 1
            mid = low + (high - low) // 2
        return word_value, word_position


# if __name__ == '__main__':
#     sarray = Suffixarray('abrakadabra')
#     shortest = sarray.find_shortest('ra')
#     print(shortest)
#     longest = sarray.find_longest('ra')
#     print(longest)
#     all_words = sarray.find_all('abra')
#     print(all_words)
