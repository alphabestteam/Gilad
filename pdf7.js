const spongBobArray = ["Patrick", "Sendy", "Plankton", "Mr. Krub", "squeed"];
console.log(spongBobArray);
console.log(spongBobArray.length);
spongBobArray.push("Perl");
console.log(spongBobArray);
console.log(spongBobArray.length);
spongBobArray[0] = "Patrick Star";
console.log(spongBobArray);

/* 
 Values ​​of an array can be changed even though it was defined as "const", 
 because the data type of the array itself was defined as "const" and not the values ​​inside the array.
*/