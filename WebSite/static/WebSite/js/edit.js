
$(document).ready(function() {

    initEditPage();
});

var gameSearchTimeout;

function initEditPage() {

    $("input#game").off("keydown").on("keydown", keydownInputGame);
}

/**
 * When user writes in the game input
 * @param {*} event 
 */
function keydownInputGame(event) {

    clearTimeout(gameSearchTimeout);
    
    gameSearchTimeout = setTimeout(function() {
        findGames();
    }, 1000);
}

/**
 * Request the server to show a list of games
 */
function findGames() {

    var data = {
        gameName: $("input#game").val()
    };

    $.ajax({
        type: 'GET',
        data: data,
        url: find_games
    }).done(function(data) {

        $(".sectionGameFinder").html(data);

        console.log(data)
    }).fail(function(data) {

        console.log('Erreur ajaxCall');
        console.log(data);
    });
}