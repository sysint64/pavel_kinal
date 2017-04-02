(function($) {
    var audios = [];
    var trackClicked = [];
    var shuffle = [];
    var repeat = [];
    var currentAudio = null;
    var $lastTrack = null;
    var $lastSrc = "";

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
        return trackClicked[$player.attr("id")];
    }

    function getAudio($player) {
        return audios[$player.data("audio")];
    }

    function setShuffle($player, value) {
        shuffle[$player.data("audio")] = value;
    }

    function setRepeat($player, value) {
        repeat[$player.data("audio")] = value;
    }

    function getPlayerNav(audio) {
        const playerId = $(audio.element).data("player");
        return $("#"+playerId);
    }

    function pauseAll() {
        $(".playing").removeClass("playing");

        if (currentAudio != null)
            currentAudio.pause();
    }

    $(".track-item .left").click(function() {
        const $toggleTrackButton = $(this).closest(".col").find(".toggle-track");
        const $parent = $(this).closest(".track-item");
        const audio = getAudio($parent);
        $lastTrack = $(this);
        $(".track-item.current").removeClass("current");
        $parent.addClass("current");

        if ($parent.hasClass("playing")) {
            pauseAll();
            return;
        }

        pauseAll();
        $toggleTrackButton.addClass("playing");
        $parent.addClass("playing");

        currentAudio = audio;

        if ($lastSrc != $parent.data("src")) {
            audio.load($parent.data("src"));
            $lastSrc = $parent.data("src");
        }

        audio.play();
    });

    $(".toggle-track").click(function() {
        const $parent = $(this).closest(".music-player");
        const audio = getAudio($parent);
        $(this).toggleClass("playing");
        // audio.playPause();
        $lastTrack.trigger("click");
    });

    $(".shuffle-queue").click(function() {
        $(this).toggleClass("active");
        const $parent = $(this).closest(".music-player");
        setShuffle($parent, $(this).hasClass("active"));
    });

    $(".loop-track").click(function() {
        $(this).toggleClass("active");
        const $parent = $(this).closest(".music-player");
        setRepeat($parent, $(this).hasClass("active"));
    });

    $(".next-track").click(function () {

    });

    $(".previous-track").click(function () {

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
            const audioId = $(item.element).attr("id");
            const albumId = $(item.element).data("album-id");
            const parentId = "player_album_" + albumId;

            console.log(audioId);
            console.log(parentId);
            item.load($("#"+parentId).data("src"));
            audios[audioId] = item;
            shuffle[audioId] = false;
            repeat[audioId] = false;
        });
    });
})(jQuery);
