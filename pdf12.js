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


