class Circle{
    constructor(n){
        this.radius = n;
    }
    get diameter(){
        return this.radius * 2
    }
    get area(){
        return this.radius * this.radius * Math.PI;
    }
    set diameter(d){
        this.radius = d / 2;
    }
}
