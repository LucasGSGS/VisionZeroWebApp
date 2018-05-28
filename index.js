const express = require('express');
const router = require('express').Router();
// const bodyParser = require('body-parser');
const app = express();
// const _ = require('loadash');
// const morgan = require('morgan');

// set the port of our application
// process.env.PORT lets the port be set by Heroku
app.set('port', (process.env.PORT || 4000));

// set the home page route
app.get("/", function (req, res) {
 res.send("Hey, I am responding to your request!");
});

//Start Server
app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});
