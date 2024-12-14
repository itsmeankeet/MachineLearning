import os
import requests


def search_image(query, api_key, num_images):
    url = "https://api.flickr.com/services/rest/"
    params = {
        "method": "flickr.photos.search",
        "api_key": api_key,
        "text": query,
        "per_page": num_images,
        "format": "json",
        "nojsoncallback": 1,
        "tags": query,
        "sort": "relevance",
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['photos']['photo']
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def get_photo_url(photo, size="large"):
    url = f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}"
    if size == "large":
        url += "_b.jpg"
    elif size == "medium":
        url += "_m.jpg"
    elif size == "small":
        url += "_n.jpg"
    return url


def download_image(photo_list, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i , photo in enumerate(photo_list):
        url = get_photo_url(photo)
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(directory, f"image_{i+1}.jpg"), "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download image {i}: {response.status_code}")


def main():
    api_key = "be94a96ec5b9e57043760e60c7fc0300"
    query = str(input("Enter the name of the image: "))
    num_images = int(input("Enter the number of images to download: "))

    photo_list = search_image(query, api_key, num_images)
    download_image(photo_list, f"{query}_images")

if __name__ == "__main__":
    main()
