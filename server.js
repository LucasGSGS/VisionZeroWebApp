const express = require('express')
const router = require('express').Router()
const bodyParser = require('body-parser')
const app = express()
var fs = require('fs')

// const _ = require('loadash');
// const morgan = require('morgan');

// set the view engine to ejs
app.set('view engine', 'ejs')

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
// make express look in the public directory for assets (css/js/img)
app.use(express.static(__dirname + '/public'))

// set the port of our application`
// process.env.PORT lets the port be set by Heroku
app.set('port', (process.env.PORT || 4000))

// set the home page route
app.get('/', function (req, res) {
	// res.send("Hey, I am responding to your request!");
	// ejs render automatically looks in the views folder
	res.render('index', {center: '[-73.99326785714284, 40.72278695238094]', coordinates: '[]'})

	//prerun python file to get Manhattan_Graph
	var PythonShell = require('python-shell')
	var options = {
		mode: 'text',
		pythonPath: '/Users/shuogong/anaconda3/envs/osmnx/bin/python3',
		pythonOptions: ['-u'], // get print results in real-time
		scriptPath: '/Users/shuogong/VisionZeroWebApp',
		args: []
	}
	PythonShell.run('prerun.py', options, function (err) {
		if (err) throw err
	})

})

// app.post('/', function(request, response){
//     console.log(request.body.coordinate.lng);
//     console.log(request.body.coordinate.lat);
// });

// app.post('/myaction', function(req, res) {
//   res.send('You sent the longitude "' + req.body.coordinate.lng + '".');
// });

app.post('/myaction', function (req, res) {
	let originlatlng = req.body.origin
	let destlatlng = req.body.destination
	let alpha = req.body.alpha

	var PythonShell = require('python-shell')
	var options = {
		mode: 'text',
		pythonPath: '/Users/shuogong/anaconda3/envs/osmnx/bin/python3',
		pythonOptions: ['-u'], // get print results in real-time
		scriptPath: '/Users/shuogong/VisionZeroWebApp',
		args: [originlatlng, destlatlng, alpha]
	}

	PythonShell.run('my_script.py', options, function (err, results) {
		if (err) throw err
		// console.log('results: %j', results)
		// results is an array consisting of messages collected during execution
		var obj
		fs.readFile('output.json', 'utf8', function (err, data) {
			if (err) throw err
			obj = JSON.parse(data)
			// console.log(JSON.stringify(obj));
			// console.log('The nearest node latlng: ')
			// console.log(JSON.stringify(obj));
			console.log('New center is ' + obj['center'])
			console.log('Safetest Path is ' + (JSON.stringify(obj['coordinates'])).replace(/\s/g,''))
			console.log('Alpha value is ' + (JSON.stringify(obj['alpha'])))
			res.render('index', {center: JSON.stringify(obj['center']), coordinates: (JSON.stringify(obj['coordinates'])).replace(/\s/g,'')})
			// res.render('index', {center: "obj['center']", coordinates: "obj['path_coordinates']"});
		})
	})
})

// app.get("/myaction", function (req, res) {
//   res.status(200).send(req);
// });

//Start Server
app.listen(app.get('port'), function() {
	console.log('Node app is running on port', app.get('port'))
})

function ignoreFavicon(req, res, next) {
	if (req.originalUrl === '/favicon.ico') {
		res.status(204).json({nope: true})
	} else {
		next()
	}
}

app.use(ignoreFavicon)
