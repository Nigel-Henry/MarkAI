import React, { useState } from 'react';
import axios from 'axios';

const ImageEditor = () => {
  const [image, setImage] = useState(null);
  const [editedImage, setEditedImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) {
      setError('الرجاء اختيار صورة.');
      return;
    }

    setLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:5000/api/image/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setImage(response.data.imageUrl);
    } catch (error) {
      console.error('Error uploading image:', error);
      setError('حدث خطأ أثناء تحميل الصورة. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  const handleEditImage = async () => {
    if (!image) {
      setError('الرجاء تحميل صورة أولاً.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/api/image/edit', { imageUrl: image });
      setEditedImage(response.data.editedImageUrl);
    } catch (error) {
      console.error('Error editing image:', error);
      setError('حدث خطأ أثناء تحرير الصورة. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <input
        type="file"
        onChange={handleImageUpload}
        className="w-full p-2 border rounded"
        accept="image/*"
      />
      {error && <p className="text-red-500 mt-2">{error}</p>}
      {image && (
        <div className="mt-4">
          <h3 className="font-bold">الصورة المرفوعة:</h3>
          <img src={image} alt="Uploaded" className="mt-2 rounded-lg shadow" />
        </div>
      )}
      <button
        onClick={handleEditImage}
        disabled={loading || !image}
        className={`mt-2 p-2 rounded ${
          loading || !image ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
        }`}
      >
        {loading ? 'جاري التحرير...' : 'تحرير الصورة'}
      </button>
      {editedImage && (
        <div className="mt-4">
          <h3 className="font-bold">الصورة المحررة:</h3>
          <img src={editedImage} alt="Edited" className="mt-2 rounded-lg shadow" />
        </div>
      )}
    </div>
  );
};

export default ImageEditor;