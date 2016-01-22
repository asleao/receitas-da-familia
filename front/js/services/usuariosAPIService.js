angular.module("receitasFamilia").service("usuarioAPI",function($http, config){   
    this.postUsuario = function(usuario){
        return $http.post(config.baseUrl +"/users/?format=json",usuario);
    };         
});