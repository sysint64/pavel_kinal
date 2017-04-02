(function($) {
    var players = [];
    var currentPlayer = null;

    function Player(audio, $container) {
        this.audio = audio;
        this.repeat = false;
        this.isTrackClicked = false;
        this.lastSrc = "";
        this.defaultOrderedTrackList = [];  // Стандартный порядок треков
        this.trackList = [];  // Треки для воспроизведения
        this.currentTrackIndex = 0;

        this.$container = $container;
        this.$lastTrack = $container.find(".track-item").first();
        this.$toggleTrackButton = $container.find(".toggle-track");
        this._load(this.$lastTrack.data("src"));

        const player = this;

        $container.find(".slider").slider({
            slide: function(event, ui) {
                $(this).find(".dark").css("width", ui.value+"%");
            },
            start: function(event, ui) {
                player.isTrackClicked = true;
            },
            stop: function(event, ui) {
                player.isTrackClicked = false;
                player.audio.skipTo(ui.value / 100);
            }
        });

        var $track = this.$lastTrack;
        var index = 0;

        while ($track.length > 0) {
            $track.trackListIndex = index;
            ++index;

            this.trackList.push($track);
            this.defaultOrderedTrackList.push($track);
            $track = $track.next();
        }
    }

    Player.prototype._selectTrack = function($track) {
        for (var i = 0; i < this.trackList.length; ++i) {
            if ($track.data("index") == this.trackList[i].data("index")) {
                this.currentTrackIndex = i;
                break;
            }
        }

        this.$lastTrack.removeClass("current");
        this.$lastTrack.removeClass("playing");
        this.$lastTrack = $track;
        this.$lastTrack.addClass("current");
    };

    Player.prototype._shuffleTrackList = function() {
        for (var trackIndex = 0; trackIndex < this.trackList.length; ++trackIndex) {
            const randomIndex = Math.floor(Math.random() * this.trackList.length);

            // Меняем местами со случайным индексом
            const tmp = this.trackList[trackIndex];
            this.trackList[trackIndex] = this.trackList[randomIndex];
            this.trackList[randomIndex] = tmp;

            if (this.currentTrackIndex == trackIndex) {
                this.currentTrackIndex = randomIndex;
            } else if (this.currentTrackIndex == randomIndex) {
                this.currentTrackIndex = trackIndex;
            }
        }
    };

    Player.prototype._restoreTrackList = function() {
        this.currentTrackIndex = this.trackList[this.currentTrackIndex].data("index");
        this.trackList = Array.from(this.defaultOrderedTrackList);
    };

    // AudioJS Handles
    Player.prototype.handleLoadStarted = function() {
        const html = formatDuration(this.audio.duration);
        this.$container.find(".time-track .end").html(html);
    };

    Player.prototype.handleUpdate = function(percent) {
        const $container = this.$container;

        if (!this.isTrackClicked) {
            $container.find(".slider").slider("value", percent * 100);
            $container.find(".slider .dark").css("width", percent * 100 + "%");
        }

        const html = formatDuration(this.audio.duration * percent);
        $container.find(".time-track .current").html(html);
    };

    Player.prototype.handleTrackEnded = function() {
        if (this.repeat) {
            this.loopNext();
        } else {
            this.next();
        }
    };

    // Navigate
    Player.prototype.next = function() {
        this.pause();

        this.$lastTrack.removeClass("current");
        this.currentTrackIndex++;

        if (this.currentTrackIndex < this.trackList.length) {
            this.$lastTrack = this.trackList[this.currentTrackIndex];
            this.toggleLastPlay();
            return true;
        } else {
            this.currentTrackIndex = 0;
            this.$lastTrack = this.trackList[this.currentTrackIndex];
            return false;
        }
    };

    Player.prototype.prev = function() {
        this.pause();

        this.$lastTrack.removeClass("current");
        this.$lastTrack = this.$lastTrack.prev();

        if (this.$lastTrack.length != 0) {
            this.toggleLastPlay();
            return true;
        } else {
            this.$lastTrack = this.$container.find(".track-item").last();
            return false;
        }
    };

    Player.prototype.loopNext = function() {
        if (!this.next())
            this.toggleLastPlay();
    };

    Player.prototype.loopPrev = function() {
        if (!this.prev())
            this.toggleLastPlay();
    };

    // Manipulate
    Player.prototype._load = function(src) {
        if (this.lastSrc == src)
            return;

        this.lastSrc = src;
        this.audio.load(src);
    };

    Player.prototype.play = function($track) {
        if (currentPlayer != null && currentPlayer != this)
            currentPlayer.pause();

        currentPlayer = this;

        this._selectTrack($track);
        this._load($track.data("src"));
        this.audio.play();

        this.$toggleTrackButton.addClass("playing");
        $track.addClass("playing");
    };

    Player.prototype.togglePlay = function($track) {
        if ($track.hasClass("playing")) {
            $track.removeClass("playing");
            this.pause();
        } else {
            $track.addClass("playing");
            this.play($track);
        }
    };

    Player.prototype.toggleLastPlay = function() {
        this.togglePlay(this.$lastTrack)
    };

    Player.prototype.pause = function() {
        this.$toggleTrackButton.removeClass("playing");
        this.$lastTrack.removeClass("playing");
        this.audio.pause();
    };

    Player.prototype.setShuffle = function(value) {
        if (value) {
            this._shuffleTrackList();
        } else {
            this._restoreTrackList();
        }
    };

    Player.prototype.setRepeat = function(value) {
        this.repeat = value;
    };

// Helpers------------------------------------------------------------------------------------------

    function getPlayerByHolder($holder) {
        return players[$holder.data("audio")];
    }

    function getPlayerByAudio(audio) {
        return players[$(audio.element).attr("id")];
    }

    // Преобразование секунд к виду 0:00, т.е. минута:секунды
    function formatDuration(duration) {
        const m = Math.floor(duration / 60);
        const s = Math.floor(duration % 60);
        return (m + ':' + ( s < 10 ? '0' : '') + s);
    }

    function getPlayerByChildOfHolder($child) {
        return getPlayerByHolder($child.closest(".music-player"));
    }

// Events ------------------------------------------------------------------------------------------

    $(".track-item .left").click(function() {
        const $track = $(this).closest(".track-item");
        const player = getPlayerByHolder($track);
        player.togglePlay($track);
    });

    $(".toggle-track").click(function() {
        const player = getPlayerByChildOfHolder($(this));
        player.toggleLastPlay();
    });

    $(".shuffle-queue").click(function() {
        $(this).toggleClass("active");
        const player = getPlayerByChildOfHolder($(this));
        player.setShuffle($(this).hasClass("active"));
    });

    $(".loop-track").click(function() {
        $(this).toggleClass("active");
        const player = getPlayerByChildOfHolder($(this));
        player.setRepeat($(this).hasClass("active"));
    });

    $(".next-track").click(function () {
        const player = getPlayerByChildOfHolder($(this));
        player.loopNext();
    });

    $(".previous-track").click(function () {
        const player = getPlayerByChildOfHolder($(this));
        player.loopPrev();
    });

// AudioJS -----------------------------------------------------------------------------------------

    audiojs.events.ready(function() {
        var a = audiojs.createAll({
            css: "",

            loadStarted: function() {
                const player = getPlayerByAudio(this);
                player.handleLoadStarted();
            },

            updatePlayhead: function(percent) {
                const player = getPlayerByAudio(this);
                player.handleUpdate(percent);
            },

            trackEnded: function() {
                const player = getPlayerByAudio(this);
                player.handleTrackEnded();
            }
        });

        a.forEach(function(item, i, arr) {
            const audioId = $(item.element).attr("id");
            const $container = $(item.element).closest(".player-container");

            players[audioId] = new Player(item, $container);
        });
    });
})(jQuery);
