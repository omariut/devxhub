# E-commerce Site

This repository contains the code for an E-commerce site implemented using Django and Django REST Framework. The site allows users to browse products, add them to their shopping cart, make purchases, and leave reviews for products they have purchased.

## Features

- User Authentication: Users can register, login, and logout. They can also manage their profile details.
- Product Management: The site maintains a database of products with information such as name, description, price, image, and stock status.
- Shopping Cart: Users can add and remove products from their shopping cart, and the cart is updated accordingly.
- Purchases and Payment Integration: Users can proceed to checkout, enter shipping information, and make payments using a real payment gateway (e.g., Stripe, PayPal). Purchase receipts are generated after successful transactions.
- Admin Interface: An admin interface is provided using Django's built-in capabilities. Admin users can add, edit, and delete products, as well as perform search functions.
- RESTful API: The site exposes a RESTful API using Django REST Framework. The API allows clients to retrieve product information and place orders with appropriate authentication and permissions.
