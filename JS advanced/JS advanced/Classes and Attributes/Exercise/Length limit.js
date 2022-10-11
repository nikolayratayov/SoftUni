class Stringer {
    constructor(str, len){
        this.innerString = str;
        this.innerLength = len;
    }
    increase(len){this.innerLength += len}
    decrease(len){
        this.innerLength -= len
        if (this.innerLength < 0){this.innerLength = 0}
    }
    toString(){
        if (this.innerString.length > this.innerLength){
            if (this.innerLength == 0){
                return '...'
            }
            else{
                return this.innerString.substring(0, this.innerLength) + '...'
            }
        }
        else{
            return this.innerString
        }
    }
}
