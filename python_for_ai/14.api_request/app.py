"""
=========================================================
API BASICS USING PYTHON (requests library)
Author : Shadan Anwar
Description :
This file explains what an API is, how requests & responses
work, HTTP request types, response status codes, and
demonstrates GET and POST requests using Python.

=========================================================
"""

# =========================================================
# 1. WHAT IS AN API?
# =========================================================
"""
API stands for Application Programming Interface.

Simple definition:
An API is a bridge that allows two applications to
communicate with each other.

Real-life example:
- You (client) order food from Swiggy app
- Swiggy app sends your order to restaurant (API request)
- Restaurant processes the order
- Restaurant sends food status back (API response)

In programming:
- Client  → sends request
- Server  → processes request
- API     → medium of communication
"""

# =========================================================
# 2. WHAT IS AN API REQUEST?
# =========================================================
"""
An API request is a message sent from client to server.

A request contains:
1. URL       → where request is sent
2. Method   → GET, POST, PUT, DELETE etc.
3. Headers  → metadata (optional)
4. Body     → data (mainly in POST/PUT)

Example:
requests.get("https://example.com/users")
"""

# =========================================================
# 3. WHAT IS AN API RESPONSE?
# =========================================================
"""
An API response is what the server sends back after
processing the request.

A response contains:
1. Status Code → success or error
2. Response Data → JSON / text / XML
3. Headers → response info

Common response formats:
- JSON (most common)
- XML
- Plain text
"""

# =========================================================
# 4. TYPES OF HTTP REQUEST METHODS
# =========================================================
"""
1. GET
   - Fetch data from server
   - No data modification
   - Example: get user details

2. POST
   - Send data to server
   - Create new resource
   - Example: create new user

3. PUT
   - Update entire existing data
   - Example: update full profile

4. PATCH
   - Update partial data
   - Example: update only email

5. DELETE
   - Delete data
   - Example: delete user
"""

# =========================================================
# 5. HTTP RESPONSE STATUS CODES
# =========================================================
"""
2xx → Success
200 OK          → Request successful
201 Created     → Resource created

3xx → Redirection
301 Moved       → URL changed

4xx → Client Error
400 Bad Request → Wrong request
401 Unauthorized→ Authentication required
403 Forbidden   → No permission
404 Not Found   → URL not found

5xx → Server Error
500 Internal Server Error
502 Bad Gateway
"""

# =========================================================
# 6. IMPORT REQUIRED LIBRARY
# =========================================================


# =========================================================
# 7. GET REQUEST EXAMPLE
# =========================================================
"""
Flow of GET request:
1. User sends request
2. Server processes request
3. Server returns response
"""

import requests
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Send GET request
    response = requests.get(url)

    # Raise exception if status code is 4xx or 5xx
    response.raise_for_status()

    # Check success response
    if response.status_code == 200:
        print("GET Request Successful")
        print("First Post Data:")
        print(response.json()[0])

except requests.exceptions.HTTPError as e:
    print("HTTP Error occurred:", e)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)


# =========================================================
# 8. POST REQUEST EXAMPLE
# =========================================================
"""
POST request:
- Used to send data to server
- Data is sent in request body
- Server processes data and returns response
"""

url_post = "https://jsonplaceholder.typicode.com/posts"

data = {
    "userId": 1,
    "title": "This is simple title",
    "body": "this is body content"
}

try:
    # Send POST request with JSON data
    response_post = requests.post(url_post, json=data)

    # Raise exception if error
    response_post.raise_for_status()

    if response_post.status_code == 201:
        print("\nPOST Request Successful")
        print("Response Data:")
        print(response_post.json())

except requests.exceptions.HTTPError as e:
    print("HTTP Error occurred:", e)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)


# =========================================================
# 9. KEY INTERVIEW POINTS (VERY IMPORTANT)
# =========================================================
"""
- API enables communication between systems
- GET → fetch data
- POST → send data
- Status codes tell request result
- JSON is most common response format
- requests library simplifies HTTP calls in Python
"""

# ====================== END OF FILE ======================
