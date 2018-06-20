var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/', {
      templateUrl: 'views/index.ejs',
    }).
    when('/shortest_path', {

    }).
    when('/safest_path', {

    });

}]);
