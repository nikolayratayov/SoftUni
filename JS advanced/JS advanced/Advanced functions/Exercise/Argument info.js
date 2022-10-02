function solve(){
    let arr = []
    let obj_count = {}
    let sortable = []
    for (let i of arguments){
        if (!(typeof(i) in obj_count)){
            arr.push([typeof(i), i])
            obj_count[typeof(i)] = 1
        }
        else{
            arr.push([typeof(i), i])
            obj_count[typeof(i)] += 1
        }
    }
    for (let i of arr){
        console.log(`${i[0]}: ${i[1]}`)
    }
    for (let i in obj_count){
        sortable.push([i, obj_count[i]])
    }
    sortable.sort(function(a, b){return b[1] - a[1]})
    for (let i of sortable){
        console.log(`${i[0]} = ${i[1]}`)
    }
}
