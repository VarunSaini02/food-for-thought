const express = require("express");
const bodyParser = require("body-parser");
const router = require("./router");
const cors = require("cors");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
dotenv.config();

const PORT = process.env.PORT || 8000;
const app = express();

app.listen(PORT, async () => {
  console.log(`Server running on port ${PORT}`);
});

mongoose
  .connect(process.env.MONGODB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.log(err);
  });

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(router);