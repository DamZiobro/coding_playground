import React from 'react';
import { Alert } from './Alert'
import './App.css';

function App() {
  return (
    <div className="App">
        <Alert heading="Success" closable>Everything is really good!</Alert>
    </div>
  );
}

export default App;
