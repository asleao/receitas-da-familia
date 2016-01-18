angular.module("receitasFamilia").controller("categoriaCtrl", function($scope,$http){
    $scope.categorias = [];

 	var carregarCategorias = function(){
 		$http.get("http://localhost:8000/app/categoria/?format=json").success(function(data){
 			$scope.categorias =data;
 		});
 	}; 

 	carregarCategorias();      
});