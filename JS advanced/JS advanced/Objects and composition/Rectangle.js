function rectangle(w, h, c){
    let first = c[0].toUpperCase();
    let rest = c.slice(1);
    let word = first + rest;
    return {width:w, height:h, color:word, calcArea:function(){return this.width * this.height}}
}