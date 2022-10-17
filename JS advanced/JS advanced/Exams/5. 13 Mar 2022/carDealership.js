class CarDealership {
    constructor(n){
        this.name = n;
        this.availableCars = [];
        this.soldCars = [];
        this.totalIncome = 0;
    }
    addCar(mod, hp, pr, mile){
        if (mod && hp >= 0 && Number.isInteger(hp) && pr >= 0 && mile >= 0){
            let price = Number(pr).toFixed(2)
            this.availableCars.push({'model': mod, 'horsepower': hp, 'price': price, 'mileage': mile})
            return `New car added: ${mod} - ${hp} HP - ${mile.toFixed(2)} km - ${price}$`
        }
        throw new Error('Invalid input!')
    }
    sellCar(mod, desire){
        for (let i = 0; i < this.availableCars.length; i++){
            if (this.availableCars[i].model == mod){
                let diff = this.availableCars[i].mileage - desire;
                if (this.availableCars[i].mileage <= desire){
                    let sold_price = this.availableCars[i].price;
                    this.soldCars.push(this.availableCars.splice(i, 1)[0]);
                    this.totalIncome += Number(sold_price);
                    return `${mod} was sold for ${sold_price}$`
                }
                else if (diff <= 40000){
                    let sold_price = (this.availableCars[i].price * 0.95).toFixed(2);
                    let sold_car = {'model': this.availableCars[i].model, 'horsepower': this.availableCars[i].horsepower, 'price': sold_price, 'mileage': this.availableCars[i].mileage}
                    this.availableCars.splice(i, 1)
                    this.soldCars.push(sold_car);
                    this.totalIncome += Number(sold_price);
                    return `${mod} was sold for ${sold_price}$`
                }
                else{
                    let sold_price = (this.availableCars[i].price * 0.9).toFixed(2);
                    let sold_car = {'model': this.availableCars[i].model, 'horsepower': this.availableCars[i].horsepower, 'price': sold_price, 'mileage': this.availableCars[i].mileage}
                    this.availableCars.splice(i, 1)
                    this.soldCars.push(sold_car);
                    this.totalIncome += Number(sold_price);
                    return `${mod} was sold for ${sold_price}$`
                }
            }
        }
        throw new Error(`${mod} was not found!`)
    }
    currentCar(){
        if (this.availableCars.length == 0){
            return 'There are no available cars'
        }
        let res = '-Available cars:\n'
        for (let car of this.availableCars){
            res += `---${car.model} - ${car.horsepower} HP - ${(car.mileage).toFixed(2)} km - ${car.price}$\n`
        }
        return res.substring(0, res.length - 1);
    }
    salesReport(crit){
        let res = `-${this.name} has a total income of ${this.totalIncome.toFixed(2)}$\n`;
        res += `-${this.soldCars.length} cars sold:\n`
        let sorted_cars
        if (crit == 'horsepower'){
            sorted_cars = this.soldCars.sort((a, b) => {return b.horsepower - a.horsepower})
        }
        else if (crit == 'model'){
            sorted_cars = this.soldCars.sort((a, b) => a.model.localeCompare(b.model))
        }
        else{throw new Error('Invalid criteria!')}
        for (let car of sorted_cars){
            res += `---${car.model} - ${car.horsepower} HP - ${car.price}$\n`
        }
        return res.substring(0, res.length - 1)
    }
}
