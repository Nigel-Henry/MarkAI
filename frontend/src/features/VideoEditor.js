import React, { useState } from 'react';
import axios from 'axios';

const VideoEditor = () => {
  const [video, setVideo] = useState(null);
  const [operations, setOperations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [editedVideoUrl, setEditedVideoUrl] = useState('');

  const handleUpload = async () => {
    if (!video) {
      setError('الرجاء اختيار فيديو.');
      return;
    }

    setLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('video', video);
    formData.append('operations', JSON.stringify(operations));

    try {
      const response = await axios.post('http://localhost:5000/api/video/edit', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setEditedVideoUrl(response.data.editedVideoUrl);
      alert('تم تحرير الفيديو بنجاح!');
    } catch (error) {
      console.error('Error editing video:', error);
      setError('حدث خطأ أثناء تحرير الفيديو. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <input
        type="file"
        onChange={(e) => setVideo(e.target.files[0])}
        className="w-full p-2 border rounded"
        accept="video/*"
      />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      <button
        onClick={handleUpload}
        disabled={loading}
        className={`mt-2 p-2 rounded ${
          loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-green-500 text-white'
        }`}
      >
        {loading ? 'جاري التحرير...' : 'تحرير الفيديو'}
      </button>
      {editedVideoUrl && (
        <div className="mt-4">
          <h3 className="font-bold">الفيديو المحرر:</h3>
          <video src={editedVideoUrl} controls className="mt-2 rounded-lg shadow" />
        </div>
      )}
    </div>
  );
};

export default VideoEditor;