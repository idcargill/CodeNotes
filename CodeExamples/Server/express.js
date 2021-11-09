"use-strict";
const express = require("express");
const app = express.app();
const cors = require("cors");
require("dotenv").config(); // config is a function

const app = express();

app.use(cors()); // activate cors

const PORT = process.env.PORT || 3001; // env port or local default

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});

// Setting Routes
app.get("/", (req, res) => {
  console.log(Object.keys(req.headers));
  res.send("HELLO From the serer");
});

app.use("/someRoute", someRouter);

app.get("/api", apiHandlerFunction);

app.get("*", (req, res) => {
  res.send(404).send("Unknown address");
});

// Router
// someRouter.js

const router = express.Router();

app.get("/", (req, res) => {});
app.post("/", (req, res) => {});
app.patch("/:id", (req, res) => {});
app.delete("/:id", (req, res) => {});
module.exports = router;
