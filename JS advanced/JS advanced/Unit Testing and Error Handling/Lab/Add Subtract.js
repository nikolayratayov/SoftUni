const {expect} = require('chai');

function createCalculator() {
    let value = 0;
    return {
        add: function(num) { value += Number(num); },
        subtract: function(num) { value -= Number(num); },
        get: function() { return value; }
    }
}

describe('createCalculator', () => {
    it('has property', () => {
        expect(createCalculator()).haveOwnProperty('add');
        expect(createCalculator()).haveOwnProperty('subtract');
        expect(createCalculator()).haveOwnProperty('get');
    });
    it('add', () => {
        let res = createCalculator();
        res.add(5);
        expect(res.get()).to.be.equal(5);
        res.add('2');
        expect(res.get()).to.be.equal(7);
    });
    it('subtract', () => {
        let res = createCalculator();
        res.subtract(5);
        expect(res.get()).to.be.equal(-5);
        res.subtract(3);
        expect(res.get()).to.be.equal(-8);
    });
    it('add subtract', () => {
        let res = createCalculator();
        res.add(4);
        res.subtract(2);
        expect(res.get()).to.be.equal(2);
    });
    it('add string', () => {
        let res = createCalculator();
        res.add('5');
        res.subtract('1');
        expect(res.get()).to.be.equal(4);
    });
    it('outer sum', () => {
        let res = createCalculator();
        res.add(5);
        let outer = createCalculator();
        outer.add(10);
        expect(outer.get()).to.be.equal(10);
    });
    it('is object', () => {
        expect(createCalculator()).to.be.an.instanceOf(Object);
    });
    it('returns value', () => {
        expect(createCalculator().get()).to.be.equal(0);
    });
    it('value', () => {
        expect(createCalculator().value).to.be.undefined
    });
    it('should return an object', () => {
        expect(typeof createCalculator()).to.equal('object');
    });

})