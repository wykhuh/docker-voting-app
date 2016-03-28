var app = angular.module('javavspython', []);
var socket = io.connect({transports:['polling']});

app.controller('statsCtrl', function($scope,$http){

  $scope.votes = [1,2,3];

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
       console.log('update', data)
       $scope.votes = [5,6,7];



      //  var a = parseInt(data.a || 0);
      //  var b = parseInt(data.b || 0);

      //  animateStats(a, b);

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
