# **Clare Golf Store**

![Amiresponsive image](media/amiresponsive.png)

For my final portfolio project, I chose to create Clare Golf Store as a mix of two of my greatest passions: golf andmy new found one coding. Having played golf since a young age, I have always been captivated by the sport. This lifelong enthusiasm for golf naturally sparked the idea of a specialized store that caters to golfers’ needs, from beginners to seasoned players. Recently, I discovered a new passion for coding, enthralled by the creative and problem-solving aspects it involves. Merging these interests, Clare Golf Store became the perfect project to not only showcase my technical skills in web development but also to create a platform that resonates with my deep-seated love for golf. This project represents a harmonious blend of my personal interests and professional growth, aiming to provide a seamless and engaging online shopping experience for golf enthusiasts.
I have learned so much and come so far in the last year of coding and I'm proud to show what I can create.

View the deployed website [here](https://clare-golf-store-e14c88b1e5dd.herokuapp.com/).(Right click to open in new tab!)

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [Agile planning](#agile-planning)
        3. [Goals Table](#goals-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Marketing](#marketing)
   1. [Search Engine Optimisation](#search-engine-optimisation)
   2. [Business Model](#business-model)
3. [Features](#features)
   1. [General](#general)
   2. [Home Page](#home-page)
   3. [Products Page](#products-page)
   4. [Product Details Page](#product-details-page)
   5. [Products Admin](#products-admin)
   5. [Shopping Bag Page](#shopping-bag-page)
   6. [Checkout Page](#checkout-page)
   7. [Checkout Success Page](#checkout-success-page)
   8. [Profile Page](#profile-page)
   9. [Favorites Page](#favorites-page)
   10. [Reviews Page](#reviews-page)
   11. [Reviews Admin](#reviews-admin)
   12. [Organizations Page](#organizations-page)
   13. [Accounts Pages](#accounts-pages)
   14. [404 Error Page](#404-error-page)
4. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Payment Service](#payment-service)
    6. [Cloud Storage](#cloud-storage)
    7. [Tools and Programs](#tools-and-programs)
5. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/josswe26/noplast/blob/main/TESTING.md#noplast-testing)
6. [Deployment](#deployment)
    1. [How To Use This Project](#how-to-use-this-project)  
    2. [Deployment to Heroku](#deployment-to-heroku)   
    3. [AWS Bucket Creation](#aws-bucket-creation)  
    4. [Connect Django to AWS Bucket](#connect-django-to-aws-bucket)
7. [Finished Product](#finished-product)
8. [Credits](#credits)
9. [Known Bugs](#known-bugs)
10. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)


### Strategy


#### Project Goals

 - Make the site responsive so it is acessible on different devices and screen sizes.

 - Make it easy to read understand and navigate the site.

 - The design and colours used in the site don't take away from the content.

 - Customers are able to register for an account for ease of use over time.

 - Make the process of buying a product easy so anyone can use the website.

 - Make it easy for users to book appointments and also edit/delete them as they wish.

 ***

#### Agile Planning

For this project I tried to learn more about the agile process and methodologies, my last project had comments about how I didn't use it properly or enough.
This time I had 21 user stories in my [github projects](https://github.com/users/JKirkby95/projects/6) in total when I first laid out my plan for this project. I feel like I did a better job with them this time and I can see why they're such a valuable tool.

I deceided to leave the reviews section in the future features as I already had the 3 custom models neccessary for the project.
But I would love to see it implemented in the future. 

This time around I put more detail into each one as seen in the example below:

![agile story detail](media/agile_user_stories.png)

Below I will show the varies stages of development for these.

Sprint 1
![github projects 1](media/06.05.24_user_stories.png)

Sprint 2 
![github projects 2](media/12-05-2024.png)

Sprint 3
![github projects 3](media/project_stories.png)

***

#### Goals Table

Goal | Achieved? |
--- | --- | 
Users able to register for an account | Yes |
Users are able to login/logout of the account| Yes |
Users are able to save their details to said account| Yes |
Users can complete a purchase with ease | Yes |
Users can view their order history afterwards | Yes |
Users can view and sort products | Yes |
Users can search for products using the search bar products | Yes |
Users can add products to their wishlist | Yes |
Users can remove products from their wishlist | Yes |
Users are able to make an appointment for club fitting| Yes  |
Users can edit/delete their appointment for club fitting| Yes  |
Users can sign up to our newsletter | Yes |
Users can find links to contact us or view our social media | Yes |
The purpose of the site is obvious immeadiatly | Yes |
The site has a responsive design to suit plenty of screen sizes |  Yes |
All forms on the site are validated and give clear feedback for errors |  Yes |
Review system in place for products |  No (future feature) |

[Back to top ⇧](#clare-golf-store)

***

### Scope

#### User Stories

As it was my first time making an ecommerce site , my user stories are not in th best order, In the future I feel like instead of typing them straight into the [github projects](https://github.com/users/JKirkby95/projects/6) i will actually start on a piece of paper to get them in the correct order.

**User Story 1**
- View list of products
    - As a user I would like to see a clear list of products so it's easy for me to make a purchase.
    - This is a huge part of the store for me, I wanted the products to look great and it be very clear what they are.

**User Story 2**
- View product details
    - As a user I would like to see more details about each product to help me make my decision.
    - This again seemed like a massive part of a store to me , you need  to give the customer all the information they'd need to want to purchase the item.

**User Story 3**
- Shopping bag
    -As a user I want to be able to view the items in my shopping bag and see the total cost.
    - I wanted it to be very clear to the user what was in their bag and what it actually was going to cost them.

**User Story 4**
- Register for an account
    - As a user I want to be able to register for an account.
    - This is absolutely neccessary for me, I find I use sites more personally that have an account where all my details are saved. It makes the whole process so much smoother.

**User Story 5**
- Login
    - As a user I want to be able to login to my account.
    - Straight forward one really you need to be able to login if youre going to be accessing the site from multiple devices.

**User Story 6**
- Logout
    - As a user I want to be able to logout of my account.
    - Again this is abolutely neccessary to protect the user.

**User story 7**
- Have a profile
    - As a user I want to be able to make a user profile to store my personal details.
    - I love this feature like I said before, it makes everything so easy it's the main reason I use sites like amazon so much.

**User story 8**
- Sort Products
    - As a user I want to be able to sort the products depending on what I'm searching for.
    - This makes it much easier for the user to identify what they want and to view all the options in that price range or a certain brand.

**User story 9**
- Product Categories
    - As a user I want to be able to search for products by categories.
    - On a site like this that has so many products categories are essential, it means the user can only search throught the products they want to see.

**User story 10**
- Adjust bag
    - As a user I want to be able to adjust the items in my shopping bag.
    - This is needed if the user adds too much of one product or adds a product they didn't want to add in the first place.

**User story 11**
- Payment info
    - As a user I want to be able to easily enter my payment information.
    - Stripe was used for this the built in validation is fantastic makes the whole process so easy.

**User story 12**
- Order Confirmation
    - As a user I want to be able to see an order confirmation after my order is placed.
    - This was used to show the customer a receipt of their purchase and an order number to view thier order history.

**User story 13**
 - Add a product
    - As an admin I want to be able to add products to the store.
    - This is possible on this site either through the admin or the product management tab but this is ONLY for admins.

**User story 14**
- Edit/Update products
    - As an admin I want to be able to edit a product or update some features about it.
    - Again this feature is only available to the admin, but is a great feature if you wanted to update a prodicts price or details.

**User story 15**
- Delete a product
    - As an admin I want to be able to delete a product from the store.
    - This is an admin only feature again, it's needed if a product becomes obselete.

**User story 16**
- Make an order
    - As a user I want to be able to make an order.
    - The main point of the site really, again stripe helped massively with this.

**User story 17**
- wishlist
    - As a user I want to be able to add items to my wishlist.
    - This is yet another great feature that comes with having an acoount with us,
    you can keep a product in their until it drops in price or you decide to buy it anyway.

**User story 18**
- Contact Form
    - As a user I want to have a contact form available to make out of business hours requests.
    - This is great for any feedback or queries a customer has.

**User story 19**
- Reviews
    - As a user I want to be able to leave or view reviews of the store.
    - I didn't get to add this feature but it's one I'd love to add. It could be attached to any product the pros who do the club fitting or the site in general.

**User story 20**
- Newsletter
    - As a user I want to be able to sign up to a newsletter to receive future offers.
    -  This is great for the site owner and the customer the user receives upcomign special and deals.

**User Story 21**
- Club Fitting
    - As a user I want to be able to make an appointment for a club fitting.
    - This ad's a luxury feature to any golf store and also ads crud functionality to the website for the user.

[Back to top ⇧](#clare-golf-store)

*** 

### Structure

***

#### Database Model

I made this database model using [lucid chart](https://lucid.app/), it was my first time using anything like this to create a database diagram. I tried to show all the links between the certain elements of this website.

![database diagram](media/db-model.png)

### Skeleton

#### Wireframes

I made these wireframes using [lucid chart](https://lucid.app/) also, I found them very easy to use although in future I would probably buy a membership for balsamiq as I prefer the look of their wireframes.

Page | Wireframe
--- | --- 
Home | ![Home](media/home_wire.png) |
Products| ![Products](media/products_wire.png) |
User Profile | ![Profile](media/user_wire.png) |
Club Fitting | ![Club fitting](media/booking_wire.png) |
Shopping Bag | ![Shoppping Bag](media/bag_wire.png)

[Back to top ⇧](#clare-golf-store)


### Surface

#### Color Scheme

The color scheme for this site was meant to be easy on the eye and not take away from the content, the main colors I used was the bootstrap dark and light class.
I used light over white so it's not quite as harsh on the eyes, and I'm personally a fan of the boostrap dark it's very clean color and lets any products with color pop.

![color scheme](media/color_scheme.png)

#### Typography

The font used for this site is Nunito.

Nunito is an excellent choice for your website's font due to its modern, clean, and highly readable design. As a sans-serif typeface, it provides a sleek and contemporary aesthetic that enhances the visual appeal of your site.