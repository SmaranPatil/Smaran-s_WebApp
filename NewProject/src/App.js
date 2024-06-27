// src/App.js
import React from 'react';
import FileUpload from './components/FileUpload';
import Results from './components/Results';
function App() {
  return (
    <div>
      <h1>Group Accommodation Allocation</h1>
      <h2>Space</h2>
      <FileUpload />
      <Results />
    </div>
  );
}

export default App;
