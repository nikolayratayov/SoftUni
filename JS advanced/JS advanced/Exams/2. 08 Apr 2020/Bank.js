class Bank {
    #bankName;
    constructor(n){
        this.#bankName = n;
        this.allCustomers = [];
    }

    newCustomer(customer){
        for (let person of this.allCustomers){
            if (person.firstName == customer.firstName && person.lastName == customer.lastName && person.personalId == customer.personalId){
                throw new Error(`${customer.firstName} ${customer.lastName} is already our customer!`)
            }   
        }
        this.allCustomers.push({
            'firstName': customer.firstName,
            'lastName': customer.lastName,
            'personalId': customer.personalId,
            'totalMoney': 0,
            'transactions': []
        })
        return customer
    }

    depositMoney(id, amount){
        for (let person of this.allCustomers){
            if (person.personalId == id){
                person.totalMoney += amount;
                person.transactions.push([person.firstName, person.lastName, 'deposit', amount]);
                return `${person.totalMoney}$`
            }
        }
        throw new Error('We have no customer with this ID!')
    }

    withdrawMoney(id, amount){
        for (let person of this.allCustomers){
            if(person.personalId == id){
                if (person.totalMoney >= amount){
                    person.totalMoney -= amount;
                    person.transactions.push([person.firstName, person.lastName, 'withdraw', amount]);
                    return `${person.totalMoney}$`
                }
                else{throw new Error(`${person.firstName} ${person.lastName} does not have enough money to withdraw that amount!`)}
            }
        }
        throw new Error('We have no customer with this ID!')
    }

    customerInfo(id){
        for (let person of this.allCustomers){
            if (person.personalId == id){
                let res = '';
                res += `Bank name: ${this.#bankName}\n`;
                res += `Customer name: ${person.firstName} ${person.lastName}\n`;
                res += `Customer ID: ${person.personalId}\n`;
                res += `Total Money: ${person.totalMoney}$\n`;
                res += `Transactions:\n`;
                for (let i = person.transactions.length - 1; i > 0; i--){
                    if (person.transactions[i][2] == 'deposit'){
                        res += `${i + 1}. ${person.firstName} ${person.lastName} made deposit of ${person.transactions[i][3]}$!\n`
                    }
                    else{
                        res += `${i + 1}. ${person.firstName} ${person.lastName} withdrew ${person.transactions[i][3]}$!\n`
                    }
                }
                if (person.transactions[0][2] == 'deposit'){
                    res += `1. ${person.firstName} ${person.lastName} made deposit of ${person.transactions[0][3]}$!`
                }
                else{
                    res += `1. ${person.firstName} ${person.lastName} withdrew ${person.transactions[0][3]}$!`
                }
                return res;
            }
            throw new Error('We have no customer with this ID!')
        }
    }
}
