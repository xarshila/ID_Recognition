# Georgian ID Card Reader #
![template](https://i.ibb.co/S6dpm5w/id-template-front.png)

# How To Run(Docker Image): #
```console
$ sudo docker run -p 8080:8080 -it id-reader:0.0.1
```
### NOTE: ###
id-reader:0.0.1 is our tag of docker image you can build it using different tag 

# How To Run(without docker): #
all what is need to run Georgian Id Card Reader server is:  
```console
$ export FLASK_APP=./app.py  
$ python3.6 -m flask run  --port=8080 --host=0.0.0.0
```
this will launch flask server on 8080 port  
NOTE:  
    if you have any errors here check Dockerfile to install required  
    modules (flask, tesseract, tesseract-ka, opencv, and so...)  

# How To USE: #
### wget: ###
```console
$ wget --post-file=pattern.jpg http://localhost:8080/read
```

# Response: #
```
{
    "name_en": "SAXELI",
    "name_ge": "სახელი",
    "last_name_en": "GVARI",
    "last_name_ge": "გვარი"
    "birth_date": "23.05.1967", 
    "card_id": "", 
    "exp_date": "1511212021",
    "nation": "GEO", 
    "person_id": "", 
    "sex": "F"
}
```