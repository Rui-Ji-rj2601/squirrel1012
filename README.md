Group name and Section: \
Rui & Minxin, Section 001\
Group Member UNI: \
UNIs:[rj2601, mz2820]\

repository: squirrel1012 - October 2020\
Author Name: Rui Ji (rj2601) and Minxin Zhang (mz2820)\
Project for E4501 Tools for Analytics - Fall A 2020 - Columbia University - IEOR\
This is a simple django project with the following functionalities:\
- Importing squirrel data by running\
    python manage.py import_squirrel_data /path/to/file.csv\
- Exporting squirrel data by running\
    python manage.py export_squirrel_data /path/to/file.csv\
- Homepage http://127.0.0.1:8000/ \
    Contains redirecting links to List of Squirrels and Map of Squirrels and some basic information\
- List of Squirrels http://127.0.0.1:8000/sightings/ \
    Contains redirecting links to Stats of Squirrels, Add New Squirrels, Back to Homepage, and Update This Squirrel\
    Has the Unique Squirrel ID, date and update link for all the squirrels in the database\
- Stats of Squirrels http://127.0.0.1:8000/sightings/stats/ \
    Contains some basic Statistical information of the squirrel database\
    Contains a redirecting link to the List of Squirrels Page\
- Add New Squirrels http://127.0.0.1:8000/sightings/add/ \
    Contains a redirecting link to the List of Squirrels Page\
    Has the functionality to add a customized squirrel into the database\
- Update This Squirrel http://127.0.0.1:8000/sightings/Unique_Squirrel_ID/ \
    Contains a redirecting link to the List of Squirrels Page\
    Has all the current information of this squirrel and allows customized update on the current data\
- Map of Squirrels http://127.0.0.1:8000/map \
    Shows the first 100 squirrel locations on the real map\
