function solve(){
    let str = ''
    return {
        append: (s) => str += s,
        removeStart: (n) => str = str.slice(n),
        removeEnd: (n) => str = str.slice(0, str.length - n),
        print: () => console.log(str)
    }
}
