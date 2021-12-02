/*
Rest - Representational State Transfer
  GET   
  POST   
  PUT   
  DELETE


  AXIOS
  axios.get()

  axios.put()

  Asynchronous
    -async/await


  URL

  query string / routing

  Website: routes 
    ?(start of query)  
    key= 
    q=



    Environment Variable
    .env 
    ROOT

    React Global Variables
    REACT_APP_LOCATION_API_KEY = 
    
    to call:
      process.env.REACT_APP_LOCATION_API_KEY
*/

import axios from "axios";

async function getData() {
  let data = await axios.get("https://pokeapi.co/api/v2/pokemon/mewtwo");
  console.log(data.data);
  return data;
}

getData();
// axios
//   .get("https://pokeapi.co/api/v2/pokemon/mewtwo")
//   .then((i) => console.log(i));

// function sayHi() {
//   return new Promise((resolved) => {
//     setTimeout(() => {
//       resolved("hello");
//     }, 2000);
//   });
// }

// const doStuff = () => {
//   let p = sayHi();
//   return p;
// };
// doStuff().then((i) => console.log(i));
