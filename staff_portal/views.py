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
    ingredients = Ingredient.objects.all()
    categories = IngredientCategory.objects.all()

    if request.method == 'POST':
        if 'delete' in request.POST:
            ingredient_id = request.POST.get('delete')
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            ingredient.delete()
            messages.success(request, "Ingredient deleted successfully.")
            return redirect('manage_ingredients')

        elif 'edit_id' in request.POST:
            ingredient_id = request.POST.get('edit_id')
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            form = IngredientForm(request.POST, request.FILES, instance=ingredient)
            if form.is_valid():
                form.save()
                messages.success(request, "Ingredient updated successfully.")
            else:
                messages.error(request, "Error updating ingredient: " + str(form.errors))
            return redirect('manage_ingredients')

        else:
                messages.error(request, "Error updating ingredient.")

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
        # Save the form to create a new Pizza instance, but don't commit to the database yet
        pizza = form.save(commit=False)
        # Manually save the Pizza instance to the database
        pizza.save()
        # Save the many-to-many fields of the form
        form.save_m2m()

        # Process and add each selected ingredient to the pizza
        for key in request.POST:
            if key.startswith('ingredient_'):
                ingredient_id = request.POST[key]
                if ingredient_id:
                    # Retrieve and add the ingredient to the pizza's ingredients
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
    # Fetch all pizza items from the database
    pizzas = Pizza.objects.all()
    
    # Pass the list of pizzas to the manage_menu_items template
    return render(request, 'manage_menu_items.html', {'pizzas': pizzas})
