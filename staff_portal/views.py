from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from cloudinary.uploader import destroy
from users.models import CustomStaffUser
from .forms import (
    StaffUserCreationForm, CustomPasswordChangeForm,
    IngredientForm, MenuItemForm
)
from .models import Ingredient, IngredientCategory, Pizza


def staff_portal(request):
    """
    View function for the staff portal page.

    Handles user login, signup, password change,
    and logout actions within the staff portal.
    Displays appropriate success or error messages and redirects as necessary.
    """

    # Initialize forms for login, signup, and password change actions
    login_form = AuthenticationForm()
    signup_form = StaffUserCreationForm()
    password_change_form = CustomPasswordChangeForm(user=request.user)

    # Handle form submission
    if request.method == 'POST':

        # Process login form submission
        if 'submit_login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_approved:
                        login(request, user)
                        messages.success(
                            request,
                            f"You have successfully logged in as {username}."
                        )
                        return redirect('staff_portal')
                    else:
                        messages.error(
                            request,
                            ("Approval pending. Please wait for a manager"
                             " to approve your account.")
                        )

        # Process signup form submission
        elif 'submit_signup' in request.POST:
            signup_form = StaffUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(
                    request,
                    "Registration successful! Your account is"
                    " pending approval."
                )

                return redirect('staff_portal')
            else:
                messages.error(request, "Invalid registration details.")

        # Process logout action
        elif 'action' in request.POST and request.POST['action'] == 'logout':
            logout(request)
            messages.success(request, "You have been successfully logged out.")
            return redirect('staff_portal')

        # Process password change form submission
        elif 'change_password' in request.POST:
            password_change_form = CustomPasswordChangeForm(
                user=request.user, data=request.POST
                )

            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request,
                    f"Password for {user.username} changed successfully."
                )
                return redirect('staff_portal')
            else:
                messages.error(request, "Error changing password.")

    # Render the staff portal page with the forms
    return render(request, 'staff_portal.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'password_change_form': password_change_form,
    })


def create_ingredient(request):
    """
    View function to create a new ingredient.

    Handles the creation of a new ingredient through a form submission.
    On successful form submission,
    saves the ingredient and redirects to the staff portal.
    """

    # Handle form submission
    if request.method == 'POST':
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ingredient created successfully.")
            return redirect('staff_portal')

    else:
        form = IngredientForm()

    # Render the add ingredient page with the form
    return render(request, 'add_ingredient.html', {'form': form})


def manage_ingredients(request):
    """
    View function for managing the ingredients.
    Displays all exisiting ingredients and categories in the database.
    It responds to both GET and POST requests,
    handling ingredient deletions and updates accordingly.
    """

    # Retrieves all ingredient categories from the database
    # and orders it based on the 'order' field
    categories = IngredientCategory.objects.order_by('order')

    # Fetch all ingredients and order them by category 'order'
    # and then by ingredient name
    ingredients = Ingredient.objects.select_related('category') \
                                    .order_by('category__order', 'name')

    # Initialize the form with POST data if available,
    # otherwise create an empty form
    form = IngredientForm(request.POST or None, request.FILES or None)

    # Retrieve 'last__ingredient_edit_details' from the session
    # or initialize with default values
    last_ingredient_edit_details = request.session.get('last_edit_details', {
        'edit_id': '',
        'name': '',
        'category': '',
        'description': '',
        'origin': '',
        'image_url': ''
    })

    # Check if the request method is POST
    if request.method == 'POST':

        # Check if the 'delete' action is specified in the POST data
        if 'delete' in request.POST:
            # Retrieve the ID of the ingredient to delete from the POST data
            ingredient_id = request.POST.get('delete')
            # Fetch the corresponding ingredient object from the database
            # or return a 404 if not found
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            # Delete the fetched ingredient object from the database
            ingredient.delete()
            # Display a success message to the user
            messages.success(request, "Ingredient deleted successfully.")
            # Redirect to the manage_ingredients page to display
            # the updated list of menu items
            return redirect('manage_ingredients')

        # Check if the 'edit_id' action is specified in the POST data
        elif 'edit_id' in request.POST:
            # Retrieve the ID of the ingredient to edit from the POST data
            ingredient_id = request.POST.get('edit_id')
            # Fetch the corresponding ingredient object from the database
            # or return a 404 if not found
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)

            # Get the current image URL if present
            existing_image_url = (
                ingredient.image.url if ingredient.image else None
            )

            # This pre-fills the form with the ingredient's
            # existing data for editing
            form = IngredientForm(
                request.POST, request.FILES, instance=ingredient
                )

            # Checks if the submitted form data is valid
            if form.is_valid():

                # Executes if the remove image checkbox is checked
                if 'remove_image' in request.POST:
                    # Specifies wich image to be deleted based on the item's id
                    public_id = f'ingredients/ingredient_image_{ingredient.id}'
                    # Deletes the image using the Cloudinary destroy function
                    destroy(public_id)
                    # Resets the image field to None
                    ingredient.image = None

                # Save the form and the ingredient instance
                form.save()

                # Displays a success message indicating the ingredient
                # has been updated successfully
                messages.success(request, "Ingredient updated successfully.")

                # Redirects the user back to the 'manage_ingredients'
                # page after the form submission
                return redirect('manage_ingredients')

            else:
                # Store the current edit details in the session for
                # re-rendering the form with validation errors
                request.session['last_ingredient_edit_details'] = {
                    'edit_id': ingredient_id,
                    'name': form.data.get('name', ''),
                    'category': form.data.get('category', ''),
                    'description': form.data.get('description', ''),
                    'origin': form.data.get('origin', ''),
                    'image_url': existing_image_url
                }

                # If the form data is not valid,
                # it displays an error message with form validation errors
                messages.error(request, "Error updating ingredient: ")

                # Return with updated form data for the first error
                return render(
                    request,
                    'manage_ingredients.html',
                    {
                        'form': form,
                        'ingredients': ingredients,
                        'categories': categories,
                        'last_ingredient_edit_details':
                            request.session['last_ingredient_edit_details'],
                    }
                )

        # Handle unexpected actions
        else:
            messages.error(request, "Error updating ingredient.")

    # Renders the 'manage_ingredients' template,
    # passing in the ingredients and categories
    return render(request, 'manage_ingredients.html', {
        'ingredients': ingredients,
        'categories': categories,
    })


