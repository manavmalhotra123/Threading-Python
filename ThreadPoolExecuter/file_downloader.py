import threading 
from concurrent.futures import futures
import requests


def download(url):
    response = requests.get(url,stream = True)
    file_name = url.split('/')[-1]
    with open(file_name,"wb") as file:
        for chunk in response.iter_content(chunk_size= 8192):
            if chunk:
                file.write(chunk)
    print("File downloaded")


file_url = ""

# creating three worker threads for the download
executor = futures.ThreadPoolExecutor(max_workers= 3)


# submit the function you want to execute along with the input to that function
future = executor.submit(download,file_url=file_url)

# waiting for the download to complete
futures.wait([future])

executor.shutdown()