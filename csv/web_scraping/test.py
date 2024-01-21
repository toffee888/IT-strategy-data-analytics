import requests
from bs4 import BeautifulSoup

def parse_university_ranking(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant elements in the HTML
        university_elements = soup.find_all('tr', class_='uni')

        # Create a list to store the extracted data
        university_data = []

        # Extract information for each university
        for university in university_elements:
            rank = university.find('div', class_='rank').text.strip()
            name = university.find('div', class_='uni_name').text.strip()
            country = university.find('div', class_='location').text.strip()

            # Store the data as a dictionary
            university_info = {
                'Rank': rank,
                'Name': name,
                'Country': country
            }

            # Append the dictionary to the list
            university_data.append(university_info)

        return university_data
    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch content. Status Code: {response.status_code}")

# Example usage with QS World University Rankings
url_qswur = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2023'
rankings_qswur = parse_university_ranking(url_qswur)

# Print the extracted data
for university in rankings_qswur:
    print(university)
