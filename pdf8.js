/*
    The difference between array[index] and array.at(index) is that array.at(index) not as widely supported as the standard bracket notation
*/

function newCharArray(num, char){
    const charArray = []
    for (let i = 0; i < num; i++){
        charArray.push(char);
    }
    return charArray;
}

// console.log(newCharArray(5, "A"))

function deleteItemArray(num, array){
    if (array.length < num){
        return "Array Length is to small";
    } else{
        for (let i = 0; i < num; i++){
            array.pop();
        }
    }
    return array;
}

// console.log(deleteItemArray(3, ['a', 'b', 'c', 'e']));

function newFirstItemArray(num, array){
    array.unshift(num);
    return array;
}

// console.log(newFirstItemArray(8, [1, 2, 3]));
function newArray(array1, array2){
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

function removeOneDigit(array){
    for (let i; i < array.length; i++){
        if (array[i].length != 2){
            array.pop(array[i]);
        }
    }
    return array;
}

function twoDigits(array){
    const newArray = array.filter(function(array){
        for (let i; i < array.length; i++){
            if (array[i].length != 2){
                array.pop(array[i]);
            }
        }
        return array;
    });
    return newArray;
}

console.log(twoDigits([1, 22, 55, 8]));