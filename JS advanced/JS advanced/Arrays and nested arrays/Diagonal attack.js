function solve(a){
    let orig_matrix = []
    for (let i = 0; i < a.length; i++){
        let el_to_push = a[i].split(' ')
        orig_matrix.push(el_to_push)
    }
    
    let diag_1 = 0
    let diag_2 = 0
    let len_rows = orig_matrix.length
    for (let i = 0; i < orig_matrix.length; i++){
        diag_1 += parseInt(orig_matrix[i][i])
        diag_2 += parseInt(orig_matrix[len_rows - i - 1][i])
    }
    if (diag_1 === diag_2){
        output_matrix = new Array(a.length)
        for (let i = 0; i < orig_matrix[0].length; i++){
            output_matrix[i] = new Array(orig_matrix[0].length).fill(diag_1)
        }
        for (let i = 0; i < orig_matrix.length; i++){
            output_matrix[i][i] = orig_matrix[i][i]
            output_matrix[len_rows - i - 1][i] = orig_matrix[len_rows - i - 1][i]
        }
    }
    else{
        output_matrix = orig_matrix
    }
    
    for (let z = 0; z < orig_matrix.length; z++){
        console.log(output_matrix[z].join(' '))
    }
}