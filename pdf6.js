function evalNumber(firstNumber, secondNumber, mathAction){
    if (mathAction == "add"){
        return `Sum of ${firstNumber} and ${secondNumber} is ${firstNumber + secondNumber} `
    }
    else if(mathAction == "subtract"){
        return `Difference of ${firstNumber} and ${secondNumber} is ${firstNumber - secondNumber}`
    }
    else if(mathAction == "multiply"){
        return `Product of ${firstNumber} and ${secondNumber} is ${firstNumber * secondNumber}`
    }
    else if(mathAction == "divide"){
        return `Division of ${firstNumber} and ${secondNumber} is ${firstNumber / secondNumber}`
    }
    else if(mathAction == "modulus"){
        return `Modulus of ${firstNumber} and ${secondNumber} is ${firstNumber % secondNumber}`
    }
}

console.log(evalNumber(15, 10, "add"))
console.log(evalNumber(20, 8, "subtract"))
console.log(evalNumber(12, 4, "multiply"))
console.log(evalNumber(28, 7, "divide"))
console.log(evalNumber(22, 3, "modulus"))