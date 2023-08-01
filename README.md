# StreamlitTemplate

Repo is a quickstart for a multi-page Streamlit App. 

## Snowflake Credentials and Environment Variables
In order to log into Snowflake you will need to have a `secrets.toml` in a folder called `.stremlit`. 
If the file is missing from the folder you just need to create a new file named `secrets.toml` containing

```angular2html
[snowflake_ms_lab_temp_check]
user = "firstname.surname@stanlib.com"
password = ""
account = "oj65307"
region = "eu-west-1"
authenticator = "externalbrowser"
warehouse = "LAB_MULTISTRAT_ANALYTICS_WH"
database = "LAB_MULTISTRAT_ANALYTICS"
schema = "TEMP_CHECK"
```

**NB/** *This is how you add any other environment variables to Streamlit beyond just snowflake*

When loading an app to run on a remote server, rather than on your local computer, there is an input area for secrets.

## Structure

```angular2html

+- .streamlit/
|-- config.tomml
|-- secrets.toml
+- data/
+- pages/
|-- 1_app1.py
|-- 2_app2.py
+- jeeves/
|-- helper_functions.py
|-- app1_helper.py
+- dashboard.py
+- notebooks/
+- requirements.txt
+- other stuff...
```

The *main* app in our Streamlit dashboard is the `dashboard.py` which can be renamed to anything. 
It will be the loading page when you run the command.

```angular2html
streamlit run ./dashboard.py
```

All other apps contained in the `pages/` folder will be loaded via the sidebar.

Streamlit allows some basic cofiguration settings via `config.toml` in the `.streamlit/` directory. 
Config covers a limit amount of styling which Streamlit allows you to do such as primary color and user stats.
Frankly, those options aren't good enough for most purposes although they can be hacked via CSS.

In the imports in the dummy dashboard file are

```angular2html
from assets.streamlit_style_hack import streamlit_boilerplate, PLOTLY_KWARGS
streamlit_boilerplate("App Title")
```

In the `assets/` directory we've built a boilerplate function which:
* names the app
* decides on wide or skinny page formatting
* uses some CSS to update some themes
* updates the default plotly theme to our own
* leaves room for other edits

For more detailed information on this look in the `assets/` folder itself

Otherwise:
* `notebooks` isn't required by Streamlit at all but is a useful store for Jupyter Notebooks
* `requirements.txt` is just a super basic outline for venv
