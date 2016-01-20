angular.module("receitasFamilia").service("receitasAPI",function($http, config){  
   this.getReceitas = function(){
        return $http.get(config.baseUrl +"/receita/?format=json");
    };
});