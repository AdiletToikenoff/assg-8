# Observer Pattern

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def register_investor(self, investor):
        self.investors.append(investor)

    def unregister_investor(self, investor):
        self.investors.remove(investor)

    def update_price(self, price):
        self.price = price
        self.notify_investors()

    def notify_investors(self):
        for investor in self.investors:
            investor.update(self)

class Investor:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def update(self, stock):
        print(f'Notified {self.name} of {stock.symbol} price change to {stock.price}')

# Iterator Pattern

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def hasNext(self):
        return self.index < len(self.collection)

    def next(self):
        if not self.hasNext():
            raise StopIteration()
        item = self.collection[self.index]
        self.index += 1
        return item

class Playlist:
    def createIterator(self):
        pass

    def addSong(self, song):
        pass

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class PlaylistImpl(Playlist):
    def __init__(self):
        self.songs = []

    def createIterator(self):
        return Iterator(self.songs)

    def addSong(self, song):
        self.songs.append(song)

# Sample client code

if __name__ == "__main__":
    # Observer Pattern
    stock1 = Stock("AAPL", 150.0)
    stock2 = Stock("GOOG", 2500.0)

    investor1 = Investor("John")
    investor2 = Investor("Alice")

    stock1.register_investor(investor1)
    stock2.register_investor(investor1)
    stock2.register_investor(investor2)

    stock1.update_price(155.0)
    stock2.update_price(2600.0)

    # Iterator Pattern
    playlist = PlaylistImpl()
    playlist.addSong(Song("Song 1", "Artist 1"))
    playlist.addSong(Song("Song 2", "Artist 2"))
    playlist.addSong(Song("Song 3", "Artist 3"))

    iterator = playlist.createIterator()
    while iterator.hasNext():
        song = iterator.next()
        print(f'Playing {song.title} by {song.artist}')
