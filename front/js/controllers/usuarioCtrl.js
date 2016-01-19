angular.module("receitasFamilia").controller("usuarioCtrl", function($scope,$http){
    $scope.usuarios = [];

    var carregarCategorias = function(){
        $http.get("http://localhost:8000/app/categoria/?format=json").success(function(data){
            $scope.categorias =data;
        });
    }; 

    carregarCategorias();      
});