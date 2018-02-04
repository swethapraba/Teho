# Teho

# Flask Info
Everything must be in a single directory (directory name is Teho)
  - Application must exist in a package (package name is teho_package)
    - package definition: Subdirectory with an __init__.py file (+some other garbage later on)
      - __init__.py file: will define what symbols package will expose to outside world
        - __name__: python pre-defined variable passed to flask to set name of module it is used in (in our case, teho)
          - location of module passed here is the starting point that flask uses to load associated resources (ex: template files)
        - teho variable is a member of the app class
        - routes module imports the teho variable defined in the script
          - make sure to include reciprocal import in bottom of __init__ file to avoid mutual reference errors between the files __init__ and routes (ex: from teho_package import routes)
      - routes:
        - defined as different url's the application implements
        - have handlers called view functions which are mapped to root url's so flask knows which logic to execute when client requests url
      - routes.py file: contains view functions
  - top level python script that defines flask application instance (script name is flask_script.py)
    - templates folder: contains html files
      - inside index.html:
        - placeholders for the dynamic content, enclosed in {{ ... }} sections. These placeholders represent the parts of the page that are variable and will only be known at runtime.
        - The operation that converts a template into a complete HTML page is called rendering. To render the template I had to import a function that comes with the Flask framework called render_template(). This function takes a template filename and a variable list of template arguments and returns the same template, but with all the placeholders in it replaced with actual values.
        - The render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework. Jinja2 substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.
  - static folder: contains javascript and css files
