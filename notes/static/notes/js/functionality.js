
document.addEventListener("DOMContentLoaded", function() {
    // Get the comment section element
    var commentArea = document.getElementById("comment-area");

// Scroll the comment section to the bottom
    commentArea.scrollTop = commentArea.scrollHeight;

    });

function showUserModal() {
    userSelectModal = document.getElementById("id_select_user_modal")
    userSelectModal.style.display = "block"
}

const userSelectButton = document.getElementById("id_user_select_button");

userSelectButton.onclick = showUserModal

const modal = document.getElementById("id_select_user_modal")
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }

