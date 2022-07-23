const Recipe = require("../model/recipe");

const getRecipes = (req, res) => {
    Recipe.find((err, recipes) => {
        if (err) {
            res.send(err);
        }
        res.json(recipes);
    });
};

const createRecipe = (req, res) => {
    const recipe = new Recipe({
        name: req.body.name,
        description: req.body.description
    });

    recipe.save((err, recipe) => {
        if (err) {
            res.send(err);
        }
        res.json(recipe);
    });
};

const updateRecipe = (req, res) => {
    Recipe.findOneAndUpdate(
        { _id: req.params.recipeID },
        {
            $set: {
                name: req.body.title,
                description: req.body.description
            },
        },
        { new: true },
        (err, Recipe) => {
            if (err) {
                res.send(err);
            } else res.json(Recipe);
        }
    );
};

const deleteRecipe = (req, res) => {
    Recipe.deleteOne({ _id: req.params.todoID })
    .then(() => res.json({ message: "Recipe Deleted" }))
    .catch((err) => res.send(err));
};

module.exports = {
    getRecipes,
    createRecipe,
    updateRecipe,
    deleteRecipe
};