const { expect, assert } = require("chai");

const rentCar = {
    searchCar(shop, model) {
        let findModel = [];
        if (Array.isArray(shop) && typeof model == 'string') {
            for (let i = 0; i < shop.length; i++) {
                if (model == shop[i]) {
                    findModel.push(shop[i]);
                }
            }
            if (findModel.length !== 0) {
                return `There is ${findModel.length} car of model ${model} in the catalog!`;
            } else {
                throw new Error('There are no such models in the catalog!')
            }
        } else {
            throw new Error('Invalid input!')
        }
    },
    calculatePriceOfCar(model, days) {
        let catalogue = {
            Volkswagen: 20,
            Audi: 36,
            Toyota: 40,
            BMW: 45,
            Mercedes: 50
        };

        if (typeof model == 'string' && Number.isInteger(days)) {
            if (catalogue.hasOwnProperty(model)) {
                let cost = catalogue[model] * days;
                return `You choose ${model} and it will cost $${cost}!`
            } else {
                throw new Error('No such model in the catalog!')
            }
        } else {
            throw new Error('Invalid input!')
        }
    },
    checkBudget(costPerDay, days, budget) {
        if (!Number.isInteger(costPerDay) || !Number.isInteger(days) || !Number.isInteger(budget)) {
            throw new Error('Invalid input!');
        } else {
            let cost = costPerDay * days;
            if (cost <= budget) {
                return `You rent a car!`
            } else {
                return 'You need a bigger budget!'
            }
        }
    }
}


describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            expect(rentCar.searchCar.bind(rentCar, ('das', 'das'))).to.throw('Invalid input!');
            expect(rentCar.searchCar.bind(rentCar, (['a', 'b'], 1))).to.throw('Invalid input!');
            expect( () => rentCar.searchCar(['a', 'b'], 'das')).to.throw('There are no such models in the catalog!')
            expect(rentCar.searchCar(['a', 'b', 'a'], 'a')).to.be.equal('There is 2 car of model a in the catalog!')

            expect(() => rentCar.calculatePriceOfCar('das', '1')).throw('Invalid input!');
            expect(() => rentCar.calculatePriceOfCar('das', 1.5)).throw('Invalid input!');
            expect(() => rentCar.calculatePriceOfCar(1, 1)).throw('Invalid input!');
            expect(() => rentCar.calculatePriceOfCar('eeee', 1)).throw('No such model in the catalog!');
            expect(rentCar.calculatePriceOfCar('Audi', 2)).to.be.equal('You choose Audi and it will cost $72!');

            expect(() => rentCar.checkBudget('1', 1, 1)).to.throw('Invalid input!');
            expect(() => rentCar.checkBudget(1, '1', 1)).to.throw('Invalid input!');
            expect(() => rentCar.checkBudget(1, 1, '1')).to.throw('Invalid input!');
            expect(rentCar.checkBudget(1, 1, 1)).to.be.equal('You rent a car!')
            expect(rentCar.checkBudget(2, 1, 1)).to.be.equal('You need a bigger budget!')
        });
     });
});
