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


let isSameLength = (firstArray, secondArray) => {
    if (firstArray.length == secondArray.length) { return true } else { return false };
};
console.log(isSameLength([1, 2, 3, 4], ["3", "aaa", "b", "q"]));


let numberToArray = (number) => { return Array.from(String(number)).map(Number) };
console.log(numberToArray(12345));


const myArr = [1, "hello", true, 0, false, "", " ", null, undefined, NaN,
    2, "world", true, {}, [], 3, "foo", 'true', 'false', "bar"];

let getTruthyFalsyArr = (array) => array.map(element => !!element);
console.log(getTruthyFalsyArr(myArr));
