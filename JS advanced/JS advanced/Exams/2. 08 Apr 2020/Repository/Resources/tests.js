const { expect } = require("chai");
let { Repository } = require("./solution.js");

describe("Tests …", function () {
    describe("TODO …", function () {
        it("TODO …", function () {
            let a = new Repository({'a': 10});
            expect(a).to.haveOwnProperty('data');
            expect(a).to.haveOwnProperty('props');
            expect(a).to.haveOwnProperty('nextId');
        });
        it('getcount', () => {
            let a = new Repository({'a': 10});
            expect(a.count).to.be.equal(0);
        })
        it('add', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "object"
            };
            let repository = new Repository(properties);
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: new Date(1998, 0, 7)
            };
            expect(repository.add(entity)).to.be.equal(0);
            let entity2 = {
                name: "Gosho",
                age: 33,
                birthday: new Date(2000, 0, 7)
            };
            let entity3 = {
                name: "eee",
                age: 43,
                birthday: new Date(2001, 0, 7)
            };
            expect(repository.add(entity2)).to.be.equal(1);
            expect(repository.getId(0)['name']).to.be.equal("Pesho")
            expect(repository.getId(1)['age']).to.be.equal(33)
            expect(repository.add.bind(repository, ({eee: 'das'}))).to.throw('Property name is missing from the entity!')
            expect(repository.add.bind(repository, ({name: "Gosho",age: '23',birthday: new Date(2000, 0, 7)}))).to.throw('Property age is not of correct type!')
            expect(repository.add.bind(repository, ({name: 1,age: 23,birthday: new Date(2000, 0, 7)}))).to.throw('Property name is not of correct type!')
            expect(repository.add.bind(repository, ({name: 'eee',age: 23,birthday: 'das'}))).to.throw('Property birthday is not of correct type!')
            repository.update(1, entity);
            expect(repository.getId(1)['name']).to.be.equal("Pesho")
            expect(repository.getId.bind(repository, (10))).to.throw('Entity with id: 10 does not exist!')
            expect(repository.update.bind(repository, (10, entity))).to.throw('Entity with id: [object Object] does not exist!')
            expect(repository.del.bind(repository, (10))).to.throw('Entity with id: 10 does not exist!')
            repository.del(1);
            expect(repository.count).to.be.equal(1)
            expect(repository.getId.bind(repository, (1))).to.throw('Entity with id: 1 does not exist!')
            expect(repository.add(entity2)).to.be.equal(2);
            repository.update(2, entity3)
            expect(() => repository.update(2, {name: 1, age: 1, birthday: 1})).to.throw(TypeError)
        });
        it('off', () => {
            let properties = {
                name: "string",
                age: "number",
                birthday: "string"
            };
            let repository = new Repository(properties);
            let entity = {
                name: "Pesho",
                age: 22,
                birthday: 'eee'
            };
            let entity_to_check = {
                op: "Pesho",
                age: 22,
                birthday: 'eee'
            };
            repository.add(entity);
            expect(repository.getId(0)['birthday']).to.be.equal('eee')
            expect(repository.getId(0)).to.be.equal(entity)
            expect(repository._validate.bind(repository, (entity_to_check))).to.throw('Property name is missing from the entity!')
            expect(repository._validate.bind(repository, ({name: "Pesho",age: 22,birthday: {}}))).to.throw(TypeError)
        })
    });
});