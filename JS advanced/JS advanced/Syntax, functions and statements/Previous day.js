function solve(a, b, c){
    const date = new Date(a, b - 1, c);
    date.setDate(date.getDate() - 1);
    year = date.getFullYear();
    month = date.getMonth();
    day = date.getDate();
    console.log(`${year}-${month + 1}-${day}`)
}