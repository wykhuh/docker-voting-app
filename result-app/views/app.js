var app = angular.module('javavspython', []);
var socket = io.connect({transports:['polling']});

app.controller('statsCtrl', function($scope,$http){

  $scope.votes = [];

  $scope.buttonPush = function() {
    $http({
  method: 'GET',
      url: '/postconfig'
    }).then(function successCallback(response) {
      console.log(response);
    }, function errorCallback(response) {
      console.log(response);
    });
  }

  var updateScores = function(){
    socket.on('scores', function (json) {
       data = JSON.parse(json);

       $scope.$apply(function() {
         $scope.votes = data;
      });
    });
  };

  var init = function(){
    document.body.style.opacity=1;
    updateScores();
  };
  socket.on('message',function(data){
    init();
  });
});
