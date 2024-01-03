// TODO: add env values
const BASE_URL = "http://localhost:8000";

const handleResponse = async (response) => {
  if (!response.ok) {
    console.log(`Request failed with status: ${response.status}`);
    const errorResponse = await response.json();
    const errorMessage = errorResponse.error || "Unknown error";
    alert(`${errorMessage}`);
  } else {
    return response.json();
  }
};

export const get = async (endpoint) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "GET",
      credentials: "include",
    });
    return handleResponse(response);
  } catch (error) {
    console.error(`Error during GET request to ${endpoint}:`, error.message);
  }
};

export const post = async (endpoint, data) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
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
  user: {
    login: async (credentials) => post("f1/login/user/", credentials),
    logout: async () => get("f1/logout/user/"),
    getUserInfo: async () => get("f1/user/"),
  },
};
