"""I'd like to compare songs by their length (measured in whole seconds). Add the required methods for 
==, <, >, <=, and >= comparisons. Probably a good idea to be able to convert Songs to ints, too, huh?"""


class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

s1 = Song('Mark', 'Life song', '300')
s2 = Song('Celine', 'Love song', '450')
print(s1 < s2, s1 > s2, s1 <= s2, s1 >= s2, s1 == s2)
