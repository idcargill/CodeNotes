//Mongoose
// in server.js

const { application } = require("express");
const mongoose = require("mongoose");

// .env MONGO_CONNECTION=mongodb://localhost:27017/ghostSmashEquip

//==============================================================
// Create Collection
mongoose.connect("mongodb://localhost:27017/ghostSmashEquip", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Connection
const db = mongoose.connection;

// ON ERROR
db.on("error", console.error(error.bind(console, "connection error:")));

// ONCE connected
db.once("open", () => console.log("mongodb database connected")); //
//==============================================================

application.listen(PORT, stuff);

// Make Schema
const equipmentSchema = new mongoose.Schema({
  name: { type: String },
  description: { type: String },
  quantity: { type: Number },
  status: { type: String, uppercase: true, enum: ["WORKING", "REPAIR", "REPLACEMENT"] },
});

// Model: Apply schema to collection
const EquipModel = mongoose.model("ghostSmashEquip", equipmentSchema); //

const sampleEntry = new EquipModel({
  name: "Proton Pack",
  description: "Unlicensed Nuclear Accelerator",
  qty: 4,
  status: "WORKING",
});

// Save to mongodb
sampleEntry.save();

// Find
EquipModel.find((err, item) => {
  if (err) return console.error(err);
  console.log(item);
});

// Endpoint Route with query
app.get("/allequip", (req, res) => {
  EquipModel.find((err, item) => {
    if (err) return res.status(500).send(err);
    res.status(200).send(item);
  });
});

app.get("/clear", bombTheBase);

// Delete everything
async function bombTheBase() {
  try {
    await EquipModel.deleteMany({});
    res.status(200).send("cleared");
  } catch (e) {
    console.warn(e.message);
  }
}

// Seed the Database ====================================
function seed() {
  const seedArr = [
    {
      name: "Proton Pack",
      description: "Unlicensed Nuclear Accelerator",
      qty: 4,
      status: "WORKING",
    },
    {
      name: "Proton Pack",
      description: "Unlicensed Nuclear Accelerator",
      qty: 4,
      status: "WORKING",
    },
    {
      name: "Proton Pack",
      description: "Unlicensed Nuclear Accelerator",
      qty: 4,
      status: "WORKING",
    },
  ];

  seedArr.forEach((seed) => {
    let entry = new EquipModel(seed);
    entry.save();
  });
  res.status(200).send("Database Seeded");
}

// Seed the Database ====================================

// Filter returned Data
async function findEntry(req, res) {
  if (req.query.status) {
    let { status } = req.query;
    let filterQ = {};
    filterQ.status = status;
    const item = await EquipModel.find({ filterQ });
    res.status(200).send(item);
  } else {
    res.status(200).send([]);
  }
}