def create_menu_item(request):
    """
    View function for creating a new pizza menu item.

    - Initializes and processes the MenuItemForm for pizza creation.
    - Handles dynamic addition of ingredients.
    - Saves the new pizza item and its ingredients to the database.
    - Redirects to the staff portal on successful creation
      or renders the form again on GET or form validation failure.
    """

    # Initialize the form with POST data if available,
    # otherwise create an empty form
    form = MenuItemForm(request.POST or None, request.FILES or None)

    # Retrieve ingredient choices for the form
    ingredient_choices = form.get_ingredient_choices()

    # Check if the form is submitted and valid
    if request.method == 'POST' and form.is_valid():
        # m2m relationships require the parent object to be saved first
        # Save the form to create a new Pizza instance,
        # but don't commit to the database yet
        pizza = form.save(commit=False)
        # Manually save the Pizza instance to the database
        pizza.save()
        # Save the many-to-many fields of the form
        form.save_m2m()

        # Clear existing ingredients and add new ones
        for key in request.POST:
            if key.startswith('ingredient_') and request.POST[key]:
                ingredient_id = request.POST[key]
                ingredient = Ingredient.objects.get(id=ingredient_id)
                pizza.ingredients.add(ingredient)

        # Display a success message and redirect to the staff portal
        messages.success(request, "Pizza created successfully.")
        return redirect('staff_portal')

    # Render the form template on GET request or if form is invalid
    return render(request, 'add_menu_item.html', {
        'form': form,
        'ingredient_choices': ingredient_choices,
    })


