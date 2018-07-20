const express = require('express')
const router = require('express').Router()
const bodyParser = require('body-parser')
const app = express()
const request=require('request')
var fs = require('fs')

app.set('view engine', 'ejs')

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
// make express look in the public directory for assets (css/js/img)
app.use(express.static(__dirname + '/public'))

// set the port of our application`
// process.env.PORT lets the port be set by Heroku
app.set('port', (process.env.PORT || 80))

// set the home page route
app.get('/', function (req, res) {
	// res.send("Hey, I am responding to your request!");
	// ejs render automatically looks in the views folder
	res.render('index', {center: '[-73.99326785714284, 40.72278695238094]', coordinates: '[]'})


})


app.post('/myaction', function (req, res) {
	var originlatlng = req.body.origin
	var destlatlng = req.body.destination
	var alpha = req.body.alpha

	const url='http://ec2-18-207-228-223.compute-1.amazonaws.com:8081'

	const query_params={origin:originlatlng,destination:destlatlng,alpha:alpha}
	request({"url":url,qs:query_params}, function(err) {
		if (err) throw err
		var obj
		fs.readFile('output.json', 'utf8', function (err, data) {
			if (err) throw err
			obj = JSON.parse(data)
			console.log('New center is ' + obj['center'])
			console.log('Safetest Path is ' + (JSON.stringify(obj['coordinates'])).replace(/\s/g,''))
			console.log('Alpha value is ' + (JSON.stringify(obj['alpha'])))
			res.render('index', {center: JSON.stringify(obj['center']), coordinates: (JSON.stringify(obj['coordinates'])).replace(/\s/g,'')})
		})
	})
})

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
