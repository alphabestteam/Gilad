/*
    The difference between array[index] and array.at(index) is that array.at(index) not as widely supported as the standard bracket notation
*/

function newCharArray(num, char) {
    const charArray = []
    for (let i = 0; i < num; i++) {
        charArray.push(char);
    }
    return charArray;
}

// console.log(newCharArray(5, "A"))

function deleteItemArray(num, array) {
    if (array.length < num) {
        return "Array Length is to small";
    } else {
        for (let i = 0; i < num; i++) {
            array.pop();
        }
    }
    return array;
}

// console.log(deleteItemArray(3, ['a', 'b', 'c', 'e']));

function newFirstItemArray(num, array) {
    array.unshift(num);
    return array;
}

// console.log(newFirstItemArray(8, [1, 2, 3]));
function newArray(array1, array2) {
    const array3 = array1.concat(array2);
    return array3;
}

// console.log(newArray(['a', 'b', 'c'], ['d', 'e', 'f']));

function stringToUpperCase(array) {
    const newArray = array.map(function (str) {
        return str.toUpperCase();
    });
    return newArray;
}

// console.log(stringToUpperCase(['gilad', 'is', 'the', 'best']));

function removeOneDigit(array) {
    for (let i; i < array.length; i++) {
        if (array[i].length != 2) {
            array.pop(array[i]);
        }
    }
    return array;
}

function twoDigits(array) {
    const newArray = array.filter((num) => num.toString().length == 2 && typeof (num) == "number");
    return newArray;
}

// console.log(twoDigits([1, 22, 55, 8, 333, 74, "df"]));

function isExist(array, parameter) {
    return array.includes(parameter);
}

// console.log(isExist([1, 2, 3, 4], "d"));

function firstBigNumber(array) {
    return array.find((value) => value > 10);
}

// console.log(firstBigNumber([2, 3, 11, 1]));

function isFirstBigNumber(firstBigNumber, array) {
    return (typeof (firstBigNumber(array)) == "number");
}

// console.log(isFirstBigNumber(firstBigNumber, [1, 3, 5]));


/*
    The function does not return a numerically sorted array because
    it returns in order starting from the first digit in the number and so on.
    To fix this you need to provide a compare function.
*/

function starsInArray(array) {
    const newArray = array.sort(function (a, b) { return a - b });
    return newArray.join("**");
}

// console.log(starsInArray([1, 2, 3, 4 ,5]));

function alphabeticalArray(array) {
    return array.sort();
}

// console.log(alphabeticalArray(["ab", "aa", "cc", "dd"])); 


function isBiggerLimit(value, limit) {
    return value < limit;
};

function arrayIsBiggerLimit(array, limit) {
    return array.every(func = (element) => isBiggerLimit(element, limit));
}

// console.log(arrayIsBiggerLimit([1, 2, 6, 1], 4));

function isBiggerFromNumber(value, limit) {
    return value > limit;
};

function arrayIsBiggerFromNumber(array, limit) {
    return array.some(func = (element) => isBiggerFromNumber(element, limit));
}

console.log(arrayIsBiggerFromNumber([1, 2, 1, 7], 4));
