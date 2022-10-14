class ChristmasDinner {
    constructor(budget){
        if (Number(budget) < 0){ throw new Error('The budget cannot be a negative number')}
        this.budget = Number(budget);
        this.dishes = [];
        this.products = [];
        this.guests = {};
    }
    shopping(pr){
        let price = Number(pr[1]);
        if (price > this.budget){throw new Error('Not enough money to buy this product')}
        this.products.push(pr[0]);
        this.budget -= price;
        return `You have successfully bought ${pr[0]}!`
    }
    recipes(recipe){
        let isPresent = true;
        let { recipeName, productsList } = recipe;
        productsList.forEach((product) => {
            if (!this.products.includes(product)) {
                isPresent = false;
            }
        });
        if (isPresent) {
            this.dishes.push({ recipeName, productsList });
            return `${recipeName} has been successfully cooked!`;
        }
        throw new Error('We do not have this product');
    }
    inviteGuests(name, dish){
        if ( !dish in this.dishes){throw new Error('We do not have this dish')}
        if ( name in this.guests){throw new Error('This guest has already been invited')}
        this.guests[name] = dish;
        return `You have successfully invited ${name}!`
    }
    showAttendance(){
        let res = '';
        for (let key in this.guests){
            for (let obj of this.dishes){
                if (obj.recipeName == this.guests[key]){
                    res += `${key} will eat ${this.guests[key]}, which consists of ${obj.productsList.join(', ')}\n`
                }
            }
        }
        res = res.substring(0, res.length - 1)
        return res;
    }
}
