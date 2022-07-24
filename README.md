# Melting Pot

Share family recipes with the world.

By Kevin Yin, Helen Nguyen, and Varun Saini

Back-end is hosted [here](https://melting-pot-backend.herokuapp.com/).

## Running Application
To run the main application, navigate to the [frontend](/frontend) directory and run `python3 app.py`.

Dependencies for the front-end are located [here](/frontend/requirements.txt).


## Inspiration
We are _huge_ foodies but college has made us realize that nothing beats a homecooked meal. Family recipes are _top-tier_, which is why we wanted to create Melting Pot to share these delicious dishes. 

## What it does
Melting Pot is a social media platform for sharing and browsing family recipes. Users can share memories or discover new recipes and make new memories! _Our goal is to connect the world through food._

## How we built it
We first started with our back-end by setting up a database on MongoDB and connecting it to a Node.js/Express.js application that we made to act as an API. After deploying our back-end application to Heroku, we started wireframing and designing our UI. Once enough of the pieces were in place, we began connecting them together. We primarily used Flask to connect the back-end work to the front-end interfaces. 

## Challenges we ran into
- Uploading images to MongoDB (had to break down into bytes)
- Formatting HTML to work with Jinja templating
- Creating functions in Flask to communicate with the Node.js API

## Accomplishments that we're proud of
- During our brainstorming phase, we classified each idea as easy, medium, and hard, and in the end, we chose the most difficult hack to tackle. 
- Image uploading
- Front-end UI design
- Efficiency of website

## What we learned
We all learned a lot while creating this project, both as a team and as individuals. 
- Creating a database in MongoDB
- Building a back-end application using Javascript frameworks
- Writing code in HTML and CSS
- Using Flask to connect our back-end to our front-end

## What's next for Melting Pot
We hope to continue developing Melting Pot so that it can ultimately be hosted online for the foreseeable future and to continue to add more sophisticated features.
