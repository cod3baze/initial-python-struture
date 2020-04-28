import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(url , full_path)

path = 'images/'
url = input("URL da imágem: ")
file_name = input("salvar como? (Nome): ")

dl_jpg(url, path, file_name)

