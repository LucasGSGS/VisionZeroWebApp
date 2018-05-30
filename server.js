const express = require('express');
const router = require('express').Router();
const bodyParser = require('body-parser');
const app = express();
var fs = require('fs');

// const _ = require('loadash');
// const morgan = require('morgan');

// set the view engine to ejs
app.set('view engine', 'ejs');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
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

// app.post('/myaction', function(req, res) {
//   res.send('You sent the longitude "' + req.body.coordinate.lng + '".');
// });

app.post('/myaction', function (req, res) {
    // res.render('the_template', { name: req.body.name });
    let inputLng = req.body.coordinate.lng;
    let inputLat = req.body.coordinate.lat;
    console.log(inputLng);
    console.log(inputLat);
  // res.send('Longitude: ' + req.body.coordinate.lng + "\n" + 'Latitude: ' + req.body.coordinate.lat);

  var PythonShell = require('python-shell');

  var options = {
    mode: 'text',
    pythonPath: '/Users/shuogong/anaconda3/envs/osmnx/bin/python3',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: '/Users/shuogong/VisionZeroWebApp/',
    args: [inputLng, inputLat]
  };

  PythonShell.run('my_script.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    var obj;
    fs.readFile('output.json', 'utf8', function (err, data) {
      if (err) throw err;
      obj = JSON.parse(data);
      // console.log(JSON.stringify(obj));
      console.log('The nearest node latlng: ')
      console.log(JSON.stringify(obj));
      console.log(JSON.stringify(obj));
      console.log(obj['id']);
      // res.render('index', {id: obj['id']})
      res.redirect('/'); 


    });
    // var obj = JSON.parse(fs.readFileSync('output.json', 'utf8'));
    // console.log(JSON.stringify(obj));
  });

  // res.end();

  // console.log(obj);

});

// app.get("/myaction", function (req, res) {
//   res.status(200).send(req);
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
