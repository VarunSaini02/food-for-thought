const Post = require("../model/post");

const getPost = (req, res) => {
    Post.findOne({ _id: req.params.postID },
        (err, post) => {
            if (err) {
                res.send(err);
            }
            res.json(post);
        });
};

const getPostLikes = (req, res) => {
    Post.findOne({ _id: req.params.postID },
        (err, post) => {
            if (err) {
                res.send(err);
            }
            res.json(post.likes);
        });
};

const getPosts = (req, res) => {
    Post.find((err, posts) => {
        if (err) {
            res.send(err);
        }
        res.json(posts);
    });
};

const createPost = (req, res) => {
    const post = new Post({
        title: req.body.title,
        date: req.body.date,
        caption: req.body.caption,
        recipe: req.body.recipe,
        likes: req.body.likes,
        comments: req.body.comments
    });

    post.save((err, post) => {
        if (err) {
            res.send(err);
        }
        res.json(post);
    });
};

const updatePost = (req, res) => {
    Post.findOneAndUpdate(
        { _id: req.params.postID },
        {
            $set: {
                title: req.body.title,
                date: req.body.date,
                caption: req.body.caption,
                recipe: req.body.recipe,
                likes: req.body.likes,
                comments: req.body.comments
            },
        },
        { new: true },
        (err, post) => {
            if (err) {
                res.send(err);
            } else res.json(post);
        }
    );
};

const deletePost = (req, res) => {
    Post.deleteOne({ _id: req.params.postID })
        .then(() => res.json({ message: "Post Deleted" }))
        .catch((err) => res.send(err));
};

module.exports = {
    getPost,
    getPostLikes,
    getPosts,
    createPost,
    updatePost,
    deletePost
};