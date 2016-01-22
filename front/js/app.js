angular.module("receitasFamilia",["ngMessages","ngRoute"]);
angular.module("receitasFamilia").run(function($http){
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
});
