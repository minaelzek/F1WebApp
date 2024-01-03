// TODO: add env values
const BASE_URL = 'http://127.0.0.1:8000';

// Helper function to handle the response from the API
const handleResponse = async (response) => {
  if (!response.ok) {
    console.log(`Request failed with status: ${response.status}`);
    const errorResponse = await response.json();
    const errorMessage = errorResponse.error || 'Unknown error';
    alert(`${errorMessage}`);
  } else {
    return response.json();
  }
};

// Function to make a GET request
export const get = async (endpoint) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`);
    return handleResponse(response);
  } catch (error) {
    console.error(`Error during GET request to ${endpoint}:`, error.message);
  }
};

// Function to make a POST request
export const post = async (endpoint, data) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    return handleResponse(response);
  } catch (error) {
    console.error(`Error during POST request to ${endpoint}:`, error.message);
  }
};

// Predefined endpoints
export const endpoints = {
  login: {
    user: async (credentials) => post('f1/login/user/', credentials),
  },
  logout: {
    user: async () => get('f1/logout/user/'),
  },
  // Add more predefined endpoints as needed
};
