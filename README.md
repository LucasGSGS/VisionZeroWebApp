# VisionZeroWebApp

This is a web map app based on python3(especially osmnx package), nodejs, expressjs, Angular to show paths switched between the shortest path and safest path.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Install Node.js https://nodejs.org/en/
* Install OSMNX(a python3 package mainly used in this web app) https://github.com/gboeing/osmnx
* Clone the repository: https://github.com/LucasGSGS/VisionZeroWebApp.git
* Change directory into the project: cd VisionZeroWebApp
* Get an MapBox api from https://www.mapbox.com/ and substitute the mapboxgl.accessToken at line70 in index.ejs with your MapBox api
* Find your python3 path where you can run osmnx. If you did create an enviroment for osmnx, you can first open Terminal and run command "source activate osmnx" to change your current enviroment to osmnx then you can find your own python3 path by command "which python3". If you didn't create and extra enviroment for osmnx, which means you can straightly run osmnx in python3. You can get your path by "which python3". Then you can substitute all the "pythonPath" to the path you get. Then you also need to substitute all the "scriptPath" to the root path of VisionZeroWebApp in your own computer. And don't forget to change output.json path to your own root path in my_script.py.

## Run web app locally
* **npm install**
* **npm start**
* Your app should now be running on localhost:4000



## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Node.js](https://nodejs.org/en/) - The web backend framework used
* [Angular](https://angular.io/) - The web frontend framework used
* [OSMNX](https://github.com/gboeing/osmnx) - The mainly used python3 package

## Contributing

Please read [CONTRIBUTING.md](https://github.com/LucasGSGS/VisionZeroWebApp/graphs/contributors?from=2018-05-20&to=2018-06-06&type=c) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* Shuo(Lucas) Gong

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
