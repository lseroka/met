# Project Name
Metropolitan Museum of Art Web Framework

## Purpose
The purpose of this project is to demonstrate how web frameworks can be adopted in museums, libraries and archives as a new way to increase access to museum and archival records. This project builds on the Institute of Museum and Library Services' focus of rethinking collections a data. This project is a digital solutions for library, archive, and museum-related data as a way to engage new users and force users to think about collections in a different way. 

Some of this data exists as item-level records on the MET’s website; however, the website includes a photograph of the image (or a gray image with a no photograph symbol) and some of the metadata.  The museum website values the image of the art more than the metadata, which is made clear by the fact that the image is at the top of the page, and the metadata cannot be seen unless a user scrolls to the bottom of the page. In addition, the image takes up the majority of the page, while the metadata appears in a small font. Alternatively, the Django app emphasize the object’s metadata, rather than the image of the metadata. The Django app also provides a user-friendly way for people to browse the metadata through predefined filters. 

## Data set
This project uses the Metropolitan Museum of Art Open Access Dataset; however, only the highlighted works of art in the dataset are represented in the web framework.  

The dataset can be found at: 
https://www.kaggle.com/metmuseum/the-metropolitan-museum-of-art-open-access 

## Data model

## Package Dependencies

certifi                        2018.10.15  
chardet                        3.0.4  
defusedxml                     0.5.0  
Django                         2.1.1  
django-crispy-forms            1.7.2  
django-filter                  2.0.0  
django-test-without-migrations 0.6  
idna                           2.7  
mysqlclient                    1.3.13  
oauthlib                       2.1.0  
pip                            18.0  
PyJWT                          1.6.4  
python3-openid                 3.1.0  
pytz                           2018.5  
requests                       2.20.0  
requests-oauthlib              1.0.0  
setuptools                     40.4.3  
six                            1.11.0  
social-auth-app-django         3.0.0  
social-auth-core               2.0.0  
urllib3                        1.24  
wheel                          0.31.1  