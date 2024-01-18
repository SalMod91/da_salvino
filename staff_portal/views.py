from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaffUserCreationForm, CustomPasswordChangeForm, IngredientForm, MenuItemForm
from .models import Ingredient, IngredientCategory, Pizza
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.models import CustomStaffUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def staff_portal(request):
    login_form = AuthenticationForm()
    signup_form = StaffUserCreationForm()
    password_change_form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'submit_login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_approved:
                        login(request, user)
                        messages.success(request, f"You have successfully logged in as {username}.")
                        return redirect('staff_portal') 
                    else:
                        messages.error(request, "Approval pending. Please wait for a manager to approve your account.")

        elif 'submit_signup' in request.POST:
            signup_form = StaffUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Registration successful! Your account is pending approval.")
                return redirect('staff_portal')
            else:
                messages.error(request, "Invalid registration details.")

        elif 'action' in request.POST and request.POST['action'] == 'logout':
            logout(request)
            messages.success(request, "You have been successfully logged out.")
            return redirect('staff_portal')

        elif 'change_password' in request.POST:
            password_change_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, f"Password for {user.username} changed successfully.")
                return redirect('staff_portal')
            else:
                messages.error(request, "Error changing password.")

    return render(request, 'staff_portal.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'password_change_form': password_change_form,
})


def create_ingredient(request):

    if request.method == 'POST':
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ingredient created successfully.")
            return redirect('staff_portal')

    else:
        form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form})


def manage_ingredients(request):
    """
    View function for managing the ingredients.
    Displays all exisiting ingredients and categories in the database.
    It responds to both GET and POST requests, handling ingredient deletions and updates accordingly.
    """

    # Retrieves all ingredients and ingredient categories from the database
    ingredients = Ingredient.objects.all()
    categories = IngredientCategory.objects.all()

    # Check if the request method is POST
    if request.method == 'POST':

        # Check if the 'delete' action is specified in the POST data
        if 'delete' in request.POST:
            # Retrieve the ID of the ingredient to delete from the POST data
            ingredient_id = request.POST.get('delete')
            # Fetch the corresponding ingredient object from the database or return a 404 if not found
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            # Delete the fetched ingredient object from the database
            ingredient.delete()
            # Display a success message to the user
            messages.success(request, "Ingredient deleted successfully.")
            # Redirect to the manage_ingredients page to display the updated list of menu items
            return redirect('manage_ingredients')

        # Check if the 'edit_id' action is specified in the POST data
        elif 'edit_id' in request.POST:
             # Retrieve the ID of the ingredient to edit from the POST data
            ingredient_id = request.POST.get('edit_id')
            # Fetch the corresponding ingredient object from the database or return a 404 if not found
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            # This pre-fills the form with the ingredient's existing data for editing
            form = IngredientForm(request.POST, request.FILES, instance=ingredient)
            # Checks if the submitted form data is valid
            if form.is_valid():
                # Checks if the submitted form data is valid
                form.save()
                # Displays a success message indicating the ingredient has been updated successfully
                messages.success(request, "Ingredient updated successfully.")
            else:
                # If the form data is not valid, it displays an error message with form validation errors
                messages.error(request, "Error updating ingredient: " + str(form.errors))
            
            # Redirects the user back to the 'manage_ingredients' page after the form submission
            return redirect('manage_ingredients')

        # Adds a general error message if an unexpected action is encountered
        else:
                messages.error(request, "Error updating ingredient.")

    # Renders the 'manage_ingredients' template, passing in the ingredients and categories
    return render(request, 'manage_ingredients.html', {'ingredients': ingredients,'categories': categories,})


def create_menu_item(request):
    """
    View function for creating a new pizza menu item.

    - Initializes and processes the MenuItemForm for pizza creation.
    - Handles dynamic addition of ingredients.
    - Saves the new pizza item and its ingredients to the database.
    - Redirects to the staff portal on successful creation or renders the form again on GET or form validation failure.
    """

    # Initialize the form with POST data if available, otherwise create an empty form
    form = MenuItemForm(request.POST or None, request.FILES or None)

    # Retrieve ingredient choices for the form
    ingredient_choices = form.get_ingredient_choices()

    # Check if the form is submitted and valid
    if request.method == 'POST' and form.is_valid():
        # m2m relationships require the parent object to be saved first
        # Save the form to create a new Pizza instance, but don't commit to the database yet
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
        'ingredient_choices': ingredient_choices
    })


def manage_menu_items(request):
    """
    View function for managing menu items.
    Displays all menu items and handles the editing/deletion of a selected menu item.
    If a POST request is made with a 'delete' action, the specified menu item is deleted.
    """
    # Fetch all pizza items from the database
    pizzas = Pizza.objects.all()

    # Initialize the form with POST data if available, otherwise create an empty form
    form = MenuItemForm(request.POST or None, request.FILES or None)

    # Retrieve ingredient choices for the form
    ingredient_choices = form.get_ingredient_choices()

    # Check if the request method is POST
    if request.method == 'POST':

        # Check if the 'delete' action is specified in the POST data
        if 'delete' in request.POST:
            # Retrieve the ID of the menu item to delete from the POST data
            menu_item_id = request.POST.get('delete')
            # Fetch the corresponding Pizza object from the database or return a 404 if not found
            menu_item = get_object_or_404(Pizza, id=menu_item_id)
            # Delete the fetched Pizza object from the database
            menu_item.delete()
            # Display a success message to the user
            messages.success(request, "Menu Item deleted successfully.")
            # Redirect to the manage_menu_items page to display the updated list of menu items
            return redirect('manage_menu_items')
        
        
        # Check if the 'edit_id' action is specified in the POST data
        elif 'edit_id' in request.POST:
            menu_item_id = request.POST.get('edit_id')
            menu_item = get_object_or_404(Pizza, id=menu_item_id)
            form = MenuItemForm(request.POST, request.FILES, instance=menu_item)

            if form.is_valid():
                # m2m relationships require the parent object to be saved first
                # Save the form to create a new Pizza instance, but don't commit to the database yet
                pizza = form.save(commit=False)
                # Manually save the Pizza instance to the database
                pizza.save()
                # Save the many-to-many fields of the form
                form.save_m2m()

                # Clear existing ingredients and add new ones
                pizza.ingredients.clear()
                for key in request.POST:
                    if key.startswith('ingredient_') and request.POST[key]:
                        ingredient_id = request.POST[key]
                        ingredient = Ingredient.objects.get(id=ingredient_id)
                        pizza.ingredients.add(ingredient)

                # Display a success message indicating the menu item has been updated successfully
                messages.success(request, "Menu Item updated successfully.")
                # Redirects the user back to the 'manage_menu_items' page after the form submission
                return redirect('manage_menu_items')

            # If the form data is not valid, display an error message with form validation errors
            else:
                messages.error(request, "Error updating menu item: " + str(form.errors))
    
    # Pass the list of pizzas and ingredients to the manage_menu_items template
    return render(request, 'manage_menu_items.html', {
        'pizzas': pizzas,
        'ingredient_choices': ingredient_choices,
        })
