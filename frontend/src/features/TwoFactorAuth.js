import React, { useState } from 'react';
import { enable2FA, verify2FA } from '../services/api';

const TwoFactorAuth = () => {
  const [token, setToken] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  const handleEnable2FA = async () => {
    setLoading(true);
    setError('');
    setMessage('');

    try {
      const response = await enable2FA();
      setMessage('تم تفعيل المصادقة الثنائية بنجاح!');
      console.log('Enable 2FA Response:', response);
    } catch (error) {
      console.error('Enable 2FA Error:', error);
      setError('حدث خطأ أثناء تفعيل المصادقة الثنائية. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  const handleVerify2FA = async () => {
    if (!token.trim()) {
      setError('الرجاء إدخال رمز التحقق.');
      return;
    }

    setLoading(true);
    setError('');
    setMessage('');

    try {
      const response = await verify2FA(token);
      setMessage('تم التحقق من الرمز بنجاح!');
      console.log('Verify 2FA Response:', response);
    } catch (error) {
      console.error('Verify 2FA Error:', error);
      setError('حدث خطأ أثناء التحقق من الرمز. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">المصادقة الثنائية (2FA)</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {message && <p className="text-green-500 mb-4">{message}</p>}
      <button
        onClick={handleEnable2FA}
        disabled={loading}
        className={`bg-blue-500 text-white p-2 rounded mb-4 ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري التفعيل...' : 'تفعيل المصادقة الثنائية'}
      </button>
      <input
        type="text"
        value={token}
        onChange={(e) => setToken(e.target.value)}
        className="w-full p-2 border rounded mb-4"
        placeholder="رمز التحقق"
      />
      <button
        onClick={handleVerify2FA}
        disabled={loading}
        className={`bg-green-500 text-white p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-green-500 text-white'
        }`}
      >
        {loading ? 'جاري التحقق...' : 'تحقق من الرمز'}
      </button>
    </div>
  );
};

export default TwoFactorAuth;