angular.module("receitasFamilia").controller("CategoriaCtrl", function($scope,$http){
    $scope.categorias = [];

 	var carregarCategorias = function(){
 		$http.get("http://localhost:8000/app/categoria/?format=json").success(function(data){
 			console.log(data);
 		});
 	}; 

 	carregarCategorias();      
});