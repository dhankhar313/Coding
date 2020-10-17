// Objects are like dictionaries in python
person = {
    name: 'Rahul',
    age: 20,
    class: 'CSE 12'
};

// Can be accessed using . operator
console.log(person.name);
console.log(person.age);
console.log(person.class);

person.name = 'Madhu';
console.log(person.name)

person['name'] = 'Rahul'
console.log(person.name)

person.clg = 'CU';
console.log(person)

delete person.clg;
console.log(person);

console.log(person.hasOwnProperty('clg'));
console.log(person.hasOwnProperty('name'));