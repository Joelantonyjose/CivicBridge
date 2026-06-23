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