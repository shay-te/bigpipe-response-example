# Bigpipe Response Example

Example project for the [Bigpipe Response](https://github.com/shacoshe/bigpipe-response)


### Start the project
1. Install dependencies `pip3 install -r requirements.txt`
2. Start django by running `PYTHONPATH=. python3 bigpipe_response_example/manage.py`
3. Open browser on address `http://localhost:8080`
 

### project structure:

- `bigpipe_response_example`    
Folder containing django project 

- `bigpipe_response_example.bigpipe_response_example.views`    
Example view file containing the examples  

- `client`    
All client assets. javascript, react, scss
 
- `data`   
Data dao object to render into components

- `public`     
Static content directory. Bigpipe Response will render assets into this folder

- `config`     
This example is using [Hydra](https://hydra.cc/) to configure bigpipe, demo data as well django server port.

### Demo view 

Open the file `bigpipe_response_example/bigpipe_response_example/views/view_demo.py`



### 
Building with docker 

```bash
docker build -t bigpipe_respose_example .
docker run -p 8080:8080 bigpipe_respose_example
```
