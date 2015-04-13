var posts = null;
$(document).ready(function () {
    window.applicationCache.onupdateready = function(e) {
        window.applicationCache.update();
    }
    $('#id_image').hide();
    $('#new_post_submit').hide();
    $('.ui.sticky').sticky();
    $('#newpostbutton').click(function () {
        $('#newpostmodal').modal('show');
    });
    $('#id_image_styled').click(function () {
        $('#id_image').click();
    });
    $('#new_post_submit_styled').click(function () {
        $('#new_post_submit').click();
    });
    $('#id_image').change( function () {
        var fileName = $(this).val().split('/').pop().split('\\').pop();
        if (fileName) {
            $('#id_image_styled').html("<div>" + fileName + "</div>");
        } else {
            $('#id_image_styled').html("<div>Upload an image</div>");
        }
    });
});

function RenderPost(post) {
    var posthtml = 
    "<div class='ui vertical segment'>" +
        "<div class='content'>";
<<<<<<< HEAD
    
=======
>>>>>>> 0b4c750479583e94c6ebe659e620665a248875d9
    var postimagesplit = post.image.split("/");
    if (postimagesplit[postimagesplit.length - 1] != "NULL") {
        posthtml +=
            "<a href='javascript:void(0);' onclick='LoadSinglePost(" + post['id'] + ");return false;'><img id='postimage" + post['id'] + "' class='ui image center' src='" + post['image'] + "' alt='user image'/></a>";
    }
    posthtml +=
    "<p id='posttext" + post['id'] + "'>" + post['text_content'] + "</p>" +
    "</div></div>"; 

    $('#postlist').html(posthtml + $('#postlist').html());
}

function PollWorker() {
    $.ajax({
        url: 'http://piper.link/api/posts/post/?format=json/',
        success: function(response) {
<<<<<<< HEAD
            var updates = JSON.parse(response);
            if (posts == null) {
=======
            var updates = response;
            if (posts === null) {
>>>>>>> 0b4c750479583e94c6ebe659e620665a248875d9
                posts = [];
                for (i = updates['objects'].length - 1; i >= 0; --i) {
                    RenderPost(updates['objects'][i]);
                    posts.unshift(updates['objects'][i]);
                }
            } else {
                var recId = posts[0].id;
                var j;
                for (j = 0; updates['objects'][j].id != recId && j < updates['objects'].length; ++j);
                for (k = j - 1; k >= 0; --k) { 
                    RenderPost(updates['objects'][i]);
                    posts.unshift(updates['objects'][i]);
                }
            }
        },
        complete: function() {
            setTimeout(PollWorker, 2000);
        }
    });
};

PollWorker();
function LoadSinglePost(postId) {
    $('#singlepostimage').attr('src', $('#postimage' + postId).attr('src'));
    $('#singlepostdescription').html($('#posttext' + postId).html());
    $('#singlepostmodal.ui.modal').modal('show');
}

