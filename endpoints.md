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
