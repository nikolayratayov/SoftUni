function solve(a, b, c){
    let price = b / 1000 * c;
    console.log(`I need $${price.toFixed(2)} to buy ${(b / 1000).toFixed(2)} kilograms ${a}.`)
}
