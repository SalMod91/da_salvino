// Waits for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function() {

    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(function (toggle) {
        const dropdownParent = toggle.closest('.dropdown, .dropend');

        dropdownParent.addEventListener('mouseenter', function () {
            const dropdown = new bootstrap.Dropdown(toggle);
            dropdown.show();
        });

        dropdownParent.addEventListener('mouseleave', function () {
            const dropdown = new bootstrap.Dropdown(toggle);
            dropdown.hide();
            // Blur the toggle button when mouse leaves the dropdown area
            toggle.blur();
        });
    });

    // Listen for the scroll event
    window.addEventListener('scroll', function() {
        // Select the header element
        let header = document.querySelector('header');
        // Check if the scroll position is greater than 50 pixels
        if (window.scrollY > 50) {
            // If true, add 'sticky-top' class to make the header sticky
            header.setAttribute('class', 'sticky-top');
        } else {
            // If false, remove the class to position the header on top
            header.removeAttribute('class');
        }
    });

    /**
     * Populates the "All" tab with content from each individual tab pane.
     * This function clears the existing content in the "All" tab and then iterates
     * through each element with the class '.tab-pane'.
     * The inner HTML of each tab pane is concatenated and then set as the inner HTML of the "All" tab.
     * This combines the content of all tab panes into the "All" tab.
     */
    function populateAllTab() {
        // Assigned a variable to the content of the "All" tab
        let allContent = ''; 
        // Clear the existing content in the "All" tab
        let allTab = document.getElementById('all');
        allTab.innerHTML = '';
        // Loop through each tab-pane and add its content to the "All" tab
        let tabPanes = document.querySelectorAll('.tab-pane');
        tabPanes.forEach(function(tabPane) {
            allContent += tabPane.innerHTML;
        });
        // Set the content of the "All" tab
        allTab.innerHTML = allContent;
    }

    // Call the populateAllTab function when the "All" tab is clicked
    let allNavTab = document.querySelector('a[href="#all"]');
    if (allNavTab) {
        allNavTab.addEventListener('click', populateAllTab);
    }

    // Retrieve the message container and message data elements
    const messageContainer = document.getElementById('message-container');
    const messagesData = document.getElementById('messages-data');
    // Check if both messageContainer and messagesData elements exist
    if (messageContainer && messagesData) {
        // Creates a variable in wich to store the message text
        let messageText = '';
        // Iterate over each element with the class '.message-item' within messagesData
        messagesData.querySelectorAll('.message-item').forEach(function(messageSpan) {
            // Adds the text by appending the 'data-message' value to messageText
            messageText += messageSpan.getAttribute('data-message');
        });

        if (messageText) {
            messageContainer.innerHTML = messageText;
            // Add the 'alert-success' Bootstrap class
            messageContainer.classList.add('alert-success');
            // Makes the message visible
            messageContainer.style.display = 'block';
            messageContainer.style.opacity = 1;

            // Start fading out after a delay
            setTimeout(function() {
                messageContainer.style.opacity = 0;
            }, 2000);

            // When the fade out timer runs out, the container will be hidden
            setTimeout(function() {
                messageContainer.style.display = 'none';
                messagesData.style.display = 'none';
            }, 2600);
        }
    }

    // Opens the Modal to the Registration/Login/Password Change Tab if there are form errors
    function openLoginRegisterTab() {
        const loginFormErrors = document.querySelectorAll('#login .alert-danger').length > 0;
        const registrationFormErrors = document.querySelectorAll('#register .alert-danger').length > 0;
        const passwordChangeFormErrors = document.querySelectorAll('#passwordChangeModal .alert-danger').length > 0;
    
        // Check for the authModal existence
        const authModalElement = document.getElementById('authModal');
        if (authModalElement) {
            const authModal = new bootstrap.Modal(authModalElement);
            // Check for specific form errors to decide which tab to show
            if (registrationFormErrors) {
                authModal.show();
                // Manually trigger click event on tab
                document.querySelector('#authModal .nav-tabs a[href="#register"]').click();
            } else if (loginFormErrors) {
                authModal.show();
                // Manually trigger click event on tab
                document.querySelector('#authModal .nav-tabs a[href="#login"]').click();
            }
        }
    
        // Check for the passwordChangeModal existence
        const passwordChangeModalElement = document.getElementById('passwordChangeModal');
        if (passwordChangeModalElement && passwordChangeFormErrors) {
            const passwordChangeModal = new bootstrap.Modal(passwordChangeModalElement);
            passwordChangeModal.show();
        }
    }

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

    // Function to reset the checkbox for removing the uploaded ingredient image
    function resetRemoveIngredientImageCheckbox() {
        let removeIngredientImageCheckbox = document.getElementById('removeIngredientImage');
        if (removeIngredientImageCheckbox) {
            removeIngredientImageCheckbox.checked = false;
        }
    }

    // Select all buttons with the class 'edit-button'
    const editButtons = document.querySelectorAll('.edit-button');
    // Iterate over each button
    editButtons.forEach(function(button) {
        // Event Listener retrieving the information of the ingredient to be edited
        button.addEventListener('click', function() {
            const ingredientId = button.getAttribute('data-ingredient-id');
            const ingredientName = button.getAttribute('data-ingredient-name');
            const ingredientCategory = button.getAttribute('data-ingredient-category');
            const ingredientDescription = button.getAttribute('data-ingredient-description');
            const ingredientOrigin = button.getAttribute('data-ingredient-origin');
            const ingredientImage = button.getAttribute('data-ingredient-image');
            const currentIngredientImage = document.getElementById('currentIngredientImage');
            const ingredientImageInput = document.getElementById('editIngredientImage');
            
            // Sets the field values
            document.getElementById('editIngredientId').value = ingredientId;
            document.getElementById('editIngredientName').value = ingredientName;
            document.getElementById('editIngredientCategory').value = ingredientCategory;
            document.getElementById('editIngredientDescription').value = ingredientDescription;
            document.getElementById('editIngredientOrigin').value = ingredientOrigin;

            // Uncheck the checkbox from remove ingredient image
            resetRemoveIngredientImageCheckbox()

            // Set the Category field value
            const editCategoryField = document.getElementById('editCategory');
            if (editCategoryField) {
                // Ensures the correct category is selected
                for (let i = 0; i < editCategoryField.options.length; i++) {
                    if (editCategoryField.options[i].value === ingredientCategory) {
                        editCategoryField.selectedIndex = i;
                        break;
                    }
                }
            }

            // Checks if there is an image and sets it as a preview
            if (currentIngredientImage) {
                currentIngredientImage.src = ingredientImage;
            }

            // If the image elements exists, resets its value to an empty string
            // This clears any file that has been previously selected 
            if (ingredientImageInput) {
                ingredientImageInput.value = "";
            }
        });
    });

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

    // Function to reset the checkbox for removing the uploaded menu image
    function resetRemoveMenuImageCheckbox() {
        let removeMenuImageCheckbox = document.getElementById('removeMenuImage');
        if (removeMenuImageCheckbox) {
            removeMenuImageCheckbox.checked = false;
        }
    }

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
            // Selects the edit image field
            let menuImageInput = document.getElementById('editMenuImage');
            
            // Sets the values of the edit form fields with the data retrieved from the clicked button
            document.getElementById('editMenuItemId').value = menuItemId;
            document.getElementById('editMenuItemName').value = menuItemName;

            // Uncheck the remove menu image checkbox
            resetRemoveMenuImageCheckbox()

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

            // If the image elements exists, resets its value to an empty string
            // This clears any file that has been previously selected 
            if (menuImageInput) {
                menuImageInput.value = '';
            }
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

    // When an error occurs opens automatically the ingredient edit modal on reload
    // When the edit modal is open through an error, repopulates the modal using the data of the past session
    // Assigns the elements with 'error-message' class to this variable
    const ingredientErrors = document.querySelector('.edit-ingredient-error-message');

    // Check if there are any error messages on the page
    // If errors exist, indicating form submission failure, repopulate the form
    if (ingredientErrors) {
        // On reload automatically open the edit modal
        const editIngredientModal = new bootstrap.Modal(document.getElementById('editIngredientModal'));
        editIngredientModal.show();

        // Uncheck the remove menu image checkbox
        resetRemoveMenuImageCheckbox()

        // Set the values of the form fields based on the values stored in the hidden inputs
        document.getElementById('editIngredientName').value = document.getElementById('lastIngredientEditName').value;
        document.getElementById('editIngredientCategory').value = document.getElementById('lastIngredientEditCategory').value;
        document.getElementById('editIngredientDescription').value = document.getElementById('lastIngredientEditDescription').value;
        document.getElementById('editIngredientOrigin').value = document.getElementById('lastIngredientEditOrigin').value;

        // If there is an image URL, set it to the image element
        const imageIngredientUrl = document.getElementById('lastIngredientEditImageURL').value;
        if (imageIngredientUrl) {
            document.getElementById('currentIngredientImage').src = imageIngredientUrl;
        }

        // Set the edit_id
        const editIngredientId = document.getElementById('lastIngredientEditId').value;
        if (editIngredientId) {
            document.getElementById('editIngredientId').value = editIngredientId;
        }
    }

    // When an error occurs opens automatically the menu edit modal on reload
    // When the edit modal is open through an error, repopulates the modal using the data of the past session
    // Assigns the elements with 'error-message' class to this variable
    const errors = document.querySelector('.edit-menu-error-message');
    // Check if there are any error messages on the page
    // If errors exist, indicating form submission failure, repopulate the form
    if (errors) {
        // On reload automatically open the edit modal
        const editMenuItemModal = new bootstrap.Modal(document.getElementById('editMenuItemModal'));
        editMenuItemModal.show();

        // Uncheck the remove menu image checkbox
        resetRemoveMenuImageCheckbox()

        // Set the values of the form fields based on the values stored in the hidden inputs
        document.getElementById('editMenuItemName').value = document.getElementById('lastEditName').value;
        document.querySelector('input[name="has_mozzarella"][value="' + document.getElementById('lastEditHasMozzarella').value + '"]').checked = true;
        document.querySelector('input[name="has_tomato"][value="' + document.getElementById('lastEditHasTomato').value + '"]').checked = true;

        // If there is an image URL, set it to the image element
        const imageUrl = document.getElementById('lastEditImageURL').value;
        if (imageUrl) {
            document.getElementById('currentMenuItemImage').src = imageUrl;
        }

        // Set the edit_id
        const editId = document.getElementById('lastEditId').value;
        if (editId) {
            document.getElementById('editMenuItemId').value = editId;
        }

        // Retrieve the stored ingredient IDs and repopulate the ingredient selectors
        const storedIngredientIds = document.getElementById('lastEditedIngredientIds').value.split(',').filter(id => id);
        manageEditIngredientSelectors(storedIngredientIds);
    }

    // Event listener for clearing the error messages when the edit ingredient modal is closed
    const editIngredientModal = document.getElementById('editIngredientModal');
    
    // Check if the modal element exists to avoid errors
    if (editIngredientModal) {
        editIngredientModal.addEventListener('hide.bs.modal', function () {
            document.querySelectorAll('.edit-ingredient-error-message').forEach(function (message) {
                // Clear the innerHTML of each message element, removing any error messages
                message.innerHTML = '';
            });
        });
    }

    // Event listener for clearing the error messages when the edit menu modal is closed
    const editMenuItemModal = document.getElementById('editMenuItemModal');
    
    // Check if the modal element exists to avoid errors
    if (editMenuItemModal) {
        editMenuItemModal.addEventListener('hide.bs.modal', function () {
            document.querySelectorAll('.edit-menu-error-message').forEach(function (message) {
                // Clear the innerHTML of each message element, removing any error messages
                message.innerHTML = '';
            });
        });
    }

    // Select the close and cancel buttons inside the editIngredientModal
    document.querySelectorAll('#editIngredientModal .close, #cancelIngredientModal').forEach(function(button) {
        // Add a click event listener to each button
        button.addEventListener('click', function() {
            // Hide the modal using BS 5
            const editIngredientModalElement = document.getElementById('editIngredientModal');
            const editIngredientModal = bootstrap.Modal.getInstance(editIngredientModalElement);
            if (editIngredientModal) {
                editIngredientModal.hide();
            }
        });
    });

    // Select the close and cancel buttons inside the editMenuItemModal
    document.querySelectorAll('#editMenuItemModal .close, #cancelMenuItemModal').forEach(function(button) {
        // Add a click event listener to each button
        button.addEventListener('click', function() {
            // Hide the modal using Bs 5
            const editMenuItemModalElement = document.getElementById('editMenuItemModal');
            const editMenuItemModal = bootstrap.Modal.getInstance(editMenuItemModalElement);
            if (editMenuItemModal) {
                editMenuItemModal.hide();
            }
        });
    });

    // Select the close button in authModal
    document.querySelectorAll('#authModal .close, #closeAuthModal').forEach(function(button) {
        // Add a click event listener to each selected button
        button.addEventListener('click', function() {
            // Hide the modal using Bs 5
            const authModalElement = document.getElementById('authModal');
            const authModal = bootstrap.Modal.getInstance(authModalElement);
            if (authModal) {
                authModal.hide();
            }
        });
    });

    // Select the close button inside the passwordChangeModal
    document.querySelectorAll('#passwordChangeModal .close, #closePasswordChangeModal').forEach(function(button) {
        // Add a click event listener to each selected button
        button.addEventListener('click', function() {
            // Hide the modal using Bs 5
            const passwordChangeModalElement = document.getElementById('passwordChangeModal');
            const passwordChangeModal = bootstrap.Modal.getInstance(passwordChangeModalElement);
            if (passwordChangeModal) {
                passwordChangeModal.hide();
            }
        });
    });

    // Fragment logic to open tabs and scroll to ingredient
    // The 'fragment' variable gets the hash part of the URL
    let fragment = window.location.hash;
    // Check if the fragment includes the string 'ingredient-'
    if (fragment.includes('ingredient-')) {
        // Selects the fragment
        let ingredientElement = document.querySelector(fragment);
        // If it exists in the DOM
        if (ingredientElement) {
            // Finds the closest parent element with the class '.tab-pane', wich should be the tab-pane in wich the ingredient resides
            let tabPane = ingredientElement.closest('.tab-pane');
            // If the parent tab-pane exists
            if (tabPane) {
                // Selects the specific tab-pane
                let tabId = tabPane.getAttribute('id');
                let tabLink = document.querySelector(`.nav-tabs a[href="#${tabId}"]`);
                // If the selected link exists
                if (tabLink) {
                    // Triggers a click on the tab link opening the corresponding tab after a short delay, scrolling to the ingredient
                    tabLink.click();
                    setTimeout(function() {
                        ingredientElement.scrollIntoView();
                    }, 100);
                }
            }
        }
    }

    openLoginRegisterTab();
});
