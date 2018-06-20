/*
API code for Vision Zero
Richard Sowers <r-sowers@illinois.edu>
Copyright 2018 University of Illinois Board of Trustees. All Rights Reserved. Licensed under the MIT license

use: node nodeget

*/
request=require("request");

url="http://localhost:8081";
//query_params={origin:4163883691,destination:42435675,alpha:0.123};
query_params={origin:"-73.99448168636604,40.716945135773784",destination:"-73.98125094767447,40.73603263690694",alpha:0.8};

//console.log("url: "+url)
request({"url":url,qs:query_params}, function(err, res)
{
  if (err) {
  	console.log(err);
  	return
  }
  data=JSON.parse(res.body);
  console.log("data: "+JSON.stringify(data));
  console.log("origin: "+data.origin);
  console.log("destination: "+data.destination);
  console.log("cheapest path: "+data.cheapest_path);
  console.log("quickest path: "+data.quickest_path);
  return;
});
