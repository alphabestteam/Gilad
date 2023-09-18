import requests
import time
import threading


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to execute")
        return result

    return wrapper


@timer
def download_jpg(url: str, number: int) -> None:
    response = requests.get(url)
    content = response.content
    path = f"{number}.jpg"
    with open(path, "wb") as local_file:
        local_file.write(content)


def main():
    first_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png"
    second_url = "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png"
    third_url = (
        "https://github.githubassets.com/images/modules/open_graph/github-mark.png"
    )
    fourth_url = "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"

    url_list = [first_url, second_url, third_url, fourth_url]

    first_thread = threading.Thread(target=download_jpg(first_url, 1))
    second_thread = threading.Thread(target=download_jpg(second_url, 1))
    third_thread = threading.Thread(target=download_jpg(third_url, 1))
    fourth_thread = threading.Thread(target=download_jpg(fourth_url, 1))

    # counter = 0
    # for url in url_list:
    #     counter += 1
    #     download_jpg(url, counter)


if __name__ == "__main__":
    main()
