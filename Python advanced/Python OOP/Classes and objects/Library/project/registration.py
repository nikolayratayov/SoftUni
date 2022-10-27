class Registration:

    def add_user(self, user, library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, id, new_username, library):
        for i in library.user_records:
            if id == i.user_id:
                if new_username != i.username:
                    if i.username in library.rented_books:
                        dct = library.rented_books[i.username]
                        del library.rented_books[i.username]
                        library.rented_books[new_username] = dct
                    i.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {id}"
                else:
                    return f"Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {id}!"
