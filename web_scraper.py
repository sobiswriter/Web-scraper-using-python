import requests
from bs4 import BeautifulSoup

def interactive_scrape(url):
    """Interactively scrapes data from a website based on user input.

    Args:
        url (str): The URL of the website to scrape.
    """

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    print("\nAvailable options:")
    print("1. Scrape all headers")
    print("2. Scrape a specific header (by text)")
    print("3. Scrape a header with its paragraph")
    print("4. Scrape all headers with their paragraphs")
    choice = int(input("Enter your choice (1-4): "))

    extracted_data = []

    if choice == 1:
        extracted_data = [header.text for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
    elif choice == 2:
        target_text = input("Enter the header text to search for: ")
        header = soup.find(["h1", "h2", "h3", "h4", "h5", "h6"], text=target_text)
        if header:
            extracted_data.append(header.text)
        else:
            print("Header not found.")
    elif choice == 3:
        target_text = input("Enter the header text to search for: ")
        header = soup.find(["h1", "h2", "h3", "h4", "h5", "h6"], text=target_text)
        if header:
            paragraph = header.find_next_sibling('p')  # Find the next paragraph sibling
            if paragraph:
                extracted_data.append({'header': header.text, 'paragraph': paragraph.text})
            else:
                print("No paragraph found after the header.")
        else:
            print("Header not found.")
    elif choice == 4:
        headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        for header in headers:
            paragraph = header.find_next_sibling('p')
            if paragraph:
                extracted_data.append({'header': header.text, 'paragraph': paragraph.text})

    if extracted_data:
        print("\nExtracted data:")
        for item in extracted_data:
            print(item)
    else:
        print("No data found.")
