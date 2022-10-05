const {expect} = require('chai');

function isSymmetric(arr) {
    if (!Array.isArray(arr)){
        return false; // Non-arrays are non-symmetric
    }
    let reversed = arr.slice(0).reverse(); // Clone and reverse
    let equal = (JSON.stringify(arr) == JSON.stringify(reversed));
    return equal;
}

describe('isSymmetric', () =>{
    it('take an array', () => {
        let arr = 'opa';
        let res = isSymmetric(arr);
        expect(res).to.be.false;
    })
    it('symmetric', () => {
        let arr = [1, 2, 3, 2, 1];
        let res = isSymmetric(arr)
        expect(res).to.be.true;
    })
    it('non-symmetric', () => {
        let arr = [1, 2, 3]
        let res = isSymmetric(arr);
        expect(res).to.be.false;
    })
    it('symmetric string', () => {
        let arr = 'abcba';
        let res = isSymmetric(arr);
        expect(res).to.be.false;
    })
    it('sym arr', () => {
        let arr = [1, '1', 'eee', '1', 1];
        let res = isSymmetric(arr);
        expect(res).to.be.true;
    })
    it('is sym', () => {
        expect(isSymmetric([1, 2, 3, '2', 1])).to.be.false;
    })
})