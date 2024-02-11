## Content Table
- [Testing Table](#testing-table)
    - [Responsiveness Testing](#responsiveness-testing)
    - [Authentication Testing](#authentication-testing)
    - [CRUD Testing](#crud-testing)
    - [Links Testing](#links-testing)
    - [Python Validator Testing](#python-validator-testing)
- [HTML Validator](#html-validator)
- [CSS Validator](#css-validator)
- [JS Validator](#js-validator)
- [Lighthouse](#lighthouse)

## Testing Table

### Responsiveness Testing:
<details>
<summary>Click to expand</summary>

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| -------- | ---------- | --------------- | ---------- |
|Home Page | Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware. | Elements look good down to 320px | ✅ |
|Menu Page | Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.| Elements look good down to 320px | ✅ |
|Ingredients Page |Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Staff Portal|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Staff Portal: Modals for Login/Register, modify password and logout|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Add Ingredient Page|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Add Menu Item Page|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Manage Ingredients Page|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Manage Ingredients Edit Modal/Delete Modal|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Manage Menu Items Page|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
|Manage Menu Items Edit Modal/Delete Modal|Size down from 1920px to 320px using Dev Tool on Chrome, Mozilla and Explorer. Safari has been so far tested only on mobile devices without the Dev Tool due to missing hardware.|Elements look good down to 320px|✅|
</details>

### Authentication Testing:
<details>
<summary>Click to expand</summary>

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| -------- | ---------- | --------------- | ---------- |
| Staff Portal | Login with approved Staff User | Correctly logs in, redirect to Staff Portal, receive feedback message with the correct username, Staff Portal welcomes the user with the correct username |✅|
| Staff Portal | Login with invalid data | Login fails, redirect to Staff Portal, receive feedback message informing the failed login, reopen login modal showcasing the error message that caused the login to fail |✅|
| Staff Portal | Login with not approved account | Login fails, redirect to Staff Portal, receive feedback message informing that the user requires approval |✅|
| Staff Portal | Login with not staff account | Correctly logs in, shows prompt of restricted access to staff accounts only, prompts to head to the Home Page |✅|
| Staff Portal | When logged in, use the logout option | Logout modal correctly opens asking for logout confirmation. Correctly logs out and redirects to Staff Portal if confirmed |✅|
| Staff Portal | Register Account | Correctly registers account, redirect to Staff Portal, receive feedback message informing the user to await the approval, the user is correctly not approved |✅|
| Staff Portal | Register Account with non unique name | Registration process fails, redirects to Staff Portal, receive feedback message informing the user that the registration process failed, reopen login/register modal in the correct tab, showcase error message of username already in use |✅|
| Staff Portal | Register Account with a username with less than 3 characters | Registration process fails, redirects to Staff Portal, receive feedback message informing the user that the registration process failed, reopen login/register modal in the correct tab, show correct error message |✅|
| Staff Portal | Modify password of logged in user with correct data | Password modification executes correctly, redirects to Staff Portal, user receives positive feedback |✅|
| Staff Portal | Modify password of logged in user with incorrect data | Password modification fails, redirects to Staff Portal, receive feedback messaging informing the user that the process failed, reopen Password Modification modal, show error message of the fields affected |✅|
| Staff Portal | Reopen Password Modification modal after an error occurred | Error messages correctly reset |✅|
| Add Ingredient Page | When logged in, use the logout option | Logout modal correctly opens asking for logout confirmation. Correctly logs out and redirects to Staff Portal if confirmed |✅|
| Add Ingredient Page | Logged in as a not staff user | Correctly restricts access asking to go back to the Home Page |✅|
| Add Ingredient Page | Access page when not logged in | Correctly restricts access asking to login through the Staff Portal |✅|
| Add Menu Item Page | When logged in, use the logout option | Logout modal correctly opens asking for logout confirmation. Correctly logs out and redirects to Staff Portal if confirmed |✅|
| Add Menu Item Page | Logged in as a not staff user | Correctly restricts access asking to go back to the Home Page |✅|
| Add Menu Item Page | Access page when not logged in | Correctly restricts access asking to login through the Staff Portal |✅|
| Manage Ingredients Page | When logged in, use the logout option | Logout modal correctly opens asking for logout confirmation. Correctly logs out and redirects to Staff Portal if confirmed |✅|
| Manage Ingredients Page | Logged in as a not staff user | Correctly restricts access asking to go back to the Home Page |✅|
| Manage Ingredients Page | Access page when not logged in | Correctly restricts access asking to login through the Staff Portal |✅|
| Manage Menu Items Page | When logged in, use the logout option | Logout modal correctly opens asking for logout confirmation. Correctly logs out and redirects to Staff Portal if confirmed |✅|
| Manage Menu Items Page | Logged in as a not staff user | Correctly restricts access asking to go back to the Home Page |✅|
| Manage Menu Items Page | Access page when not logged in | Correctly restricts access asking to login through the Staff Portal |✅|
</details>

### CRUD Testing:
<details>
<summary>Click to expand</summary>

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| -------- | ---------- | --------------- | ---------- |
|Add Ingredient Page||||
|Create Ingredient| Add new Instance to Ingredient Model| Instance created|✅|
|Create Ingredient|Create Ingredient with Image| Instance created, Image uploaded to Cloudinary with the correct name: ingredient_ID|✅|
|Create Ingredient|Create Ingredient without Image| Instance created, Image set to default image|✅|
|Create Ingredient|Add new Instance to Ingredient Model with non-unique name| Form not valid, redirect to Add Ingredient page, error message informs the user|✅|
|Create Ingredient|Add new Instance to Ingredient Model with a file that is not an image format| Form not valid, redirect to Add Ingredient page, error message informs the user|✅|
|Add Menu Item Page||||
|Create Pizza Menu Item| Add new Instance to Pizza Model| Instance created|✅|
|Create Pizza Menu Item|Create Pizza with Image| Instance created, Image uploaded to Cloudinary with the correct name: pizza_ID|✅|
|Create Pizza Menu Item|Create Pizza without Image| Instance created, Image set to default image|✅|
|Create Pizza Menu Item| Add new Instance to Pizza Model with Selector open but set to Placeholder| Instance created, Ingredient Selector has been correctly ignored|✅|
|Create Pizza Menu Item| Add new Instance to Pizza Model with 2 selectors with the same ingredient| Form not valid, redirect to Add Menu Item page, error message informs the user|✅|
|Create Pizza Menu Item|Add new Instance to Pizza Model with non-unique name| Form not valid, redirect to Add Menu Item page, error message informs the user|✅|
|Create Pizza Menu Item|Add new Instance to Pizza Model with a file that is not an image format| Form not valid, redirect to Add Menu Item page, error message informs the user|✅|
| Manage Ingredients Page |  |  |  |
| Manage Ingredients | Order of appearance | Ingredients are correctly ordered based on Ingredient Category Order and then alphabetically | ✅ |
| Manage Ingredients| Click the Edit button | Correctly opens the selected Ingredient Modal and populates it with the correct data| ✅ |
| Manage Ingredients| Upload new Image | Correctly changes the image preview to the new image, new image's name correctly assigned to ingredient_ID, old image correctly overwritten| ✅ |
| Manage Ingredients| Check Remove Image Box | Correctly removes the existing image and setting the current image to the default image | ✅ |
| Manage Ingredients| Upload new image while simultaneously checking the "remove image" box | Remove image overrides the uploaded image resulting in the new image being the default assigned image | ✅ |
| Manage Ingredients| Change the ingredient name to another ingredients existing name | Form not valid, redirects to Manage Ingredients Page, reopens the Edit Modal of the invalid Ingredient, correctly repopulates the values in the modal, error message informs the user| ✅ |
| Manage Ingredients| Edit the Ingredient with a non image file | Form not valid, redirects to Manage Ingredients Page, reopens the Edit Modal of the invalid Ingredient, correctly repopulates the values in the modal, error message informs the user| ✅ |
| Manage Ingredients| Close the edit modal after it was automatically opened due to an invalid form | Error messages correctly reset as to not appear in next Modals| ✅ |
|Manage Ingredients| Delete the Ingredient| Correctly opens the selected Ingredients delete modal and upon confirmation correctly deletes the instance, correctly deletes the image associated to the ingredient from Cloudinary | ✅ |
| Manage Menu Item Page |  |  |  |
| Manage Menu Item | Order of appearance | Menu Items correctly ordered alphabetically | ✅ |
| Manage Menu Item | Click the Edit button | Correctly opens the selected Menu Item Modal and populates it with the correct data| ✅ |
| Manage Menu Item | Upload new Image | Correctly changes the image preview to the new image, new image's name correctly assigned to pizza_ID, old image correctly overwritten| ✅ |
| Manage Menu Item | Check Remove Image Box | Correctly removes the existing image and setting the current image to the default image | ✅ |
| Manage Menu Item | Upload new image while simultaneously checking the "remove image" box | Remove image overrides the uploaded image resulting in the new image being the default assigned image | ✅ |
| Manage Menu Item | Change the menu item name to another menu items existing name | Form not valid, redirects to Manage Menu Items Page, reopens the Edit Modal of the invalid Menu Item, correctly repopulates the values in the modal, error message informs the user | ✅ |
| Manage Menu Item | Edit the Menu Item with a non image file | Form not valid, redirects to Manage Menu Items Page, reopens the Edit Modal of the invalid Menu Item, correctly repopulates the values in the modal, error message informs the user | ✅ |
| Manage Menu Item | Edit the Menu Item by adding 2 of the same ingredient | Form not valid, redirects to Manage Menu Items Page, reopens the Edit Modal of the invalid Menu Item, correctly repopulates the values in the modal, error message informs the user | ✅ |
| Manage Menu Item | Edit the Menu Item with an empty Ingredient Selector | Instance correctly created, the empty ingredient selector was correctly ignored | ✅ |
| Manage Menu Item | Close the edit modal after it was automatically opened due to an invalid form | Error messages correctly reset as to not appear in next Modals | ✅ |
| Manage Menu Item | Delete the Menu Item | Correctly opens the selected Menu Items delete modal and upon confirmation correctly deletes the instance, correctly deletes the image associated to the menu item from Cloudinary | ✅ |
</details>

### Links Testing:
<details>
<summary>Click to expand</summary>

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| -------- | ---------- | --------------- | ---------- |
| Base | Click on Navigation Links | Correctly routed to the associated link |✅|
| Base | Logged in as Staff User | Correctly show the Staff Portal link |✅|
| Base | Hover the Staff Portal Link | Correctly opens a dropdown menu |✅|
| Home Page | Click on Home Page Buttons | Correctly routed to the associated page |✅|
| Footer | Click on Map Icon | Correctly opens a new Tab to Google Maps |✅|
| Footer | Click on Social Links | Correctly opens a new Tab to the associated links |✅|
| Menu Page | Click on Tabs | Correctly populates the tab content |✅|
| Menu Page | Click on Ingredient | Correctly routed to the Ingredients Page, correctly opens the associated Ingredient Category tab after a short delay, correctly scrolls to the chosen Ingredient |✅|
| Ingredient Page | Click on Tabs | Correctly populates the tab content |✅|
| Ingredient Page | Click on Staff Portal Links | Correctly routes the user to the associated page chosen |✅|
</details>

### Python Validator Testing:
<details>
<summary>Click to expand</summary>

The modules have been tested and reviewed using the Code Institute's linter.<br>

There is one line in staff_portal - views.py and users - middleware.py that exceed the recommended 79 characters.<br>
The code works regardless but breaking these specific lines into multiple lines exceeds my current capabilities.

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| -------- | ---------- | --------------- | ---------- |
| da_salvino - urls.py | PEP8 Validator| No issues found |✅|
| home - apps.py | PEP8 Validator| No issues found |✅|
| home - urls.py | PEP8 Validator| No issues found |✅|
| home - views.py | PEP8 Validator| No issues found |✅|
| ingredients - apps.py | PEP8 Validator| No issues found |✅|
| ingredients - urls.py | PEP8 Validator| No issues found |✅|
| ingredients - views.py | PEP8 Validator| No issues found |✅|
| menu - apps.py | PEP8 Validator| No issues found |✅|
| menu - urls.py | PEP8 Validator| No issues found |✅|
| menu - views.py | PEP8 Validator| No issues found |✅|
| staff_portal - admin.py | PEP8 Validator| No issues found |✅|
| staff_portal - apps.py | PEP8 Validator| No issues found |✅|
| staff_portal - forms.py | PEP8 Validator| No issues found |✅|
| staff_portal - models.py | PEP8 Validator| No issues found |✅|
| staff_portal - urls.py | PEP8 Validator| No issues found |✅|
| staff_portal - views.py | PEP8 Validator| No issues found |❗|
| users - admin.py | PEP8 Validator| No issues found |✅|
| users - apps.py | PEP8 Validator| No issues found |✅|
| users - middleware.py | PEP8 Validator| No issues found |❗|
| users - urls.py | PEP8 Validator| No issues found |✅|
| users - views.py | PEP8 Validator| No issues found |✅|
</details>

## HTML Validator:
<details>
<summary>Click to expand</summary>

For the HTML validation, all pages passed except for two, where the validator mistakenly flagged the src attribute in 'img src="{{ ingredient.image.url }}"' and 'img src="{{ pizza.image.url }}"' as empty. This issue arises because the validator doesn't recognize dynamic Django template language, which populates the src attribute with the URL of an ingredient's/menu item's image at runtime.

![Home Page Validator](/static/media/readme/home-validator.png)
![Menu Page Validator](/static/media/readme/menu-validator.png)
![Ingredients Page Validator](/static/media/readme/ingredients-validator.png)
![Staff Portal Validator](/static/media/readme/staff-validator.png)
![Add Ingredient Validator](/static/media/readme/add-ingredient-validator.png)
![Add Menu Item Validator](/static/media/readme/add-menu-validator.png)
![Manage Ingredient Validator](/static/media/readme/manage-ingredients-validator.png)
![Manage Menu Item Validator](/static/media/readme/manage-menu-validator.png)
</details>

## CSS Validator:
<details>
<summary>Click to expand</summary>

![CSS validator](/static/media/readme/css-validator.png)
</details>

## JS Validator:
<details>
<summary>Click to expand</summary>

![JS Validator](/static/media/readme/js-validator.png)
</details>

## Lighthouse:
<details>
<summary>Click to expand</summary>

![Home Desktop Lighthouse](/static/media/readme/light-home-desktop.png)
![Home Mobile Lighthouse](/static/media/readme/light-home-mobile.png)
![Menu Desktop Lighthouse](/static/media/readme/light-menu-desktop.png)
![Menu Mobile Lighthouse](/static/media/readme/light-menu-mobile.png)
![Ingredients Desktop Lighthouse](/static/media/readme/light-ingredient-desktop.png)
![Ingredients Mobile Lighthouse](/static/media/readme/light-ingredient-mobile.png)
![Staff Portal Desktop Lighthouse](/static/media/readme/light-staff-desktop.png)
![Staff Portal Mobile Lighthouse](/static/media/readme/light-staff-mobile.png)
![Add Ingredient Desktop Lighthouse](/static/media/readme/light-add-ing-desktop.png)
![Add Ingredient Mobile Lighthouse](/static/media/readme/light-add-ing-mobile.png)
![Add Menu Desktop Lighthouse](/static/media/readme/light-add-menu-desktop.png)
![Add Menu Mobile Lighthouse](/static/media/readme/light-add-menu-mobile.png)
![Manage Ingredient Desktop Lighthouse](/static/media/readme/light-manage-ing-desktop.png)
![Manage Ingredient Mobile Lighthouse](/static/media/readme/light-manage-ing-mobile.png)
![Manage Menu Desktop Lighthouse](/static/media/readme/light-manage-menu-desktop.png)
![Manage Menu Mobile Lighthouse](/static/media/readme/light-manage-menu-mobile.png)
</details>