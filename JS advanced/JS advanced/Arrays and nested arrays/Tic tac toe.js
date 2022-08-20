function solve(arr){
    function if_winner(board){
        if ((board[0][0] === board[0][1] && board[0][1]=== board[0][2] && board[0][2]=== 'X') ||
        (board[1][0] === board[1][1] && board[1][1] === board[1][2] && board[1][2] === 'X') ||
        (board[2][0] === board[2][1] && board[2][1] === board[2][2] && board[2][2] === 'X') ||
        (board[0][0] === board[1][0] && board[1][0] === board[2][0] && board[2][0] === 'X') ||
        (board[0][1] === board[1][1] && board[1][1] === board[2][1] && board[2][1] === 'X') ||
        (board[0][2] === board[1][2] && board[1][2] === board[2][2] && board[2][2] === 'X') ||
        (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[2][2] === 'X') ||
        (board[2][0] === board[1][1] && board[1][1] === board[0][2] && board[0][2] === 'X')){
            return true
        }
        else if ((board[0][0] === board[0][1] && board[0][1]=== board[0][2] && board[0][2]=== 'O') ||
        (board[1][0] === board[1][1] && board[1][1] === board[1][2] && board[1][2] === 'O') ||
        (board[2][0] === board[2][1] && board[2][1] === board[2][2] && board[2][2] === 'O') ||
        (board[0][0] === board[1][0] && board[1][0] === board[2][0] && board[2][0] === 'O') ||
        (board[0][1] === board[1][1] && board[1][1] === board[2][1] && board[2][1] === 'O') ||
        (board[0][2] === board[1][2] && board[1][2] === board[2][2] && board[2][2] === 'O') ||
        (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[2][2] === 'O') ||
        (board[2][0] === board[1][1] && board[1][1] === board[0][2] && board[0][2] === 'O')){
            return true
        }
        return false
        }
    let a = [[false, false, false],
            [false, false, false],
            [false, false, false]]
    let taken = 0
    let player = 'X'
    for(let i = 0; i < arr.length; i++){
        let nums_str = arr[i].split(' ')
        row = parseInt(nums_str[0])
        col = parseInt(nums_str[1])
        if (a[row][col] != false){
            console.log("This place is already taken. Please choose another!")
            continue
        }
        a[row][col] = player
        if (if_winner(a)){
            console.log(`Player ${player} wins!`)
            for (let j = 0; j < 3; j++){
                console.log(a[j].join('\t'))
            }
            break
        }
        taken += 1
        if (player === 'X'){
            player = 'O'
        }
        else{
            player = 'X'
        }
        if (taken == 9){
            console.log("The game ended! Nobody wins :(")
            for (let j = 0; j < 3; j++){
                console.log(a[j].join('\t'))
            }
            break
        }
    }
}