# Odin Control Adapter Template
[Copier](https://copier.readthedocs.io/en/stable) templated Adapter project for Odin Control.

## Usage Guide:

Uses requires a **Python 3.10 or Newer** environment with Copier installed. This can be a virtual environment.
```bash
pip install copier
```

Once installed, use it to generate your project with the template:
```bash
# Copier can create a new directory for your project. Provide it as the second argument to the "copier copy" command
copier copy gh:stfc-aeg/odin-control-adapter-template projects/new_adapter
```

Copier will then prompt various inputs, with default options, to name the project and fill in the project information. An example of this is shown below.
```
🎤 Name of the Project.
   New Adapter
🎤 Name of the Python package this project will create.
   new_adapter
🎤 Your Name
   Penny Sterling
🎤 Your Email Address
   penny.sterling@example.com
🎤 Short description for the Python Package
   Demo of Template
🎤 The organisation that owns the Github repo for this project
   stfc-aeg
🎤 The URL of the github repo for this project
   https://github.com/stfc-aeg/new_adapter

Copying from template version 1.0.0
    create  README.md
    create  src
    create  src/new_adapter
    create  src/new_adapter/__init__.py
    create  src/new_adapter/controller.py
    create  src/new_adapter/adapter.py
    create  .gitignore
    create  pyproject.toml
    create  .copier-answers.yml
    create  test
    create  test/config
    create  test/config/odin.cfg
    create  test/static
    create  test/static/index.html


```
> [!NOTE]
> Some of these will have default values already filled in, based on previous answers.
> For instance, the email field will be generated from whatever was entered in the "Your Name" field.


## Installing the Project
It is recommended that Odin Control projects are installed into Virtual Environments specific for each project.
You can create this venv with whatever tools you prefer. The standard method is shown here as an example:

```bash
# If an alternate Virtual Environment was used for the previous step, deactive it
deactivate
# Move into the project directory.
cd projects/new_adapter
# Create the Venv using the standard tools from Python.
virtualenv new-adapter
# Activate the Virtual Environment
source new-adapter/bin/activate
```

We can then install the project into the virtual enviroment, where it will also install the required dependencies.

```bash
# First, ensure the project is a valid Git Repo, so that the tools to generate versioning tags can function.
git init
# Then, install the project in Editable Mode, so that any changes made are automatically updated in the instaled package.
pip install -e .
```
### Expected output:
```
.....
Successfully built new-adapter
Installing collected packages: tornado, psutil, odin-control, new-adapter
Successfully installed new-adapter-0.0.post1.dev0+d20261006 odin-control-2.1.0 psutil-7.2.2 tornado-6.5.10
```

> [!NOTE]
> Some version numbers may be different, depending on development of the required packages.
> This should not cause any issue, but be sure to check the [Odin Control Documentation](https://odin-detector.github.io/odin-control/) and
> [Release Page](https://github.com/odin-detector/odin-control/releases) for information about any changes.


## Running the Project
See the [Odin Control Docs](https://odin-detector.github.io/odin-control/getting-started/) for detailed info on running and interacting with Adapter projects.

```bash
odin_control --config test/config/odin.cfg
```
### Expected output:
```
[D YYMMDD hh:mm:dd selector_events:54] Using selector: EpollSelector
[D YYMMDD hh:mm:dd base_adapter:61] NewAdapterAdapter loaded
[D YYMMDD hh:mm:dd api:101] Registered API adapter class NewAdapterAdapter from module new_adapter.adapter for path new_adapter
[D YYMMDD hh:mm:dd adapter:72] NewAdapterAdapter initialize called with 1 adapters
[D YYMMDD hh:mm:dd controller:31] Adapters initialized: []
[W YYMMDD hh:mm:dd default:32] Static path for default handler is test/static
[I YYMMDD hh:mm:dd server:85] HTTP server listening on 127.0.0.1:8888
```

## Updating from the Template

Copier can be used to [update a project](https://copier.readthedocs.io/en/stable/updating/) after creation. This can be used to make changes to the answers given when first creating the project, or copy updates made to the template.

Ensure any current changes have been commited to Git, and then run the following command from within the project directory:

```bash
copier update
```

This will show the prompts for input again, with the already entered values. These values can be altered, and Copier will attempt to update the project with the new values and any updates made to the template.

> [!WARNING]
> Depending on your development, this may cause Conflicts. Be sure to check your project for any inline Conflict markers after this step.
> See the [Copier Docs](https://copier.readthedocs.io/en/stable/updating/) for more information.

