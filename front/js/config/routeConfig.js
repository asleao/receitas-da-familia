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
        $routeProvider.otherwise({redirectTo: "/home"});      
});