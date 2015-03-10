$(document).ready(function () {
    girder.apiRoot = 'http://localhost:8000/api/v1';
    girder.router.enabled(false);

    $('#login').click(function () {
        var loginView = new girder.views.LoginView({
            el: this.$('#dialog-container'),
        });
        loginView.render();
    });

    $('#register').click(function () {
        var registerView = new girder.views.RegisterView({
            el: this.$('#dialog-container')
        });
        registerView.render();
    });

    $('#logout').click(function () {
        girder.restRequest({
            path: 'user/authentication',
            type: 'DELETE'
        }).done(function () {
            girder.currentUser = null;
            girder.events.trigger('g:login');
        });
    });

    girder.events.on('g:login', function () {
        if (girder.currentUser) {
            $("#login").addClass("hidden");
            $("#register").addClass("hidden");
            $("#name").removeClass("hidden");
            $("#logout").removeClass("hidden");
            $("#name").text("Logged in as " + girder.currentUser.get('firstName') + " " +
                            girder.currentUser.get('lastName'));

            // Do anything else you would like to do on login.
        } else {
            $("#login").removeClass("hidden");
            $("#register").removeClass("hidden");
            $("#name").addClass("hidden");
            $("#logout").addClass("hidden");

            // Do anything else you would like to do on logout.
        }
    });

    // Check who is logged in initially.
    girder.restRequest({
        path: 'user/authentication',
        error: null
    }).done(function () {
        girder.events.trigger('g:login');
    });

});