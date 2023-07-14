import requests
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

def download_segment(url, start_byte, end_byte, segment_index):
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 206:  # Partial Content (successful segment download)
        with open(f'segment{segment_index}.bin', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Error downloading segment {segment_index}')

def download_file(url, num_segments):
    response = requests.head(url)
    file_size = int(response.headers['Content-Length'])
    segment_size = file_size // num_segments

    num_workers = multiprocessing.cpu_count()  # Use available CPU cores
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_segments):
            start_byte = i * segment_size
            end_byte = start_byte + segment_size - 1 if i < num_segments - 1 else None
            executor.submit(download_segment, url, start_byte, end_byte, i)

    print('File download completed!')

# Example usage
file_url = 'https://example.com/file_to_download.bin'
segments = 4  # Number of segments to split the file into

download_file(file_url, segments)
