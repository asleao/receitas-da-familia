angular.module("receitasFamilia",["ngMessages","ngRoute"]);
angular.module("receitasFamilia").run(function($http){
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';    
});
