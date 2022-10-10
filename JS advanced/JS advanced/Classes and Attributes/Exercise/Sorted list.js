class List {
    constructor(){
        this.list = []
        this.size = 0
    }
    add(el){ this.list.push(Number(el)); this.size += 1; this.list.sort((a, b) => {return a - b})}
    remove(idx){ 
        if (idx >= 0 && idx < this.list.length){
            this.list.splice(idx, 1); this.size -= 1
        }    
    }
    get(idx){
        if (idx >= 0 && idx < this.list.length){
            return this.list[idx]
        }
    }
}
