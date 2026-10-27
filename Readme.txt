Little Lemon Back-End Developer Capstone - API endpoints

Public:
GET  /api/menu/                 List menu items
GET  /api/menu/<id>/            Retrieve one menu item
POST /api-token-auth/           Obtain an authentication token (send username and password)
POST /auth/users/               Register a user

Authentication required (Token: <your-token>):
POST   /api/menu/               Create a menu item
PUT    /api/menu/<id>/          Update a menu item
PATCH  /api/menu/<id>/          Partially update a menu item
DELETE /api/menu/<id>/          Delete a menu item
GET    /api/bookings/           List bookings
POST   /api/bookings/           Create a booking
GET    /api/bookings/<id>/      Retrieve a booking
PUT/PATCH /api/bookings/<id>/   Update a booking
DELETE /api/bookings/<id>/      Delete a booking

Legacy booking page:
http://127.0.0.1:8000/book/

Authentication flow:
1. Register using POST /auth/users/ with username, password, and re_password.
2. Obtain a token using POST /api-token-auth/ with username and password.
3. In Insomnia, add header: Authorization: Token YOUR_TOKEN
