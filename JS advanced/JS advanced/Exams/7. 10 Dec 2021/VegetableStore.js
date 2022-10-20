class VegetableStore{
    constructor(ow, lo){
        this.owner = ow;
        this.location = lo;
        this.availableProducts = [];
    }

    loadingVegetables(veges){
        let added = [];
        for (let vege of veges){
            let [ime, kol, cena] = vege.split(' ');
            kol = Number(kol);
            cena = Number(cena);
            let not_found = true;
            for (let product of this.availableProducts){
                if (product.type == ime){
                    product.quantity += kol;
                    if (cena > product.price){
                        product.price = cena;
                    }
                    not_found = false;
                    break
                }
            }
            if (not_found){
                this.availableProducts.push({'type': ime, 'quantity': kol, 'price': cena})
            }
            if (!added.includes(ime)){
                added.push(ime);
            }
        }
        let res = `Successfully added ${added.join(', ')}`
        return res
    }

    buyingVegetables(selected){
        let total_price = 0;
        for (let sel of selected){
            let [typ, quan] = sel.split(' ')
            let not_found = true;
            for (let product of  this.availableProducts){
                if (typ == product.type){
                    if (quan <= product.quantity){
                        product.quantity -= quan;
                        total_price += product.price * quan;
                        not_found = false;
                    }
                    else{
                        throw new Error(`The quantity ${quan} for the vegetable ${typ} is not available in the store, your current bill is $${total_price.toFixed(2)}.`)
                    }
                }
            }
            if (not_found){
                throw new Error(`${typ} is not available in the store, your current bill is $${total_price.toFixed(2)}.`)
            }
            not_found = true;
        }
        return `Great choice! You must pay the following amount $${total_price.toFixed(2)}.`
    }

    rottingVegetable(typ, quan){
        for (let product of this.availableProducts){
            if (typ == product.type){
                if (quan >= product.quantity){
                    product.quantity = 0;
                    return `The entire quantity of the ${typ} has been removed.`
                }
                else{
                    product.quantity -= quan;
                    return `Some quantity of the ${typ} has been removed.`
                }
            }
        }
        throw new Error(`${typ} is not available in the store.`)
    }

    revision(){
        let res = "Available vegetables:\n"
        let sorted = this.availableProducts.sort((a, b) => a.price - b.price)
        for (let product of sorted){
            res += `${product.type}-${product.quantity}-$${product.price}\n`
        }
        res += `The owner of the store is ${this.owner}, and the location is ${this.location}.`
        return res
    }

}