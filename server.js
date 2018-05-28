const express = require('express');
const router = require('express').Router();
// const bodyParser = require('body-parser');
const app = express();
// const _ = require('loadash');
// const morgan = require('morgan');

// set the view engine to ejs
app.set('view engine', 'ejs');

// app.use(express.bodyParser());

// make express look in the public directory for assets (css/js/img)
app.use(express.static(__dirname + '/public'));

// set the port of our application
// process.env.PORT lets the port be set by Heroku
app.set('port', (process.env.PORT || 4000));

// set the home page route
app.get("/", function (req, res) {
 // res.send("Hey, I am responding to your request!");
 // ejs render automatically looks in the views folder
 res.render('index');
});

// app.post('/', function(request, response){
//     console.log(request.body.coordinate.lng);
//     console.log(request.body.coordinate.lat);
// });


//Start Server
app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});

function ignoreFavicon(req, res, next) {
  if (req.originalUrl === '/favicon.ico') {
    res.status(204).json({nope: true});
  } else {
    next();
  }
}

app.use(ignoreFavicon);
