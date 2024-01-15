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

// Adds an Event Listener to each ingredient delete button
document.addEventListener('DOMContentLoaded', function () {
    // Assigns all buttons with the class 'delete-ingredient-button'to a constant variable
    const deleteIngredientButtons = document.querySelectorAll('.delete-ingredient-button');

    // Iterates over each button in the deleteIngredientButtons variable
    deleteIngredientButtons.forEach(function (button) {
        // Adds a click event listener to each button
        button.addEventListener('click', function () {
            // Retrieves the 'data-ingredient-id' attribute from the clicked button, which contains the ID of the ingredient item to delete
            let ingredientId = button.getAttribute('data-ingredient-id');
            // Sets the value of the delete button in the modal to the ingredient's ID.
            let ingredientToDeleteId = document.getElementById('deleteIngredientId');
            ingredientToDeleteId.value = ingredientId;
        });
    });
});

// Waits for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
    // Assigns all buttons with the class 'delete-menu-item-button'to a constant variable
    const deleteMenuItemButtons = document.querySelectorAll('.delete-menu-item-button');

    // Iterates over each button in the deleteMenuItemButtons variable
    deleteMenuItemButtons.forEach(function (button) {
        // Adds a click event listener to each button
        button.addEventListener('click', function () {
            // Retrieves the 'data-menu_item-id' attribute from the clicked button, which contains the ID of the menu item to delete
            let menuItemId = button.getAttribute('data-menu_item-id');
            // Sets the value of the delete button in the modal to the menu item's ID.
            let menuItemToDeleteId = document.getElementById('deleteMenuItemId');
            menuItemToDeleteId.value = menuItemId;
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

// Waits for the document to load before executing
document.addEventListener('DOMContentLoaded', function() {

    // Variable to keep track of the number of visible ingredient selectors
    let ingredientCount = 0;
    // Assigns the Add Ingredient button to a variable
    let addIngredientButton = document.getElementById('add-ingredient');

    /**
     * Updates the numbering and names of all visible ingredient selectors.
     * This function iterates through each selector and, if it is visible,
     * updates its displayed number and the 'name' attribute of its 'select' element.
     */
    function updateSelectors() {
        // Assigns all ingredient selector divs to a variable
        let selectors = document.querySelectorAll('#ingredient-selectors .ingredient-selector');
        // Initialize a counter to assign new numbers to visible selectors
        let newCount = 1;

        // Iterate through each selector
        selectors.forEach(function(selector) {
            // Check if the selector is not hidden
            if (!selector.classList.contains('hidden')) {
                // Update the displayed number for the selector
                selector.querySelector('.ingredient-number').textContent = 'Ingredient #' + newCount;
                // Update the name attribute of the selector's <select> element to match the new number
                selector.querySelector('select').name = 'ingredient_' + newCount;
                // Increment the counter for the next visible selector
                newCount++;
            }
        });
        ingredientCount = newCount - 1;
    }

    // Event listeners for remove buttons (one of my first tests with arrow functions)
    document.querySelectorAll('.remove-ingredient').forEach(button => {
        // Adds an Event listener to the remove button
        button.addEventListener('click', function() {
            // Find the closest parent div with the class 'ingredient-selector'
            let selectorDiv = this.closest('.ingredient-selector');
            // Call the function to hide and reset the closest div with the class 'ingredient selector'
            removeIngredientSelector(selectorDiv);
        });
    });

    /**
     * Hides a specified ingredient selector and resets its selection.
     * This function performs several actions on the selectorDiv:
     * 1. Adds the 'hidden' class to make the selector invisible.
     * 2. Removes the 'visible' class.
     * 3. Resets the select element to the placeholder.
     * 4. Calls the updateSelectors function to renumber and update the names of all remaining visible selectors.
     */
    function removeIngredientSelector(selectorDiv) {
        // Add 'hidden' class to the selector div, making it invisible
        selectorDiv.classList.add('hidden');
        // Remove 'visible' class from the selector div
        selectorDiv.classList.remove('visible');
        // Reset to default placeholder
        selectorDiv.querySelector('select').selectedIndex = 0;
        // Call updateSelectors to renumber and rename remaining selectors
        updateSelectors();
        addIngredientButton.classList.remove('hidden');
    }

    // Event listener for adding ingredients
    addIngredientButton.addEventListener('click', function() {
        // Check if the total number of selectors is less than 10
        if (ingredientCount < 10) {
            // Assign all selector divs to a variable
            let selectorDivs = document.querySelectorAll('#ingredient-selectors .ingredient-selector');
            // Assigns the next hidden selector to a variable
            let nextSelector = Array.from(selectorDivs).find(function(div) {
                return div.classList.contains('hidden');
            });
            // If there is still a hidden selector available the "Add Ingredient" is still visible
            if (nextSelector) {
                nextSelector.classList.remove('hidden');
                nextSelector.classList.add('visible');
                updateSelectors();
            }
            // If the total number of selectors reaches 10, hide the "Add Ingredient" button
            if (ingredientCount === 10) {
                addIngredientButton.classList.add('hidden');
            }
        }
    });
});
