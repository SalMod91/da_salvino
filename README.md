## Introduction

"Da Salvino" is a full-stack website for a fictional pizzeria, designed to facilitate the management of ingredients and pizzas by staff users. These items are dynamically updated on the website, allowing visitors to view the latest menu and ingredients.

Staff functionalities, including adding and managing ingredients and pizzas, are restricted to registered staff users through a hidden staff portal. Registrations require admin approval to ensure secure management access.

Intended for real-life application, the website plans to expand with features like booking, customer reviews, and favourites to enhance user engagement and operational efficiency.

The website is live [HERE](https://da-salvino-0dcb8f7f1479.herokuapp.com/)

![Responsive Screenshot](/static/media/readme/responsive-screenshot.png)

## Content Table
- [Introduction](#introduction)
- [UX](#ux)
    - [Scope & Strategy](#scope--strategy)
        - [Project Purpose](#project-purpose)
        - [Project Goal](#project-goal)
        - [Audience](#audience)
        - [Communication](#communication)
        - [Current User Goals](#current-user-goals)
        - [New User Goals](#new-user-goals)
        - [Future User Goals](#future-user-goals)
        - [User Stories](#user-stories)
    - [Structure](#structure)
        - [Public Facing Pages](#public-facing-pages)
        - [Staff Portal](#staff-portal)
        - [Staff Portal Pages](#staff-portal-pages)
        - [Site Flow](#site-flow)
    - [Skeleton](#skeleton)
        - [Wireframes & Design Evolution](#wireframes-and-design-evolution)
    - [Surface](#surface)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
- [Database Structure](#database-structure)
- [Agile Development](#agile-development)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Navigation](#navigation)
        - [Authentication](#authentication)
        - [CRUD](#crud)
        - [User Feedback System](#user-feedback-system)
        - [General Pages](#general-pages)
    - [Future Features](#future-features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
    - [Main Languages Used](#main-languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
    - [Installed Packages](#installed-packages)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)

## UX

### Scope & Strategy
<details>
<summary>Click to expand</summary>


#### Project Purpose
The "Da Salvino" website aims to provide users with a comprehensive view of the restaurant, from essential details like location, opening times, and contact information to a deeper understanding of our identity and culinary offerings. It showcases our menu in an interactive manner, allowing users to explore each dish and its ingredients with just a click.<br> This feature opens a new page for each ingredient, where users can learn about its description and origin, emphasizing our commitment to transparency and quality.<br> Through this platform, we strive to inform and engage our customers, ensuring they have all the information they need about the high standards and authenticity of the ingredients used in our kitchen.

#### Project Goal
Build a website that offers clients an intuitive and informative browsing experience while providing a seamless backend experience for the staff managing the menu and updating ingredient information.

#### Audience
Those who cherish an authentic Italian dining experience, particularly enthusiasts of traditional Italian-style pizza making. This audience includes not just aficionados of genuine Italian cuisine seeking the nuanced flavours of Italy but also health-conscious individuals who value the quality and sourcing of ingredients that go into traditional pizza.

#### Communication
The website is structured in a way to ensure, upon arrival, that users are greeted with a clear and accessible overview of what the site has to offer, without feeling overwhelmed by too much information. The homepage effectively summarizes the key sections and potential reasons for your visit, allowing for a seamless navigation experience from the start.

#### Current User Goals
- For the visitors to keep being updated about the menu items.
- Providing the staff users with a user-friendly interface for updating menu and ingredients.

#### New user Goals
- To navigate the site with ease and clearly understand the information provided.
- To inform new user about the location and contact information.
- To inform new user about the theme of the restaurant.
- To introduce new users to the social media platforms.

#### Future User Goals
- To be able to provide and read reviews.
- To be able to provide and read meal specific reviews.
- To be able to be informed about the favourite menu items.
- To be able to place orders online.
- To be able to book a table.
- To be able to subscribe to a newsletters.
- To be able to participate to loyalty activities.

#### User Stories
| Epic       |                                                          User Story                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Navigation |                                                                                                                                                              |
|            | As a visitor/user, I'd like to be able to have a navigation bar so that I can navigate through the website.                                                  |
|            | As a visitor/user, I want to easily understand which page I find myself on at any moment while navigating the website.                                       |
|            | As a visitor/user, I want to find links to the restaurant's social media so that I can follow them etc.                                                      |
|            | As a visitor/user, I want the website to have an intuitive design to make navigating easier                                                                  |
|            | As a visitor/user, I want to find links to the restaurant's social media so that I can follow them etc.                                                      |
| Home Page  |                                                                                                                                                              |
|            | As a visitor/user, I want to visit the homepage of the pizzeria website so that I can learn about the restaurant's information.                              |
|            | As a visitor/user, I want to access the menu page from the homepage so that I can view the different categories of items available.                          |
|            | As a visitor/user, I want to be able to see the opening times of the restaurant so that I can plan my visit or order accordingly.                            |
|            | As a visitor/user, I want to be able to get information about the restaurant (phone, address) so that I can easily make inquiries or find the location of the restaurant.                                                                                                                                                                 |
| Menu Page  |                                                                                                                                                              |
|            | As a visitor/user, I want to be shown menu categories in an organized manner so that the menu will be easy to see and understand.                            |
|            | As a user/visitor, I want an "All Menu" category option available so that I can have an overview of everything the restaurant has to offer in one glance.    |
|            | As a visitor/user, I want to be shown menu categories in an organized manner so that the menu will be easy to see and understand.                            |
|            | As a visitor/user, I want to see photos of the menu items alongside their descriptions so that I can visually assess the dishes before making a decision.    |
|            | As a visitor/user, I want to easily reach the ingredient I am interested in without having to search for it, so that I can quickly find detailed information about it.                                                                                                                                                                   |
| Ingredients Page  |                                                                                                                                                       |
|            | As a visitor/user, I want to view the list of ingredients to learn more about it so that I can make better informed choices.                                 |
| Admin      |                                                                                                                                                              |
|            | As an admin, I want a clear separation between staff and normal users to ensure that administrative and operational functionalities are securely managed and accessible only to authorized personnel. |
|            | As an admin, I want my registered staff to be first approved by me, so that i can ensure only authorized personell can perform sensitive operations.         |
|            | As an admin, I want to be able to manage user roles and permissions to ensure that each staff member has access only to the functionalities necessary for their role.        |
|            | As an admin, I want to add new ingredient categories and delete existing ones to maintain a well-organized and relevant categorization system.               |
| Staff      |                                                                                                                                                              |
|            | As a staff member, I want to have the possibility to change my password whenever needed to maintain control over my personal information.                                                                                                                                                                |
|            | As a staff user, I want to receive a clear message that I am logged in, to confirm my access.                                                                |
|            | As a staff user, I want to always have the option to log out of the staff portal easily, to ensure my account's security and privacy when I'm not using it.  |
|            | As a staff user, I want a convenient way to navigate through the different operations I can perform within the staff portal, to improve my efficiency and effectiveness in completing my tasks.                                                                                                                                       |
|            | As a staff user, I want immediate feedback whenever I perform an action within the staff portal, such as adding or editing menu items or ingredients, to ensure that my changes have been successfully applied and to enhance my workflow efficiency.                                                                                       |
|            | As a staff user, I want to always have the option to log out of the staff portal easily, to ensure my account's security and privacy when I'm not using it, to easily navigate and ensure I am working on the correct task without confusion.                                                                                              |
|            | As a staff user, I want the details to be prefilled when editing an ingredient or menu item as it makes my job easier by allowing me to quickly identify and modify only the necessary information.                                                                                                                                      |
|            | As a staff user, I want to be automatically logged out of the staff portal if I leave my account inactive for a certain period, to safeguard my account against unauthorized access and maintain security. |

Explore the User Stories and to-do issues by navigating to the GitHub Projects page through this [link](https://github.com/users/SalMod91/projects/7).
</details>

### Structure
<details>
<summary>Click to expand</summary>

#### Public Facing Pages
- Homepage: Serves as the landing page for all visitors, providing general information about the restaurant, links to the menu, ingredients pages, and for logged in staff users, access to the staff portal.

- Menu Page: Showcases the restaurant's menu items iterating through the menu items model, with features allowing users to click on items for more details.

- Ingredients Page: Offers detailed information about the ingredients used in the menu items, emphasizing quality and sourcing.

#### Staff Portal
- The Staff Portal is accessed by appending /staff_portal to the website's base URL or through a bookmark, in order to limit the access to the public. 
- Within the Staff Portal, functionality is restricted to approved staff users, requiring login authentication and user role validation.
- Register,Login, Password modification and Logout are all handled through different modals, avoiding the need to have specific pages for these actions.

#### Staff Portal Pages
Within the Staff Portal there are 4 additional pages only accessible post-login by approved staff users.
- Add Ingredient: Allows staff to input new ingredients into the database.
- Manage Ingredients: Provides functionality to edit and delete ingredient entries.
- Add Menu Items: Enables staff to introduce new dishes or offerings to the menu. For now restricted only to Pizzas.
- Manage Menu Items: Allows for the editing and deletion of menu items, similar to ingredient management.

The Staff Portal has been planned for a future visitor user login capability.
If the visitor users may happen in the future to land inside the Staff Portal they will be prompted to head back to the Home Page.

#### Site Flow
![Flowchart Screenshot](/static/media/readme/structure-flowchart.png)
</details>

### Skeleton
<details>
<summary>Click to expand</summary>

#### Wireframes and Design Evolution
The development of the website underwent significant modifications from the initial wireframes to the completed product, most notably:
- The Home Page initially included a "Most Liked Dishes" feature, which would showcase a scrolling list of user favourites. This idea was set aside because the functionality to "like" a dish has not yet been introduced.

- The initial design intended for a reversed row layout on the ingredient page. This concept was reconsidered to achieve a more visually comfortable and straightforward presentation for users.

- Staff Portal was developed after the initial ideas, consequently, there were no original wireframes for this feature.

    - Mobile Home Page

        ![Mobile Home Wireframe](/static/media/readme/wireframe-home-mobile.png)

    - Desktop Home Page

        ![Mobile Home Wireframe](/static/media/readme/wireframe-home.png)

    - Mobile Menu/Ingredient Page

        ![Mobile Home Wireframe](/static/media/readme/wireframe-menu-mobile.png)

    - Desktop Menu Page

        ![Mobile Home Wireframe](/static/media/readme/wireframe-menu.png)

    - Desktop Ingredient Page

        ![Mobile Home Wireframe](/static/media/readme/wireframe-ingredients.png)
</details>

### Surface
<details>
<summary>Click to expand</summary>

#### Colour Scheme
Upon falling in love with a dark chalkboard background found on Canva, i decided to centre the font colour scheme around it, opting for white text to ensure strong contrast and readability against the dark background. This choice was made to guarantee that the text stands out clearly and is easily readable.

#FFB018 has been chosen purely for nostalgic reasons, as it was also used in my first project and first time writing code completely independent ever. Although the choice is nostalgic, it still offers good visibility against a dark background, ensuring interactive elements and interactive feedback are easily recognizable.

![Colour Palette](/static/media/readme/colour-palette.png)

#### Typography
During the process of exploring Google Fonts for the website, I also considered the importance of a reliable fallback font. Initially, i chose Times New Roman to take on the job as a fallback font and upon implementation it became clear to me that this classic font also perfectly complements the website's theme. Its professional appearance aligns with the operational needs of the staff portal, while its timeless elegance enhances the overall layout of the website, marrying functionality with style.

While a different font for the headings could have added further distinction to the website's design, I ultimately chose to maintain consistency by using the same font throughout.
</details>

## Database Structure
<details>
<summary>Click to expand</summary>

This ERD represents the database schema for the  application.

- Custom Staff User

    The Django User Model has been customized to "Custom Staff User".

    Only usernames are required for staff logins, while an admin-granted approval status is necessary for operational access.

    The staff portal is fortified with a security measure requiring admin approval for new registrations. This ensures that even if visitors accidentally find their way to the staff portal and register, they must be authorized by an admin to gain access.

- Ingredient Categories

    Ingredient categories are exclusively managed by the admin, with the ability to create, modify, and delete them. Any deletion of a category will result in the removal of all associated ingredients, demonstrating a cascading delete functionality.

- Ingredients

    Staff users have the authority to create ingredients, which are then utilized in menu items and displayed on the ingredients page. A default image is assigned in the absence of an uploaded image. Uploaded images are named using the ingredient's ID for consistency and to streamline management. To prevent cloud storage clutter, replacing an image results in the original being overwritten. Additionally, deleting an ingredient will also remove its associated image.

- Pizza Menu Item

    Staff users have also the authority to create pizza menu items with two predefined boolean fields: 'has tomato' and 'has mozzarella'. This design choice simplifies the process by providing quick access to these staple ingredients, eliminating the need to select them from a list each time. Other ingredients can be added as needed from the created selection. Image management for pizza menu items mirrors that of ingredients, with the same naming conventions and overwrite protocols to ensure efficient use of cloud storage.


![Database ERD](/static/media/readme/database-erd.png)
</details>

## Agile Development
Throughout the development of the project, a physical Kanban board served as the primary tool for tracking progress due to initial insecurities about using GitHub issues.

As the README was compiled my familiarity with GitHub's project management grew, revealing the platform's ease of use, which in hindsight could have proven useful.

User Stories were retrospectively documented within GitHub project.

Despite the traditional approach with a physical Kanban board and post-its, Agile principles were upheld, including the assignment of MoSCoW priorities to focus on delivering a minimum viable product (MVP) in the time given.

<details>
<summary>Sprint Details</summary>

- Sprint 1 - Planning and Initial Setup<br>
The initial phase of development focused on laying the foundational elements of the project.

    
    - Initial Sketches <br>
        Created wireframes and database designs to establish the visual layout and data structure.

    - Environment Setup <br>
        Configured the development environment using Gitpod, integrating Django as the web framework, PostgreSQL for database management, and Cloudinary for image storage solutions.

    - Deployment <br>
        Deployed the initial build on Heroku.

- Sprint 2 - Navigation and Page Content<br>
    This sprint established the core navigational and content framework of the website.<br>
    The focus was on structuring the website for ease of navigation and preparing content placeholders. <br>

    - Navigation Bar <br>
        Implemented a navigation bar to guide users through the website,  with attention to ensuring its adaptability across various devices and screen sizes.

    - Footer <br>
        Added a footer section, providing additional information and navigation options, adaptability across various devices and screen sizes partly handled but not optimized.

    - Home Page Content <br>
        Drafted initial content for the home page to welcome users.
    
    - Menu Page <br>
        Developed the menu page with temporary content to layout the structure for future menu items.
    
    - Ingredients Page <br>
        Developed the ingredients page with temporary content to layout the structure for future ingredients.

- Sprint 3 - User Management and Authentication<br>

    Facing the inevitable, this sprint marked the initial dive into the database, a step i could no longer postpone as the project's further development depended on it.<br>

    Given the database structure, it became essential to establish a user management system first, as it laid the foundation of the operational processes.<br>
    
    - Custom Staff User Model <br>
        Developed to tailor user authentication and roles, specifically catering to staff functionalities.

    - User Authentication <br>
        Integrated Django's allauth library to manage user authentication processes, including login, registration, and password management.

    - Interactive Forms and Modals <br>
        Implemented forms and views for user login and registration, alongside modals for login, logout, and password modification, enhancing user interaction.

- Sprint 4 -  Ingredient Model and Addition Functionality<br>
This sprint focused on establishing the ingredient component of the database.<br>
This phase was instrumental in enhancing the site's capability to catalogue and manage ingredients efficiently, setting the groundwork for menu item development.

    - Ingredient Model <br>
        Introduced the initial ingredient model along with necessary views and forms.
    
    - Add Ingredient Page <br>
        Developed a dedicated page for adding ingredients, incorporating error management to ensure smooth and accurate ingredient submissions.

- Sprint 5 - Managing Ingredients<br>
The fifth sprint advanced the ingredient management system by introducing functionalities for reading, modifying, and efficiently handling ingredient data.
This sprint significantly improved the backend's usability, making ingredient management more accessible and error-resistant.
    
    - Ingredient Management Page <br>
        Implemented a page for overseeing the existing ingredients, allowing for editing and deletion.
    
    - Ingredient-Specific Modals <br>
        Introduced modals that open for each ingredient, facilitating detailed viewing and editing directly from the management page.
    
    - Confirmation Modals <br>
        Added confirmation prompts for ingredient deletion.

- Sprint 6 - Pizza Model and Addition Functionality <br>
The final requirement for the planned MVP, the addition of the menu item. <br>
This sprint added to the website a menu addition ability, enabling a versatile and user-friendly interface for adding pizza items to the menu.

    - Pizza Model Implementation <br>
        Developed the pizza model to encapsulate all necessary data attributes, including ingredient selections and boolean fields for common toppings like tomato and mozzarella.
    
    - Add Pizza Page <br>
        Introduced a dedicated page for adding pizza items to the menu, complete with views and forms tailored to the process.
    
    - Ingredient Selectors <br>
        Integrated ingredient selectors, allowing staff to dynamically read from the existing ingredients model and incorporating it into the new menu item.

- Sprint 7 - Managing Pizza Menu Items <br>
Sprint 7 focused on the management of pizza menu items, introducing comprehensive editing and deletion capabilities.
This sprint significantly improved the backend interface for pizza menu management, making the process of editing and deleting items more intuitive and error-proof.

    - Edit Menu Page <br>
        A new page was added to facilitate the editing of existing pizza menu items, complete with associated views and URLs for seamless navigation and functionality.
    
    - Edit Functionality <br>
        Implemented the ability for staff to modify details of pizza menu items.
    
    - Delete Functionality <br>
        Introduced a delete option for pizza menu items.
    
    - Menu Item and Deletion Modals <br>
        Similar to ingredient management, modals were added for each pizza item to facilitate editing, and confirmation modals were implemented for deletions to prevent accidental loss.
    
    - JavaScript Enhancements <br>
        Developed JavaScript functionality to re-open modals upon submission failure, ensuring that users can correct errors without losing their progress or having to restart the process.

- Sprint 8 - Finalizing Ingredients Page <br>
Focused on finalizing the ingredients page, removing the temporary content and adding the dynamic rendering of the page showcasing the ingredients in the database.

    - Dynamic Rendering <br>
        Implemented a dynamic rendering system on the ingredients page, allowing for the display of each ingredient from the model. This ensures that all current ingredients are visible to users, reflecting real-time updates.
    
    - Categorization and Tabs <br>
        Ingredients organized in tabs according to their categories, making navigation and exploration of different types of ingredients more intuitive and user-friendly.

- Sprint 9 - Finalizing Menu Page <br>
This sprint was dedicated to enhancing the menu page, paralleling the dynamic and interactive functionalities established in the ingredients management system. <br>
Furthermore improved the ingredients management system by mirroring the menu management system.

    - Dynamic Menu Rendering <br>
        Adopted a dynamic rendering approach for the menu page, ensuring that all menu items are displayed directly from the model. This allows for real-time reflection of the menu offerings.
    
    - JavaScript Enhancements <br>
        Applied the JavaScript functionality of the menu management to the ingredient management, mirroring the process to maintain a consistent user experience and reduce frustration during data entry corrections.
    
    - Ingredient Links <br>
        Added hyperlinks to the ingredients listed in menu items, connecting users to the detailed ingredients page.

- Sprint 10 - Enhancing Responsiveness<br>
In Sprint 10, the project's focus shifted towards optimizing the website's responsiveness of all elements, ensuring a seamless and accessible experience across all devices.

    - Responsiveness Optimization <br>
        Implemented CSS adjustments to enhance the responsiveness of all web pages.

- Sprint 11 - Testing <br>
This sprint marked a critical phase of thorough testing and refinement, focusing on ensuring every aspect of the website operates seamlessly

    - Functionality Testing <br>
        Conducted extensive tests on all website functionalities, including navigation, links on the home page, menu, ingredients, and the staff portal.
    
    - CRUD Operations <br>
        Verified the creation, reading, updating, and deletion (CRUD) processes for ingredients and menu items.
    
    - User Authentication Tests <br>
        Tested user registration, login, and password modification processes.
</details>


## Features

### Existing Features

### Navigation
<details>
<summary>Click to expand</summary>

### Header:
The navigation bar includes the site's logo, which doubles as a link to the home page.<br>

Direct Links to the Home, Menu and Ingredients page are prominently displayed, ensuring users can easily navigate these key sections.<br>

The navigation dynamically assigns an "active" class to the link corresponding to the current page, based on the URL request path.<br>
This visual cue helps users identify which page they are viewing.<br>

For Staff Users that are logged in, an additional link to the Staff Portal appears.<br>
This link features a split button that, upon hover, reveals four links dedicated to operational services: Add Ingredient, Manage Ingredients, Add Menu Item and Manage Menu Items.

![Navigation](/static/media/readme/navigation-bar.png)
![Navigation Portal Links](/static/media/readme/staff-portal-links.png)

When a user navigates to one of the four links within the staff portal dropdown menu, the button used to open the dropdown menu is also marked with an active status. This feature signals to the user that they are currently engaged with the staff portal section.


![Navigation Staff Portal](/static/media/readme/navigation.png)
![Navigation Staff Portal Link](/static/media/readme/navigation-staff.png)

On smaller screens, the navigation bar collapses into a hamburger menu, maintaining accessibility and user experience across devices.

![Collapsed Navigation](/static/media/readme/navigation-mobile.png)

### Footer:
The footer of the website is designed to provide essential contact information and encourage user interaction.

- Contact Information:

    Features a phone number with a playful wiggle animation on hover, simulating a ringing phone.

- Address Section:

    Includes a location detail that, when hovered over, enlarges to signify interactivity. Clicking on it directs users to a Google Maps link for the restaurant's address.

- Opening times:
    
    Clearly displays the restaurant's hours of operation for user convenience.

- Social Media Links

    A set of social media icons that connects users to the restaurant's social platforms.

![Footer](/static/media/readme/footer.png)
</details>

### Authentication
<details>
<summary>Click to expand</summary>

Within the staff portal, authentication is tailored to ensure secure and efficient access to CRUD functionalities. Staff users can log in to engage with the system, while new staff registrations require admin approval. This approval process is crucial to prevent unauthorized access by visitors who might discover the staff portal. Additionally, to enhance security, an automatic logout feature triggers after 3 minutes of inactivity, redirecting users back to the staff portal login page.

### Staff Portal:

Upon entering the Staff Portal, users are greeted with a prompt to log in or register. Selecting this option activates a modal window with a tabbed interface, allowing for a seamless transition between login and registration forms. This design choice streamlines the authentication process, eliminating the need for separate pages and ensuring a quick, user-friendly experience.

If submission of the modal encounters errors, the page will reload and the modal will automatically reopen to the tab where the issue occurred. Error messages will be displayed to inform the user of the specific problem, guiding them to correct the information and successfully complete the authentication process.


![Staff Portal](/static/media/readme/staff-portal-notloggedin.png)
![Login Modal](/static/media/readme/login-modal.png) ![Register Modal](/static/media/readme/register-modal.png)
![Errors Login](/static/media/readme/login%20errors.png)

Upon logging in, users are welcomed by a personalized message acknowledging their access.<br>
To elevate user convenience, options to modify the password or log out are integrated within the interface through modals, eliminating the disruption of page redirections.<br>
Should there be any errors in the submission, the modal will reappear with highlighted errors for correction.


![Logged in as](/static/media/readme/logged-in-as.png)
![Modify Password](/static/media/readme/modify-password.png)
![Logout Modal](/static/media/readme/logout.png)
</details>

### CRUD
<details>
<summary>Click to expand</summary>

Within the staff portal, logged-in staff members have access to various operational functionalities.

![Staff Portal Logged In](/static/media/readme/staff-portal-loggedin.png)

### Add Ingredient Page / Add Menu Item:

The Add Ingredient and Add Menu Item pages feature a form that leverages Django's capabilities to auto-generate fields.<br>
This leaves the layout somewhat utilitarian.<br>

To enhance user experience and interface design, future forms have been personally customized, moving away from the auto-generated approach.


- Create New Ingredient Entries:<br>
    Input the ingredient's name, assign it to a category, and add descriptions and origin details.

- Image Upload:<br>
    There's an option to upload an image for the ingredient or the menu item. If no image is uploaded, a default one is used.

- Image File Naming and Management: <br>
     Uploaded images are automatically named using a standard format that includes the ingredient's unique ID (e.g., ingredient_ID). Should an image be updated, the new file replaces the previous one, ensuring the storage remains uncluttered. Similarly, if an ingredient is deleted from the database, its associated image is also removed, keeping the system efficient and organized.

- Error Handling:<br>
    In the event of an error during  submission, such as uploading a non-image file, the page will refresh, displaying a specific error message next to the relevant field to inform the user of the exact issue that needs resolution.

![Add Ingredients Page](/static/media/readme/add-ingredient-page.png)
![Add Ingredient Error](/static/media/readme/add-ingredient-error.png)

The 'Add New Menu Item' page is currently tailored for pizza creations, with plans to expand for additional items like salads and pasta.

- Essential Ingredients Toggle:<br>
    Staff can quickly indicate whether a pizza includes common ingredients like tomato sauce and mozzarella with a simple yes/no toggle.

- Image Upload:<br>
    The image upload functionality mirrors that of the 'Add Ingredient' feature, maintaining consistency across the platform.

- Dynamic Ingredient Selector:<br>
    An 'Add Ingredient' button initiates a selector, bringing up a list of ingredient categories from the database. Ingredients within these categories are displayed in alphabetical order for easy selection, with an option to remove the selector if needed. If an ingredient selector is activated but not specified upon submission, it will not be added to the database.

![Menu Item Page](/static/media/readme/add-new-menu-item.png)
![Ingredient Selector](/static/media/readme/ingredient-selector.png)
![Ingredient Selector 2](/static/media/readme/ingredient-selector-2.png)

### Manage Ingredients/Menu Items:

Both the ingredient and menu item management pages share a virtually identical design, with tailored differences in the iteration of model instances.

Moving away from the Django auto-generated forms used initially, these pages feature customized forms, resulting in a more aesthetically pleasing interface. This customization has allowed for a more engaging and visually coherent presentation compared to the standard Django form layout.

- Database Iteration:<br>
    The ingredients page categorizes items, listing them alphabetically within each category, while menu items are currently listed alphabetically and will be categorized in future updates.

- Edit & Delete Functions:<br>
    Both pages feature edit and delete buttons next to each item. The delete button triggers a confirmation modal to prevent accidental deletions. The edit button opens a modal containing a form pre-filled with the item's current details, allowing staff to see and modify information directly.

- Custom Form Design:<br>
    Unlike the auto-generated Django forms, these edit forms have been personally customized for better aesthetics and usability.

- Image Handling: <br>
    The edit form includes an image preview  which uses the URL from Cloudinary. Users have the option to remove the image, which also deletes it from cloud storage.

- Error Handling:<br>
    If form submission fails, the page reloads with the modal open and an error message displayed next to the problematic field, guiding the user to resolve the specific issue.

![Manage Ingredients Page](/static/media/readme/manage-ingredients-page.png)
![Manage Menu Item Page](/static/media/readme/manage-menu-item-page.png)
![Edit Ingredient Modal](/static/media/readme/edit-ingredient-modal.png)
![Edit Menu Item Modal](/static/media/readme/edit-menu-modal.png)
![Delete Modal](/static/media/readme/deletion-modal.png)
</details>

### User Feedback System
<details>
<summary>Click to expand</summary>

The website is designed with a comprehensive feedback system that acknowledges every user action. Whether it’s logging in, registering, changing passwords, logging out, or performing database operations such as adding, modifying, or deleting instances, users receive immediate feedback. This ensures users are always informed of the success or need for attention of their recent action, enhancing the interactivity and responsiveness of the user experience.

In future updates a distinction between positive and negative messages will be included.

When logging in and logging out:

![Login Feedback](/static/media/readme/login-confirmation.png)
![Logout Feedback](/static/media/readme/logout-feedback.png)

When trying to login with an account that has not been approved by the Admin:

![Pending Approval](/static/media/readme/approval-pending.png)

When creating and deleting an Item:

![Creation Feedback](/static/media/readme/creation-confirmation.png)
![Deletion Feedback](/static/media/readme/delete-feedback.png)

When the edit submission raises an error:

![Error Update Feedback](/static/media/readme/error-edit-feedback.png)
</details>

### General Pages
<details>
<summary>Click to expand</summary>

### Home Page:
The home page thoughtfully combines elements traditionally found on separate "About Us" and "Location" pages to streamline the user experience and reduce the number of navigational elements. <br>It features a concise description of the restaurant alongside a photo of the interior, providing visitors with a warm introduction.<br> Additionally, a clickable map icon is incorporated, which opens a Google Maps link to the restaurant's location, offering users an intuitive way to find us without navigating away from the home page.
![Home Page](/static/media/readme/homepage-1.png)
![Home Page 2](/static/media/readme/homepage-2.png)

### Menu Page:
The menu page dynamically renders an alphabetical list of menu items directly from the pizza model. Each ingredient associated with a menu item acts as a hyperlink, opening the detailed ingredient information in a new tab on the ingredients page. This real-time update feature ensures that the menu is always current and provides users with a seamless and informative browsing experience.

The Menu Page also features a tabbed interface with categories such as "All", "Pizza", "Salads", and "Desserts". The "All" tab gets populated with items from all categories thanks to use of JavaScript.

![Menu Page](/static/media/readme/menu-page.png)

### Ingredients Page:

Mirroring the functionality of the menu page, the ingredients page is dynamically rendered using the ingredient models. It features a tab layout that organizes content by category. These categories are filled by iterating through the 'Ingredient Category' model, with the display order determined by an 'order' attribute assigned by the admin. Categories with a lower 'order' value are presented first, allowing for a custom, prioritized arrangement of ingredient listings.

![Ingredients Page](/static/media/readme/ingredients-page.png)

### Staff Portal:

The Staff Portal serves as a dedicated access point for staff members to log in and manage their tasks. It ensures secure and exclusive access, keeping it off-limits to general visitors. To maintain confidentiality and security, the portal is deliberately made less accessible.

- Visibility: <br>
    The link to the Staff Portal appears in the navigation menu solely for logged-in staff members, ensuring it remains invisible to unauthorized users.

- Access:<br>
    Staff members can navigate to the Staff Portal by appending staff_portal/ to the website's base URL. For convenience and faster access, it's highly recommended that staff users bookmark this page.

![Staff Portal Page](/static/media/readme/staff-portal.png)
### Error Pages:

During the testing phase of this project's features, I frequently encountered errors 403 and 500. Given their prevalence, alongside the well-known 404 error, I was inspired to create custom error pages for these specific situations. The design of these pages is closely aligned, with the primary distinction being the specific error number displayed. 

![Error 404](/static/media/readme/404.png)
</details>

### Future Features
- Visitor Login/Registration
- Visitor Reviews
- Visitor ability to like meals and review individual meals
- Visitor able to make a reservation
- Allergen information in the menu/ingredients page
- Special offers for loyal customers
- Real-time Sales and Inventory for the Admin
- Ability to respond to customer feedback
- Staff User work schedule

## Testing
Testing has been documented in [TESTING.md](/TESTING.md)

## Technologies Used

### Main Languages Used
- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- Font Awesome - Used for the icons in the navigation bar and the footer.
- GitPod - Used as IDE for writing and editing the project.
- GitHub - Used for version control and repository hosting.
- ElephantSQL - Used to host PostgreSQL Database.
- Cloudinary - Used to store image files.
- Heroku - Used for deploying the project.
- Balsamiq - Used to create wireframes.
- Am I Responsive? - Used to ensure the project is responsive.
- Favicon.io - Used to convert png to ico.
- Lucidchart - Used to create Site Flow and ERD.
- DALL-E - Used for generation of images.
- Lighthouse - Used to test performances.
- Wave - Used to evaluate the site's accessibility.
- TinyPNG - Used for compressing PNG.
- JsHint - Used for validating the JS code.
- W3C HTML Validator - Used for validating the HTML code.
- Jigsaw CSS Validator - Used for validating the CSS code.
- CI Python linter - Used for validating the Python code.
- Django
- Bootstrap - Used for styling.

### Installed Packages:
- asgiref
- cloudinary
- dj-database-url
- dj3-cloudinary-storage
- Django
- django-allauth
- gunicorn
- oauthlib
- psycopg2
- PyJWT
- python3-openid
- sqlparse

## Deployment

The site was deployed to Heroku. The steps to deploy were as follows:

1. Used pip3 to install gunicorn, cloudinary and psycopg2 through the terminal
2. Updated the requirements.txt using the command pip3 freeze > requirements
3. Created a Procfile and added the line web: gunicorn name_of_your_app.wsgi
4. Navigated to [Heroku Link](https://www.heroku.com/)
5. Created a new App
6. Navigated to Settings Tab and added the key/value pairs to the Config Vars

    - SECRET_KEY - Your Secret Key
    - DATABASE_URL - Your Database URL
    - CLOUDINARY_URL - Your Cloudinary URL
7. Added Python to Buildpacks.
8. Added the secret key, cloudinary and database URL to env.py
9. Added the secret key, cloudinary and database URL to settings.py
10. Added Heroku as allowed host in settings.py
11. Connected my GitHub account to heroku to facilitate the automatic Deployment whenever pushed
12. Chose the main branch for deploying and enabled the automatic deployment

## Credits
### Content
How to save a m2m model: [Stackoverflow](https://stackoverflow.com/questions/5612991/saving-many-to-many-data-via-a-modelform-in-django)

How to iterate through a model using "context": [Copyprogramming](https://copyprogramming.com/howto/python-loop-through-objects-django-template-code-example)

How to use window.location.hash: [Educative](https://www.educative.io/answers/what-is-windowlocationhash-in-javascript)

Button animation in the Home Page: [Lambdatest](https://www.lambdatest.com/blog/best-css-button-hover-effects/)

How to logout inactive user: [Medium](https://medium.com/@m.ambenge01/implementing-user-inactivity-logout-in-django-a020f6ebeb27)

Testing Table - Testing table layout inspired by my mentor [Lauren](https://github.com/CluelessBiker)

### Media
Logo and favicon - [Link](https://www.flaticon.com/free-icon/pizza_1404945)

Error 404 page - [Link](https://frontendshape.com/post/bootstrap-5-404-page-examples)

Chalky Background - [Pixabay](https://pixabay.com/photos/black-board-traces-of-chalk-school-1072366/)

Wooden Boards Background - [Pixabay](https://www.pexels.com/photo/macro-shot-of-wooden-planks-326333/)

Waiter Image - [Thenounproject](https://thenounproject.com/icon/waiter-382671/)

Wood Oven - Photo of the Restaurant of my Father, used with his permission [Restaurant](https://www.google.com/maps/place/Pizzeria+Restaurant+Schwert/@47.5142396,7.86384,11.75z/data=!4m6!3m5!1s0x479049c95df512a1:0x2bbf51aabcbb664d!8m2!3d47.5142102!4d7.9672351!16s%2Fg%2F11c1xhlxp0?entry=ttu)

Every other Image file has been generated by AI [DALL-E](https://openai.com/dall-e-2)