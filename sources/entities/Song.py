class Song:

    def __init__(self, title, year, genre, performer):
        self.title = title
        self.year = year
        self.genre = genre
        self.performer = performer

    def upvote(self):
        self.rating += 1

    def downvote(self):
        self.rating -= 1

        if self.rating<0:
            self.rating = 0