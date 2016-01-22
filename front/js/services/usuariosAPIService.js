angular.module("receitasFamilia").service("usuarioAPI",function($http, config){   
    this.postCadastrarUsuario = function(usuario){
        return $http.post(config.baseUrl +"/users/?format=json",usuario);
    };         
});