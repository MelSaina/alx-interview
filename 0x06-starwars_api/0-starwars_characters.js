#!/usr/bin/node

/**
 * Wrapper function for request object that allows it
 * to work with async and await
 * @param   {String} url - site url
 * @returns {Promise}    - promise object that resolves
 *                         with parsed JSON response
 *                         and rejects with the request error.
 */
function makeRequest(url) {
    // Using the 'request' library for making HTTP requests
    const request = require('request');
  
    // Returning a Promise for asynchronous handling
    return new Promise((resolve, reject) => {
      // Making a GET request to the provided URL
      request.get(url, (error, response, body) => {
        if (error) {
          // Rejecting the promise if there is an error
          reject(error);
        } else {
          // Resolving the promise with parsed JSON response
          resolve(JSON.parse(body));
        }
      });
    });
  }
  
  /**
   * Entry point - makes requests to Star Wars API
   * for movie info based on the movie ID passed as a CLI parameter.
   * Retrieves movie character info then prints their names
   * in order of appearance in the initial response.
   */
  async function main() {
    // Getting command-line arguments
    const args = process.argv;
  
    // Checking if movie ID is provided as a CLI parameter
    if (args.length < 3) return;
  
    // Constructing the URL for the Star Wars API based on movie ID
    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  
    // Making a request to fetch movie details
    const movie = await makeRequest(movieUrl);
  
    // Checking if 'characters' property exists in the movie response
    if (movie.characters === undefined) return;
  
    // Looping through each character URL and fetching details
    for (const characterUrl of movie.characters) {
      // Making a request to fetch character details
      const character = await makeRequest(characterUrl);
  
      // Printing the name of the character
      console.log(character.name);
    }
  }
  
  // Calling the main function to start the script
  main();  