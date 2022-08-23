function createSortedList(){
    let obj = new Object;
    obj['arr'] = [];
    obj['add'] = function(a){this.arr.push(a); this.size += 1; this.arr.sort(function(a, b){return a - b})};
    obj['remove'] = function(idx){
        if(idx >= obj['arr'].length || idx < 0){
            return
        }
        this.arr.splice(idx, 1);
        this.size -= 1;
    };
    obj['get'] = function(idx){
        if (idx >= obj['arr'].length || idx < 0){
            return
        }
        return this.arr[idx]
    }
    obj['size'] = 0;
    return obj;
}