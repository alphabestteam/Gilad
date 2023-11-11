function helloWorld() {
    return "Hello World";
}
console.log(helloWorld());


function sayHi(name) {
    return `Hello ${name}`;
}
console.log(sayHi('Gilad'));


let setSquared = (num) => num ** 2;
console.log(setSquared(4));

let rectangleArea = (firstRib, secondRib) => firstRib * secondRib;
console.log(rectangleArea(6, 5));


let circleValues = (radius) => { return [(2 * Math.PI * radius), ((radius ** 2) * Math.PI)] };
console.log(circleValues(1));

let mone = 0;

let countVowels = (text) => {
    Array.from(text).forEach(element => {
        if (["a", "e", "i", "o", "u"].includes(element.toLowerCase())) {
            mone++;
        }
    });
    return mone;
};
console.log(countVowels('May the Force be with you. Always'));


