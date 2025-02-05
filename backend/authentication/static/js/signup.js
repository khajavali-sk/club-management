document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#signup-form");
    
    form.addEventListener("input", function (event) {
        const field = event.target;
        validateField(field);
    });

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default submission
        const formData = new FormData(form);
        
        fetch("../validate-signup/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = "/signup-success/";  // ✅ Redirect after signup
            } else {
                alert(data.errors);
            }
        });
    });

    function validateField(field) {
        fetch(`../validate-field/?field=${field.name}&value=${field.value}`)
        .then(response => response.json())
        .then(data => {
            if (!data.valid) {
                field.classList.add("border-red-500");
                field.nextElementSibling.textContent = data.error;
            } else {
                field.classList.remove("border-red-500");
                field.nextElementSibling.textContent = "";
            }
        });
    }
});
