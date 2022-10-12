class HEX {
    constructor(n){
        this.num = Number(n);
    }
    valueOf(){return this.num}
    toString(){return '0x' + this.num.toString(16).toUpperCase();}
    plus(neshto){
        if (typeof(neshto) == 'number'){
            return new HEX(neshto + this.num)
        }
        else{
            return new HEX(neshto.valueOf() + this.num)
        }
    }
    minus(neshto){
        if (typeof(neshto) == 'number'){
            return new HEX(this.num - neshto)
        }
        else{
            return new HEX(this.num - neshto.valueOf())
        }
    }
    parse(hextodec){return parseInt(hextodec, 16)}
}
