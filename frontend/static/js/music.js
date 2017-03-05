(function($) {
    $(document).ready(function () {
        $(".slider").slider({
            slide: function(event, ui) {
                var width = ui.value;
                $(this).find(".dark").css("width", width+"%");
            }
            // create: function(event, ui){
            //     $(this).slider('value', 5);
            //     $(this).find(".dark").css("width", "5%");
            // }
        });
    });
})(jQuery);
