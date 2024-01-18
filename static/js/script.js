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
// Remember to specify that this is the first usage of jquery
// Maybe refactor everything using jquery later after gaining more confidence with it
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

// Adds an Event Listener to the ingredients edit button, populating the fields with data from the database
document.addEventListener('DOMContentLoaded', function() {
    var editButtons = document.querySelectorAll('.edit-button');
    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var ingredientId = button.getAttribute('data-ingredient-id');
            var ingredientName = button.getAttribute('data-ingredient-name');
            var ingredientDescription = button.getAttribute('data-ingredient-description');
            var ingredientCategory = button.getAttribute('data-ingredient-category');
            var ingredientImage = button.getAttribute('data-ingredient-image');
            var currentIngredientImage = document.getElementById('currentIngredientImage');
            
            // Sets the field values
            document.getElementById('editIngredientId').value = ingredientId;
            document.getElementById('editIngredientName').value = ingredientName;
            document.getElementById('editIngredientDescription').value = ingredientDescription;

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

            if (currentIngredientImage) {
                currentIngredientImage.src = ingredientImage;
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
        let newCount = 0;

        // Iterate through each selector
        selectors.forEach(function(selector) {
            // Check if the selector is not hidden
            if (!selector.classList.contains('hidden')) {
                // Update the displayed number for the selector
                selector.querySelector('.ingredient-number').textContent = 'Ingredient #' + (newCount + 1);
                // Update the name attribute of the selector's <select> element to match the new number
                selector.querySelector('select').name = 'ingredient_' + newCount;
                // Increment the counter for the next visible selector
                newCount++;
            }
        });
        ingredientCount = newCount;
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

    // Check if the button exists on the page
    if (addIngredientButton) {
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
    }
});

// Adds an Event Listener to the edit menu item button, populating the fields with data from the database
document.addEventListener('DOMContentLoaded', function() {
    // Selects all buttons with the class 'edit-menu-item-button'
    const editMenuItemButtons = document.querySelectorAll('.edit-menu-item-button');
    // Iterates over each button in the editMenuItemButtons
    editMenuItemButtons.forEach(function(button) {
        // Adds a click event listener to each button
        button.addEventListener('click', function() {
            // Retrieves various data attributes from the clicked button
            // These attributes contain the current values of the menu item to be edited
            let menuItemId = button.getAttribute('data-menu_item-id');
            let menuItemName = button.getAttribute('data-menu_item-name');
            let menuItemTomato = button.getAttribute('data-menu_item-has_tomato');
            let menuItemMozzarella = button.getAttribute('data-menu_item-has_mozzarella');
            let menuItemImage = button.getAttribute('data-menu_item-image');

            // Selects the image element inside the edit modal to update its source
            let currentMenuItemImage = document.getElementById('currentMenuItemImage');
            
            // Sets the values of the edit form fields with the data retrieved from the clicked button
            document.getElementById('editMenuItemId').value = menuItemId;
            document.getElementById('editMenuItemName').value = menuItemName;

            // Checks the tomato and mozzarella checkboxes based on the retrieved values
            // Set the checked state of the checkboxes based on the data attributes
            // The '===' operator compares both the value and the type
            if (menuItemTomato === 'True') {
                document.getElementById('editMenuItemHasTomatoYes').checked = true;
            } else {
                document.getElementById('editMenuItemHasTomatoNo').checked = true;
            }
            
            if (menuItemMozzarella === 'True') {
                document.getElementById('editMenuItemHasMozzarellaYes').checked = true;
            } else {
                document.getElementById('editMenuItemHasMozzarellaNo').checked = true;
            }

            // Checks if there is an image and sets it as a preview
            if (currentMenuItemImage) {
                currentMenuItemImage.src = menuItemImage;
            }
        });
    });
});

// Function that handles resetting and populating ingredient selectors
function manageEditIngredientSelectors(ingredientIds) {
    // Selects all elements wich the class 'ingredient-selector' within the modal with ID 'editMenuItemModal'
    const selectors = document.querySelectorAll('#editMenuItemModal .ingredient-selector');
    let visibleCount = 0;
    // Reset all selectors
    selectors.forEach(selector => {
        // Adds the class 'hidden' to each selector and removes the 'visible' class
        selector.classList.add('hidden');
        // Resets the selector to the placeholder
        selector.querySelector('select').selectedIndex = 0;
    });

    // Populate selectors and count visible ones
    ingredientIds.forEach((ingredientId, index) => {
        // Check if the current index is within the range of available selectors
            // Select the ingredient selector based on its position
            const selector = selectors[index];
            // Remove the 'hidden' class to make the selector visible
            selector.classList.remove('hidden');
            // Select the 'select' element within the current selector
            const selectElement = selector.querySelector('select');
            // Set the value of the 'select' element to the current ingredient ID
            selectElement.value = ingredientId;
            // Increment the count of visible selectors
            visibleCount++;
    });

    // Select the "Add Ingredient" button within the edit modal
    const addButton = document.querySelector('#editMenuItemModal #add-ingredient');
    // Checks if the visible selectors are 10 or more
    if (visibleCount >= 10) {
        // If there are 10 or more selectors hides the "Add ingredient" button
        addButton.classList.add('hidden');
    } else {
        // If there are fewer than 10 visible selectors makes the "Add ingredient" button visible
        addButton.classList.remove('hidden')
    }
}



// Selects all elements with the class 'edit-menu-item-button' and adds a 'click' event listener to each of them
document.querySelectorAll('.edit-menu-item-button').forEach(button => {
    button.addEventListener('click', function() {
        // Get the ingredient IDs from the edit button's data attribute
        // Split: Separates the string of ID's into an array of single ID's
        // Filter: Removes empty strings from the list that occur due to the last comma
        const ingredientIds = this.getAttribute('data-menu_item-ingredients').split(',').filter(id => id);
        manageEditIngredientSelectors(ingredientIds);
    });
});
