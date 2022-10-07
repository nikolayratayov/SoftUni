const {expect} = require('chai');

let mathEnforcer = {
    addFive: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num + 5;
    },
    subtractTen: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num - 10;
    },
    sum: function (num1, num2) {
        if (typeof(num1) !== 'number' || typeof(num2) !== 'number') {
            return undefined;
        }
        return num1 + num2;
    }
};

describe('test', () => {
    it('add', () => {
        expect(mathEnforcer.addFive('1')).to.be.undefined;
        expect(mathEnforcer.addFive([])).to.be.undefined;
        expect(mathEnforcer.addFive({})).to.be.undefined;
        expect(mathEnforcer.addFive(3)).to.be.equal(8);
        expect(mathEnforcer.addFive(3.3)).to.be.closeTo(8.3, 0.01);
        expect(mathEnforcer.addFive(-5.3)).to.be.closeTo(-0.3, 0.01);
    });
    it('subtract', () => {
        expect(mathEnforcer.subtractTen('1')).to.be.undefined;
        expect(mathEnforcer.subtractTen([])).to.be.undefined;
        expect(mathEnforcer.subtractTen({})).to.be.undefined;
        expect(mathEnforcer.subtractTen(3)).to.be.equal(-7);
        expect(mathEnforcer.subtractTen(3.3)).to.be.closeTo(-6.7, 0.01);
        expect(mathEnforcer.subtractTen(-3.3)).to.be.closeTo(-13.3, 0.01);
    });
    it('sum', () => {
        expect(mathEnforcer.sum('1', 1)).to.be.undefined;
        expect(mathEnforcer.sum('1', '2')).to.be.undefined;
        expect(mathEnforcer.sum([], 1)).to.be.undefined;
        expect(mathEnforcer.sum({}, 1)).to.be.undefined;
        expect(mathEnforcer.sum(1, '2')).to.be.undefined;
        expect(mathEnforcer.sum(1, [])).to.be.undefined;
        expect(mathEnforcer.sum(1, {})).to.be.undefined;
        expect(mathEnforcer.sum(1, 1.5)).to.be.closeTo(2.5, 0.01);
        expect(mathEnforcer.sum(-1, -1.5)).to.be.closeTo(-2.5, 0.01);
        expect(mathEnforcer.sum(-1, 5)).to.be.equal(4);
        expect(mathEnforcer.sum(1, -5)).to.be.equal(-4);
        expect(mathEnforcer.sum(1, 5)).to.be.equal(6);
        expect(mathEnforcer.sum(-1, -5)).to.be.equal(-6);
        expect(mathEnforcer.sum(2.5, 3)).to.be.closeTo(5.5, 0.01);
    })
})
