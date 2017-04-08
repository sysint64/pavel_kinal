(function($) {
    var $menu;
    var menuTargetOffset;

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

        $menu = $("ul.main_menu");
        updateMenuTargetOffset();
    });

    function pinMenuHandle() {
        const scrollTop = $(window).scrollTop();

        if (scrollTop >= menuTargetOffset) {
            $menu.css("top", scrollTop - menuTargetOffset);
        } else {
            $menu.css("top", 0);
        }
    }

    function updateMenuTargetOffset() {
        $menu.css("top", 0);
        menuTargetOffset = $menu.offset().top - 20;
        pinMenuHandle();
    }

    $(window).scroll(function() {
        pinMenuHandle();
    });

    $(window).resize(function() {
        updateMenuTargetOffset();
    });
})(jQuery);
