# Usage
This section will guide you through to finish setting up Web Portal. It assumes you have gone through the install wizard and have the app running.

After finishing the install wizard you will either be met by the public dashboard or a login screen, this will depend on what you set the "Public Portal" setting to.

> This guide will not show any setup of plugins other than the "Core" & "Core-Extras" plugin.

> Please read the whole guide, to understand all base functionality


## Terminology
### The Public User
Web Portal and the documentation reference a user with the username of "public". This is a virtual account, which only admins can access. It is used to provide a dashboard for when the dashboard is in public mode, and it will also be used when a user has not configured their own dashboard.

### Core
When "Core" is referenced it means the "Core" plugin, which is the plugin built-in to Web Portal. It can also be removed if needed.

### Core-Extras
When "Core-Extras" is referenced it means the "Core-Extras" plugin, which is the plugin built-in to Web Portal. It can also be removed if needed.


## Logging In
To login click on the "Log In" button at the top navigation bar. Use the admin credentials you setup earlier.


## The Dashboard
This is where widgets will be displayed. It is the homepage (or index page) of Web Portal.

- During the install if you set the portal as private you will have to login to see it
- After installing, this page will be blank
- Unless a user has created their own dashboard, they will see the inherited "public" user's one.


## Accessing User Settings
Now you are logged in you should navigate to the user settings page. Click on the cog icon in the top navigation bar.

Once loaded you should see the page welcoming you by your username.

From this page you can access the following:

- Dashboard Settings
- Administrations (if logged in as a admin)
- Plugin Settings

If you want to override the public dashboard for the current user click on the "Create Custom" button which will then allow the currently logged in user to create their own dashboard.

If you have a dashboard this button will be called "Editor" instead. You can reset back to the public dashboard by clicking "Restore To Defaults".


## Accessing Administration Settings
Once at the "Administration" page. We have the following options:

- Plugin Settings - Takes you to the same as the standard plugin settings button
- Switch To Public - Switch to the Web Portal virtual public account, this can also be accessed in the user management page under "Force Login".
- Users - Takes you into a manage users page; allowing for you to add new users, modify existing ones and force login to standard account users. It also display a table of all users currently registered with their corresponding management buttons.
- Import V1 Widgets - Import links from Web Portal V1 (only works when Core plugin is installed)


## Dashboard Editor
Inside the dashboard editor we can add new widgets and manage our currently placed ones.

- If you want to access the public dashboard navigate to: `Settings > Administration > Switch To Public`
- Creating a dashboard for a user will override the "public" one

### Add Widget
Depending on what plugins you have installed you may have more options. However You can add a widget to the dashboard by selecting the widget type and giving it a name (this will show up in the widgets header if enabled).

> Core widgets are spoken about in the "Plugin - Core" section

> Core-Extras widgets are spoken about in the "Plugin - Core-Extras" section

### Manage Placed Widget
Once a widget has been placed, the dashboard editor will display the widgets and their corresponding management buttons (Edit, Delete).

Clicking on the "Edit" button will take you to the widgets edit page, depending on how the plugin is implemented it may look different to the Web Portal theme.


## Plugin Settings
This page allows the management of plugins. If you are an admin you may see more options.

Each plugin is listed, with a link to it's plugin settings.

### Missing Plugins
Removing a plugin from the plugin folder while the Web Portal is shutdown will only prevent it from being loaded, Web Portal will recognise it as missing.

To truly remove it you will need to deregister the plugin after you have removed it from the plugin folder. This can be done from "Plugin Settings" and navigating to the "Missing Plugins" section (which will appear once a plugin is not found) and pressing the delete button.

Please note before removing a plugin, you may need to tell the plugin it is being removed (this depends on the plugin), as any data that is controlled by the plugin and not Web Portal will **not** be removed.

> If a plugin has failed to load it will also appear in the "Missing Plugins" section


## Plugin - Core
The Core plugin which is built-in to Web Portal (unless you removed it). It provides several widgets which are listed below:

- Digital Clock - A digital clock which also displays the date
- Links - The links widget allows for placement of customisable links
- Web Search - Add your own search engine to search the internet

### Administration Settings
This plugin also has a management page, which is accessed from the "Plugin Settings" page. It has the following sub pages:

- Engine Management - Allows admin to add search engines which can be selected from the search widget
- Links Management - Allows admin to add links which can be selected from the links widget
- Upload Icons - Allows admin to upload icons which can be used in the links widget for a app icon

### Widget Editor (In Dashboard)
Some widgets included in this plugin allow you to configure them.
#### Links
In the widget editor you can place links onto the widget. These links have to be added by an admin first, by going to the plugin "Administration Settings" page and navigating to "Links Management".

You may also set "Compact Links" configuration which allows the links widget to display in a compact format, useful for when you have lots of links.

#### Web Search
In the widget editor you to select a specific search engine. These search engines have to be added by an admin first, by going to the plugin "Administration Settings" page and navigating to "Engine Management".

## Plugin - Core-Extras
The Core-Extras plugin which is built-in to Web Portal (unless you removed it). It provides several widgets which are listed below:

- Embed HTML - Embed some custom HTML code (also known as injection)
- Embed Website - Embed a website by providing its url, uses an iframe so may not work with all sites


## Plugins
Web Portal works by implementing a plugin system allowing for different widgets to be installed.

Plugins are stored in a plugins folder, this plugin system allows you to easily install a new plugin (or remove) without requiring Web Portal to be re-installed.

### Add
To install a plugin into this folder follow these steps:

1. Ensure Web Portal is shutdown
2. Ensure plugin loader is enabled (set by the environment variable)
3. Ensure "plugins" directory has a empty file called `__init__.py` in it.
4. Copy/Move plugin package into folder
5. Startup Web Portal
6. Plugin should now be registered

### Remove
To remove follow these steps:

1. Follow any steps given by the plugins guide
2. Ensure Web Portal is shutdown
3. Move/Delete the specific plugin package from the "plugins" directory
4. Startup Web Portal
5. Go to `"Plugin Settings" > "Missing Plugins"` (as admin) to remove plugin data

### Where Is The Plugins Directory?
Assuming you are running the official Docker image; Web Portal is structured as shown below:

```
data/
    ...

app/
    web_portal/
        ...

    plugins/
        core
        core_extras
        another_plugin
        ...
```

To add plugins you can mount a volume as shown below using Docker Compose:

```yml
# filepath: docker-compose.yml
volumes:
  - ./data:/app/data
  - ./plugins:/app/plugins
```

> IMPORTANT: When you mount the plugins folder as a docker volume it will disable the built-in plugins provided by the image.


## The End
This is the end of the usage tutorial for Web Portal, maybe checkout the upgrading and migrating guide next [here](upgrading.md)
