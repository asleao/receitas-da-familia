angular.module("receitasFamilia").service("categoriasAPI",function($http, config){
  
   this.getCategorias = function(){
        return $http.get(config.baseUrl + "/categoria/?format=json");
    };
});