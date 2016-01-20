angular.module("receitasFamilia").controller("usuarioCtrl", function($scope,$http){
        $scope.usuarios = [];
        
        $scope.cadastrarUsuario = function(usuario){
            $scope.usuarios.push(angular.copy(usuario));
            delete $scope.usuario;
            $scope.formCadastro.$setPristine();
        };   
});