def manage_menu_items(request):
    """
    View function for managing menu items.
    Displays all menu items and handles the editing/deletion
    of a selected menu item.
    If a POST request is made with a 'delete' action,
    the specified menu item is deleted.
    """

    # Retrieve 'last_edit_details' from the session
    # or initialize with default values
    last_edit_details = request.session.get('last_edit_details', {
        'name': '',
        'has_mozzarella': False,
        'has_tomato': False,
        'image_url': '',
        'ingredient_ids': '',
        'edit_id': '',
    })

    # Fetch all pizza items from the database
    pizzas = Pizza.objects.all().order_by('name')

    # Initialize the form with POST data if available,
    # otherwise create an empty form
    form = MenuItemForm(request.POST or None, request.FILES or None)

    # Retrieve ingredient choices for the form
    ingredient_choices = form.get_ingredient_choices()

    if request.method == 'POST':

        # Check if the 'delete' action is specified in the POST data
        if 'delete' in request.POST:
            # Retrieve the ID of the menu item to delete from the POST data
            menu_item_id = request.POST.get('delete')
            # Fetch the corresponding Pizza object from the database
            # or return a 404 if not found
            menu_item = get_object_or_404(Pizza, id=menu_item_id)
            # Delete the fetched Pizza object from the database
            menu_item.delete()
            # Display a success message to the user
            messages.success(request, "Menu Item deleted successfully.")
            # Redirect to the manage_menu_items page
            # to display the updated list of menu items
            return redirect('manage_menu_items')

        # Check if the 'edit_id' action is specified in the POST data
        elif 'edit_id' in request.POST:

            # Retrieve the ID of the menu item to edit from the POST request
            menu_item_id = request.POST.get('edit_id')
            # Store the editing pizza's ID in the session
            # for tracking across requests
            request.session['editing_pizza_id'] = str(menu_item_id)
            # Fetch the Pizza object to edit from the database,
            # or return a 404 error if not found
            menu_item = get_object_or_404(Pizza, id=menu_item_id)
            # Initialize the form for editing
            form = MenuItemForm(
                request.POST, request.FILES, instance=menu_item
                )

            # Store the original image URL if any
            original_image_url = menu_item.image.url if menu_item.image else None

            if form.is_valid():
                # m2m relationships require the parent object to be saved first
                # Save the form to create a new Pizza instance,
                # but don't commit to the database yet
                pizza = form.save(commit=False)

                # Executes if the remove image checkbox is checked
                if 'remove_image' in request.POST:
                    # Specifies wich image to be deleted based on the item's id
                    public_id = f'pizzas/pizza_image_{menu_item.id}'
                    # Deletes the image using the Cloudinary destroy function
                    destroy(public_id)
                    # Resets the image field to None
                    menu_item.image = None

                # Manually save the Pizza instance to the database
                pizza.save()
                # Save the many-to-many fields of the form
                form.save_m2m()

                # Clear existing ingredients and add new ones
                pizza.ingredients.clear()

                # Iterate over each key in the POST request data
                for key in request.POST:
                    # Check if the key starts with 'ingredient_'
                    if key.startswith('ingredient_') and request.POST[key]:
                        # Retrieve the ingredient ID from the POST data
                        ingredient_id = request.POST[key]
                        # Fetch corresponding Ingredient object from database
                        ingredient = Ingredient.objects.get(id=ingredient_id)
                        # Add Ingredient object to the pizza's ingredients list
                        pizza.ingredients.add(ingredient)

                # Display a success message indicating the menu item
                # has been updated successfully
                messages.success(request, "Menu Item updated successfully.")
                # Redirects the user back to the 'manage_menu_items' page
                # after the form submission
                return redirect('manage_menu_items')

            # This code block is executed when the form submission is invalid
            else:
                # Update session data for invalid form submission
                request.session['last_edit_details'] = {
                    'name': form.cleaned_data.get('name', ''),
                    'has_mozzarella': form.cleaned_data.get(
                        'has_mozzarella', False),
                    'has_tomato': form.cleaned_data.get('has_tomato', False),
                    'image_url': original_image_url,
                    'ingredient_ids': ','.join(
                        str(ingredient.id) for ingredient in menu_item.ingredients.all()
                    ),
                    'edit_id': menu_item_id
                }

                # Display an error message indicating
                # there was an error editing the item
                messages.error(request, "Error updating menu item.")

                # Return with updated form data for the first error
                return render(request, 'manage_menu_items.html', {
                    'pizzas': pizzas,
                    'ingredient_choices': ingredient_choices,
                    'form': form,
                    'last_edit_details': request.session['last_edit_details'],
                })

                # Display an error message indicating there was an error
                # editing the menu item
                messages.error(request, "Error updating menu item.")

    # Check if the request is a GET request
    # or a POST request without an 'edit_id'
    if (request.method == 'GET' or
            (menu_item_id is None and 'edit_id' in request.POST)):

        # Remove 'last_edit_details' from the session if it exists
        # This is to clear any previously stored form data
        request.session.pop('last_edit_details', None)

        # Remove 'editing_pizza_id' from the session if it exists
        # This ensures the session doesn't hold onto an old pizza ID
        request.session.pop('editing_pizza_id', None)

    return render(request, 'manage_menu_items.html', {
        'pizzas': pizzas,
        'ingredient_choices': ingredient_choices,
        'form': form,
        'last_edit_details': last_edit_details,
    })
