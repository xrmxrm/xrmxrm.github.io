# About the Dad Joke API

When you're in a certain mood, a dad joke can be just what you need. By providing an API, `icanhazdadjoke.com`: 

* Makes dad jokes available in many high-stress environments.
* Provides a great way to learn about RESTful APIs.
* Gives developers a simple but non-trivial test case for API-related software.

## What the API provides

Using the API's various endpoints, you can:

* Fetch a random dad joke.
* Fetch a specific dad joke.
* Search for dad jokes containing specified text.
* Search for dad jokes using a GraphQL query.

## How the API provides jokes

The returned results from the above endpoints can be in the following formats:

* Json.
* Plain text.
* Image (.png).
* Specific to an app like Slack.

## Details

The API does not use authentication, but it requests that you use a `User-Agent` header. 

The API recognizes several `Accept` headers and adjusts its response formats accordingly. 


