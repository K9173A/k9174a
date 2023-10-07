import axios from 'axios';

const service = axios.create({
    baseURL: 'https://k9174a.com/api',
    timeout: 1000
});

export const register = async (data) => service.post('/auth/register/', data);
export const login = async (data) => service.post('/auth/login/', data);
export const logout = async (data) => service.post('/auth/logout/', data);
export const logoutall = async (data) => service.post('/auth/logoutall/', data);
export const validate = async (data) => service.get('/auth/validate/', data);