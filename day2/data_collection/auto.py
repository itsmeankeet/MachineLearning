# kk library chayenxa bhney
# web ma request garena 'request"library use garera 
# '200'respond ayo bhney sucessfull

# import necessary library

import requests
import os

# image haru sab data_collection bhitra download garney 
# os chai kun file directory ma download garera save garney and to get the path of working directory

# url pass garney ani image haru search garney hai 
#flickr ma photo search garna function banauney 
# provide the url of the image(Link)


def search_flickr(query,api_key,num_images):
    #pass the url
    url = "https://api.flickr.com/services/rest/"

    #parameter kk chayeo tw? 
    #api search garda kk parameter pass garney bhney ho hai params chai 
    #url pathaye paxi parameter haru pani pass garney ho hai 
    params = { 
        "method": "flickr.photos.search",
        #yo bhneko chai api lai hamlae photo search garney bhneko ho 
        #api lae multiple function haru support garxa tra hamlae aaila chai image haru search matra garney ho hai 
        #api method to search the photo

        "api_key": api_key,
        #yo bhneko chai api key pass garney bhneko ho 
        #api key is a unique identifier for the application that is making the request
        #api key is a string of characters that is used to authenticate the application with the api

        "text": query,
        #yo bhneko chai text pass garney bhneko ho 
        #text is the keyword that is used to search the photo
        #k search garney bhneraw ho hai for example "dog" "cat" "bird"

        "tags" : "bird",
        #yo bhneko chai tags pass garney bhneko ho 
        #tags is the keyword that is used to search the photo
        #k search garney bhneraw ho hai for example "bird" "cat" "dog"

        "sort" : "relvance",
        #yo bhneko chai sort pass garney bhneko ho 
        #sort is the keyword that is used to sort the photo
        #katiko milxa search query ko aadhar ma image haru lai sort garxa 
        # dherai relevant haru mathi hunxa thorai relevant bhako image haru tala hunxa 

        "per_page": num_images,
        #yek choti ma kati ota image return garney bhneko ho 
        #malai 100  ota chayeko bhye 100 rakhey tesko valye

        "format": "json",
        #malai payeko respond chai json format ma chayeoo bhneko hai 
        #python ma json format lai tukrauna sajilo huney bhyerw json file ma rakhney

        "nojsoncallback": 1,
        # hamlai pure json ma file chayene bhyeraw 
        #json file ma aaye python ma handle garnu sajilo huunxa 
    }
    response = requests.get(url, params=params)
    # server bata kei data lenu "get" method
    #url bhneko hamlae use garney url rw params ma aagi ko parameter 
    # server ma kunai data rakhnu "Put " method
    # aba response aauxa hamlae tyo response check garxam
    # yedi response 200 xah bhney chai sucessfull hunxa  hai 
    
    # we need to check for permission (request successful or not)
    #if status code is 200 then we can proceed with the next step

    if response.status_code == 200:
        #if status code is 200 then we can proceed with the next step

        #response.json() is a function that returns the json data of the response(converts to python dictionary)
        #response.json()['photos']['photo'] is a list of dictionaries that contains the photo data
        #convert the json response from api/web into python dictionary
        return response.json()['photos']['photo']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []
        # kinw empty list return garera bhnda kinw ki function lae wait nagaros bhneraw empty list return garney 

# phtoto download garna photo ko url extract garnu paryo 
# extract the url of the photo

#this get the url of the photo
def get_photo_url(photo,size= "large"):
    #base url of the photo
    url = f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}"
    # yo chai base url ho hai 
    #flickr ma yesari image haru save hunxa hai tyo bhyeraw yesto gareko ho 

    # append size suffix 
    # image download garda kasto size ko download garney bhneraw ho hai 
    if size == "large":
        url += "_b.jpg"
        #large rayexa bhney _b aauxa 
    elif size == "medium":
        url += "_z.jpg"
        #medium rayexa bhney _z aauxa 
    else:
        url += "_n.jpg"
        #small rayexa bhney _n aauxa 
    return url
##aba last kam bhneko image download garney

def download_image(photo_list, directory):
    #create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i,photo in enumerate(photo_list):
        # i ma chai index aauxa 
        # photo ma chai actual photo aauxa 
        # image download garna image ko url chayeoo 

        img_url = get_photo_url(photo)

        #construct the path of the image
        # image ko name

        img_path = os.path.join(directory, f"image_{i+1}.jpg")

        #save the image now

        with open(img_path, "wb") as img_file:
            img_file.write(requests.get(img_url).content)

#define a main function
def main():
        #what to search 
    query = 'bird'
    api_key = "be94a96ec5b9e57043760e60c7fc0300"
    num_images = 100


    photo_list = search_flickr(query,api_key,num_images)

    download_image(photo_list,'bird_images')
    print(f"Downloaded {len(photo_list)} images to {os.path.abspath('bird_images')}")

if __name__ == "__main__" :
    main()