(function($) {
    var audios = [];
    var trackClicked = [];

    $(".slider").slider({
        slide: function(event, ui) {
            var width = ui.value;
            $(this).find(".dark").css("width", width+"%");
        },
        start: function(event, ui) {
            const parentId = $(this).closest(".music-player").attr("id");
            trackClicked[parentId] = true;
        },
        stop: function(event, ui) {
            const parentId = $(this).closest(".music-player").attr("id");
            const audio = getAudio($(this).closest(".music-player"));
            audio.skipTo(ui.value/100);
            trackClicked[parentId] = false;
        }
    });

    function isTrackClicked($player) {
        console.log(trackClicked);
        console.log($player.attr("id"));
        return trackClicked[$player.attr("id")];
    }

    function getAudio($player) {
        return audios[$player.data("audio")];
    }

    function getPlayerNav(audio) {
        const playerId = $(audio.element).data("player");
        return $("#"+playerId);
    }

    function pauseAll() {
        $(".playing").removeClass("playing");

        audios.forEach(function(item, i, arr) {
            item.pause();
        });
    }

    $(".track-item .left").click(function() {
        pauseAll();
        const $parent = $(this).closest(".track-item");
        $parent.addClass("playing");
        const audio = getAudio($parent);

        audio.load($parent.data("src"));
        audio.play();
    });

    audiojs.events.ready(function() {
        var a = audiojs.createAll({
            css: "",
            loadStarted: function() {
                const $nav = getPlayerNav(this);
                const m = Math.floor(this.duration / 60);
                const s = Math.floor(this.duration % 60);
                const html = (m+':'+(s<10?'0':'')+s);

                $nav.find(".time-track .end").html(html);
            },
            updatePlayhead: function(percent) {
                const $nav = getPlayerNav(this);

                if (!isTrackClicked($nav)) {
                    $nav.find(".slider").slider("value", percent * 100);
                    $nav.find(".slider .dark").css("width", percent * 100 + "%");
                }

                const p = this.duration * percent, m = Math.floor(p / 60), s = Math.floor(p % 60);
                const html = (m+':'+(s<10?'0':'')+s);
                $nav.find(".time-track .current").html(html);
            }
        });

        a.forEach(function(item, i, arr) {
            audios[$(item.element).attr("id")] = item;
        });
    });
})(jQuery);
