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