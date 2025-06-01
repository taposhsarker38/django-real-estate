import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import PropertiesPage from './pages/PropertiesPage';
import { ToastContainer } from 'react-bootstrap';

const App=()=> {
  return (
    <>
      <Router>
        <Header />
        <main className='py-3'>
          <Routes>
            <Route path='/' element={<HomePage />} />
          </Routes>
          <Routes>
            <Route path='/properties' element={<PropertiesPage />} />
          </Routes>
        </main>
      </Router>
      <ToastContainer />
    </>
  );
}

export default App;
