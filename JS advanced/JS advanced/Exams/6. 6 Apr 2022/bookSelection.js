const { expect } = require("chai");

const bookSelection = {
  isGenreSuitable(genre, age) {
    if (age <= 12 && (genre === "Thriller" || genre === "Horror")) {
      return `Books with ${genre} genre are not suitable for kids at ${age} age`;
    } else {
      return `Those books are suitable`;
    }
  },
  isItAffordable(price, budget) {
    if (typeof price !== "number" || typeof budget !== "number") {
      throw new Error("Invalid input");
    }

    let result = budget - price;

    if (result < 0) {
      return "You don't have enough money";
    } else {
      return `Book bought. You have ${result}$ left`;
    }
  },
  suitableTitles(array, wantedGenre) {
    let resultArr = [];

    if (!Array.isArray(array) || typeof wantedGenre !== "string") {
      throw new Error("Invalid input");
    }
    array.map((obj) => {
      if (obj.genre === wantedGenre) {
        resultArr.push(obj.title);
      }
    });
    return resultArr;
  },
};


describe("Tests …", function() {
  describe("TODO …", function() {

      it("TODO …", function() {
          expect(bookSelection.isGenreSuitable('Thriller', 12)).to.be.equal('Books with Thriller genre are not suitable for kids at 12 age')
          expect(bookSelection.isGenreSuitable('Horror', 12)).to.be.equal('Books with Horror genre are not suitable for kids at 12 age')
          expect(bookSelection.isGenreSuitable('Horror', 13)).to.be.equal('Those books are suitable')
          expect(bookSelection.isGenreSuitable('opa', 13)).to.be.equal('Those books are suitable')

          expect(() => bookSelection.isItAffordable('1', 1)).to.throw('Invalid input')
          expect(() => bookSelection.isItAffordable(1, '1')).to.throw('Invalid input')
          expect(bookSelection.isItAffordable(3, 2)).to.be.equal('You don\'t have enough money')
          expect(bookSelection.isItAffordable(2, 3)).to.be.equal('Book bought. You have 1$ left')

          expect(() => bookSelection.suitableTitles('ads', 's')).to.throw('Invalid input')
          expect(() => bookSelection.suitableTitles([], 1)).to.throw('Invalid input')
          expect(bookSelection.suitableTitles([{'title': 'niki', 'genre': 'opa'}, {'title': 'ioni', 'genre': 'ne'}], 'opa')).to.have.members(['niki'])
      });
   });
});
