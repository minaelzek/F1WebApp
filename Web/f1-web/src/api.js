// TODO: add env values
const BASE_URL = "http://localhost:8000";

const handleResponse = async (response, showAlert) => {
  const contentType = response.headers.get('content-type');
  if (!response.ok) {
    console.log(`Request failed with status: ${response.status}`);
    const errorResponse = await response.json();
    const errorMessage = errorResponse.error || "Unknown error";
    if(showAlert){
      alert(`${errorMessage}`);
    }
    return false
  } else if(contentType && contentType.includes('application/json')) {
    return response.json();
  }
};

export const get = async (endpoint, showAlert) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "GET",
      credentials: "include",
    });
    return handleResponse(response, showAlert);
  } catch (error) {
    console.error(`Error during GET request to ${endpoint}:`, error.message);
    return false
  }
};

export const post = async (endpoint, data, showAlert) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return handleResponse(response, showAlert);
  } catch (error) {
    console.error(`Error during POST request to ${endpoint}:`, error.message);
    return false
  }
};

// Predefined endpoints
export const endpoints = {
  user: {
    login: async (credentials, ) => post("f1/login/user/", credentials, true),
    logout: async () => get("f1/logout/user/", false),
    register: async (userData) => post("f1/register/user/", userData, true),
    getUserInfo: async () => get("f1/user/", false),
    getLoginSummary: async () => get("f1/user/loginSummary", false),
  },
};
