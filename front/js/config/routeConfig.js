angular.module("receitasFamilia").config(function($routeProvider){
        $routeProvider.when("/home",{
            templateUrl:"view/home.html" ,
            controller: "receitaCtrl" ,
            resolve:{
                    receitas: function(receitasAPI){
                            return receitasAPI.getReceitas();
                    }
            }             
        });
         $routeProvider.when("/cadastro",{
            templateUrl:"view/cadastro.html" ,
            controller: "usuarioCtrl"                        
        });

         $routeProvider.when("/login",{
            templateUrl:"view/login.html" ,
            controller: "usuarioCtrl"                        
        });

         $routeProvider.when("/detalhesCategoria/:id",{
            templateUrl:"view/detalhesCategoria.html" ,
            controller: "detalhesCategoriaCtrl",
            resolve:{
                    categoria: function(categoriasAPI,$route){
                            return categoriasAPI.getCategoria($route.current.params.id);
                    }
            }               
        });

        $routeProvider.otherwise({redirectTo: "/home"});      
});