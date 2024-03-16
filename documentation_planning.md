# API Documentation for Your Blog

## Overview

This API allows developers to interact with a blogging platform, enabling operations such as user management, blog post creation, interaction through comments and likes, subscription management, and notification handling. This document provides detailed information on how to use the various endpoints to integrate with the blog's functionalities.

## Getting Started

To start using the API, you need to:

    Obtain an API key by registering on the platform.
    Make sure to use HTTPS for all API requests.
    The API uses JSON format for request and response bodies.

## Authentication

Authentication is performed via API keys. Include your API key in each request to the API in the request header as X-API-Key: YOUR_API_KEY.
Error Codes

    401 Unauthorized: Returned when the API key is missing, malformed, or invalid.

## Endpoints

### User Management

#### Login

    POST /api/user/login
    Authenticates a user and returns an authentication token.
    Body:
        username: The user's username.
        password: The user's password.
    Responses:
        200 OK: Returns user details and token.

#### Register

    POST /api/user/register
    Registers a new user account.
    Body:
        username, email, first_name, last_name, password, password_confirm.
    Responses:
        200 OK: User created successfully.

#### Logout

    POST /api/user/logout
    Logs out the current user by invalidating their authentication token.
    Header:
        Authorization: Token <user_token>
    Responses:
        200 OK: User logged out successfully.

### Blog Posts

#### All Posts

    GET /api/blog/blogs
    Retrieves a list of all blog posts.
    Responses:
        200 OK: Returns an array of blog posts.

#### Create Blog Post

    POST /api/blog/blogs/
    Creates a new blog post.
    Body:
        title, snippet, content, category, tags, is_public.
    Responses:
        201 Created: Returns the created blog post details.

#### Get Blog By ID

TODO

#### Update blog post

### Comments and Likes

#### Add Comment

    POST /api/interactions/comment/add
    Adds a comment to a blog post.
    Body:
        blog: The ID of the blog post.
        message: The comment text.
    Responses:
        201 Created: Comment added successfully.

#### Get Comments On Blog

#### Delete Comment

#### Toggle Like

    POST /api/interactions/like/{blog_id}/toggle-like
    Toggles a like for a blog post.
    Path Parameters:
        blog_id: The ID of the blog post to toggle the like on.
    Responses:
        200 OK: Like status updated successfully.

#### Blog Likes

### Subscriptions

#### Subscribe

#### Unsubscribe

#### Total Subscriptions

#### Total Subscribers

#### List Blogs User Subscribed To

### Notifications

#### Get Notifications

#### Mark Notification As Read

## Further Help

    For additional assistance, visit our FAQ page or reach out to our support team.

Updates

    Make sure to regularly check this documentation for updates on new endpoints and changes to existing ones.
