$(document).ready(function() {
    var articleDetailUrl = urls.articleDetailUrl + $("div#article-id").text() + '/';

    function retrieveArticleInformation() {
        $.ajax({
            type: 'GET',
            url: articleDetailUrl
        }).done(function(response) {
            var fields = ['title', 'url', 'text'];
            fields.forEach(function(element) {
                $(`div#article-${element}`).html(response[element]);
                $(`input#article-${element}`).val(response[element]);
            });
        })
        .fail(function(response) {
            alert('Something wrong(Retrieve Article Information)!');
        });
    }

    function updateArticle() {
        console.log($("form#updateArticleForm").serialize())
        $.ajax({
            type: 'PUT',
            url: articleDetailUrl,
            data: $("form#updateArticleForm").serialize(), 
        }).done(function(response) {
            $('#updateArticleModal').modal('toggle');
            retrieveArticleInformation();
        })
        .fail(function(response) {
            alert(response.responseText)
        });
    }

    retrieveArticleInformation();
    $("#submitArticleForm").click(updateArticle);
});
