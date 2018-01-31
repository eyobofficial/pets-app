# DJANGO SKILL TEST

## Test Instructions
Build and deploy a web application representing Dogs and Cats.

- Each dog and cat must have a name and birthday, and be linked to an Owner
- Owners should be able to access dogs and cats via an API and carry out CRUD operations on their Dog and Cat
- Owners should also be able to access dogs and cats via an admin interface

## Implementation
- Django REST Framework is used to develop an API
- Django's built in User model is used an "Owner" of the pets
- For this task, I decided not to create any Form and View for managing pets in userspace, but rather create a second, restricted admin ("owners' admin") which will do all the job for me. I just need to make some modifications:
- A second admin, call "Owners Admin" is implemented for managing pets.
