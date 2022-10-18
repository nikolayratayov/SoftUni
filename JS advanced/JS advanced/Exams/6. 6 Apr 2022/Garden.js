class Garden {
    constructor(sp){
        this.spaceAvailable = Number(sp);
        this.plants = [];
        this.storage = [];
    }

    addPlant(n, req){
        if (this.spaceAvailable - req <= 0){throw new Error('Not enough space in the garden.')}
        this.plants.push({'plantName': n, 'spaceRequired': req, 'ripe': false, 'quantity': 0});
        this.spaceAvailable -= req;
        return `The ${n} has been successfully planted in the garden.`
    }

    ripenPlant(n, quan){
        for (let plant of this.plants){
            if (plant.plantName == n){
                if (!plant.ripe){
                    if (quan > 0){
                        plant.ripe = true;
                        plant.quantity += quan
                        if (quan == 1){
                            return `${quan} ${n} has successfully ripened.`
                        }
                        else{
                            return `${quan} ${n}s have successfully ripened.`
                        }
                    }
                    throw new Error('The quantity cannot be zero or negative.')
                }
                throw new Error(`The ${n} is already ripe.`)
            }
        }
        throw new Error(`There is no ${n} in the garden.`)
    }

    harvestPlant(n){
        for (let i = 0; i < this.plants.length; i++){
            if (this.plants[i].plantName == n){
                if (this.plants[i].ripe){
                    this.spaceAvailable += this.plants[i].spaceRequired;
                    this.storage.push({'plantName': n, 'quantity': this.plants[i].quantity})
                    this.plants.splice(i, 1);
                    return `The ${n} has been successfully harvested.`
                }
                throw new Error(`The ${n} cannot be harvested before it is ripe.`)
            }
        }
        throw new Error(`There is no ${n} in the garden.`)
    }

    generateReport(){
        let res = `The garden has ${this.spaceAvailable} free space left.\n`;
        let arr_of_plants = []
        for (let plant of this.plants){
            arr_of_plants.push(plant.plantName)
        }
        arr_of_plants.sort();
        res += `Plants in the garden: ` + `${arr_of_plants.join(', ')}\n`;

        let storage_plants
        if (this.storage.length == 0){
            storage_plants = 'Plants in storage: The storage is empty.'
        }
        else{
            storage_plants = 'Plants in storage: '
            for (let stor of this.storage){
                storage_plants += `${stor.plantName} (${stor.quantity}), `
            }
            storage_plants = storage_plants.substring(0, storage_plants.length - 2)
        }
        res += storage_plants;
        return res
    }
}