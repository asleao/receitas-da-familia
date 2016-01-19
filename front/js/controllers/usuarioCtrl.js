angular.module("receitasFamilia").controller("usuarioCtrl", function($scope,$http){
    $scope.usuarios = [];

    var carregarUsuarios = function(){
        $http.get("http://localhost:8000/app/users/?format=json").success(function(data){
            $scope.usuarios =data;
        });
    }; 

    carregarUsuarios();      
});