const mongoose = require("mongoose");

const RecipeSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        default: "No description given"
    }
});

module.exports = mongoose.model("Recipe", RecipeSchema);