import React, { useState } from 'react';
import axios from 'axios';

const ProjectRequest = () => {
  const [projectName, setProjectName] = useState('');
  const [request, setRequest] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    if (!projectName.trim() || !request.trim()) {
      setError('الرجاء إدخال اسم المشروع ووصف الطلب.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/api/project/request', {
        project_name: projectName,
        request: request,
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error submitting request:', error);
      setError('حدث خطأ أثناء إرسال الطلب. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">طلب مشروع جديد</h2>
      <input
        type="text"
        value={projectName}
        onChange={(e) => setProjectName(e.target.value)}
        className="w-full p-2 border rounded mb-4"
        placeholder="اسم المشروع"
      />
      <textarea
        value={request}
        onChange={(e) => setRequest(e.target.value)}
        className="w-full p-2 border rounded mb-4"
        placeholder="وصف الطلب"
        rows={4}
      />
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button
        onClick={handleSubmit}
        disabled={loading}
        className={`bg-blue-500 text-white p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري الإرسال...' : 'طلب المشروع'}
      </button>
    </div>
  );
};

export default ProjectRequest;