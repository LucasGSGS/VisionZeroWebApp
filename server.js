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
 res.render('index', {id: 'id placeholder', coordinates: '[]'
 // '[[-73.9947223, 40.7164964], [-73.9944558, 40.7169745], [-73.9954317, 40.7173076], [-73.9948124, 40.7184578], [-73.9943905, 40.7194567], [-73.9941321, 40.7200948], [-73.9939823, 40.7203048], [-73.9937341, 40.7209205], [-73.9934649, 40.7216124], [-73.9932043, 40.7223416], [-73.9930317, 40.7228017], [-73.9925624, 40.7240528], [-73.99251, 40.724192], [-73.9922645, 40.7248794], [-73.9921428, 40.7252143], [-73.9919974, 40.7256194], [-73.9917229, 40.7263629], [-73.9918561, 40.726419], [-73.99364, 40.727289], [-73.993147, 40.727867], [-73.9914198, 40.7298614]]'
  });
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
    // let inputLng = req.body.coordinate.lng;
    // let inputLat = req.body.coordinate.lat;
    // console.log(inputLng);
    // console.log(inputLat);
    let inputlatlng = req.body.origin
    console.log(inputlatlng)
  // res.send('Longitude: ' + req.body.coordinate.lng + "\n" + 'Latitude: ' + req.body.coordinate.lat);

  var PythonShell = require('python-shell');

  var options = {
    mode: 'text',
    pythonPath: '/Users/shuogong/anaconda3/envs/osmnx/bin/python3',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: '/Users/shuogong/VisionZeroWebApp/',
    args: [inputlatlng]
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
      res.render('index', {id: obj['id'], coordinates:
      '[[-73.9947223, 40.7164964], [-73.9944558, 40.7169745], [-73.9954317, 40.7173076], [-73.9948124, 40.7184578], [-73.9943905, 40.7194567], [-73.9941321, 40.7200948], [-73.9939823, 40.7203048], [-73.9937341, 40.7209205], [-73.9934649, 40.7216124], [-73.9932043, 40.7223416], [-73.9930317, 40.7228017], [-73.9925624, 40.7240528], [-73.99251, 40.724192], [-73.9922645, 40.7248794], [-73.9921428, 40.7252143], [-73.9919974, 40.7256194], [-73.9917229, 40.7263629], [-73.9918561, 40.726419], [-73.99364, 40.727289], [-73.993147, 40.727867], [-73.9914198, 40.7298614]]'})


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
