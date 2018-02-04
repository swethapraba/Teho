# Teho

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
  - static folder: contains javascript and css files
