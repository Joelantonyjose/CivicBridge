# CivicBridge Development Journal

## Day 0
- Finalized project idea
- Chosen project name: CivicBridge
- Created GitHub repository
- Installed Git
- Verified Python installation
- Opened project in VS Code

## Day 1 - Flask Setup & First Launch

### Tasks Completed
- Created a Python virtual environment (`venv`)
- Activated the virtual environment in PowerShell
- Installed Flask using pip
- Verified Flask installation
- Created the first Flask application (`app.py`)
- Created the homepage route (`/`)
- Started the Flask development server
- Successfully opened CivicBridge at `http://127.0.0.1:5000`

### Concepts Learned
- Purpose of virtual environments (dependency isolation)
- Flask application structure
- Flask routing using `@app.route()`
- Request–response cycle between browser and server
- Difference between system Python and virtual environment Python

### Challenges Faced
- PowerShell execution policy blocked virtual environment activation
- Flask was initially run using the system Python instead of the virtual environment Python

### Outcome
Successfully launched the first working version of CivicBridge with a basic homepage displaying:

**Welcome to CivicBridge**  
*Report. Track. Resolve.*

## Day 2 - Templates and CSS

### Tasks Completed
- Created first HTML template (index.html)
- Connected Flask route to HTML using render_template()
- Fixed TemplateNotFound error
- Learned Flask template structure
- Created first CSS file (style.css)
- Connected CSS using url_for()
- Improved homepage appearance

### Concepts Learned
- Templates folder
- Static folder
- render_template()
- Jinja syntax {{ }}
- url_for()
- Basic HTML structure
- Basic CSS styling

### Challenges Faced
- Flask could not locate index.html initially
- Resolved by placing templates inside the app folder

### Outcome
Successfully built a homepage using HTML templates and CSS styling.

## Day 3 - Multi-Page Website

### Tasks Completed
- Created Report Issue page
- Created View Issues page
- Created About page
- Added Flask routes for each page
- Built navigation bar
- Connected pages using hyperlinks
- Tested navigation across the application

### Concepts Learned
- Flask routes
- URL mapping
- Anchor tags (<a>)
- Navigation bars
- Multi-page website structure

### Challenges Faced
- Navigation bar initially did not appear on all pages
- Resolved by verifying templates and refreshing the application

### Outcome
CivicBridge evolved from a single-page site into a multi-page web application with working navigation


## Day 4 - Template Inheritance

### Tasks Completed
- Created base.html
- Moved navigation bar to base template
- Linked CSS through base template
- Converted all pages to inherit from base.html
- Removed duplicate navigation code
- Tested template inheritance

