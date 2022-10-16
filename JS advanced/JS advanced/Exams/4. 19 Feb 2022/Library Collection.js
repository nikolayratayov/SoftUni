class LibraryCollection {
    constructor(cap){
        this.capacity = Number(cap);
        this.books = [];
    }

    addBook(name, author){
        if (this.books.length == this.capacity){ throw new Error('Not enough space in the collection.')}
        this.books.push({'bookName': name, 'bookAuthor': author, 'payed': false});
        return `The ${name}, with an author ${author}, collect.`
    }

    payBook(name){
        for (let book of this.books){
            if (book.bookName == name ){
                if (book.payed){throw new Error(`${name} has already been paid.`)}
                book.payed = true;
                return `${name} has been successfully paid.`
            }
        }
        throw new Error(`${name} is not in the collection.`)
    }

    removeBook(name){
        for (let i = 0; i < this.books.length; i++){
            if (this.books[i].bookName == name){
                if (this.books[i].payed){
                    this.books.pop(i);
                    return `${name} remove from the collection.`
                }
                throw new Error(`${name} need to be paid before removing from the collection.`)
            }
        }
        throw new Error('The book, you\'re looking for, is not found.')
    }

    getStatistics(author){
        if (author){
            for (let book of this.books){
                if (book.bookAuthor == author){
                    let paid;
                    if (book.payed){paid = 'Has Paid'}
                    else{paid = 'Not Paid'}
                    return `${book.bookName} == ${book.bookAuthor} - ${paid}.`
                }
            }
            throw new Error(`${author} is not in the collection.`)
        }
        let res = `The book collection has ${this.capacity - this.books.length} empty spots left.\n`
        let sorted_books = this.books.sort((a, b) => a.bookName.localeCompare(b.bookName));
        for (let book of sorted_books){
            let paid
            if (book.payed){paid = 'Has Paid'}
            else{paid = 'Not Paid'}
            res += `${book.bookName} == ${book.bookAuthor} - ${paid}.\n`
        }
        return res.substring(0, res.length - 1)
    }
}