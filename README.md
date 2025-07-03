# odin-control-adapter-template
CookieCutter templated repo for setting up a new odin-control adapter, for usage with Github action or to be used as a template with cookiecutter on terminals.


## Github Action usage - For members of STFC-AEG organisation in the "dssg_developers" team:

1) Click on actions within the odin-control-adapter-template
2) Click on "Create odin-control Adapter Repo" workflow
3) Look for box with "This workflow has a workflow_dispatch event trigger." and a "Run workflow" dropdown
4) Click "Run workflow" choose the workflow from a branch (main only currently), input the required information into the form
5) New Adapter repo created!

## Manual adapter creation - For all users:

```bash
# Create virtual environments, one for cookiecutter to install into,
# we can delete this later, one to isntall the created odin-control package into
# Alternatively, use pipx to run cookiecutter without creating a virtualenv if installed on your machine
mkdir dir_name
cd dir_name
virtualenv cc
virtualenv adapter
source cc/bin/activate

# Install cookiecutter
pip install cookiecutter

# Create adapter directory
mkdir odin-adapter
cd odin-adapter

# Initialize git repository
git init

cookiecutter gh:stfc-aeg/odin-control-adapter-template
```
### Expected output: 
Here you can see the inputs and the auto-generated defaults from the package name input, new_adpater is generated for the package name, and NewAdapter for the class prefix, as these prompts show, if you are happy with the default value just press enter, else enter a string to override the default generated value.
```
[1/10] project_name (Package Name): new adapter
[2/10] project_slug (control):
[3/10] package_name (new_adapter):
[4/10] class_prefix (NewAdapter):
[5/10] author_name (Your Name): Josh Harris
[6/10] author_email (your.email@example.com): josh.harris@stfc.ac.uk
[7/10] description (Package description): Creating new odin-control adapter
[8/10] python_requires (3.10):
[9/10] github_org (stfc-aeg):
[10/10] github_url (https://github.com/stfc-aeg/new_adapter/control):
```


```bash
deactivate
rm -rf ../cc
source ../adapter/bin/activate
cd control
pip install --upgrade pip
pip install -e .
```
### Expected output:
```
.....
Successfully built new_adapter odin-control
Installing collected packages: tornado, pyzmq, psutil, future, odin-control, new_adapter
Successfully installed future-1.0.0 new_adapter-0.0.post1.dev0+d20250703 odin-control-1.5.0 psutil-7.0.0 pyzmq-27.0.0 tornado-6.5.1
```

```bash
odin_control --config web/config/odin.cfg
```
### Expected output:
```
[D 250703 14:20:28 selector_events:59] Using selector: EpollSelector
[D 250703 14:20:28 base_adapter:27] NewAdapterAdapter loaded
[D 250703 14:20:28 api:145] Registered API adapter class NewAdapterAdapter from module new_adapter.adapter for path new_adapter
[D 250703 14:20:28 base_adapter:31] NewAdapterAdapter initialize called with 1 adapters
[D 250703 14:20:28 controller:23] Adapters initialized: []
[W 250703 14:20:28 default:38] Default handler static path does not exist: web/static
[I 250703 14:20:28 server:78] HTTP server listening on 127.0.0.1:8888
```

```bash
http get 127.0.0.1:8888/api/0.1/new_adapter
```

### Expected output:
```
HTTP/1.1 200 OK
Content-Length: 28
Content-Type: application/json; charset=UTF-8
Date: Thu, 03 Jul 2025 13:21:46 GMT
Etag: "d0ac11012c5651469a98785c95dbc896119b1c0a"
Server: TornadoServer/6.5.1

{
    "example_param": "Example"
}
```
