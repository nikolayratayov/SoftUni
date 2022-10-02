function solve(){
    let protein = 0;
    let carbohydrate = 0;
    let fat = 0;
    let flavours = 0;
    return function(a){
        [command, second, qty] = a.split(' ')
        if (command == 'report'){
            return `protein=${protein} carbohydrate=${carbohydrate} fat=${fat} flavour=${flavours}`
        }
        else if (command == 'restock'){
            if (second == 'protein'){protein += Number(qty)}
            else if (second == 'fat'){fat += Number(qty)}
            else if (second == 'flavour'){flavours += Number(qty)}
            else{carbohydrate += Number(qty)}
            return 'Success'
        }
        else{
            if (second == 'apple'){
                if (carbohydrate < 1 * qty){return `Error: not enough carbohydrate in stock`}
                else if (flavours < 2 * qty){return `Error: not enough fat in stock`}
                else {
                    carbohydrate -= 1 * qty;
                    flavours -= 2 * qty;
                    return 'Success'
                }
            }
            else if (second == 'lemonade'){
                if (carbohydrate < 10 * qty){return 'Error: not enough carbohydrate in stock'}
                else if (flavours < 20 * qty){return 'Error: not enough flavours in stock'}
                else{
                    carbohydrate -= 10 * qty;
                    flavours -= 20 * qty;
                    return 'Success'
                }
            }
            else if (second == 'burger'){
                if (carbohydrate < 5 * qty){return 'Error: not enough carbohydrate in stock'}
                else if (fat < 7 * qty){return 'Error: not enough fat in stock'}
                else if (flavours < 3 * qty){return 'Error: not enough flavours in stock'}
                else{
                    carbohydrate -= 5 * qty;
                    fat -= 7 * qty;
                    flavours -= 3 * qty;
                    return 'Success'
                }
            }
            else if (second == 'eggs'){
                if (protein < 5 * qty){return 'Error: not enough protein in stock'}
                else if (fat < 1 * qty){return 'Error: not enough fat in stock'}
                else if (flavours < 1 * qty){return 'Error: not enough flavours in stock'}
                else{
                    protein -= 5 * qty;
                    fat -= 1 * qty;
                    flavours -= 1 * qty;
                    return 'Success'
                }
            }
            else{
                if (protein < 10 * qty){return 'Error: not enough protein in stock'}
                else if (carbohydrate < 10 * qty){return 'Error: not enough carbohydrate in stock'}
                else if (fat < 10 * qty){return 'Error: not enough fat in stock'}
                else if(flavours < 10 * qty){return 'Error: not enough flavours in stock'}
                else{
                    protein -= 10 * qty;
                    carbohydrate -= 10 * qty;
                    fat -= 10 * qty;
                    flavours -= 10 * qty;
                    return 'Success'
                }
            }
        }
    }
}
