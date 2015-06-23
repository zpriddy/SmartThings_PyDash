
# SmartThings PyDash
##### Credits:
*Credit given to: FlorianZ for hadashboard [https://github.com/FlorianZ/hadashboard]*


## Requirements
To run SmartThings PyDash, you'll need the python packages specified in [requirements.txt](./requirements.txt). Note that this application is built on [pyDashie](https://github.com/evolvedlight/pydashie) and and so has the same runtime requirements. Those packages are:

````
*flask>=0.9
*CoffeeScript
*requests
````
You can install those from the root of this project by running

`pip install -r requirements.txt`

from the project root.


## Developing
*If you aren't planning on contributing to this project, skip to the next section, "Install the SmartApp"*

### Required
*[NPM](https://docs.npmjs.com/getting-started/installing-node)
*[Grunt](http://gruntjs.com/)

### Recommended
*[virtualenv](https://pypi.python.org/pypi/virtualenv)
*[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

Once the above requirements are in place on your system (and, optionally, you're in a virtual environment), run `npm install` from the root of the project.

Next, run `grunt`. You can check the Gruntfile.js for the details, but basically this will find all the .scss files throughout the project and compile them into a single application.css file.

To customize styling, edit the .scss files found throughout the project. There's one with each widget in ZP_PyDash/widgets, as well as the main one under ZP_PyDash/assets/stylesheets/application.scss.

````
NOTE: Suggested future enhancement is to make these scss files more "locked down", and then offer a "custom.css" file or similar that will be gitignored, and will get concatenated onto the end of the compiled application.css. This will make it easier for novices to clone the project and do a little style customizing without having to dig around, and without having their customizations wiped out if they update.
````

## Install the SmartApp
Navigate to https://graph.api.smartthings.com and log in to your SmartThings IDE account. Select the **'My SmartApps'** tab, and click the **'+ New SmartApp'** button to create a new SmartApp.

Fill in the required information. The **'Name'** and **'Description'** are both required fields, but their values are not important.

Make sure to click the **'Enable OAuth in Smart App'** button to grant REST API access to the new SmartApp. Note the **'OAuth Client ID'** and **'OAuth Client Secret'**. Both will later be required by the Dashing backend to authenticate with the new SmartApp and talk to SmartThings.

Hit the **'Create'** button to get to the code editor. Replace the content of the code editor with the content of the file at: `Documents/ZP_PyDash_Access.groovy`

Click the **'Save'** button and then **'Publish -> For Me'**.

## Configure oauthin.json File
Copy the 'Documents/sample_oauthin.json' to the 'ZP_PyDash/oauthin.json' on your host/server. Once copied open the file in a text editor and past the **'OAuth Client ID'** and **'OAuth Client Secret'** from the last step. Also if you are not going to be running this as localhost, enter the server hostname/ip/url here. (If you want to chnage the port you will have to chnage it in another spot as well..)


## Usage
````
run: python main.py

open your browser and goto http://localhost:5000/ 
````
*If you chnaged the host url/IP replace the localhost with that IP. On first run the app will do the smartthings auth as long as you compleated oathin.json.*

## Info

## Sample Images
![alt text](https://raw.githubusercontent.com/zpriddy/SmartThings_PyDash/master/Documents/Images/ZP_SmartThings_PyDash1.png "Main Page")
![alt text](https://raw.githubusercontent.com/zpriddy/SmartThings_PyDash/master/Documents/Images/ZP_SmartThings_PyDash2.png "Dimmer Level")
![alt text](https://raw.githubusercontent.com/zpriddy/SmartThings_PyDash/master/Documents/Images/ZP_SmartThings_PyDash3.png "Sensors")

## Notes


## To Do:
*Add a Update All devices function - This will make it so all devices are updated in only one call..*


