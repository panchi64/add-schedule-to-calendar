# About
This script uses Selenium in order to scrape the UPRM portal website and generate an `.ics` file containing class' schedules. This file can be imported to any calendar application. 

*NOTE*
The application does not gather or store any information other than the courses found, your log-in information is never touched.

(The courses are removed from memory once the application closes, feel free to look at the source code :D)

## How to use
If using the `.exe` file in the [Releases](https://github.com/panchi64/add-schedule-to-calendar/releases) page. You just have to log in once the page opens.

If running the python script directly:
- Please make sure you have all of the dependencies installed. These dependencies are listed below:
  - Use `pip install [dependency name]` to installed the dependency (if `pip` doesn't work try using `pip3`)
    - selenium
    - pytz
    - os
    - icalendar
    - datetime
    - dateutil
    - pathlib

