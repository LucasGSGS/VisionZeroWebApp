const express = require('express');
// const bodyParser = require('body-parser');
const app = express();
// const _ = require('loadash');
// const morgan = require('morgan');

app.listen(3000, function() {
  console.log("App listening on port 3000!");
});

app.get("/", function (req, res) {
 res.send("Hey, I am responding to your request!");
});
