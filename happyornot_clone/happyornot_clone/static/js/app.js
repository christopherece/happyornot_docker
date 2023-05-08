$(document).ready(function() {

    $('#myForm input[type=radio]').click(function() {
        $('#myForm').submit();
    });


    $('#myForm').submit(function(event) {
        event.preventDefault();
        var user = $('#user').val();
        var comment = $('#comment').val();
        var rating = $('input[name="rating"]:checked').val();

        console.log(user, comment, rating); // Add this line to log the form data to the console

        $.ajax({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
              },
            url: '/save-feedback/',
            type: 'POST',
            data: { 
                'user': user,
                'comment': comment,
                'rating': rating,
                'csrfmiddlewaretoken': '{{ csrf_token }}' // Include the CSRF token in the data
            },
            processData: true,
            contentType: 'application/x-www-form-urlencoded',
            dataType: 'json',
            success: function(response) {
                console.log(response.message)
                $('#textNotification').text(response.success_message).addClass('success').fadeIn();
                $('#notification').attr('src', response.success_image);
                $('#myForm').find("input[type=text], textarea").val(""); // clear the input fieldsgit
                $('#myForm').hide();


                setTimeout(function() {
                    $('#notification').fadeOut().removeClass('success');
                    $('#textNotification').fadeOut().removeClass('success');
                    $('#myForm').show();


                }, 5000);
            },
            error: function(xhr, status, error) {

                $('#notification').text('An error occurred. Please try again later.').addClass('error').fadeIn();
                setTimeout(function() {
                    $('#notification').fadeOut().removeClass('error');
                }, 5000);
            }
        });
    });
});
