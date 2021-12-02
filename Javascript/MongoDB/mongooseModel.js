const mongoose = require("mongoose");

// Mongoose Schema
// define type, required, default: optional

const mySchema = new mongoose.Schema({
  name: { type: String, require: true },
  description: { type: String },
  date: { type: Date, required: true, default: Date.now },
});

// mongoose.model('Name', Schema)

module.exports = mongoose.model("myModel", mySchema);
