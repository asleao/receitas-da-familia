angular.module("receitasFamilia").service("categoriasAPI",function($http){
  
   this.getCategorias = function(){
        return $http.get("http://localhost:8000/app/categoria/?format=json");
    };
});