const axios = require('axios');

async function getMovieTitleAndCharacters(movieId) {
  try {
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    return {
      title: response.data.title,
      characters: response.data.characters
    };
  } catch (error) {
    console.error(`Error fetching movie with ID ${movieId}:`, error.message);
    return null;
  }
}

async function getCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    console.error(`Error fetching character from ${characterUrl}:`, error.message);
    return null;
  }
}

async function main(movieId) {
  const movieData = await getMovieTitleAndCharacters(movieId);
  if (!movieData) {
    console.error(`Movie with ID ${movieId} not found.`);
    return;
  }

  console.log(`Characters in '${movieData.title}':`);
  for (const url of movieData.characters) {
    const name = await getCharacterName(url);
    if (name) {
      console.log(name);
    }
  }
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error("Usage: node star_wars_characters.js <Movie ID>");
} else {
  const movieId = parseInt(args[0], 10);
  if (isNaN(movieId)) {
    console.error("Movie ID must be an integer.");
  } else {
    main(movieId);
  }
}

