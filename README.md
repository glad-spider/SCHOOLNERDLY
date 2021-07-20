Build an online learning web application.

# Short description

The web application should have 2 types of users: teachers and students.
The goal of teachers is to publish courses. Courses consist of reading
materials and tests. The goal of students is to enroll in courses and
try to learn by going through every step of the course.

# Glossary

*Reading material* - a page with a bunch of text that the student can
read (the page can have headings, bold text, etc)

*Test* - a page with a bunch of questions. Every question can have
one/multiple answers.

# Pages

A list of pages that the web application should have (sorted by priority):

- Login page
- Signup page
- Reset password page
- Courses page (a list of all available courses)
- Course page (a page with course description and details. On this page,
the student can click on "Enroll" button and then start going through
the course)
- Classroom page (a page that shows all the courses that the student
is working on)
- Classroom course page (the student opens this page when he/she wants
to work on the course. It shows the progress. What steps were already
done. What's the current step the student is working on, etc)
- Profile page
- Teacher's dashboard (create/publish/edit/delete courses. These pages
have the least priority. We can use admin panel for creating courses
at the beginning)

# Tech

Backend:

- Python
- Django REST Framework

Frontend:

- JavaScript
- Vue
- Vue Router
- Vuex
- Bootstrap Vue
