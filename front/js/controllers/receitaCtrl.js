angular.module("receitasFamilia").controller("receitaCtrl", function($scope,receitasAPI){
    $scope.receitas= [];

    var carregarReceitas = function(){
        receitasAPI.getReceitas().success(function(data){
            $scope.receitas =data;            
        });
    }; 

    carregarReceitas();      
});