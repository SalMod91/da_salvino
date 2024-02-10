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

## UX

### Scope & Strategy
<details>
<summary>Click to expand</summary>


#### Project Purpose
The "Da Salvino" website aims to provide users with a comprehensive view of the restaurant, from essential details like location, opening times, and contact information to a deeper understanding of our identity and culinary offerings. It showcases our menu in an interactive manner, allowing users to explore each dish and its ingredients with just a click. This feature opens a new page for each ingredient, where users can learn about its description and origin, emphasizing our commitment to transparency and quality. Through this platform, we strive to inform and engage our customers, ensuring they have all the information they need about the high standards and authenticity of the ingredients used in our kitchen.

#### Project Goal
Build a website that offers clients an intuitive and informative browsing experience while providing a seamless backend experience for the staff managing the menu and updating ingredient information.

#### Audience
Those who cherish an authentic Italian dining experience, particularly enthusiasts of traditional Italian-style pizza making. This audience includes not just aficionados of genuine Italian cuisine seeking the nuanced flavors of Italy but also health-conscious individuals who value the quality and sourcing of ingredients that go into traditional pizza.

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
- To be able to be informed about the favorite menu items.
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

Explore the User Stories and todo issues by navigating to the GitHub Projects page through this [link](https://github.com/users/SalMod91/projects/7).
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
Withing the Staff Portal there are 4 additional pages only accessible post-login by approved staff users.
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
- The Home Page initially included a "Most Liked Dishes" feature, which would showcase a scrolling list of user favorites. This idea was set aside because the functionality to "like" a dish has not yet been introduced.

- The initial design intended for a reversed row layout on the ingredient page. This concept was reconsidered to achieve a more visually comfortable and straightforward presentation for users.

- Staff Portal was developed after the initial ideas, onsequently, there were no original wireframes for this feature.

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
Upon falling in love with a dark chalkboard background found on Canva, i decided to center the font color scheme around it, opting for white text to ensure strong contrast and readability against the dark background. This choice was made to guarantee that the text stands out clearly and is easily readable.

#FFB018 has been chosen purely for nostalgic reasons, as it was also used in my first project and first time writing code completely indepedent ever. Although the choice is nostalgic, it still offers good visibility against a dark background, ensuring interactive elements and interactive feedback are easily recognizable.

![Colour Palette](/static/media/readme/colour-palette.png)

#### Typography
During the process of exploring Google Fonts for the website, I also considered the importance of a reliable fallback font. Initially, i chose Times New Roman to take on the job as a fallback font and upon implementation it became clear to me that this classic font also perfectly complements the website's theme. Its professional appearance aligns with the operational needs of the staff portal, while its timeless elegance enhances the overall layout of the website, marrying functionality with style.

While a different font for the headings could have added further distinction to the website's design, I ultimately chose to maintain consistency by using the same font throughout.
</details>

### Database Structure
