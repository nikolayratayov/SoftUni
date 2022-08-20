function solve([cols, rows, x, y]){
    let matrix = new Array(rows)
    for (let i = 0; i < cols; i++){
        matrix[i] = new Array(cols).fill(false)
    }
    for (let row = 0; row < rows; row++){
        for (let col = 0; col < cols; col++){
            let diff_rows = Math.abs(x - row)
            let diff_cols = Math.abs(y - col)
            let diff = Math.max(diff_cols, diff_rows)
            matrix[row][col] = diff + 1
        }
    }

    for (let x = 0; x < matrix.length; x++){
        console.log(matrix[x].join(' '))
    }
}