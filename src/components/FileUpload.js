// src/components/FileUpload.js

import React, { useState } from 'react';

function FileUpload() {
  const [groupFile, setGroupFile] = useState(null);
  const [hostelFile, setHostelFile] = useState(null);

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('group_file', groupFile);
    formData.append('hostel_file', hostelFile);

    fetch('/upload-csv/', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => console.log(data));
  };

  return (
    <div>
      <input type="file" onChange={(e) => setGroupFile(e.target.files[0])} />
      <input type="file" onChange={(e) => setHostelFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;
