1. Ran the app.py file which is the server 
   - Used the Flask web application framework to do following:
        - Starting the server
        - Making it listen to the url http://127.0.0.1:5000
        - Establish routing
   - Used the postgres driver to establish connection with the postgres database 
        - user name, password, hostname, port, database name

2. User types in the url in the browser: http://127.0.0.1:5000/
   - 127.0.0.0 is the local machine ip. Its a special ip.
   - 5000 is the port
   - It also happened to be the root url ('/')
   - url's /landing
   - /landing?parameter=1&parameter=100
   
3. Browser sends this request to the server
   - url, method (GET)
   - wait for the response

4. Request arrives at the server   
   - With routing established flask routes that request to the route '/'   
   - Route '/' is processed by python function home()

5. home function
   - initializes a list contacts
   - gets cursor from the connection
   - queries the database student table to get all records
   - appends the student names to the contacts list
   - calls the render template function
        - provided by the flask module
        - Uses jinja2 template framework to read the specified html (index.html) from templates folder
        - Replaces the placeholder by running the templating engine e.g. message (direct replace), contacts (replace using for loop)
   - returns the html to the browser
   
6. Browser got the response from the server
   - Response contains contents of the index.html file
   - Note: browser is not opening the html file. html file was opened by the server, contents were read, file was closed and contents were returned to the browser.
   - Parsing the html content
   - Internally browse creates DOM (document object model)
     Tree data structure
     html
       |- head
       |    - title 
       |         value
       |    - href (attributes list)  
       |- body
   - While creating this dom browser detects that it needs the main.css file
   - browser makes another call to the server requesting the main.css file
       - http://127.0.0.1:5000/static/css/main.css   
   - browser waits for the response from the server
   
7. main.css request arrives at the server
   - Flask knows how to handle this request which is not the root url or this url is also not handled by app.py
   - Flask knows static directory
   - Flask will serve the main.css file from the static/css directory as is
   
8. Browser got the contents of the main.css file from the server
   - Note: browser is not opening the css file. css file was opened by the server, contents were read, file was closed and contents were returned to the browser.
   - starts parsing again
   - browser not detects that it needs the main.js file
   - browser makes a request to the server to get this main.js file
   - browser waits for the response from the server

9. main.js request arrives at the server
   - Flask knows how to handle this request which is not the root url or this url is also not handled by app.py
   - Flask knows static directory
   - Flask will serve the main.js file from the static/js directory as is
 
10. Browser gets the contents of the main.js file from the server
    - Note: browser is not opening the js file. js file was opened by the server, contents were read, file was closed and contents were returned to the browser.  
    - completes the parsing and renders the html in the screen
    - while rendering the html on the screen browser also applies the css

11. When the button is clicked on the browser we see the alert message.


12. We can also debug the javascript within the browser. You can also change the element styling in the browser to view how the page looks


13. html, css, javascript, python, html templating language, sql