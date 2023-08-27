# LittleLemon
Hello, Reviewers!

You can run available unittests from VS terminal using command: python manage.py test 
The test file is in the restaurant app folder.

# This path can be used to check that web application serves static HTML content with images and styles
/restaurant/

You can use the following API paths for testing purposes using Insomnia or Postman clients
OR just browse using your favorite browser.

# JDOSER endpoint, for example, to make POST request and create new user
/auth/users/ 

# to login using JDOSER endpoint
/auth/token/login 

# menu items
/restaurant/menu/
/restaurant/menu/{menuItemId}

# menu items
/api/menu-items/
/api/menu-items/4

# table booking 
/restaurant/booking/tables/
/restaurant/booking/tables/{bookingId}
