angular.module("receitasFamilia").controller("categoriaCtrl", function($scope,categoriasAPI){
    $scope.categorias = [];

 	var carregarCategorias = function(){
 		categoriasAPI.getCategorias().success(function(data){
 			$scope.categorias =data;
 		});
 	}; 

 	carregarCategorias();      
});