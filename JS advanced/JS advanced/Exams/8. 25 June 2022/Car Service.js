const { expect } = require("chai");

const carService = {
  isItExpensive(issue) {
    if (issue === "Engine" || issue === "Transmission") {
      return `The issue with the car is more severe and it will cost more money`;
    } else {
      return `The overall price will be a bit cheaper`;
    }
  },
  discount(numberOfParts, totalPrice) {
    if (typeof numberOfParts !== "number" || typeof totalPrice !== "number") {
      throw new Error("Invalid input");
    }

    let discountPercentage = 0;

    if (numberOfParts > 2 && numberOfParts <= 7) {
      discountPercentage = 15;
    } else if (numberOfParts > 7) {
      discountPercentage = 30;
    }

    let result = (discountPercentage / 100) * totalPrice;

    if (numberOfParts <= 2) {
      return "You cannot apply a discount";
    } else {
      return `Discount applied! You saved ${result}$`;
    }
  },
  partsToBuy(partsCatalog, neededParts) {
    let totalSum = 0;

    if (!Array.isArray(partsCatalog) || !Array.isArray(neededParts)) {
      throw new Error("Invalid input");
    }
    neededParts.forEach((neededPart) => {
      partsCatalog.map((obj) => {
        if (obj.part === neededPart) {
          totalSum += obj.price;
        }
      });
    });

    return totalSum;
  },
};


describe("Tests …", function() {
  describe("TODO …", function() {
      it("TODO …", function() {
          expect(carService.isItExpensive('Engine')).to.be.equal('The issue with the car is more severe and it will cost more money')
          expect(carService.isItExpensive('Transmission')).to.be.equal('The issue with the car is more severe and it will cost more money')
          expect(carService.isItExpensive('das')).to.be.equal('The overall price will be a bit cheaper')

          expect(() => carService.discount('1', '1')).to.throw('Invalid input')
          expect(() => carService.discount(1, '1')).to.throw('Invalid input')
          expect(() => carService.discount('1', 1)).to.throw('Invalid input')
          expect(carService.discount(2, 5)).to.be.equal("You cannot apply a discount")
          expect(carService.discount(3, 100)).to.be.equal("Discount applied! You saved 15$")
          expect(carService.discount(7, 100)).to.be.equal("Discount applied! You saved 15$")
          expect(carService.discount(8, 100)).to.be.equal("Discount applied! You saved 30$")

          expect(() => carService.partsToBuy('a', 'a')).to.throw('Invalid input')
          expect(() => carService.partsToBuy([], 'a')).to.throw('Invalid input')
          expect(() => carService.partsToBuy('', [])).to.throw('Invalid input')
          expect(carService.partsToBuy([], ['a', 'b'])).to.be.equal(0)
          expect(carService.partsToBuy([], ['a', 'b'])).to.be.equal(0)
          expect(carService.partsToBuy([{'part': 'a', 'price': 5}], ['a', 'b'])).to.be.equal(5)
          expect(carService.partsToBuy([{'part': 'a', 'price': 5}], ['a', 'x'])).to.be.equal(5)
          expect(carService.partsToBuy([{'part': 'a', 'price': 5}, {'part': 'b', 'price': 15}, {'part': 'x', 'price': 15}], ['a', 'b'])).to.be.equal(20)
      });
   });
});
