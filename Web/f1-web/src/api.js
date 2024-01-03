// TODO: add env values
const BASE_URL = "http://localhost:8000";

const handleResponse = async (response) => {
  const contentType = response.headers.get('content-type');
  if (!response.ok) {
    console.log(`Request failed with status: ${response.status}`);
    const errorResponse = await response.json();
    const errorMessage = errorResponse.error || "Unknown error";
    // alert(`${errorMessage}`);
  } else if(contentType && contentType.includes('application/json')) {
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
    register: async (userData) => post("f1/register/user/", userData),
    getUserInfo: async () => get("f1/user/"),
  },
};
