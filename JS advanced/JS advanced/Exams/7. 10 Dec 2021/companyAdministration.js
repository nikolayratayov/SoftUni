const { expect } = require("chai");

const companyAdministration = {

    hiringEmployee(name, position, yearsExperience) {
        if (position == "Programmer") {
            if (yearsExperience >= 3) {
                return `${name} was successfully hired for the position ${position}.`;
            } else {
                return `${name} is not approved for this position.`;
            }
        }
        throw new Error(`We are not looking for workers for this position.`);
    },
    calculateSalary(hours) {

        let payPerHour = 15;
        let totalAmount = payPerHour * hours;

        if (typeof hours !== "number" || hours < 0) {
            throw new Error("Invalid hours");
        } else if (hours > 160) {
            totalAmount += 1000;
        }
        return totalAmount;
    },
    firedEmployee(employees, index) {

        let result = [];

        if (!Array.isArray(employees) || !Number.isInteger(index) || index < 0 || index >= employees.length) {
            throw new Error("Invalid input");
        }
        for (let i = 0; i < employees.length; i++) {
            if (i !== index) {
                result.push(employees[i]);
            }
        }
        return result.join(", ");
    }

}


describe("Tests …", function() {
    describe("TODO …", function() {
        it("TODO …", function() {
            expect(() => companyAdministration.hiringEmployee('niki', 'asd', 5)).to.throw(`We are not looking for workers for this position.`)
            expect(companyAdministration.hiringEmployee('niki', 'Programmer', 3)).to.be.equal(`niki was successfully hired for the position Programmer.`)
            expect(companyAdministration.hiringEmployee('niki', 'Programmer', 2)).to.be.equal(`niki is not approved for this position.`)
        
            expect(() => companyAdministration.calculateSalary('s')).to.throw('Invalid hours');
            expect(() => companyAdministration.calculateSalary(-1)).to.throw('Invalid hours');
            expect(companyAdministration.calculateSalary(5)).to.be.equal(75);
            expect(companyAdministration.calculateSalary(161)).to.be.equal(3415);

            expect(() => companyAdministration.firedEmployee('da', 2)).to.throw('Invalid input');
            expect(() => companyAdministration.firedEmployee(['a', 'b'], 's')).to.throw('Invalid input');
            expect(() => companyAdministration.firedEmployee(['a', 'b'], 1.5)).to.throw('Invalid input');
            expect(() => companyAdministration.firedEmployee(['a', 'b'], -1)).to.throw('Invalid input');
            expect(() => companyAdministration.firedEmployee(['a', 'b'], 2)).to.throw('Invalid input');
            expect(companyAdministration.firedEmployee(['a', 'b', 'c'], 1)).to.be.equal('a, c')
        });
     });
});
