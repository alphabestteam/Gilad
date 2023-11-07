function findSeashellsIndicies (target, numberArray){
    const newNumberArray = []
    for (let i = 0; i < numberArray.length; i++){
        for (let j = i; j < numberArray.length; j++){
            if (numberArray[i] + numberArray[j] == target && i != j){
                newNumberArray.push([i, j])
            }
        }
    }
    return newNumberArray;
}

console.log(findSeashellsIndicies(30, [5, 15, 15, 21, 25]))