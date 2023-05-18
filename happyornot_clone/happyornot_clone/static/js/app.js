const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


$(document).ready(function() {
    $('#speaker').change(function() {
      var speakerId = $(this).val();
      console.log(speakerId)
      $.ajax({
        url: '/get-training-titles/',
        data: {
          'speaker_id': speakerId
        },
        dataType: 'json',
        success: function(data) {
            console.log(data)
          var options = '<option value="">Select a Training Title</option>';
          for (var i = 0; i < data.length; i++) {
            options += '<option value="' + data[i].id + '">' + data[i].title + '</option>';
          }
          $('#training-title').html(options);
        }
      });
    });
  });


$(document).ready(function() {

    $('#myForm input[type=radio]').click(function() {
        $('#myForm').submit();
    });


    $('#myForm').submit(function(event) {
        event.preventDefault();
        var rater = $('#rater').val();
        var comment = $('#comment').val();
        var rating = $('input[name="rating"]:checked').val();
        var speaker = $('#speaker').val();
        var trainingtitle = $('#training-title').val();

        console.log(speaker)
        // Check if input fields are empty
        if(rater === '' || comment === '' || speaker === '' || trainingtitle === '' || rating === 'undefined'){
            alert("Please fill all the fields");
            return false;
        }
        console.log(rater, comment, rating, speaker, trainingtitle); // Add this line to log the form data to the console
        

        $.ajax({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
              },
            url: '/save-feedback/',
            type: 'POST',
            data: { 
                'speaker': speaker,
                'rater':rater,
                'comment': comment,
                'rating': rating,
                'trainingtitle': trainingtitle,
                'csrfmiddlewaretoken': '{{ csrf_token }}' // Include the CSRF token in the data
            },
            processData: true,
            contentType: 'application/x-www-form-urlencoded',
            dataType: 'json',
            success: function(response) {
                $('#textNotification').text(response.success_message).addClass('alert alert-success').fadeIn();
                $('#notification').attr('src', response.success_image);
                $('#myForm').find("input[type=text], textarea").val(""); // clear the input fieldsgit
                $('#speaker').val(""); // clear the input fieldsgit
                $('#training-title').val(""); // clear the input fieldsgit

                $('#myForm').hide();

        


                setTimeout(function() {
                    $('#notification').attr('src', '');
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
