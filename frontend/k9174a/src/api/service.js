import axios from 'axios';
import { useCookies } from 'react-cookie';

const authTokenName = 'K9174A_TOKEN';
const baseDomainName = 'k9174a.com';

const service = axios.create({
    baseURL: `https://${baseDomainName}/api`,
    timeout: 1000
});

const [cookies, setCookie, removeCookie] = useCookies([authTokenName]);

const makeRequestConfigWithLoginToken = (username, password) => {
    const token = btoa(`${username}:${password}`);
    return {
        headers: {
            Authorization: `Basic ${token}`
        }
    }
};

const makeRequestConfigWithAuthToken = () => {
    const token = cookies[authTokenName];
    return {
        headers: {
            Authorization: `Token ${token}`
        }
    };
};

export const register = async (data) => {
    return service.post('/auth/register/', data)
        .then(() => true)
        .catch(() => false);
};

export const login = async (data) => {
    const config = makeRequestConfigWithLoginToken(data.username, data.password);
    return service.post('/auth/login/', data, config)
        .then((response) => {
            setCookie(authTokenName, response.data['token'], {
                path: '/',
                expires: response.data['expires'],
                domain: `.${baseDomainName}`,
                secure: true
            });
            return true;
        })
        .catch((reason) => {
            console.error(reason);
            return false;
        });
};

export const logout = async (data) => {
    const config = makeRequestConfigWithAuthToken();
    return service.post('/auth/logout/', data, config)
        .then(() => {
            removeCookie(authTokenName);
            return true;
        })
        .catch((reason) => {
            console.error(reason);
            return false;
        });
};

export const logoutall = async (data) => {
    const config = makeRequestConfigWithAuthToken();
    return service.post('/auth/logoutall/', data, config)
        .then(() => {
            removeCookie(authTokenName);
            return true;
        })
        .catch((reason) => {
            console.error(reason);
            return false;
        });
};

export const validate = async () => {
    const config = makeRequestConfigWithAuthToken();
    return service.get('/auth/validate/', config)
        .then(() => true)
        .catch(() => false);
};