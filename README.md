# API Documentation for Your Blog

## Overview

This API allows developers to interact with a blogging platform, enabling operations such as user management, blog post creation, interaction through comments and likes, subscription management, and notification handling.

## Technologies Used

- Python
- Django
- PostgreSQL
- Django Token Authentication

## Features

- User Registration and authentication
- CRUD operations for blog posts
- Comment and Like Management
- Subscription Management
- Notification Handling

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/CP-Payne/django-blog-api.git
```

2. Install dependencies

```bash
pip install django djangorestframework
```

3. Apply migrations

```bash
python manage.py migrate
```

4. Run the server

```bash
python manage.py runserver
```

## API Endpoints

### User Authentication

- **Register a User**: `POST /api/user/register` - Register a new user.
- **Login**: `POST /api/user/login` - Login and retrieve a token for authentication.
- **Logout**: `POST /api/user/logout` - Invalidate a users token.

### Blog Posts

- **List Posts**: `GET /api/blog/blogs` - Retrieve a list of blog posts.
- **Create Post**: `POST /api/blog/blogs` - Create a new blog post.
- **Retrieve Post**: `GET /api/blog/blogs/<id>` - Retrieve a blog post by ID.
- **Update Post**: `PUT /api/blog/blogs/<id>` - Update an existing blog post.

### Comments

- **List Comments on Post**: `GET /api/interactions/comment/list/<id>` - Get comments for a specific post.
- **Add Comment**: `POST /api/interactions/comments/add` - Add a comment to a post.
- **Delete Comment**: `DELETE /api/interactions/comments/add` - Delete a comment on a post.

### Likes

- **Toggle like on Post**: `POST /api/interactions/like/<id>/toggle-like` - Like and unlike a blog post.
- **Retrieve Likes on a Post**: `GET /api/interactions/like/<id>` - Get the total like number of a post.

### Subscriptions

- **Subscribe**: `POST /api/subscriptions/subscribe/<id>` - Subscribe to another user/author.
- **Unsubscribe**: `DEL /api/subscriptions/subscribe/<id>` - Unsubscribe from a user/author.
- **List Subscriptions**: `GET /api/subscriptions/get-subscriptions` - List all subscribed to users/authors.
- **Total Subscriptions**: `GET /api/subscriptions/count` - Retreive total number of subscriptions.
- **Total Subscribers**: `GET /api/subscriptions/subscribers/count` - Retreive total number of subscribers.

### Notifications

- **Get Notifications**: `GET /api/notifications/all` - Retreive all notifications for logged in user.
- **Mark Notifications as Read**: `POST /api/notifications/read/7` - Mark notifications as read.

## Do ASAP

- Add endpoint to create bio
- Add endpoint to delete blog post (History as well?)
- Fix auth bypass in update blog
- Fix Custom Permissions Only endpoints. Incorrect error message when token is not provided. (Verbose error messages)
- Update environment variables. Create environment file

## Future Enchancements

- Implement a mechanism for cleaning up old notifications from database, either by deleting them after a certain period or providing users the option to clear their notifications.
- Integrate real-time notifications using WebSockets with Django Channels or a service like Pusher. This would allow notifications to be pushed to users without requiring a page refresh.
- Add feature to allow user to set settings such as whether their full name should be displayed or if they want to be anonymous.
- Implement blog search functionality.
- Implement pagination for blog posts.
- Implement UUID instead of sequential IDs for better security.
- Create two separate tables for User and Author, instead of using one.
- Add feature to view active/in-active subscribers/subscriptions.
