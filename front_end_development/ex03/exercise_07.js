class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getName() {
        return this.name;
    }

    getAge() {
        return this.age;
    }

    sayGreeting() {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
}

const person1 = new Person('Pentti', 55);
const person2 = new Person('Marjatta', 53);


console.log(person1.getName());
console.log(person2.getAge());
console.log(person1.sayGreeting());
console.log(person2.sayGreeting());
