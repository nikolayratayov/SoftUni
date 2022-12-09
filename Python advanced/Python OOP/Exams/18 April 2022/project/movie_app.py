from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        for i in self.users_collection:
            if i.username == username:
                raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')
        for i in self.users_collection:
            if i.username == username:
                if movie.owner.username != username:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")
                else:
                    i.movies_owned.append(movie)
                    self.movies_collection.append(movie)
                    return f'{username} successfully added {movie.title} movie.'
        raise Exception('This user does not exist!')

    def edit_movie(self, username, movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for k, v in kwargs.items():
            setattr(movie, k, v)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        for i in self.users_collection:
            if i.username == username:
                i.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for i in self.users_collection:
            if i.username == username:
                if movie in i.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
                else:
                    i.movies_liked.append(movie)
                    movie.likes += 1
                    return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        for i in self.users_collection:
            if i.username == username:
                if movie not in i.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        for i in self.users_collection:
            if i.username == username:
                i.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) > 0:
            lst = sorted(self.movies_collection, key=lambda x: x.title)
            lst = sorted(lst, key=lambda x: x.year, reverse=True)
            res = ''
            for i in lst:
                res += f'{i.details()}\n'
            return res[0:len(res) - 1]
        return 'No movies found.'

    def __str__(self):
        if len(self.users_collection) == 0:
            res = 'All users: No users.\n'
        else:
            res = f"All users: {', '.join(x.username for x in self.users_collection)}\n"
        if len(self.movies_collection) == 0:
            res += 'All movies: No movies.'
        else:
            res += f"All movies: {', '.join(x.title for x in self.movies_collection)}"
        return res
