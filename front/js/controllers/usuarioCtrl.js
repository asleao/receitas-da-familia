angular.module("receitasFamilia").controller("usuarioCtrl", function($scope, usuarioAPI){
        $scope.usuarios = [];
        
        $scope.cadastrarUsuario = function(usuario){            
            usuarioAPI.postUsuario(usuario).success(function(data){
               delete $scope.usuario;
                $scope.formCadastro.$setPristine();
            }); 
        };   
});