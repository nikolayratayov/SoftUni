const {expect} = require('chai');

function isOddOrEven(string) {
    if (typeof(string) !== 'string') {
        return undefined;
    }
    if (string.length % 2 === 0) {
        return "even";
    }

    return "odd";
}

describe('odd/even', () => {
    it ('not string', () => {
        expect(isOddOrEven([1, 2])).to.be.undefined;
        expect(isOddOrEven(['asd'])).to.be.undefined;
        expect(isOddOrEven(1)).to.be.undefined;
        expect(isOddOrEven(true)).to.be.undefined;
        expect(isOddOrEven({})).to.be.undefined;
        expect(isOddOrEven(2.5)).to.be.undefined;
    });
    it('even', () => {
        expect(isOddOrEven('asdf')).to.be.equal('even');
        expect(isOddOrEven('')).to.be.equal('even');
        expect(isOddOrEven('d5s6gh')).to.be.equal('even');
    });
    it('odd', () => {
        expect(isOddOrEven('asd')).to.be.equal('odd');
        expect(isOddOrEven('a')).to.be.equal('odd');
        expect(isOddOrEven('adasdas')).to.be.equal('odd');
    })
})