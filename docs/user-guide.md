# User Guide — Portfolio Website

## Getting Started

This portfolio is a full-stack application with a React-like frontend and a Django REST API backend.

### For Visitors

1. **Browse Projects**: Visit the homepage to see featured enterprise projects and course apps.
2. **View Tech Stacks**: Navigate to `/pages/stacks.html` to see detailed stack breakdowns.
3. **Contact**: Use the contact form on the homepage to send a message.

### For Recruiters

1. **Request Recruiter Access**: Contact the site owner to get a RECRUITER account.
2. **Login**: Use the Login button in the navigation bar.
3. **View Protected Content**: Once logged in, you can view your own contact message history.

### For Administrators

1. **Admin Dashboard**: Access `/admin/` on the backend to manage users, contact messages, and analytics.
2. **User Management**: Promote users to RECRUITER or ADMIN roles via bulk actions.
3. **Analytics**: View page visit statistics with role-based segmentation at `/api/analytics/stats/`.

## Account Roles

| Role      | Permissions                                                  |
| --------- | ------------------------------------------------------------ |
| USER      | Basic access, can submit contact form                        |
| RECRUITER | Can view public portfolio, submit contact, view own messages |
| ADMIN     | Full access to admin panel, analytics, all contact messages  |

## AI Tools Used

This portfolio was built with AI augmentation:

- **ChatGPT**: Architecture design, debugging
- **Claude**: Code review, documentation
- **Amazon Q**: AWS patterns, security validation
