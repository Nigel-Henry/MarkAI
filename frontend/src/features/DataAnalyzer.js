import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataAnalyzer = () => {
  const [data, setData] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // استرجاع النتائج من localStorage عند تحميل المكون
  useEffect(() => {
    const cachedResult = localStorage.getItem('analysisResult');
    if (cachedResult) {
      setResult(JSON.parse(cachedResult));
    }
  }, []);

  const handleAnalyze = async () => {
    if (!data.trim()) {
      setError('الرجاء إدخال بيانات للتحليل.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/api/data/analyze', { data });
      setResult(response.data);
      localStorage.setItem('analysisResult', JSON.stringify(response.data)); // حفظ النتائج في localStorage
    } catch (error) {
      console.error('Error analyzing data:', error);
      setError('حدث خطأ أثناء تحليل البيانات. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  const handleSaveResults = () => {
    if (!result) return;

    const blob = new Blob([JSON.stringify(result, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'analysis_results.json';
    link.click();
    URL.revokeObjectURL(url);
  };

  const handleClearResults = () => {
    setResult(null);
    localStorage.removeItem('analysisResult'); // حذف النتائج من localStorage
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <textarea
        value={data}
        onChange={(e) => setData(e.target.value)}
        className="w-full p-2 border rounded"
        placeholder="أدخل البيانات هنا..."
        rows={5}
      />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      <button
        onClick={handleAnalyze}
        disabled={loading}
        className={`mt-2 p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري التحليل...' : 'تحليل البيانات'}
      </button>
      {result && (
        <div className="mt-4">
          <h3 className="font-bold">النتائج:</h3>
          <pre className="bg-gray-100 p-2 rounded">{JSON.stringify(result, null, 2)}</pre>
          <div className="flex gap-2 mt-2">
            <button
              onClick={handleSaveResults}
              className="bg-green-500 text-white p-2 rounded"
            >
              حفظ النتائج كملف JSON
            </button>
            <button
              onClick={handleClearResults}
              className="bg-red-500 text-white p-2 rounded"
            >
              مسح النتائج
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DataAnalyzer;