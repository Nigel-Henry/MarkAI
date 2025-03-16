import React from 'react';

const SocialAuth = () => {
    const handleGoogleLogin = () => {
        window.location.href = '/api/auth/google';
    };

    return (
        <div>
            <h2>Social Authentication</h2>
            <button onClick={handleGoogleLogin}>Login with Google</button>
        </div>
    );
};

export default SocialAuth;