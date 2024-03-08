# How to access the dad jokes `search` endpoint using Python

This procedure uses the `request` package, the most popular Python package for interacting with RESTful APIs like this one. To install it on your Python system, use the following command at a terminal prompt:

    pip install request

The procedure uses the following Python program, which it assumes you have open in your Python development system:

```python
"""Access the dad joke search endpoint"""
    import requests

    headers = {'User-Agent': '<my-url>', 'Accept':"application/json"}

    query_params = {'page':1, 'limit':4, 'term':"bike"}
    r = requests.get('https://icanhazdadjoke.com/search', headers=headers,  params=query_params)

    print(r.status_code)
    print(r.json())
```
If you run it you should see the following output:
```
    200
{'current_page': 1, 'limit': 4, 'next_page': 1, 'previous_page': 1, 
'results': [
    {'id': 'R7UfaahVfFd', 'joke': 'My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.'}, 
    {'id': 'HtcNuHJBQCd', 'joke': "How many kids with ADD does it take to change a lightbulb? Let's go ride bikes!"}], 
'search_term': 'bike', 'status': 200, 'total_jokes': 2, 'total_pages': 1}
```

To perform a dad joke search:

1. Edit the `headers` dictionary in the above code to supply:

   * Your own user agent to replace `<my-url>`.
     Ideally, this should include the name of the library or website that is accessing the API and a URL or contact email address. For example:

        ```
            https://github.com/username/repo
        ```

   * An `Accept` header to specify the desired response type. The allowed values are:
     
     - `text/html` -- HTML (default)
     - `application/json`  -- JSON
     - `text/plain`  -- Plain text

2. Edit the `query_params` dictionary to set any query parameters you wish to use. The available parameters are:

   * `page` -- an integer specifying which page of results to return (default = 1)

   * `limit` -- an integer specifying the number of results to return from each page (default = 20; maximum = 30)

   * `term` -- a string specifying text that returned jokes must contain (default = '', meaning return all jokes)

The above code prints the returned jokes. Modify it as you see fit to use them in other ways.