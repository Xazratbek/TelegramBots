# import requests
# from bs4 import BeautifulSoup

# # Replace with the URL of the website you want to access
# url = 'https://www.threads.net/@samar_badriddinov/post/Cxf4xKQMSpq'

# # Replace 'your_session_id' with your actual session ID
# session_id = '38322609809%3ApoGeHSAo91ecPj%3A27%3AAYegUtdiU7rVv97qe7-S04uZsrVXQR93DMMfksFOiQ'

# # Create a session object to persist cookies across requests
# session = requests.Session()

# # Add your session ID as a cookie to the session
# session.cookies.set('sessionid', session_id)

# # Send a GET request to the website
# try:
#     response = session.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content
#         with open('index.html','w') as index:
#             index.write(response.text)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the 'picture' tag
#         picture_tag = soup.find('picture')

#         # Check if the 'picture' tag exists
#         if picture_tag:
#             # Find the 'img' tag within the 'picture' tag
#             img_tag = picture_tag.find('img')

#             # Check if the 'img' tag exists
#             if img_tag:
#                 # Get the 'src' attribute value
#                 src = img_tag['src']
#                 r = requests.get(src)

#                 # Find the 'span' tag within the 'div' tag
#                 span_tag = soup.find('div').find('span')

#                 # Get the text content of the 'span' tag
#                 text_content = span_tag.get_text(strip=True)

#                 # Print the extracted text
#                 print("Extracted Text:", text_content)

#                 # Save the image
#                 with open('image.jpg', 'wb') as media:
#                     media.write(r.content)
#             else:
#                 print("Image not found")
#         else:
#             print("Picture tag not found")
#     else:
#         print(f"Request failed with status code: {response.status_code}")

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {str(e)}")
