const {expect} = require('chai');

function lookupChar(string, index) {
    if (typeof(string) !== 'string' || !Number.isInteger(index)) {
        return undefined;
    }
    if (string.length <= index || index < 0) {
        return "Incorrect index";
    }

    return string.charAt(index);
}

describe('lookup', () => {
    it('not correct type', () => {
        expect(lookupChar(1, 1)).to.be.undefined;
        expect(lookupChar([], 1)).to.be.undefined;
        expect(lookupChar({}, 1)).to.be.undefined;
        expect(lookupChar('dasd', 'das')).to.be.undefined;
        expect(lookupChar('dasd', {})).to.be.undefined;
        expect(lookupChar('dasd', [])).to.be.undefined;
        expect(lookupChar('dasd', 1.5)).to.be.undefined;
    });
    it('incorrect index', () => {
        expect(lookupChar('dasdas', -1)).to.be.equal('Incorrect index');
        expect(lookupChar('dasdas', 6)).to.be.equal('Incorrect index');
        expect(lookupChar('dasdas', 7)).to.be.equal('Incorrect index');
    });
    it ('valid', () => {
        expect(lookupChar('asdf', 2)).to.be.equal('d');
        expect(lookupChar('asdfdas', 0)).to.be.equal('a');
    })
})