$(document).ready(function() {
    $("#greeter__welcome_button").click(function() {
        $("#greeter__welcome_button").animate({ opacity: 0 }, 200);
        $("#greeter").animate({ height: 0 }, 1000, function () {
            setTimeout(function() {
                window.location.href = "/music/";
            }, 500);
            $(this).remove();
        });
    });
});
