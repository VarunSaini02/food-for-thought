const router = require("express").Router();
const { getPosts, createPost, updatePost, deletePost } = require("./controllers/post");

router.get("/", (req, res) => {
    res.send("Pot melting...");
});

// router.get("/posts/:postID", getPost);
router.get("/posts", getPosts);
router.post("/posts", createPost);
router.put("/posts/:postID", updatePost);
router.delete("/posts/:postID", deletePost);

module.exports = router;