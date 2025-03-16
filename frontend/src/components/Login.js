// frontend/src/components/Login.js
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import axios from 'axios';
import { loginStart, loginSuccess, loginFailure } from '../features/auth/authSlice';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const dispatch = useDispatch();
    const { status, error } = useSelector((state) => state.auth);

    const handleLogin = async () => {
        dispatch(loginStart());
        try {
            const response = await axios.post('http://localhost:5000/api/login', { username, password });
            dispatch(loginSuccess(response.data));
        } catch (error) {
            dispatch(loginFailure(error.message));
        }
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
            {status === 'loading' && <p>Loading...</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default Login;