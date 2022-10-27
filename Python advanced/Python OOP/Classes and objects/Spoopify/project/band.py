class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        for i in self.albums:
            if i == album:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for i in self.albums:
            if i.name == album_name:
                if i.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(i)
                    return f'Album {album_name} has been removed.'
        return f"Album {album_name} is not found."

    def details(self):
        res = f'Band {self.name}\n'
        for i in self.albums:
            res += f'{i.details()}\n'
        return res[0: len(res) - 1]
    