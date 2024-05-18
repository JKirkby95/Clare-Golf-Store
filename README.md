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
