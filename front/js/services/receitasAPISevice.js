angular.module("receitasFamilia").service("receitasAPI",function($http){
  
   this.getReceitas = function(){
        return $http.get("http://localhost:8000/app/receita/?format=json");
    };
});