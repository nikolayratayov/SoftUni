function solve(arr, criteria){
    class ticket{
        constructor(destination, price, status){
            this.destination = destination;
            this.price = Number(price);
            this.status = status;
        }
    }
    let new_arr = []
    for (let i of arr){
        [dest, pr, st] = i.split('|');
        new_arr.push(new ticket(dest, pr, st));
    }

    new_arr.sort((a, b) => {
        if (a[criteria] < b[criteria]){
            return -1
        }
        else if (a[criteria] > b[criteria]){
            return 1
        }
        else{
            return 0
        }
    })
    return new_arr
}
