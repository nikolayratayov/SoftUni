const { expect } = require("chai");

const flowerShop = {
    calcPriceOfFlowers(flower, price, quantity) {
        if (typeof flower != 'string' || !Number.isInteger(price) || !Number.isInteger(quantity)) {
            throw new Error('Invalid input!');
        } else {
            let result = price * quantity;
            return `You need $${result.toFixed(2)} to buy ${flower}!`;
        }
    },
    checkFlowersAvailable(flower, gardenArr) {
        if (gardenArr.indexOf(flower) >= 0) {
            return `The ${flower} are available!`;
        } else {
            return `The ${flower} are sold! You need to purchase more!`;
        }
    },
    sellFlowers(gardenArr, space) {
        let shop = [];
        let i = 0;
        if (!Array.isArray(gardenArr) || !Number.isInteger(space) || space < 0 || space >= gardenArr.length) {
            throw new Error('Invalid input!');
        } else {
            while (gardenArr.length > i) {
                if (i != space) {
                    shop.push(gardenArr[i]);
                }
                i++
            }
        }
        return shop.join(' / ');
    }
}


describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            expect(flowerShop.calcPriceOfFlowers('ease', 1, 1)).to.be.equal('You need $1.00 to buy ease!');
            expect(flowerShop.calcPriceOfFlowers('ease', 5, 2)).to.be.equal('You need $10.00 to buy ease!');
            expect(flowerShop.calcPriceOfFlowers.bind(flowerShop, ('ease', 'das', 2))).to.throw('Invalid input!');
            expect(flowerShop.calcPriceOfFlowers.bind(flowerShop, ('ease', 1, 'das'))).to.throw('Invalid input!');
            expect(flowerShop.calcPriceOfFlowers.bind(flowerShop, ('ease', 1.5, 2))).to.throw('Invalid input!');
            expect(flowerShop.calcPriceOfFlowers.bind(flowerShop, ('ease', 2, 2.5))).to.throw('Invalid input!');
            expect(flowerShop.calcPriceOfFlowers.bind(flowerShop, (2, 2, 2))).to.throw('Invalid input!');

            expect(flowerShop.checkFlowersAvailable('opa', ['opa', 'da', 'ne'])).to.be.equal('The opa are available!');
            expect(flowerShop.checkFlowersAvailable('opsa', ['opa', 'da', 'ne'])).to.be.equal('The opsa are sold! You need to purchase more!');
            
            expect(flowerShop.sellFlowers.bind(flowerShop, (["Rose", "Lily", "Orchid"], -1))).to.throw('Invalid input!');
            expect(flowerShop.sellFlowers.bind(flowerShop, (["Rose", "Lily", "Orchid"], 3))).to.throw('Invalid input!');
            expect(flowerShop.sellFlowers.bind(flowerShop, (["Rose", "Lily", "Orchid"], 1.5))).to.throw('Invalid input!');
            expect(flowerShop.sellFlowers.bind(flowerShop, ('das', 1))).to.throw('Invalid input!')

            expect(flowerShop.sellFlowers(["Rose", "Lily", "Orchid"], 1)).to.be.equal('Rose / Orchid');
        });
     });
});
