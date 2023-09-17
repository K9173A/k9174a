import axios from 'axios';

const service = axios.create({
    baseURL: 'https://k9174a.com/api',
    timeout: 1000
});

export const register = (data) => service.post('register/', data);
export const login = (data) => service.post('token/', data);