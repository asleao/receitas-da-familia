angular.module("receitasFamilia").controller("receitaCtrl", function($scope,$http){
    $scope.receitas= [];

    var carregarReceitas = function(){
        $http.get("http://localhost:8000/app/receita/?format=json").success(function(data){
            $scope.receitas =data;            
        });
    }; 

    carregarReceitas();      
});