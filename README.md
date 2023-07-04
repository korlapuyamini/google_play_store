
# Google Play Store App Details API

This is a simple API built with FastAPI and google-play-scraper library that retrieves the details of an app from the Google Play Store based on a given domain name.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.6+
- FastAPI
- google-play-scraper

## Installation


 Install the dependencies:

   ```
   pip install fastapi
   pip install google-play-scraper
   pip install uvicorn
   ```

## Usage

1. Start the FastAPI server using Uvicorn:

   ```
   uvicorn main:app --reload
   ```

   The server should now be running on http://localhost:8000.

   - `uvicorn`: Uvicorn is a lightning-fast ASGI server that provides high-performance for Python web applications.

   - `main:app`: This part of the command specifies the module and object to run. In this case, it tells Uvicorn to run the `app` object from the `main` module. The `main` module is typically the entry point of your application where you define and configure the FastAPI application.

   - `--reload`: This flag enables automatic code reloading. With `--reload` specified, Uvicorn will monitor the application's source code for changes. If any changes are detected, it will automatically restart the server, allowing you to see the updates without manually stopping and starting the server.

2. Open your web browser or API testing tool (e.g., Postman) and make requests to the following endpoints:

   - **GET /google_store/{domain_name}**

     Retrieves the details of an app based on the provided domain name.

     Example: http://localhost:8000/google_store/com.example.app

3. The API will return a JSON response containing the app details if found, or an appropriate error message if not found.

   Example response:

   ```json
   {
     "App Title": "My App",
     "Developer": "Example Developer",
     "Genre": "Productivity",
     "Rating": 4.5,
     "Installs": "1,000,000+",
     "URL": "https://play.google.com/store/apps/details?id=com.example.app"
   }
   ```

## Server Configuration

The server is configured to run on `http://localhost:8000` by default. If you want to change the host and port or enable automatic code reloading, you can modify the `uvicorn.run()` line in the `main.py` file.

To change the server configuration, locate the following line in the `main.py` file:

```python
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
```

You can modify the parameters of the `uvicorn.run()` function according to your needs:

- `host`: Specify the host IP address on which the server should listen. By default, it is set to `"0.0.0.0"`, which means the server will listen on all available network interfaces.

- `port`: Specify the port number on which the server should listen. By default, it is set to `8001`. You can change this value to a different port number if needed.

- `reload`: Set this parameter to `True` to enable automatic code reloading. When set to `True`, Uvicorn will monitor the application's source code for changes and automatically restart the server when changes are detected. By default, it is set to `True`.

