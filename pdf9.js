let stringParagraph = " Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo'sdream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages. "

function paragraphArray() {
    const myArray = stringParagraph.split("\n");
    return myArray;
}

// console.log(paragraphArray());

function convertWords() {
    stringParagraph = stringParagraph.replace("movie", "film");
    return stringParagraph;
}

// console.log(convertWords());

function replaceAllOccurrence() {
    stringParagraph = stringParagraph.replaceAll("Panda", "Bear");
    return stringParagraph;
}

// console.log(replaceAllOccurrence());

function replaceUpperCase() {
    stringParagraph = stringParagraph.toUpperCase();
    return stringParagraph;
}

// console.log(replaceUpperCase());

function replaceUpperCase() {
    stringParagraph = stringParagraph.toLowerCase();
    return stringParagraph;
}

// console.log(replaceUpperCase());


function firstIndexOfPo() {
    let indexOfPo = stringParagraph.indexOf("Po");
    return indexOfPo;
}

// console.log(firstIndexOfPo());


function cutPoText() {
    stringParagraph = stringParagraph.slice(firstIndexOfPo());
    return stringParagraph;
}

// console.log(cutPoText());

function withOutWhiteSpace() {
    stringParagraph = stringParagraph.replaceAll(' ', "");
    return stringParagraph;
}

// console.log(withOutWhiteSpace());

function cutPoTextUntilParagraph() {
    stringParagraph = stringParagraph.slice(firstIndexOfPo, 126);
    return stringParagraph;
}

// console.log(cutPoTextUntilParagraph());

function arrayFromString() {
    stringParagraph = stringParagraph.split(" ");
    return stringParagraph;
}

// console.log(arrayFromString());


function checkIfEndWith() {
    let boolIf = stringParagraph.endsWith("ages. ");
    return boolIf;
}

// console.log(checkIfEndWith());

function addString() {
    stringParagraph = stringParagraph.concat("is one of my favorite movies!");
    return stringParagraph;
}

// console.log(addString());