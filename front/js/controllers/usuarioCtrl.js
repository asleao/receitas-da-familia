angular.module("receitasFamilia").controller("usuarioCtrl", function($scope, usuarioAPI,$location){
        $scope.usuarios = [];
        
        $scope.cadastrarUsuario = function(usuario){            
            usuarioAPI.postUsuario(usuario).success(function(data){
               delete $scope.usuario;
                $scope.formCadastro.$setPristine();
                $location.path("/home");
            }); 
        };   
});