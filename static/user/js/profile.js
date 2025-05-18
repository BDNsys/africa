
  document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.querySelectorAll(".edit-btn[data-field-id]");
    const saveBtn = document.getElementById("saveBtn");
    const profileForm = document.getElementById("profileForm");

    editButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const fieldId = button.getAttribute("data-field-id");
        const inputField = document.getElementById(fieldId);

        if (inputField) {
          inputField.disabled = false;
          inputField.focus();
          saveBtn.style.display = "block";
          button.style.display = "none";
        }
      });
    });

    // Show Save button when a new avatar is selected
    const avatarInput = document.getElementById("avatarInput");
    avatarInput.addEventListener("change", () => {
      if (avatarInput.files.length > 0) {
        saveBtn.style.display = "block";

        // Preview selected image
        const reader = new FileReader();
        reader.onload = (e) => {
          document.getElementById("avatarPreview").src = e.target.result;
        };
        reader.readAsDataURL(avatarInput.files[0]);
      }
    });

    // Re-enable all disabled fields before form submission
    profileForm.addEventListener("submit", () => {
      const disabledFields = profileForm.querySelectorAll("[disabled]");
      disabledFields.forEach((field) => {
        field.removeAttribute("disabled");
      });
    });
  });

  function clearAvatar() {
    const avatarInput = document.getElementById("avatarInput");
    avatarInput.value = "";
    document.getElementById("avatarPreview").src =
      "{% static 'images/default-avatar.png' %}";
    document.getElementById("saveBtn").style.display = "block";
  }
