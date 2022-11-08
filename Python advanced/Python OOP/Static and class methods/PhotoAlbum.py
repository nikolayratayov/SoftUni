import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, count):
        return cls(math.ceil(count / 4))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return 'No more free slots'

    def display(self):
        res = '-' * 11 + '\n'
        for page in self.photos:
            row = []
            for photo in range(len(page)):
                row.append('[]')
            res += f'{" ".join(row)}\n'
            res += '-' * 11 + '\n'
        return res[0: len(res) - 1]
