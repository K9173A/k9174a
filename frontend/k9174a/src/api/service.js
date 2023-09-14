import axios from 'axios';


export default class RequestService {
    constructor() {
        this.client = axios.create({
            baseURL: 'https://k9174a.com/api',
            timeout: 1000
        });
    }

    async authorize() {
        return this.client.get('token/');
    }

    async register() {
        return this.client.post('register/');
    }
}