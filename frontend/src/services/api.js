import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const login = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/login`, { username, password });
    return response.data;
};

export const register = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/register`, { username, password });
    return response.data;
};

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};


export const enable2FA = async () => {
    const response = await axios.post('/api/security/enable-2fa');
    return response.data;
};

export const verify2FA = async (token) => {
    const response = await axios.post('/api/security/verify-2fa', { token });
    return response.data;
};


export const enrollBiometric = async (username, faceData) => {
    const response = await axios.post('/api/biometric/enroll', { username, faceData });
    return response.data;
};

export const authenticateBiometric = async (username, faceData) => {
    const response = await axios.post('/api/biometric/authenticate', { username, faceData });
    return response.data;
};



import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const login = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/login`, { username, password });
    return response.data;
};

export const register = async (username, password) => {
    const response = await axios.post(`${API_BASE_URL}/register`, { username, password });
    return response.data;
};

export const generateApiKey = async () => {
    const response = await axios.post(`${API_BASE_URL}/integration/generate-api-key`);
    return response.data;
};

export const validateApiKey = async (apiKey) => {
    const response = await axios.post(`${API_BASE_URL}/integration/validate-api-key`, { api_key: apiKey });
    return response.data;
};