function solve(rows, cols){
    let matrix = new Array(rows)
    for (let i = 0; i < rows; i++){
        matrix[i] = new Array(cols).fill(false)
    }
    let count = 0
    let top = 0
    let right = matrix[0].length - 1
    let down = matrix.length - 1
    let left = 0
    go = true
while (go){
    for (let i = 0; i < matrix[0].length; i++){
        if (matrix[top][i] == false){
            count += 1
            matrix[top][i] = count
        }
        if (count == rows * cols){go = false}
    }
    for (let i = 0; i < matrix.length; i++){
        if (matrix[i][right] == false){
            count += 1
            matrix[i][right] = count
        }
        if (count == rows * cols){go = false}
    }

    for (let i = matrix[0].length - 1; i >= 0; i--){
        if (matrix[down][i] == false){
            count += 1
            matrix[down][i] = count
        }
        if (count == rows * cols){go = false}
    }

    for (let i = matrix.length - 1; i >= 0; i--){
        if (matrix[i][left] == false){
            count += 1
            matrix[i][left] = count
        }
        if (count == rows * cols){go = false}
    }

    top += 1
    right -= 1
    down -= 1
    left += 1

    }

    for (let i = 0; i < rows; i++){
        console.log(matrix[i].join(' '))
    }
}