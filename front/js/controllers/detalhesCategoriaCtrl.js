angular.module("receitasFamilia").controller("detalhesCategoriaCtrl", function($scope,$routeParams,categoria,receitasAPI){
    $scope.categoria = categoria.data;       
     $scope.receitas = receitasAPI.getReceitas();        
});