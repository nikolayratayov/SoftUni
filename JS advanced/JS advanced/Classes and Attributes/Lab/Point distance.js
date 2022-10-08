class Point {
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    static distance(point1, point2){
        let x_dif = Math.abs(point1.x - point2.x);
        let y_dif = Math.abs(point1.y - point2.y);
        let res = Math.sqrt(x_dif * x_dif + y_dif * y_dif)
        return res;
    }
}
