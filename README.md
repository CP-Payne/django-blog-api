# README

// NOT FINISHED UNTIL:

- Add endpoint to create bio
- Fix Auth bypass in update blog

Blog API

// Working on it...

## Todo For Github Documentation

- Implement settings data for users
  - Should user full name be displayed in comments, blogs, etc. Should user be anonymous
- Implement blog search functionality
- Implement UUID instead of Sequential IDs

Future Todo:

- Error message not correct when token is not provided (Custom Permissions Only)
- Add ability to choose which subscriptions/subscribers to view (Active/in-active)
- Rename user column in database to author were applicable

## Advanced TODO

Real-time Notifications (Advanced)

For a more dynamic user experience, consider integrating real-time notifications using WebSockets with Django Channels or a service like Pusher. This allows notifications to be pushed to users without requiring a page refresh.

Notification Cleanup

Consider implementing a mechanism for cleaning up old notifications, either by deleting them after a certain period or providing users the option to clear their notifications.
