## Author
> Faith Kwamboka Okong'o

# Kwamboka's Gallery
This is a personal gallery application that displays my photos for others to see.

![gallery](https://user-images.githubusercontent.com/100117264/170846752-bf477629-d175-4b06-829b-9f92d12ed29d.png)

## User Stories
As a user of the application I should be able to:
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo.
* The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Culture, Food, Nature)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.


## Admin Abilities
As an admin i should be able to:
* Sign in to the application
* Create new images 
* Delete images
* Update images

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add image categories, description and location|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details for editing|
| To delete an image  | **Through Admin dashboard** | click on image object and confirm delete|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images by Location|
| To filter by Category  | **Click drop-down on navbar** | Users can view images by category|

## Technologies used
* Python3
* Django & postresql
* Html5
* Css3
* Bootstrap4


## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/FaithKwamboka/Kwamboka-Gallery.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual``

3. Activating the virtual environment
>``source virtual/bin/activate``

4. Running the application
>``python3 manage.py runserverserver``

5. Running tests

 > ``python3 manage.py test.``

## [License](https://github.com/FaithKwamboka/Kwamboka-Gallery/blob/master/LICENSE)

## Collaborate
For any collaborations, reach me on [okongofaith3@gmail.com]()