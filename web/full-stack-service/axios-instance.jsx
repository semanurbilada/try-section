import axios from 'axios';

export const AXIOS_INSTANCE = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  timeout: 1000,
  withCredentials: false,
});

AXIOS_INSTANCE.interceptors.request.use(
  function (config) {
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

AXIOS_INSTANCE.interceptors.response.use(
  function (response) {
    console.log('Interceptor response');

    console.log(response.config.url);
    if (response.config.url.includes('token')) {
      console.log('apiToken');
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
    }
    return response;
  },
  function (error) {
    return Promise.reject(error);
  }
);