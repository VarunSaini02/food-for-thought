const mongoose = require("mongoose");

const IngredientSchema = new mongoose.Schema({
    name: String,
    amount: Number,
    unit: String,
});

const RecipeSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    ingredients: [IngredientSchema],
    servingSize: {
        type: String,
        required: true,
    },
    steps: [{
        type: String,
        required: true,
    }]
});

const CommentSchema = new mongoose.Schema({
    user: {
        type: String,
        required: true,
    },
    text: {
        type: String,
        required: true,
    }
});

const PostSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    name: {
        type: String,
        default: "Anonymous"
    },
    date: {
        type: Date,
        default: Date.now,
    },
    caption: {
        type: String,
        default: "",
    },
    recipe: {
        type: RecipeSchema,
        required: true,
    },
    likes: {
        type: Number,
        default: 0,
    },
    comments: [CommentSchema],
    image: String,
});

module.exports = mongoose.model("Post", PostSchema);