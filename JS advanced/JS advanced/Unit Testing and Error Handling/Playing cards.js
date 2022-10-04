function solve(a, b){
    let face = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    if (!face.includes(a)){
        throw new Error('Error')
    }
    let validCardSuits = {
        S: '\u2660',
        H: '\u2665',
        D: '\u2666',
        C: '\u2663',
    }
    return {
        a,
        b,
        toString(){
            return this.a + validCardSuits[this.b]
        }
    }
}
