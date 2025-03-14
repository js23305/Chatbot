function testJS() {
    alert("Hello");
}

function sendMessageToServer() {

    console.log("Hello")

    var formData = new FormData()
    formData.append('genre', $('#inputGenre').val(''))

    $.ajax(
        {
            url: "/chatbotui/send_film_to_user/",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {

                //window.location.replace("/experiment/?experiment="+response.uid)

                // $('#loading-animation-container').addClass("d-none")
                // $('#form').removeClass("d-none")

                // worstCaseGameStates = response['finalResult']['worst_case']['game_state:']

                // worstCaseGameStates.forEach(appendGameStatesToResultsView)
            },
            error: function(error) {

                console.log(error)
            }
        }
    )
}