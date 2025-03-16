import React, { useState } from 'react';

const SocialAuth = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGoogleLogin = () => {
    setLoading(true);
    setError('');

    try {
      window.location.href = '/api/auth/google';
    } catch (error) {
      console.error('Error redirecting to Google login:', error);
      setError('حدث خطأ أثناء التوجيه لتسجيل الدخول عبر Google. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">تسجيل الدخول عبر وسائل التواصل الاجتماعي</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button
        onClick={handleGoogleLogin}
        disabled={loading}
        className={`bg-blue-500 text-white p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري التوجيه...' : 'تسجيل الدخول عبر Google'}
      </button>
    </div>
  );
};

export default SocialAuth;