class Movie:
    def start(self):
       print("welcome")
    def interval(self):
       print("Interval, have coffee for rs 50/-")
    def end(self):
       print("thank you come again")
class JungleBook(Movie):
    def reelOne(self):
       print("Mowgli enters the jungle")
    def reelTwo(self):
       print("Bagheera saves Mowgli")
    def interval(self):
       super().interval()
       print("and have chilled bear for rs 200/-")
j=JungleBook()
j.start()
j.reelOne()
j.interval()
j.reelTwo()
j.end()
print(JungleBook.mro())