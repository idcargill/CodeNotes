/* Server

express
cors
dotenv



root
  -frontend
  -backend



*/

//Boiler Plate
"use-strict";

const express = require("express");
const cors = require("cors");
require("dotenv").config; // call in

const app = express();
app.use(cors()); // activate cors
const PORT = process.env.PORT || 3001;

const person = [
  {
    name: "Frank",
    job: "Broom pusher",
    salary: "$100,000",
  },
  {
    name: "Charlie",
    job: "Chappin",
    salary: "$10",
  },
];

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});

// Setting Routes
app.get("/", (req, res) => {
  console.log(Object.keys(req.headers));
  res.send("HELLO From the serer");
});

app.get("/allData", getAllData);

function getAllData(req, res) {
  const allData = person.map((person) => {
    return person.name;
  });
  let reqName = req.query.name;
  console.log(reqName);

  const resName = person.filter((i) => i.name === reqName);

  res.status("200").send(resName);
}

app.get("*", (req, res) => {
  res.status("404").send("We ain't found shit");
});

// Boiler End
