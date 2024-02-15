let person = {name: "Pentti", age: 22, country: "Finland"};
let json_person = JSON.stringify(person);

console.log(json_person);

let jsonString = '{"name":"Pentti","age":22,"country":"Finland"}';
let js_person = JSON.parse(jsonString);

console.log(js_person);