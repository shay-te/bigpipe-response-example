# Bigpipe Response Example

Example project for the [Bigpipe Response](https://github.com/shacoshe/bigpipe-response)


### Start the project
1. start django by running `python manage.py`
2. open browser on address `http://localhost:8080`
 

### project structure:

- `bigpipe_response_example`    
folder containing django project 

- `bigpipe_response_example.bigpipe_response_example.views`    
example view file containing the examples  

- `client`    
all client assets. javascript, react, scss
 
- `data`   
data dao object to render into components

- `public`     
static content directory. Bigpipe Response will render assets into this folder

- `config`     
this example is using [hydra](https://hydra.cc/) to configure bigpipe, demo data as well django server port.
   
- `hydra_plugins`
tell hydra where to look for bigpipe config file.


### Demo view 

open the file `bigpipe_response_example/bigpipe_response_example/views/view_demo.py`


