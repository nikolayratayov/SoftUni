const {expect} = require('chai');

function sum(arr) {
    let sum = 0;
    for (let num of arr){
        sum += Number(num);
    }
    return sum;
}

describe('sum', () => {
    it('non array', () => {
        let arr = 'das';
        let res = sum(arr);
        expect(res).to.be.NaN;
    })
    it('correct sum', () => {
        let arr = [1, 2, 3];
        let res = sum(arr);
        expect(res).to.be.equal(6)
    })
})