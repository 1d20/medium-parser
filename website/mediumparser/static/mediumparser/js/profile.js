$(document).ready(function() {
    var profileDetailUrl = urls.profileDetailUrl + $("div#profile-id").text() + '/';

    function retrieveProfileInformation() {
        $.ajax({
            type: 'GET',
            url: profileDetailUrl
        }).done(function(response) {
            var fields = ['username', 'email', 'confirm_email', 'password'];
            fields.forEach(function(element) {
                $(`div#profile-${element}`).html(response[element]);
                $(`input#profile-${element}`).val(response[element]);
            });
        })
        .fail(function(response) {
            alert('Something wrong(Retrieve Profile Information)!');
        });
    }

    function updateProfile() {
        console.log($("form#updateProfileForm").serialize())
        $.ajax({
            type: 'PUT',
            url: profileDetailUrl,
            data: $("form#updateProfileForm").serialize(), 
        }).done(function(response) {
            $('#updateProfileModal').modal('toggle');
            retrieveProfileInformation();
        })
        .fail(function(response) {
            alert(response.responseText)
        });
    }

    retrieveProfileInformation();
    $("#submitProfileForm").click(updateProfile);
});
