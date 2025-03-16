import React, { useState } from 'react';
import { uploadFile } from '../services/api';

function FileManager() {
    const [file, setFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState('');

    const handleFileUpload = async () => {
        if (!file) {
            setUploadStatus('Please select a file to upload.');
            return;
        }

        try {
            const result = await uploadFile(file);
            setUploadStatus('File uploaded successfully.');
            console.log('File uploaded:', result);
        } catch (error) {
            setUploadStatus('Error uploading file.');
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <h2>File Manager</h2>
            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
            />
            <button onClick={handleFileUpload}>Upload</button>
            {uploadStatus && <p>{uploadStatus}</p>}
        </div>
    );
}

export default FileManager;