function solve(area, vol, input) {
    let arr = JSON.parse(input)
    let arr_to_return = []
    for (let i of arr){
        let obj = {
            'area': area.call(i),
            'volume': vol.call(i)
        }
        arr_to_return.push(obj)
    }
    return arr_to_return
}
