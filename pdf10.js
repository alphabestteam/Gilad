const spongBobMap = new Map([['main character', 'spongebob'], ['best friend', 'patrick'], ['pet', 'gary'], ['word buddy', 'squidward'], ['manager', 'Mr. Krubs'], ['teacher', 'Mrs. Puff'], ['location', 'bikini bottom']]);

console.log(spongBobMap);

const keysArray = Array.from(spongBobMap.keys());
console.log(keysArray);

console.log(spongBobMap.get('location'));

console.log(spongBobMap.size);

spongBobMap.delete('location');

console.log(spongBobMap.size);

console.log(spongBobMap);

console.log(spongBobMap.has('location'));

