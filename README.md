I built an authentication REST API using Django, Django REST Framework, and PostgreSQL. I implemented user registration, email-based JWT login, token refresh, password recovery using an emailed OTP, and authenticated account deletion.

I created a custom user model, used serializers to validate registration data, and accessed PostgreSQL through Django ORM. The password-reset flow checks a six-digit OTP that expires after five minutes and removes it after a successful reset.

The project helped me practise backend API development, authentication, database relationships, and email integration. I am still improving its validation, permission handling, and automated tests.
