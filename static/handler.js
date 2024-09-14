$(document).ready(function () {
    $('#scrape-form').submit(function (event) {
        event.preventDefault();
        alert('Scraping has started, the estimated processing time is 5-15 mins'); 
        $.ajax({
            // TODO: add the link here for api requests 
            url: "http://127.0.0.1:5000/scrape",
            // url: "https://reviews-rating-research-api-e1d7a9ccd772.herokuapp.com/scrape",
            type: "POST",
            success: function (res) {
                $(".info").html('<div class="finished">Success! Find the updated product ratings and reviews below.</div >');
                alert('Scraping was successful. You can now download the files'); 
            }, // success 
            error: function (e) {
                $(".info").html('<div class="error">Error! An error occurred while scraping. Please contact tna324@lehigh.edu</div>');
                alert('Error Occurred: ', e);
            },
        }) // ajax
    }); // form-submit
}); // document.ready 