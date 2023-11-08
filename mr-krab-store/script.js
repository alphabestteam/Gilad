
/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/
// let promise1 = new Promise(function(myResolve, myReject){
//   setTimeout(function() { myResolve()})
//   fetch("https://jsonplaceholder.typicode.com/posts/1")
//     .then((response) => response.json())
//     .then((json) => console.log(json));
// });

async function fetchLatestOrderJSON() {
  const response = await fetch('http://localhost:8000/latest-order');
  const order = await response.json();
  return order;
}

fetchLatestOrderJSON().then(order => {
  document.getElementById("order-form").innerHTML = order; // fetched order
});