const firstStudent = {
    name: "Gilad",
    age: 19,
    grades: [95, 96, 97, 98, 99],
    average: function () {
        let sum = this.grades.reduce(function (a, b) {
            return a + b;
        });
        let myAverage = sum / this.grades.length;

        // Function that count all the vowels letters in the name
        let countVowel = () => {
            return this.name.match(/[aeiou]/gi).length;
        }
        return myAverage + countVowel();
    }
}
const secondStudent = {
    name: "Evyatar",
    age: 25,
    grades: [95, 96, 97, 98, 99],
    average: function () {
        let sum = this.grades.reduce(function (a, b) {
            return a + b;
        });
        let myAverage = sum / this.grades.length;

        // Function that count all the vowels letters in the name
        let countVowel = () => {
            return this.name.match(/[aeiou]/gi).length;
        }
        return myAverage + countVowel();
    }
}
const thirdStudent = {
    name: "Yonatan",
    age: 16,
    grades: [95, 96, 97, 98, 99],
    average: function () {
        let sum = this.grades.reduce(function (a, b) {
            return a + b;
        });
        let myAverage = sum / this.grades.length;

        // Function that count all the vowels letters in the name
        let countVowel = () => {
            return this.name.match(/[aeiou]/gi).length;
        }
        return myAverage + countVowel();
    }
}
const forthStudent = {
    name: "Iftach",
    age: 29,
    grades: [95, 96, 97, 98, 99],
    average: function () {
        let sum = this.grades.reduce(function (a, b) {
            return a + b;
        });
        let myAverage = sum / this.grades.length;

        // Function that count all the vowels letters in the name
        let countVowel = () => {
            return this.name.match(/[aeiou]/gi).length;
        }
        return myAverage + countVowel();
    }
}
const fifthStudent = {
    name: "Malka",
    age: 32,
    grades: [95, 96, 97, 98, 99],
    average: function () {
        let sum = this.grades.reduce(function (a, b) {
            return a + b;
        });
        let myAverage = sum / this.grades.length;

        // Function that count all the vowels letters in the name
        let countVowel = () => {
            return this.name.match(/[aeiou]/gi).length;
        }
        return myAverage + countVowel();
    }
}

console.log(firstStudent);
console.log(secondStudent);
console.log(thirdStudent);
console.log(forthStudent);
console.log(fifthStudent);

const studentsArray = [firstStudent, secondStudent, thirdStudent, forthStudent, fifthStudent];

for (let i = 0; i < studentsArray.length; i++) {
    console.log(`The index of the student ${studentsArray[i].name} in students array is: ${i}`);
}


for (let i = 0; i < studentsArray.length; i++) {
    console.log(`name: ${studentsArray[i].name}`);
    console.log(`age: ${studentsArray[i].age}`);
    console.log(`grades: ${studentsArray[i].grades}`);
    console.log(`average: ${studentsArray[i].average()}`);
    console.log(`\n`);
}


function checkAdult(student) {
    return student.age >= 18;
}


const adultsArray = studentsArray.filter(checkAdult);
console.log(adultsArray);


class Car {
    constructor(manufactorCompany, model, manufactorYear){
        this.manufactorCompany = manufactorCompany;
        this.model = model;
        this.manufactorYear = manufactorYear;
    }
    age() {
        const date = new Date();
        return date.getFullYear() - this.manufactorYear;
    }
}

const myFirstCar = new Car("Ford", "kk", 2014);
const mySecondCar = new Car("BMW", "i", 2018);
const myThirdCar = new Car("mazda", "x3", 2021);


console.log(`The properties of my first car: \n manufactorCompany: ${myFirstCar.manufactorCompany}, model: ${myFirstCar.model}, manufactorYear: ${myFirstCar.manufactorYear}`);

console.log(`The properties of my second car: \n manufactorCompany: ${mySecondCar.manufactorCompany}, model: ${mySecondCar.model}, manufactorYear: ${mySecondCar.manufactorYear}`);

console.log(`The properties of my third car: \n manufactorCompany: ${myThirdCar.manufactorCompany}, model: ${myThirdCar.model}, manufactorYear: ${myThirdCar.manufactorYear}`);