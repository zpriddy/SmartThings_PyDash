
# SmartThings PyDash
##### Credits:
*Credit given to: FlorianZ for hadashboard [https://github.com/FlorianZ/hadashboard]*

## Requirements
*pydashie*


## ?. Install the SmartApp
Navigate to https://graph.api.smartthings.com and log in to your SmartThings IDE account. Select the **'My SmartApps'** tab, and click the **'+ New SmartApp'** button to create a new SmartApp.

Fill in the required information. The **'Name'** and **'Description'** are both required fields, but their values are not important.

Make sure to click the **'Enable OAuth in Smart App'** button to grant REST API access to the new SmartApp. Note the **'OAuth Client ID'** and **'OAuth Client Secret'**. Both will later be required by the Dashing backend to authenticate with the new SmartApp and talk to SmartThings.

Hit the **'Create'** button to get to the code editor. Replace the content of the code editor with the content of the file at: `Documents/ZP_PyDash_Access.groovy`

Click the **'Save'** button and then **'Publish -> For Me'**.

## ?. Configure oauthin.json File
Copy the sample_oauthin.json from the Documanets folder to the ZP_PyDash folder on your host/server and rename it oauthin.json. Once copied open the file in a text editor and past the **'OAuth Client ID'** and **'OAuth Client Secret'** from the last step. Also if you are not going to be running this as localhost, enter the server hostname/ip/url here. (If you want to chnage the port you will have to chnage it in another spot as well..)


## Usage
````
To Come
````
## Info



## Notes


