#import necessary libraries
import requests
import os

#define to search for photos in flickr

def search_flickr(query,api_key,num_images):
    #url
    url="https://api.flickr.com/services/rest/"
    params={
        "method":"flickr.photos.search", #api method to search for photos
        "api_key":api_key,
        "text":query,
        "tags":query,
        "sort":"relevance",
        "per_page":num_images,
        "format":"json",
        "nojsoncallback":1
    }
    response=requests.get(url,params=params)
    #print(response)

    #check if the request is successful
    if response.status_code == 200:
        # response.json() converts the json response from api/web into python dictionary
        return response.json()['photos']['photo']
    else:
        print('failed to fetch data')
        return []
#extract the url of the photo
def get_photo_url(photo,size='large'):
    #base url of the photo
    url=f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}"

    # append size suffix
    if size=='large':
        url += '_b.jpg'
    elif size=='medium':
        url += '_z.jpg'
    else:
        url += '.jpg'
    return url

# download images
def download_images(photo_list,directory):
    #create a new folder if it doesnot exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i,photo in enumerate(photo_list):
        img_url = get_photo_url(photo)

        #construct the path of the image
        img_path = os.path.join(directory,f"image_{i+1}.jpg")
    #save the image
        with open(img_path,'wb') as img_file:
            img_file.write(requests.get(img_url).content)
#define a main function
def main():
    #search image needed  
    query=input("Enter the image you want to search for: ")
    api_key='608271e250f04b2ba6f965dd20a0b073'  
    # number of images
    num_images=int(input("Enter the number of images you want to search for: "))
    photo_list=search_flickr(query,api_key,num_images)
     
    if photo_list:
        download_images(photo_list, f"{query}_images")
    else:
        print("No images found or there was an error fetching images.")


if __name__ == "__main__":
    main()