### Concepts Learned
- Jinja template inheritance
- {% extends %}
- {% block %}
- DRY (Don't Repeat Yourself) principle

### Outcome
CivicBridge now uses a professional template structure where shared layout elements are maintained in a single file.

## Day 5 - Forms and User Input

### Tasks Completed
- Created Report Issue form
- Added Name field
- Added Location field
- Added Issue Title field
- Added Description field
- Added Submit button
- Configured form to use POST method
- Imported request from Flask
- Processed form submissions using request.form
- Displayed submitted data back to the user

### Concepts Learned
- HTML Forms
- Input fields
- Textarea
- GET vs POST requests
- Flask request object
- request.form

### Outcome
CivicBridge can now collect and process user-submitted issue reports.

## Day 6 - Displaying Reports

### Tasks Completed
- Created reports list for temporary storage
- Created report dictionary structure
- Stored submitted reports using append()
- Passed reports data to issues template
- Used Jinja for-loop to display reports
- Displayed submitted issues on View Issues page

### Concepts Learned
- Python Lists
- Python Dictionaries
- append()
- render_template variables
- Jinja loops
- Dynamic content rendering

### Outcome
Users can submit issues and view them on the View Issues page during the current application session.

## Day 7 - User Experience Improvements

### Tasks Completed
- Added redirect after form submission
- Learned redirect() and url_for()
- Implemented Post/Redirect/Get pattern
- Styled issue reports using CSS cards
- Added Jinja if/else condition
- Displayed message when no reports exist

### Concepts Learned
- redirect()
- url_for()
- CSS classes
- Jinja if statements
- Conditional rendering

### Outcome
Users are redirected to the Issues page after submission, reports are displayed in styled cards, and the application handles empty states gracefully.

## Day 8 - SQLite Database Integration

### Tasks Completed
- Created SQLite database (civicbridge.db)
- Created reports table
- Connected Flask application to SQLite
- Saved submitted reports into the database
- Retrieved reports from the database
- Displayed database records on the Issues page
- Verified reports persist after restarting Flask

### Concepts Learned
- SQLite
- SQL
- CREATE TABLE
- INSERT INTO
- SELECT
- PRIMARY KEY
- AUTOINCREMENT
- fetchall()
- commit()
- database connections

### Outcome
CivicBridge now stores reports permanently using SQLite instead of an in-memory Python list.

## Day 9 - Delete Issue Feature

### Tasks Completed
- Added Delete link for each issue
- Created dynamic delete route
- Used report ID to identify records
- Deleted reports from SQLite database
- Redirected users back to the Issues page

### Concepts Learned
- Dynamic routes
- Route parameters
- DELETE FROM
- WHERE clause
- SQL placeholders (?)
- Database record deletion

### Outcome
Users can now remove issues from CivicBridge. Deleted reports are permanently removed from the SQLite database.


## Day 10 - Status Tracking Setup

### Tasks Completed
- Added status column to the reports table
- Learned ALTER TABLE and ADD COLUMN
- Updated report insertion logic
- Set default status to "Pending"
- Displayed status on the Issues page

### Concepts Learned
- ALTER TABLE
- ADD COLUMN
- Database schema updates
- NULL values in SQLite
- None values in Python

### Outcome
CivicBridge can now track the status of issues. New reports are automatically marked as Pending.


## Day 11 - Resolve Issue Feature

### Tasks Completed
- Created resolve route
- Learned SQL UPDATE
- Updated report status
- Redirected after update
- Tested status change from Pending to Resolved

### Concepts Learned
- UPDATE
- SET
- WHERE
- Database updates
- CRUD operations

### Outcome
Users can now mark issues as Resolved without deleting them.


## Day 12 - Resolve Feature and Status Filtering

### Tasks Completed
- Added a Resolve link for each issue
- Created a resolve route using a dynamic URL parameter
- Updated issue status from Pending to Resolved
- Redirected users back to the Issues page after resolving
- Added conditional rendering for the Resolve button
- Displayed "Resolved ✅" for resolved issues
- Added filter links (All / Pending / Resolved)
- Implemented status-based filtering using query parameters

### Concepts Learned
- SQL UPDATE
- SET and WHERE clauses
- Query Parameters
- request.args.get()
- Jinja if-else conditionals
- Conditional rendering
- Database filtering

### Outcome
Users can now mark issues as Resolved instead of deleting them. The Issues page displays the Resolve button only for Pending issues and allows filtering reports by status (All, Pending, Resolved). CivicBridge now supports complete CRUD operations and basic issue management workflows.


## Day 13 - Search Feature

### Tasks Completed
- Added a search form to the Issues page
- Learned how GET forms work
- Retrieved search input using query parameters
- Implemented search functionality using request.args.get()
- Learned SQL LIKE for partial matching
- Enabled searching reports by title
- Tested search functionality successfully

### Concepts Learned
- GET requests
- Query Parameters
- request.args.get()
- SQL LIKE
- Wildcards (%)
- Search functionality in Flask

### Outcome
Users can now search for issues by title. The application filters reports and displays only matching results, making it easier to find specific issues when many reports exist.


## Day 14 - Edit Issue Feature

### Tasks Completed
- Added Edit links to each issue
- Created a dynamic edit route using report IDs
- Retrieved a specific report from the database
- Created a dedicated edit page (edit.html)
- Pre-filled form fields with existing report data
- Learned GET and POST request handling
- Retrieved submitted form data using request.form
- Updated report title and description in the database
- Redirected users back to the Issues page after saving changes

### Concepts Learned
- Dynamic Routes
- GET vs POST Requests
- request.method
- request.form
- SQL UPDATE
- Pre-filled Forms
- Redirects

### Outcome
Users can now edit previously submitted issues. The application fetches existing report data, displays it in a form, and updates the database when changes are submitted.


## Day 15 - Basic Validation and Data Cleaning

### Tasks Completed
- Added validation for empty form fields
- Prevented reports from being saved when required fields are missing
- Learned how `if` conditions can be used for validation
- Improved validation using `.strip()`
- Tested submissions containing only spaces

### Concepts Learned
- Input Validation
- Logical Operators (`or`)
- Empty String Checks
- String `.strip()`
- Data Cleaning

### Outcome
Users can no longer submit reports with empty fields. Inputs containing only spaces are also rejected, improving data quality in the database.


## Day 16 - Flash Messages and User-Friendly Validation

### Tasks Completed
- Added Flask secret key
- Learned Flask flash messages
- Replaced plain validation response with flash()
- Redirected users back to the report form after validation failures
- Displayed flashed messages in report.html
- Improved user experience for form validation

### Concepts Learned
- Flask Secret Key
- flash()
- Redirects
- get_flashed_messages()
- User-friendly validation feedback

### Outcome
Users now remain on the report page when validation fails and receive a clear error message. This creates a smoother and more professional user experience.


## Day 17 - UI Enhancement for Validation Messages

### Tasks Completed
- Added a CSS class to flash messages
- Styled validation messages using CSS
- Improved visibility of error feedback
- Learned how HTML classes connect with CSS selectors

### Concepts Learned
- HTML class attribute
- CSS class selectors
- padding
- margin
- border

### Outcome
Validation messages are now displayed inside a styled alert box, making them easier for users to notice and understand.


## Day 18 - End-to-End Testing and Application Refinement

### Tasks Completed
- Performed end-to-end testing of the complete CivicBridge workflow.
- Verified report creation, search functionality, status filtering, editing, resolving, and deletion.
- Modified the interface so only pending reports display the **Edit** option.
- Prevented resolved reports from being edited through backend validation.
- Moved flash message handling to `base.html` so all pages can display flash messages.
- Added validation to handle invalid or deleted report IDs gracefully.
- Improved the application's robustness by enforcing business rules on both the frontend and backend.

### Concepts Learned
- End-to-End Testing
- Business Rules
- Defensive Programming
- DRY (Don't Repeat Yourself) Principle
- Backend Validation
- Handling Missing Database Records

### Outcome
Successfully verified the complete CivicBridge workflow from report creation to deletion. Improved the application's reliability by enforcing business rules, preventing unauthorized edits, handling invalid URLs safely, and making flash messages available across the entire application.



#  CivicBridge Development Journal – Day 19

**Date:** 25 July 2026

## Objective

Begin the CivicBridge v2.0 UI redesign by establishing a modern design foundation inspired by the selected Canva template.

## Work Completed

- Backed up the original stylesheet by creating `style_v1.css`.
- Redesigned the application's base layout by updating `base.html`.
- Added the Google Fonts **Poppins** font for a modern and consistent typography.
- Created a new horizontal navigation bar using Flexbox.
- Added a professional footer that will be shared across all pages.
- Designed and implemented a new homepage hero section.
- Added:
  - Main headline
  - Project description
  - "Report an Issue" button
  - "View Issues" button
- Styled the hero section using a two-column responsive layout.
- Established the official green-and-white design language for CivicBridge v2.0.
- Built the initial CSS framework that will be reused throughout the application.

## Testing

- Verified that the redesigned navigation bar displays correctly.
- Confirmed that the hero section loads successfully.
- Tested the navigation links to ensure they remain functional.
- Verified that the new stylesheet is applied correctly.
- Identified that the View Issues page temporarily lost its previous spacing due to the new global stylesheet. This was expected and scheduled for redesign in a future session.

## Files Modified

- `app/templates/base.html`
- `app/templates/index.html`
- `app/static/style.css`

## Files Added

- `app/static/style_v1.css`

## Challenges

- The previous styling of the View Issues page was affected after introducing the new global CSS. This will be addressed during the dedicated redesign of that page in a future development session.

## Next Steps

- Design the Community Impact section.
- Create the How CivicBridge Works section.
- Continue redesigning the homepage using reusable UI components.
- Improve the overall visual consistency across all pages.

## Reflection

Today's session marked the beginning of CivicBridge v2.0. Rather than focusing on new backend features, the objective was to establish a modern, clean, and professional user interface. The new navigation, hero section, typography, and colour palette provide a strong foundation for the upcoming redesign of the remaining pages.



#  CivicBridge Development Journal – Day 20

**Date:** 30 July 2026

## Objective
Continue the CivicBridge v2.0 UI redesign by expanding the homepage with modern, informative sections while maintaining the new green-and-white design language.

## Work Completed

- Added the **Community Impact** section below the hero section.
- Created three statistics cards:
  - Total Reports
  - Pending Reports
  - Resolved Reports
- Styled the statistics cards with rounded corners, soft shadows, hover animations, and a consistent green-and-white theme.
- Added the **How CivicBridge Works** section.
- Designed three workflow cards representing the CivicBridge process:
  - 📝 Report
  - 📍 Track
  - ✅ Resolve
- Applied a consistent UI design by reusing the same card style and spacing across the homepage.
- Continued following the Canva-inspired design language established for CivicBridge v2.0.

## Testing

- Verified that the Community Impact section displays correctly.
- Confirmed that all three statistics cards render properly.
- Verified that the How CivicBridge Works section displays correctly.
- Tested hover animations on both statistics cards and workflow cards.
- Confirmed that the homepage layout remains clean and functional after the additions.

## Files Modified

- `app/templates/index.html`
- `app/static/style.css`

## Challenges

- No major issues encountered during today's development.

## Next Steps

- Add the Recent Issues section to the homepage.
- Replace placeholder statistics with live data from the SQLite database.
- Improve responsiveness for mobile and tablet devices.
- Continue redesigning the remaining pages using the new CivicBridge v2.0 design language.

## Reflection

Today's work focused on enhancing the homepage by introducing informative and visually appealing sections. The addition of the Community Impact and How CivicBridge Works sections strengthens the user experience while maintaining a clean, modern, and consistent interface. The homepage now better communicates CivicBridge's purpose and workflow, bringing the project another step closer to a production-quality web application.


# 🌉 CivicBridge Development Journal – Day 21

**Date:** 31 July 2026

## Objective

Enhance the CivicBridge v2.0 homepage by integrating live database content, replacing placeholder data with dynamic information retrieved from the SQLite database.

## Work Completed

- Added the **Recent Issues** section to the homepage.
- Designed modern issue cards displaying:
  - Issue title
  - Location
  - Status badge (Pending/Resolved)
- Styled the Recent Issues section to match the existing green-and-white design language.
- Modified the Flask `home()` route to retrieve the latest three reports from the SQLite database.
- Implemented an SQL query to fetch the three most recent reports using:
  ```sql
  SELECT * FROM reports
  ORDER BY id DESC
  LIMIT 3;
  ```
- Passed the retrieved reports from Flask to the Jinja template.
- Replaced the placeholder Recent Issues cards with dynamically generated content using Jinja templating.
- Implemented SQL `COUNT(*)` queries to calculate:
  - Total Reports
  - Pending Reports
  - Resolved Reports
- Connected the Community Impact cards to live database statistics.
- Successfully converted the homepage into a dynamic, database-driven interface.

## Testing

- Verified that the latest three reports are displayed correctly on the homepage.
- Confirmed that the Community Impact statistics update automatically based on the database.
- Tested Pending and Resolved status badges.
- Identified and resolved HTML structure issues caused by incorrect closing tags (`</div>`), restoring the proper card layout.
- Confirmed that all homepage sections display correctly after integrating dynamic content.

## Files Modified

- `app/app.py`
- `app/templates/index.html`
- `app/static/style.css`

## Challenges

- Encountered HTML layout issues due to missing closing tags while updating the Community Impact section.
- Corrected the HTML structure and verified that the layout returned to its intended design.

## Next Steps

- Redesign the View Issues page using the CivicBridge v2.0 design language.
- Improve the Report Issue page.
- Make the homepage responsive for mobile and tablet devices.
- Continue refining animations and overall UI consistency.

## Reflection

Today's development session marked an important milestone in CivicBridge v2.0. The homepage is no longer dependent on placeholder content; it now displays live statistics and the latest reported issues directly from the SQLite database. Integrating the backend with the redesigned frontend significantly improves both functionality and user experience, bringing CivicBridge closer to a production-quality full-stack web application.


# 🌉 CivicBridge Development Journal – Day 22

**Date:** 1 August 2026

## Objective

Redesign the View Issues page to match the CivicBridge v2.0 interface while preserving all existing functionality.

## Work Completed

- Redesigned the View Issues page with a modern layout.
- Added a professional page header with a short description.
- Redesigned the filter section using styled buttons for:
  - All
  - Pending
  - Resolved
- Improved the search bar styling to match the CivicBridge theme.
- Enhanced the search experience by preserving the user's search query after submission.
- Redesigned each issue into a modern information card.
- Added status badges for Pending and Resolved issues.
- Improved the presentation of:
  - Reporter Name
  - Location
  - Description
- Styled the Resolve, Edit, and Delete buttons with distinct colors.
- Centered the issue list using a dedicated container layout.
- Added a clean empty-state design for situations where no reports match the search or filter.

## Testing

- Verified that filtering by status works correctly.
- Tested search functionality.
- Confirmed that the search value remains visible after submitting the search.
- Verified that Resolve, Edit, and Delete actions continue to function correctly.
- Confirmed that the redesigned layout displays correctly.

## Files Modified

- app/templates/issues.html
- app/static/style.css

## Challenges

- Adjusted the HTML structure to improve spacing and maintain a consistent layout.
- Refined the page without affecting existing backend functionality.

## Next Steps

- Redesign the Report Issue page.
- Improve the Edit Issue page.
- Enhance the About page.
- Continue making the application responsive for mobile devices.

## Reflection

Today's work significantly improved one of the application's primary pages. The View Issues page now presents information in a cleaner, more organized, and visually appealing manner while maintaining all existing functionality. These improvements contribute to a more professional and user-friendly CivicBridge experience.


# 🌉 CivicBridge Development Journal – Day 23

**Date:** 3 August 2026

## Objective

Redesign the Report Issue and Edit Issue pages to match the CivicBridge v2.0 interface, creating a consistent and modern user experience across the application.

## Work Completed

- Redesigned the Report Issue page with a modern, card-based layout.
- Added a professional page header with a brief description.
- Improved the report form using organized form groups.
- Added descriptive placeholders to all input fields.
- Applied HTML validation using the `required` attribute.
- Styled the form with rounded input fields and improved spacing.
- Added focus effects to input fields for better user experience.
- Designed a full-width green Submit Report button with hover effects.
- Redesigned the Edit Issue page using the same layout and styling as the Report Issue page.
- Updated the Edit Issue form to display existing issue details in a clean and consistent interface.
- Reused existing CSS components to maintain a uniform design across the application.

## Testing

- Verified that new issues can be submitted successfully.
- Confirmed that form validation prevents empty submissions.
- Tested editing existing issues and verified that updates are saved correctly.
- Confirmed that all redesigned pages display correctly without affecting backend functionality.
- Verified visual consistency with the Homepage and View Issues pages.

## Files Modified

- `app/templates/report.html`
- `app/templates/edit.html`
- `app/static/style.css`

## Challenges

- Redesigned the forms while preserving the existing Flask routes and backend logic.
- Ensured the Edit Issue page reused the same design components as the Report Issue page to maintain consistency.

## Next Steps

- Implement flash messages for successful actions such as reporting, editing, resolving, and deleting issues.
- Redesign the About page.
- Improve responsiveness for mobile and tablet devices.
- Continue enhancing the overall user experience.

## Reflection

Today's development session focused on improving the application's data entry and editing experience. Both the Report Issue and Edit Issue pages now share a consistent visual identity with the rest of CivicBridge v2.0. Reusing the same design components helped maintain consistency while keeping the code organized and easier to maintain.

# 🌉 CivicBridge Development Journal – Day 24

**Date:** 4 August 2026

## Objective

Improve the user experience by implementing flash messages to provide feedback after important user actions.

## Work Completed

- Implemented Flask flash messages across the application.
- Added success notifications for:
  - Reporting a new issue.
  - Updating an existing issue.
  - Resolving an issue.
  - Deleting an issue.
- Updated the base template to display flash messages globally.
- Designed a modern notification component using the CivicBridge green-and-white theme.
- Reused the same notification system for validation and error messages.

## Testing

- Verified that a success message appears after reporting an issue.
- Verified that editing an issue displays a confirmation message.
- Confirmed that resolving an issue shows a success notification.
- Confirmed that deleting an issue displays a confirmation message.
- Verified that validation and existing flash messages continue to work correctly.

## Files Modified

- app.py
- app/templates/base.html
- app/static/style.css

## Challenges

- Integrated Flask's flash message system without affecting existing application logic.
- Created a reusable notification component that works across all pages.

## Next Steps

- Redesign the About page.
- Improve mobile responsiveness.
- Add icons and visual enhancements.
- Continue preparing CivicBridge for deployment.

## Reflection

Today's improvements focused on user experience rather than adding new functionality. Flash messages provide immediate feedback after user actions, making the application feel more interactive and professional while keeping the interface consistent with CivicBridge v2.


# 🌉 CivicBridge Development Journal – Day 25

**Date:** 5 August 2026

## Objective

Redesign the About page to match the CivicBridge v2.0 interface and provide users with a clear overview of the application's purpose, features, and technology stack.

## Work Completed

- Redesigned the About page with a modern, card-based layout.
- Added a professional hero section with the CivicBridge introduction.
- Created a dedicated Mission section explaining the purpose of the application.
- Added a Key Features section highlighting the application's core functionality.
- Added a Technologies Used section listing the development stack.
- Implemented a responsive grid layout for the information cards.
- Styled the cards with rounded corners, shadows, and hover effects.
- Maintained the green-and-white CivicBridge theme for visual consistency.

## Testing

- Verified that the About page loads correctly.
- Confirmed that all cards display properly.
- Tested the responsive grid layout.
- Verified that the hover animations work as expected.
- Confirmed consistency with the other redesigned pages.

## Files Modified

- app/templates/about.html
- app/static/style.css

## Challenges

- Structured the information into clear sections while keeping the page clean and easy to read.
- Reused the existing design language to maintain consistency across the application.

## Next Steps

- Improve mobile responsiveness across the application.
- Refine the navigation experience.
- Add additional UI enhancements where necessary.
- Prepare CivicBridge for deployment and portfolio presentation.

## Reflection

Today's work completed the redesign of the application's primary pages. The About page now provides users with a professional overview of CivicBridge while maintaining a consistent visual identity throughout the application.


# 🌉 CivicBridge Development Journal – Day 26

**Date:** 19 August 2026

## Objective

Improve the responsiveness of the CivicBridge application to ensure that the user interface works properly across mobile, tablet, and desktop screen sizes.

## Work Completed

- Added responsive CSS using a media query for screens with a maximum width of 768px.
- Updated the navigation bar to adapt to smaller screens.
- Allowed navigation links to wrap and remain properly aligned on mobile devices.
- Adjusted the homepage hero section for smaller screen sizes.
- Reduced heading and paragraph sizes for better mobile readability.
- Improved the Community Impact statistics section for mobile screens.
- Adjusted statistic cards to fit comfortably within smaller screen widths.
- Updated the How It Works section to stack cards vertically on mobile devices.
- Improved the Recent Issues section layout for smaller screens.
- Adjusted the footer text and spacing for mobile devices.
- Made the View Issues page responsive, including the page header, filters, and search form.
- Updated issue cards so that titles, status indicators, and action buttons adapt properly on smaller screens.
- Improved the responsiveness of the Report Issue and Edit Issue forms.
- Adjusted the About page layout so that information cards stack properly on mobile devices.

## Testing

- Tested the application using Chrome's responsive device mode.
- Tested the mobile layout at a width of 375px.
- Tested the responsive layout at a width of 768px.
- Checked the application on the normal desktop layout.
- Verified that no major overflowing or overlapping issues were present.
- Confirmed that the responsive styles did not affect the desktop layout.

## Files Modified

- `app/static/style.css`

## Challenges

- Learned how to use Chrome Developer Tools and Device Toolbar to test responsive layouts.
- Ensured that responsive styles were placed inside the media query without affecting the existing desktop design.
- Adjusted multiple sections of the application individually to improve the overall mobile experience.

## Next Steps

- Perform final UI polish across the application.
- Review navigation and spacing for consistency.
- Add any remaining visual improvements.
- Prepare the project for deployment and portfolio presentation.

## Reflection

Today's development session focused on making CivicBridge more accessible across different screen sizes. By adding responsive styling through a media query, the application's main pages can now adapt more effectively to mobile and tablet devices while preserving the existing desktop layout. This was an important step toward making CivicBridge feel more complete and production-ready.


# 🌉 CivicBridge Development Journal – Day 27

**Date:** 20 August 2026

## Objective

Improve the overall visual consistency and user experience of CivicBridge through final UI polish and interaction improvements.

## Work Completed

- Added active navigation link functionality.
- Updated the navigation bar so the current page is visually highlighted.
- Added green styling and increased font weight for the active navigation link.
- Added an underline to the active navigation link.
- Improved navigation link hover effects with a green underline.
- Added smooth hover transitions to the navigation links.
- Added a subtle lift effect to the Resolve, Edit, and Delete action buttons.
- Added a subtle lift effect to the homepage hero buttons.
- Performed a final visual consistency check across the main pages.
- Verified that the new UI improvements did not negatively affect the responsive layout.

## Files Modified

- `templates/base.html`
- `static/style.css`

## Testing

- Tested active navigation links across:
  - Home
  - Report Issue
  - View Issues
  - About
- Tested navigation hover effects.
- Tested hero button hover effects.
- Tested Resolve, Edit, and Delete button hover effects.
- Checked the application in desktop view.
- Checked the application in mobile view to ensure responsiveness remained intact.

## Reflection

Today's session focused on small but important UI improvements. The application now provides clearer navigation feedback by highlighting the active page and adding consistent hover interactions. Button hover effects also make the interface feel more interactive and polished. These refinements improve the overall user experience without changing the core functionality of CivicBridge.

## Next Steps

- Review the project as a complete application.
- Identify any remaining bugs or improvements.
- Consider deployment and portfolio preparation.


# 🌉 CivicBridge Development Journal – Day 28

**Date:** 26 August 2026

## Objective

Begin implementing user authentication for CivicBridge by creating a user database and adding user registration functionality.

## Work Completed

- Reviewed the existing database setup.
- Created a new `users` table in `civicbridge.db`.
- Added `id`, `username`, and `password` fields.
- Set the username field as `UNIQUE` to prevent duplicate accounts.
- Added password hashing using `generate_password_hash()`.
- Added the `/register` route with GET and POST methods.
- Created the `register.html` registration page.
- Added validation for empty username and password fields.
- Added duplicate username handling using `try` and `except sqlite3.IntegrityError`.
- Added flash messages for successful registration and registration errors.
- Tested successful user registration.
- Tested duplicate username validation.

## Challenges

- Worked with an existing SQLite database while adding a new table.
- Learned how password hashing protects user passwords.
- Practiced handling database errors using `try` and `except`.
- Fixed indentation issues while working with Python's `try` and `except` blocks.

## Next Steps

- Implement user login functionality.
- Verify passwords using `check_password_hash()`.
- Add user sessions.
- Implement logout functionality.

## Reflection

Today's session marked the beginning of the user authentication phase of CivicBridge. The application can now register users securely, store hashed passwords, validate required fields, and prevent duplicate usernames. This creates the foundation for implementing login and session management in the next stage.


# 🌉 CivicBridge Development Journal – Day 29

**Date:** 29 August 2026

## Objective

Implement user login, session management, logout functionality, and connect authenticated users with submitted reports.

## Work Completed

- Created the `/login` route with GET and POST methods.
- Created `login.html` for user login.
- Retrieved registered users from the SQLite database.
- Used `check_password_hash()` to verify passwords securely.
- Added Flask session support using `session`.
- Stored the logged-in username in the session.
- Created the `/logout` route.
- Added dynamic Login, Register, and Logout links to the navigation bar.
- Protected the `/report` route so only logged-in users can submit issues.
- Protected the `/edit/<id>` and `/delete/<id>` routes from unauthenticated access.
- Added a `username` column to the `reports` table.
- Updated the report submission logic to store the logged-in user's username with each report.
- Tested the complete authentication flow successfully.

## Testing

- Successfully logged in using a registered account.
- Successfully handled incorrect passwords.
- Successfully logged out.
- Confirmed that the navigation changes depending on login status.
- Confirmed that unauthenticated users are redirected to the login page when accessing protected routes.
- Successfully submitted a report while logged in.
- Confirmed that the submitted report appears correctly in View Issues.

## Files Created

- `templates/login.html`

## Files Modified

- `app.py`
- `templates/base.html`
- `update_database.py`

## Database Changes

Added the following column to the `reports` table:

- `username`

This allows CivicBridge to associate reports with the registered user who submitted them.

## Challenges

- Learned how Flask sessions maintain login information between requests.
- Learned how to protect routes using session checks.
- Learned how to dynamically display navigation links based on authentication status.
- Connected authenticated users with their submitted reports.
- Practiced updating an existing SQLite database using `ALTER TABLE`.

## Authentication Phase Status

- ✅ User database
- ✅ User registration
- ✅ Password hashing
- ✅ User login
- ✅ Password verification
- ✅ Session management
- ✅ Logout
- ✅ Protected routes
- ✅ User-report association
- ✅ Authentication testing

## Next Steps

The core user authentication phase is now complete.

Future improvements can include:

- User profile functionality
- Showing only a user's own reports
- Role-based access for Citizens and Representatives
- Improved authorization for editing and deleting reports
- Additional security improvements

## Reflection

Today's session completed the core authentication functionality of CivicBridge. Users can now register, securely log in, remain recognized through sessions, log out, and submit reports associated with their accounts. Protected routes also prevent unauthenticated users from accessing report-related actions. This represents a major step toward making CivicBridge a more complete and realistic civic reporting platform.


# 🌉 CivicBridge Development Journal – Day 30

**Date:** 31 August 2026

## Objective

Implement user-specific report viewing so that logged-in users can view the reports they have personally submitted.

## Work Completed

- Added a **My Reports** option to the navigation bar for logged-in users.
- Created the `/my-reports` route in `app.py`.
- Added authentication protection to the `/my-reports` route.
- Used Flask sessions to identify the currently logged-in user.
- Used `session["username"]` to retrieve the username of the logged-in user.
- Added a database query to retrieve only reports belonging to the logged-in user.
- Created `my_reports.html` to display the user's reports.
- Displayed report title, location, description, and status on the My Reports page.
- Reused the existing CivicBridge report-card design.
- Tested the My Reports functionality successfully.

## Testing

- Successfully logged in using a registered account.
- Confirmed that the **My Reports** option appears in the navigation bar after login.
- Successfully opened the My Reports page.
- Confirmed that the user's submitted reports are displayed.
- Confirmed that reports are retrieved based on the logged-in user's username.
- Confirmed that unauthenticated users are redirected to the login page when accessing `/my-reports`.

## Files Created

- `templates/my_reports.html`

## Files Modified

- `app.py`
- `templates/base.html`

## Database Integration

The existing `reports` table contains a `username` column that was added during the previous authentication phase.

The My Reports feature uses the logged-in user's username to retrieve their reports from the database.

## Next Steps

The next session will focus on report ownership and authorization.

Future improvements can include:

Preventing users from editing reports belonging to other users.
Preventing users from deleting reports belonging to other users.
Adding ownership checks to the edit and delete routes.
Ensuring that users can only manage their own reports.
Introducing role-based access for Citizens and Representatives.
Creating a Representative dashboard.

## Reflection

Today's session started Phase 2 of CivicBridge by implementing user-specific functionality. The application can now identify the logged-in user and display only the reports associated with that user. This makes the authentication system more meaningful and moves CivicBridge closer to becoming a proper multi-user civic reporting platform.


# 🌉 CivicBridge Development Journal – Day 31

**Date:** 2 September 2026

## Objective

Implement **report ownership and authorization** so that users can only edit or delete reports that they personally submitted.

## Work Completed

- Implemented report ownership verification for editing reports.
- Prevented users from editing reports belonging to other users.
- Added Edit and Delete options to the **My Reports** page.
- Restricted editing of resolved reports.
- Implemented ownership verification for deleting reports.
- Prevented users from deleting reports belonging to other users.
- Added proper authorization messages for unauthorized actions.
- Tested both authorized and unauthorized editing.
- Tested both authorized and unauthorized deletion.
- Confirmed that report ownership is now enforced.

## Testing

- Successfully edited a report belonging to the logged-in user.
- Confirmed that edited report details were saved.
- Logged in as a different user and attempted to edit another user's report.
- Confirmed that unauthorized editing was blocked.
- Successfully deleted a report belonging to the logged-in user.
- Logged in as a different user and attempted to delete another user's report.
- Confirmed that unauthorized deletion was blocked.
- Confirmed that reports belonging to other users remain protected.

## Files Modified

- `app.py`
- `templates/my_reports.html`

## Challenges

- Learned the difference between **authentication** and **authorization**.
- Learned how report ownership can be connected with the logged-in user's session.
- Learned how to restrict database operations based on the current user.
- Understood why authorization should be enforced when performing database operations.
- Tested direct URL access to verify that unauthorized users cannot manipulate other users' reports.

## Phase 2 Status

- ✅ User authentication
- ✅ Registration and login
- ✅ Session management
- ✅ Protected report submission
- ✅ Username stored with reports
- ✅ My Reports feature
- ✅ Edit ownership protection
- ✅ Delete ownership protection
- 🔜 Report resolution authorization
- 🔜 Citizen and Representative roles
- 🔜 Representative dashboard

## Next Steps

The next session will focus on the **Resolve** functionality.

The current Resolve feature does not have proper authorization. Instead of allowing ordinary users to resolve reports, CivicBridge will move toward a role-based system.

Planned improvements:

- Review and secure the Resolve functionality.
- Introduce user roles such as **Citizen** and **Representative**.
- Add role-based permissions.
- Allow Representatives to review and resolve civic reports.
- Create a Representative dashboard.
- Improve report status management.

## Reflection

Today's session was an important security milestone for CivicBridge.
The application can now distinguish between a user being **logged in** and a user being **authorized** to modify a particular report.
Users can edit and delete their own reports while reports belonging to other users remain protected.
This makes CivicBridge a more secure multi-user platform and provides a strong foundation for introducing **Citizen and Representative roles** in the next stage.
The project is gradually moving from a basic civic reporting application toward a more structured and scalable platform.


# 🌉 CivicBridge Development Journal – Day 32

**Date:** 4 September 2026

## Objective

Introduce **role-based access control** to CivicBridge and secure the issue resolution functionality so that only Representatives can resolve civic reports.

## Work Completed

- Added a `role` column to the `users` table.
- Set the default role of newly registered users to **Citizen**.
- Promoted an existing test account to the **Representative** role.
- Updated the login system to store the user's role in the Flask session.
- Secured the Resolve functionality so that only Representatives can resolve reports.
- Prevented unauthenticated users from accessing the Resolve functionality.
- Updated the Issues page so that the **Resolve** button is visible only to Representatives.
- Kept backend authorization in place even after hiding the button from Citizens.
- Verified that Representatives can successfully resolve pending reports.

## Testing

### Citizen Testing

- Logged in as a Citizen.
- Confirmed that the **Resolve** button is not visible.
- Attempted to access the Resolve URL directly.
- Confirmed that the action was rejected with an authorization message.

### Representative Testing

- Logged in as a Representative.
- Confirmed that the **Resolve** button is visible for pending reports.
- Successfully clicked Resolve.
- Confirmed that the report status changed from **Pending** to **Resolved**.

## Files Modified

- `app.py`
- `templates/issues.html`
- `update_database.py`

## Database Changes

The `users` table was updated with a new role field.

The available roles currently include:

- **Citizen**
- **Representative**

New users automatically receive the Citizen role.

An existing test account was manually assigned the Representative role for testing.

## Security Improvements

Day 32 introduced the first role-based authorization system in CivicBridge.

The application now distinguishes between:

**Authentication**  
Whether a user is logged in.

**Authorization**  
Whether the logged-in user has permission to perform a particular action.

Only users with the **Representative** role are authorized to resolve civic reports.

The backend authorization check protects the actual route, while the frontend condition prevents Citizens from seeing an action they cannot perform.

## Challenges

- Learned how to introduce user roles into an existing database.
- Learned how database defaults can assign a role to newly registered users.
- Learned how to store a user's role in a Flask session.
- Learned how to implement role-based authorization for a Flask route.
- Learned why frontend button visibility and backend authorization should both be implemented.
- Tested authorization by attempting to access a protected route directly.

## Phase 2 Status

- ✅ User authentication
- ✅ Registration and login
- ✅ Session management
- ✅ Protected report submission
- ✅ Username stored with reports
- ✅ My Reports feature
- ✅ Report ownership protection
- ✅ Edit authorization
- ✅ Delete authorization
- ✅ Citizen and Representative roles
- ✅ Role stored in session
- ✅ Resolve authorization
- ✅ Representative-only Resolve button
- 🔜 Representative dashboard
- 🔜 Advanced report management

## Reflection

Today's session introduced an important architectural improvement to CivicBridge.
The application is no longer treating every authenticated user the same. CivicBridge can now distinguish between **Citizens** and **Representatives** and assign different permissions to each role.
Citizens can report and manage their own issues, while Representatives can perform administrative actions such as resolving civic reports.
This role-based foundation will make it possible to build a dedicated **Representative side of CivicBridge** in future sessions.
The project is continuing to evolve from a basic reporting application into a structured multi-user civic platform.


# 🌉 CivicBridge Development Journal – Day 33

**Date:** 17 September 2026

## Objective

Strengthen the role-based permission system in CivicBridge by ensuring that **Representatives cannot edit or delete civic reports**, while **Citizens can manage their own pending reports**.

## Work Completed

- Restricted the **Edit** functionality to Citizens.
- Added backend role authorization to the Edit route.
- Prevented Representatives from accessing the Edit functionality through direct URLs.
- Restricted the **Delete** functionality to Citizens.
- Added backend role authorization to the Delete route.
- Updated the Issues page so Representatives no longer see the Delete button.
- Ensured Citizens can still edit their own pending reports.
- Ensured Citizens can still delete their own reports.
- Kept the Resolve functionality restricted to Representatives.
- Tested the permission system using both Citizen and Representative accounts.

## Testing

### Representative Testing

- Logged in as a Representative.
- Confirmed that the **Edit** button is not visible.
- Attempted to access the Edit URL directly.
- Confirmed that the action was rejected with an authorization message.
- Confirmed that the **Delete** button is not visible.
- Attempted to access the Delete URL directly.
- Confirmed that the action was rejected with an authorization message.
- Confirmed that the **Resolve** button remains available for pending reports.

### Citizen Testing

- Logged in as a Citizen.
- Confirmed that the **Edit** button is visible for pending reports.
- Successfully edited a report owned by the Citizen.
- Confirmed that the **Delete** button is visible for pending reports.
- Successfully deleted a report owned by the Citizen.
- Confirmed that Citizens cannot access the Resolve functionality.

## Security Improvements

Day 33 strengthened the authorization system introduced in Day 32.

The application now uses both **frontend visibility controls** and **backend authorization checks**.

### Frontend

The Issues page displays actions according to the user's role:

- Citizens → Edit and Delete
- Representatives → Resolve

### Backend

The corresponding Flask routes also verify the user's role before performing the action.

This means that hiding a button is not the only security mechanism. A user attempting to manually access a protected URL is also prevented from performing an unauthorized action.

## Current Permission Model

| Action | Citizen | Representative |
|---|---|---|
| Report an issue | ✅ | — |
| Edit own pending issue | ✅ | ❌ |
| Delete own pending issue | ✅ | ❌ |
| Resolve an issue | ❌ | ✅ |

## Files Modified

- `app.py`
- `templates/issues.html`

## Challenges

- Learned that frontend restrictions alone are not sufficient for authorization.
- Learned how to enforce role permissions directly inside Flask routes.
- Tested protected functionality through direct URL access.
- Strengthened the separation between Citizen and Representative capabilities.
- Verified that existing Citizen functionality continued to work after adding role restrictions.

## Phase 2 Status

- ✅ User authentication
- ✅ Registration and login
- ✅ Session management
- ✅ Protected report submission
- ✅ Username stored with reports
- ✅ My Reports feature
- ✅ Report ownership protection
- ✅ Edit authorization
- ✅ Delete authorization
- ✅ Citizen and Representative roles
- ✅ Role stored in session
- ✅ Resolve authorization
- ✅ Representative-only Resolve button
- ✅ Representative blocked from Edit
- ✅ Representative blocked from Delete
- 🔜 Representative dashboard
- 🔜 Advanced report management

## Reflection

Today's work further established CivicBridge as a **multi-user platform with role-based permissions**.

The application now clearly separates the responsibilities of Citizens and Representatives. Citizens can manage their own pending reports, while Representatives are responsible for resolving civic issues.

More importantly, the permission system is enforced at the backend level rather than relying only on the interface. This provides a stronger foundation for building the dedicated **Representative side of CivicBridge** in future sessions.

The next stage can focus on building more functionality around Representatives and their workflow for managing civic reports.


# 🌉 CivicBridge Development Journal – Day 34

**Date:** 21 September 2026

## Objective

Begin building the **Representative side of CivicBridge** by creating a dedicated **Representative Dashboard** where Representatives can monitor the overall state of civic reports and quickly access pending issues.

The dashboard was designed with role-based access control so that only users with the **Representative** role can access it.

## Work Completed

- Added a **Representative Dashboard** link to the navigation bar.
- Made the dashboard link visible only to users with the **Representative** role.
- Created the `/representative-dashboard` route.
- Added authentication protection to the Representative Dashboard.
- Added role-based authorization to prevent Citizens from accessing the dashboard.
- Created the `representative_dashboard.html` template.
- Connected the dashboard to the SQLite database.
- Added live statistics for:
  - Total Reports
  - Pending Reports
  - Resolved Reports
- Passed database statistics from the Flask route to the Jinja template.
- Displayed the statistics as dashboard cards.
- Added a **View Pending Reports** button.
- Connected the button to the existing Pending Reports filter.
- Added CSS styling for the dashboard layout and statistics.
- Centered the **View Pending Reports** button.
- Tested the dashboard using both Representative and Citizen accounts.

## Representative Dashboard

The new dashboard currently provides Representatives with an overview of the reports stored in CivicBridge.

The dashboard displays:

- **Total Reports**
- **Pending Reports**
- **Resolved Reports**

During testing, the database contained:

```text
Total Reports:     6
Pending Reports:   1
Resolved Reports:  5

## Phase 2 Status

✅ User authentication
✅ Registration and login
✅ Session management
✅ Protected report submission
✅ Username stored with reports
✅ My Reports feature
✅ Report ownership protection
✅ Edit authorization
✅ Delete authorization
✅ Citizen and Representative roles
✅ Role stored in session
✅ Resolve authorization
✅ Representative-only Resolve button
✅ Representative blocked from Edit
✅ Representative blocked from Delete
✅ Representative Dashboard
✅ Representative Dashboard authentication
✅ Representative Dashboard authorization
✅ Live report statistics
✅ Pending Reports shortcut
🔜 Advanced Representative dashboard functionality
🔜 Advanced report management

## Reflection

Day 34 marked the beginning of the dedicated Representative side of CivicBridge.
Previously, Representatives mainly interacted with the general Issues page. The new dashboard provides them with a dedicated starting point for monitoring civic reports.
The dashboard is currently simple, but it is already connected to the real SQLite database and displays live information about the current state of reports.
The addition of the dashboard also demonstrates how the role-based authorization system can be extended beyond individual actions such as Edit, Delete, and Resolve.
CivicBridge is gradually moving from a basic civic issue reporting application toward a more structured multi-user platform where different types of users have different responsibilities and workflows.
The Representative Dashboard provides the foundation for adding more advanced management functionality in future development sessions.


# 🌉 CivicBridge Development Journal – Day 35

**Date:** 26 October 2026

## Objective

Enhance the **Representative Dashboard** by displaying actual pending civic reports directly on the dashboard, allowing Representatives to monitor unresolved issues and quickly access their details without navigating to a separate page first.

The objective was to extend the dashboard introduced on Day 34 and make it more useful for managing civic issues reported by the community.

## Work Completed

- Added a database query to retrieve all reports with the **Pending** status.
- Sorted pending reports by ID in descending order so that newer reports appear first.
- Retrieved the pending report records using `fetchall()`.
- Passed the pending report list from the Flask route to the dashboard template.
- Updated `representative_dashboard.html` to display pending reports dynamically.
- Displayed the issue title, location, description, reporter name, and status for each report.
- Used a Jinja2 `for` loop to generate individual cards for pending reports.
- Added conditional handling for situations where no pending reports exist.
- Added an empty-state message for when all reports have been resolved.
- Added a **Manage Reports** link to each pending report card.
- Connected the link to the existing Pending Reports filter.
- Added CSS styling for the pending reports section.
- Styled individual report cards with white backgrounds, rounded corners, shadows, and an amber-colored left border.
- Improved the spacing and readability of the report details.
- Tested the dashboard and confirmed that the new functionality and styling work correctly.

## Pending Reports on the Representative Dashboard

The Representative Dashboard previously displayed statistics and a shortcut to the Pending Reports page.

Today's update allows Representatives to view actual pending report details directly on the dashboard.

Each pending report card displays:

- **Issue Title**
- **Location**
- **Description**
- **Reported By**
- **Status**

The dashboard retrieves these details from the SQLite database rather than displaying hardcoded information.

### Database Query

The following SQL query was added to retrieve pending reports:

```sql
SELECT *
FROM reports
WHERE status = 'Pending'
ORDER BY id DESC;

The query retrieves all columns for pending reports and displays newer reports first, assuming report IDs increase as reports are created.

The fetchall() method is used to retrieve all matching records.

UI Improvements
CSS styling was added to improve the appearance of the pending reports section.

The styling includes:
- White backgrounds for report cards.
- Rounded corners for a cleaner appearance.
- Subtle shadows to distinguish individual cards.
- An amber-colored left border to highlight pending issues.
- Appropriate spacing between report cards.
- Improved readability through margins and line spacing.
- Consistent presentation of report details and the Manage Reports link.
These changes make pending issues easier to identify and review from the dashboard.

Testing
Representative Dashboard Testing
- Logged in using the Representative account.
- Opened the Representative Dashboard.
- Confirmed that the existing report statistics continued to display correctly.
- Verified that pending reports appeared directly on the dashboard.
- Confirmed that each report displayed its title, location, description, reporter name, and status.
- Verified that newer reports appeared before older reports.
- Confirmed that the pending report cards displayed correctly after applying CSS styling.
- Clicked the Manage Reports link.
- Verified that it opened the Pending Reports list.
- Confirmed that the existing dashboard functionality remained operational.
Empty-State Handling
The dashboard template includes conditional logic for situations where no pending reports exist.

When the pending report list is empty, a friendly message is displayed instead of an empty list of cards.

Files Modified
- app.py
- templates/representative_dashboard.html
- static/style.css

Technical Concepts Learned
- Retrieving filtered records from an SQLite database.
- Using SQL conditions to select reports by status.
- Sorting database results using ORDER BY.
- Understanding the difference between retrieving a count and retrieving complete records.
- Using fetchall() to retrieve multiple database rows.
- Passing data from Flask routes to Jinja2 templates.
- Iterating over database records using a Jinja2 for loop.
- Using conditional statements in templates to handle empty results.
- Displaying database-driven content dynamically.
- Styling repeated content using CSS card layouts.
- Connecting dashboard information to existing application workflows.

Challenges
- Extending the existing dashboard without disturbing its report statistics.
- Retrieving complete pending report records while preserving the existing count queries.
- Passing the new data from the Flask backend to the frontend.
- Accessing the correct report fields using their database column positions.
- Displaying multiple reports dynamically rather than using hardcoded content.
- Handling situations where no pending reports are available.
- Integrating the new report cards with the existing dashboard layout and styling.

Reflection
Day 35 further developed the dedicated Representative side of CivicBridge.

On Day 34, the Representative Dashboard was introduced with live statistics and a shortcut to view pending reports. Today's work extended that foundation by displaying actual pending civic issues directly on the dashboard.

Representatives can now see the details of unresolved reports, identify their locations, understand the reported problems, and navigate to the existing issue management page when action is required.


# 🌉 CivicBridge Development Journal – Day 36

**Date:** 29 October 2026

## Objective

Enhance the **Representative Dashboard** by introducing a report status filter that allows Representatives to switch between **Pending** and **Resolved** civic reports without leaving the dashboard.

The objective was to improve report management and make it easier for Representatives to monitor unresolved issues and review completed reports through a dedicated interface.

## Work Completed

- Extended the existing Representative Dashboard functionality.
- Added status selection to the Flask dashboard route.
- Implemented support for retrieving Pending and Resolved reports.
- Added validation to accept only the supported report statuses.
- Updated the SQL query to retrieve reports according to the selected status.
- Passed the selected status and filtered report list from Flask to the Jinja2 template.
- Replaced the pending-only report list variable with a general report list.
- Added **Pending** and **Resolved** filter buttons to the dashboard.
- Made the dashboard heading change dynamically according to the selected status.
- Added conditional styling to highlight the currently selected filter.
- Updated the empty-state message to match the selected report status.
- Added CSS styling for the filter buttons.
- Improved the visual appearance of the filters using spacing, padding, hover effects, and an active state.
- Tested the filtering functionality and confirmed that switching between Pending and Resolved reports works correctly.

## Representative Dashboard Report Filtering

Previously, the Representative Dashboard displayed pending reports directly below the statistics cards.

Although Representatives could access the Pending Reports list through a navigation link, the dashboard did not provide a way to switch between pending and resolved reports within the same page.

Today's update introduced a **report status filtering system**.

Representatives can now select either:

- **Pending** – Displays reports that are awaiting resolution.
- **Resolved** – Displays reports that have already been marked as resolved.

The dashboard retrieves and displays the reports according to the selected status.

## Backend Implementation

### Retrieving the Selected Status

The Flask route was updated to read the selected report status from the URL.

```python
status = request.args.get("status", "Pending")
If no status is provided in the URL, the dashboard defaults to Pending reports.

Status Validation
A validation check was introduced to ensure that only the supported statuses are accepted.

if status not in ["Pending", "Resolved"]:
    status = "Pending"

This ensures that unexpected status values fall back to Pending rather than being used as the selected filter.

UI Improvements
CSS styling was added to make the filter buttons more consistent and visually clear.

The styling includes:
- Flexbox layout to position the buttons horizontally.
- Appropriate spacing between buttons.
- Padding to make the buttons easier to click.
- Rounded corners for a cleaner appearance.
- Hover effects to provide visual feedback.
- A distinct active state for the currently selected filter.
The active state is controlled through a Jinja2 conditional expression, which adds the active class to the button matching the selected status.

This allows Representatives to identify the current filter at a glance.

Testing
Pending Reports Testing
- Logged in using the Representative account.
- Opened the Representative Dashboard.
- Confirmed that Pending reports were displayed by default.
- Clicked the Pending filter button.
- Verified that only pending reports were displayed.
- Confirmed that the Pending button was highlighted as active.

Resolved Reports Testing
- Clicked the Resolved filter button.
- Verified that resolved reports were displayed.
- Confirmed that the dashboard heading changed to Resolved Reports.
- Verified that the Resolved button was highlighted as active.
- Switched back to Pending reports and confirmed that the original report list returned.

UI Testing
- Confirmed that the filter buttons appeared next to each other.
- Verified that the hover styling worked.
- Confirmed that the active filter was visually distinguishable.
- Verified that the existing report cards and dashboard statistics continued to function correctly.

Files Modified
- app.py
- templates/representative_dashboard.html
- static/style.css

Technical Concepts Learned
- Reading query parameters from a URL using Flask's request.args.
- Providing default values for optional URL parameters.
- Validating user-selected values before using them in application logic.
- Retrieving database records dynamically based on a selected filter.
- Using parameterized SQL queries.
- Passing filtered data from Flask routes to Jinja2 templates.
- Reusing a template structure to display different groups of records.
- Dynamically updating headings according to the selected status.
- Applying conditional CSS classes using Jinja2.
- Creating interactive navigation through URL query parameters.
- Styling active filter buttons using CSS.
- Improving the usability of a database-driven dashboard.

Reflection

Day 36 improved the Representative Dashboard by introducing status-based report filtering.

On Day 35, the dashboard was enhanced to display actual pending civic reports as individual cards. Today's work builds on that functionality by allowing Representatives to switch between Pending and Resolved reports without navigating away from the dashboard.

The filtering system connects the URL, Flask backend, SQLite database, and Jinja2 frontend. Representatives select a status, Flask validates the selection, the database retrieves the matching reports, and the template displays the results dynamically.

The interface also provides visual feedback by highlighting the active filter and updating the report section heading. This makes the dashboard easier to understand and use.

The existing authentication and authorization checks remain intact, ensuring that the dashboard continues to be restricted to Representatives.