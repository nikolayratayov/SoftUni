const { expect } = require("chai");

const numberOperations = {
    powNumber: function (num) {
        return num * num;
    },
    numberChecker: function (input) {
        input = Number(input);

        if (isNaN(input)) {
            throw new Error('The input is not a number!');
        }

        if (input < 100) {
            return 'The number is lower than 100!';
        } else {
            return 'The number is greater or equal to 100!';
        }
    },
    sumArrays: function (array1, array2) {

        const longerArr = array1.length > array2.length ? array1 : array2;
        const rounds = array1.length < array2.length ? array1.length : array2.length;

        const resultArr = [];

        for (let i = 0; i < rounds; i++) {
            resultArr.push(array1[i] + array2[i]);
        }

        resultArr.push(...longerArr.slice(rounds));

        return resultArr
    }
};


describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            expect(numberOperations.powNumber(2)).to.be.equal(4);
            expect(numberOperations.numberChecker.bind(numberOperations, ('das'))).to.throw('The input is not a number!');
            expect(numberOperations.numberChecker(50)).to.be.equal('The number is lower than 100!');
            expect(numberOperations.numberChecker(150)).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.numberChecker(100)).to.be.equal('The number is greater or equal to 100!');
            expect(numberOperations.sumArrays([1, 2, 3], [4, 5, 6])).to.have.members([5, 7, 9]);
            expect(numberOperations.sumArrays([1, 2, 3], [4, 5, 6, 50])).to.have.members([5, 7, 9, 50]);
            expect(numberOperations.sumArrays([1, 2, 3, 10], [4, 5, 6])).to.have.members([5, 7, 9, 10]);
        });
     });
});
