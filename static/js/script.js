// Listen for the scroll event
window.addEventListener('scroll', function() {

    // Select the header element
    var header = document.querySelector('header');

    // Check if the scroll position is greater than 50 pixels
    if (window.scrollY > 50) {
        // If true, add 'sticky-top' class to make the header sticky
        header.setAttribute('class', 'sticky-top');
    } else {
        // If false, remove the class to position the header on top
        header.removeAttribute('class');
    }
});

// Waits for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function() {
    // Function to "populate" the "All" tab
    function populateAllTab() {
        var allContent = ''; // Assigned a variable to the content of the "All" tab

        // Clear the existing content in the "All" tab
        var allTab = document.getElementById('all');
        allTab.innerHTML = '';

        // Loop through each tab-pane and add its content to the "All" tab
        var tabPanes = document.querySelectorAll('.tab-pane');
        tabPanes.forEach(function(tabPane) {
            allContent += tabPane.innerHTML;
        });

        allTab.innerHTML = allContent; // Set the content of the "All" tab
    }

    // Call the function when the "All" tab is clicked
    var allNavTab = document.querySelector('a[href="#all"]');
    if (allNavTab) {
        allNavTab.addEventListener('click', populateAllTab);
    }
});

// Informs the user about their actions during authentication
document.addEventListener('DOMContentLoaded', function() {
    const messageContainer = document.getElementById('message-container');
    const messagesData = document.getElementById('messages-data');
    if (messageContainer && messagesData) {
        let messageText = '';
        messagesData.querySelectorAll('.message-item').forEach(function(messageSpan) {
            messageText += messageSpan.getAttribute('data-message');
        });

        if (messageText) {
            messageContainer.innerHTML = messageText;
            messageContainer.classList.add('alert-success');
            messageContainer.style.display = 'block';
            messageContainer.style.opacity = 1;

            // Start fading out after a delay
            setTimeout(function() {
                messageContainer.style.opacity = 0;
            }, 2000);

            // When the fade out timer runs out, the container will be hidden
            setTimeout(function() {
                messageContainer.style.display = 'none';
                messageContainer.classList.remove('alert-success');
            }, 2600);
        }
    }
});

// Opens the Modal to the Registration Tab if there are form errors
document.addEventListener('DOMContentLoaded', function() {
    function openLoginRegisterTab() {
        var loginFormErrors = document.querySelectorAll('#login .alert-danger').length > 0;
        var registrationFormErrors = document.querySelectorAll('#register .alert-danger').length > 0;
        var passwordChangeFormErrors = document.querySelectorAll('#passwordChangeModal .alert-danger').length > 0;
        if (registrationFormErrors) {
            $('#authModal').modal('show');

            $('#authModal .nav-tabs a[href="#register"]').tab('show');
        }

        if (loginFormErrors) {
            $('#authModal').modal('show');
            $('#authModal .nav-tabs a[href="#login"]').tab('show');
        }

        if (passwordChangeFormErrors) {
            $('#passwordChangeModal').modal('show');
        }
    }
    openLoginRegisterTab();
});

// Adds an Event Listener to each delete button
document.addEventListener('DOMContentLoaded', function () {
    var deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var ingredientId = button.getAttribute('data-ingredient-id');
            var ingredientToDeleteId = document.getElementById('deleteIngredientId');
            ingredientToDeleteId.value = ingredientId;
        });
    });
});

// Adds an Event Listener to the edit button, populating the fields with data from the database
document.addEventListener('DOMContentLoaded', function() {
    var editButtons = document.querySelectorAll('.edit-button');
    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var ingredientId = button.getAttribute('data-ingredient-id');
            var ingredientName = button.getAttribute('data-ingredient-name');
            var ingredientDescription = button.getAttribute('data-ingredient-description');
            var ingredientCategory = button.getAttribute('data-ingredient-category');
            var ingredientImage = button.getAttribute('data-ingredient-image');
            
            // Sets the field values
            document.getElementById('editIngredientId').value = ingredientId;
            document.getElementById('editName').value = ingredientName;
            document.getElementById('editDescription').value = ingredientDescription;

            // Set the Category field value
            var editCategoryField = document.getElementById('editCategory');
            if (editCategoryField) {
                // Ensures the correct category is selected
                for (var i = 0; i < editCategoryField.options.length; i++) {
                    if (editCategoryField.options[i].value === ingredientCategory) {
                        editCategoryField.selectedIndex = i;
                        break;
                    }
                }
            }

            var currentImage = document.getElementById('currentImage');
            if (currentImage) {
                currentImage.src = ingredientImage;
            }
                    });
    });
});

// Wait for the DOM to be loaded before executing
document.addEventListener('DOMContentLoaded', function() {
    // Initialize a counter to keep track of the number of ingredient selectors added.
    let ingredientCount = 0;

    // Add a click event listener to the 'add-ingredient' button.
    document.getElementById('add-ingredient').addEventListener('click', function() {
        // Check if the number of added ingredient selectors is less than 10.
        if (ingredientCount < 10) {
            // Get all elements with the class 'ingredient-selector'.
            let selectorDivs = document.getElementsByClassName('ingredient-selector');
            // Check if there is an ingredient selector corresponding to the current count.
            if (selectorDivs[ingredientCount]) {
                // Set the display style of the next ingredient selector to 'flex' to make it visible.
                selectorDivs[ingredientCount].classList.remove('hidden');
                selectorDivs[ingredientCount].classList.add('visible');
                // Increment the ingredient counter
                ingredientCount++;
            }
        }
    });
});
