var current_code = "ru";

(function($) {

    function update_actives(plus) {
        $(".languages-widget li.empty").removeClass("empty");
        $(".languages-widget li").each(function() {
            var a = $(this).children("a");
            var code = $(a).attr("lang");
            var counter = 0;

            $(".flag").each(function() {
                if ($(this).hasClass("flag-"+code)) {
                    counter++;
                }
            });

            if (counter <= 1) { // 1 - empty field
                $(this).addClass("empty");
            } else

            if (plus && code === current_code && counter <= 2)
                $(this).addClass("empty");
        });
    }

    function update_languages($row, single) {
        $(".js-languages-formset .inline-language-row .vTextField").each(function() {
            var parent = $(this).closest(".inline-language-row");
            if ($(parent).hasClass("has_original") || $(this).val().trim() !== "")
                return;

            $(parent).find(".flag").attr("class", "flag flag-"+current_code);
        });

        $(".js-languages-formset .inline-language-row textarea").each(function() {
            var parent = $(this).closest(".inline-language-row");
            if ($(parent).hasClass("has_original") || $(this).val().trim() !== "")
                return;

            $(parent).find(".flag").attr("class", "flag flag-"+current_code);
        });

        var counter = 0;
        $(".flag").each(function() {
            var parent = $(this).closest(".inline-language-row");
            if ($(parent).hasClass("empty-form"))
                return;

            if ($(this).hasClass("flag-"+current_code)) {
                $(this).closest(".field-language").find("input").val(current_code);
                $(parent).show();
                counter++;
                return;
            }

            $(parent).hide();
        });

        if (counter > 2 && single) // TODO: Why 2?
            $($row).remove();

        console.log(counter);
    }

    $(document).on('formset:added', function(event, $row, formsetName) {
        var parent = $($row).closest("fieldset");
        if ($(parent).length <= 0) parent = $($row).closest(".inline-group");
        if (!$(parent).hasClass("js-languages-formset"))
            return;

        update_languages($row, $(parent).hasClass("js-languages-single"), true);
        update_actives(false);
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        update_actives(true);
    });

    $(document).ready(function() {
        update_languages();
        update_actives(false);

        $(".languages-widget a").click(function(e) {
            $(".languages-widget .active").removeClass("active");
            $(this).parent("li").addClass("active");
            current_code = $(this).attr("lang");
            update_languages();
            e.preventDefault();
        });
    });

})(django.jQuery);
