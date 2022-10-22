const { expect } = require("chai");

const chooseYourCar = {
    choosingType(type, color, year) {
        if (year < 1900 || year > 2022) {
            throw new Error(`Invalid Year!`);
        } else {
            if (type == "Sedan") {

                if (year >= 2010) {
                    return `This ${color} ${type} meets the requirements, that you have.`;
                } else {
                    return `This ${type} is too old for you, especially with that ${color} color.`;
                }
            }
            throw new Error(`This type of car is not what you are looking for.`);
        }
    },

    brandName(brands, brandIndex) {

        let result = [];

        if (!Array.isArray(brands) || !Number.isInteger(brandIndex) || brandIndex < 0 || brandIndex >= brands.length) {
            throw new Error("Invalid Information!");
        }
        for (let i = 0; i < brands.length; i++) {
            if (i !== brandIndex) {
                result.push(brands[i]);
            }
        }
        return result.join(", ");
    },

    carFuelConsumption(distanceInKilometers, consumptedFuelInLiters) {

        let litersPerHundredKm =((consumptedFuelInLiters / distanceInKilometers)* 100).toFixed(2);

        if (typeof distanceInKilometers !== "number" || distanceInKilometers <= 0 ||
            typeof consumptedFuelInLiters !== "number" || consumptedFuelInLiters <= 0) {
            throw new Error("Invalid Information!");
        } else if (litersPerHundredKm <= 7) {
            return `The car is efficient enough, it burns ${litersPerHundredKm} liters/100 km.`;
        } else {
            return `The car burns too much fuel - ${litersPerHundredKm} liters!`;
        }
    }
}


describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            expect(() => chooseYourCar.choosingType('sad', 'red', 1990)).to.throw(`This type of car is not what you are looking for.`);
            expect(() => chooseYourCar.choosingType('Sedan', 'red', 1899)).to.throw(`Invalid Year!`);
            expect(() => chooseYourCar.choosingType('Sedan', 'red', 2023)).to.throw(`Invalid Year!`);
            expect(chooseYourCar.choosingType('Sedan', 'red', 2009)).to.be.equal(`This Sedan is too old for you, especially with that red color.`)
            expect(chooseYourCar.choosingType('Sedan', 'red', 2010)).to.be.equal(`This red Sedan meets the requirements, that you have.`)

            expect(() => chooseYourCar.brandName('das', 1)).to.throw('Invalid Information!');
            expect(() => chooseYourCar.brandName(['a', 'b'], -1)).to.throw('Invalid Information!');
            expect(() => chooseYourCar.brandName(['a', 'b'], 2)).to.throw('Invalid Information!');
            expect(() => chooseYourCar.brandName(['a', 'b'], 1.5)).to.throw('Invalid Information!');
            expect(() => chooseYourCar.brandName(['a', 'b'], '1')).to.throw('Invalid Information!');
            expect(chooseYourCar.brandName(["BMW", "Toyota", "Peugeot"], 0)).to.be.equal('Toyota, Peugeot')
            expect(chooseYourCar.brandName(["BMW", "Toyota", "Peugeot"], 1)).to.be.equal('BMW, Peugeot')
            expect(chooseYourCar.brandName(["BMW", "Toyota", "Peugeot"], 2)).to.be.equal('BMW, Toyota')

            expect(() => chooseYourCar.carFuelConsumption('1', 1.5)).to.throw('Invalid Information!')
            expect(() => chooseYourCar.carFuelConsumption(-1, 1.5)).to.throw('Invalid Information!')
            expect(() => chooseYourCar.carFuelConsumption(1, '1')).to.throw('Invalid Information!')
            expect(() => chooseYourCar.carFuelConsumption(1, -0.1)).to.throw('Invalid Information!')
            expect(chooseYourCar.carFuelConsumption(2, 3)).to.be.equal('The car burns too much fuel - 150.00 liters!')
            expect(chooseYourCar.carFuelConsumption(100, 7.1)).to.be.equal('The car burns too much fuel - 7.10 liters!')
            expect(chooseYourCar.carFuelConsumption(100, 3)).to.be.equal('The car is efficient enough, it burns 3.00 liters/100 km.')
            expect(chooseYourCar.carFuelConsumption(100, 7)).to.be.equal('The car is efficient enough, it burns 7.00 liters/100 km.')

        });
     });
});
