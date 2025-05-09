const axios = require('axios');
const fs = require('fs');

const geminiApiKey = process.env.GEMINI_API_KEY;  // Using the secret
const endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY';   // Replace with the correct Gemini endpoint

const generateDSAProblem = async () => {
  try {
    const response = await axios.post(endpoint, {
      prompt: 'Write a random DSA problem and provide the solution in code.',
      apiKey: geminiApiKey,
    });

    // Assuming the response contains the code solution in response.data.text
    const dsaSolution = response.data.text;

    // Save the solution to a file
    fs.writeFileSync('dsa_solution.txt', dsaSolution);
    console.log('DSA problem generated and saved!');
  } catch (error) {
    console.error('Error generating DSA problem:', error);
  }
};

generateDSAProblem();
