class ChristmasMovies {
    constructor() {
        this.movieCollection = [];
        this.watched = {};
        this.actors = [];
    }

    buyMovie(movieName, actors) {
        let movie = this.movieCollection.find(m => movieName === m.name);
        let uniqueActors = new Set(actors);

        if (movie === undefined) {
            this.movieCollection.push({ name: movieName, actors: [...uniqueActors] });
            let output = [];
            [...uniqueActors].map(actor => output.push(actor));
            return `You just got ${movieName} to your collection in which ${output.join(', ')} are taking part!`;
        } else {
            throw new Error(`You already own ${movieName} in your collection!`);
        }
    }

    discardMovie(movieName) {
        let filtered = this.movieCollection.filter(x => x.name === movieName)

        if (filtered.length === 0) {
            throw new Error(`${movieName} is not at your collection!`);
        }
        let index = this.movieCollection.findIndex(m => m.name === movieName);
        this.movieCollection.splice(index, 1);
        let { name, _ } = filtered[0];
        if (this.watched.hasOwnProperty(name)) {
            delete this.watched[name];
            return `You just threw away ${name}!`;
        } else {
            throw new Error(`${movieName} is not watched!`);
        }

    }

    watchMovie(movieName) {
        let movie = this.movieCollection.find(m => movieName === m.name);
        if (movie) {
            if (!this.watched.hasOwnProperty(movie.name)) {
                this.watched[movie.name] = 1;
            } else {
                this.watched[movie.name]++;
            }
        } else {
            throw new Error('No such movie in your collection!');
        }
    }

    favouriteMovie() {
        let favourite = Object.entries(this.watched).sort((a, b) => b[1] - a[1]);
        if (favourite.length > 0) {
            return `Your favourite movie is ${favourite[0][0]} and you have watched it ${favourite[0][1]} times!`;
        } else {
            throw new Error('You have not watched a movie yet this year!');
        }
    }

    mostStarredActor() {
        let mostStarred = {};
        if (this.movieCollection.length > 0) {
            this.movieCollection.forEach(el => {
                let { _, actors } = el;
                actors.forEach(actor => {
                    if (mostStarred.hasOwnProperty(actor)) {
                        mostStarred[actor]++;
                    } else {
                        mostStarred[actor] = 1;
                    }
                })
            });
            let theActor = Object.entries(mostStarred).sort((a, b) => b[1] - a[1]);
            return `The most starred actor is ${theActor[0][0]} and starred in ${theActor[0][1]} movies!`;
        } else {
            throw new Error('You have not watched a movie yet this year!')
        }
    }
}

let christmas = new ChristmasMovies();
christmas.buyMovie('Home Alone', ['Macaulay Culkin', 'Joe Pesci', 'Daniel Stern']);
christmas.buyMovie('Home Alone 2', ['Macaulay Culkin']);
christmas.buyMovie('Last Christmas', ['Emilia Clarke', 'Henry Golding']);
christmas.buyMovie('The Grinch', ['Benedict Cumberbatch', 'Pharrell Williams']);
christmas.watchMovie('Home Alone');
christmas.watchMovie('Home Alone');
christmas.watchMovie('Home Alone');
christmas.watchMovie('Home Alone 2');
christmas.watchMovie('The Grinch');
christmas.watchMovie('Last Christmas');
christmas.watchMovie('Home Alone 2');
christmas.watchMovie('Last Christmas');
christmas.discardMovie('The Grinch');
christmas.favouriteMovie();
christmas.mostStarredActor();

module.exports = ChristmasMovies;

const{expect} = require('chai');

describe('tests', () => {
    describe('chrsitmas movies', () => {
        it('constructor', () => {
            let c = new ChristmasMovies;
            expect(c).to.haveOwnProperty('actors');
            expect(c.actors.length).to.be.equal(0);
            expect(c).to.haveOwnProperty('watched');
            expect(c).to.haveOwnProperty('movieCollection');
            expect(c.movieCollection.length).to.be.equal(0);
        })
        it('buymovie', () => {
            let eee = new ChristmasMovies;
            expect(eee.buyMovie('movie', ['1', '2'])).to.be.equal('You just got movie to your collection in which 1, 2 are taking part!')
            expect(eee.buyMovie.bind(eee, 'movie', ['1', '2'])).to.throw('You already own movie in your collection!')
        })
        it('discardmovie', () => {
            let dis = new ChristmasMovies;
            expect(dis.discardMovie.bind(dis, 'movie')).to.throw('movie is not at your collection!')
            dis.buyMovie('op');
            expect(dis.discardMovie.bind(dis, 'op')).to.throw('op is not watched!')
            dis.buyMovie('op');
            dis.watchMovie('op');
            expect(dis.discardMovie('op')).to.be.equal('You just threw away op!')
        })
        it('watchmovie', () => {
            let c = new ChristmasMovies;
            c.buyMovie('op');
            c.watchMovie('op');
            expect(c.watched['op']).to.be.equal(1);
            c.watchMovie('op');
            expect(c.watched['op']).to.be.equal(2);
            expect(c.watchMovie.bind(c, 'ne')).to.throw('No such movie in your collection!')
        })
        it('fav', () => {
            let c = new ChristmasMovies;
            expect(c.favouriteMovie.bind(c)).to.throw('You have not watched a movie yet this year!')
            c.buyMovie('off');
            c.watchMovie('off');
            expect(c.favouriteMovie()).to.be.equal('Your favourite movie is off and you have watched it 1 times!')
            c.watchMovie('off');
            expect(c.favouriteMovie()).to.be.equal('Your favourite movie is off and you have watched it 2 times!')
            c.buyMovie('eee');
            c.watchMovie('eee');
            expect(c.favouriteMovie()).to.be.equal('Your favourite movie is off and you have watched it 2 times!')
        })
        it('actors', () => {
            let c = new ChristmasMovies;
            expect(c.mostStarredActor.bind(c)).to.throw('You have not watched a movie yet this year!')
            c.buyMovie('off', ['a', 'b'])
            c.buyMovie('eee', ['a', 'c'])
            expect(c.mostStarredActor()).to.be.equal('The most starred actor is a and starred in 2 movies!')
        })
    })
})