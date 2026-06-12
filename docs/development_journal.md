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