import React, { useState } from 'react';
import axios from 'axios';

const KnowledgeBase = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    if (!query.trim()) {
      setError('الرجاء إدخال مصطلح للبحث.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.get('http://localhost:5000/api/knowledge/search', {
        params: { q: query },
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error searching knowledge base:', error);
      setError('حدث خطأ أثناء البحث. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-full p-2 border rounded"
        placeholder="ابحث في قاعدة المعرفة..."
      />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      <button
        onClick={handleSearch}
        disabled={loading}
        className={`mt-2 p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري البحث...' : 'بحث'}
      </button>
      <div className="mt-4">
        {results.length > 0 ? (
          results.map((result, index) => (
            <div key={index} className="p-2 border-b">
              <h3 className="font-bold">{result[1]}</h3>
              <p>{result[2]}</p>
            </div>
          ))
        ) : (
          <p className="text-gray-500">لا توجد نتائج للعرض.</p>
        )}
      </div>
    </div>
  );
};

export default KnowledgeBase;