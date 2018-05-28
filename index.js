const express = require('express');
// const bodyParser = require('body-parser');
const app = express();
// const _ = require('loadash');
// const morgan = require('morgan');

app.set('port', (process.env.PORT || 4000));

//Start Server
app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});

// app.get("/", function (req, res) {
//  res.send("Hey, I am responding to your request!");
// });
