# VisionZeroWebApp

This is a web map app based on python3(especially osmnx package), nodejs, expressjs, Angular to show paths switched between the shortest path and safest path.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Install Node.js https://nodejs.org/en/
* Install OSMNX(a python3 package mainly used in this web app) https://github.com/gboeing/osmnx
* Clone the repository: https://github.com/LucasGSGS/VisionZeroWebApp.git
* Change directory into the project: cd VisionZeroWebApp
* Get an MapBox api from https://www.mapbox.com/ and substitute the mapboxgl.accessToken in index.ejs with your MapBox api

## Run web app locally
* First go to Python_Backend and run pyserver then open another Terminal window run the following
* **npm install**
* **npm start**
* Your app should now be running on localhost:4000 now



## Deployment

This app is deployed at http://ec2-18-205-198-227.compute-1.amazonaws.com/

## Built With

* [Node.js](https://nodejs.org/en/) - The web backend framework used
* [Python](https://docs.python.org/2/library/simplehttpserver.html) - Another server run before nodejs server, which keeps running OSMNX
* [Angular](https://angular.io/) - The web frontend framework used
* [OSMNX](https://github.com/gboeing/osmnx) - The mainly used python3 package

## Contributing

Please read [CONTRIBUTING.md](https://github.com/LucasGSGS/VisionZeroWebApp/graphs/contributors?from=2018-05-20&to=2018-06-06&type=c) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* Shuo(Lucas) Gong
* Ziwei Liu

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

Python_Backend:
* python pyserver.py runs backend API
* nodeget.js tests pyserver.
