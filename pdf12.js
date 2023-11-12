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
    age: 30,
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