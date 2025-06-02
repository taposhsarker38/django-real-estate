import React from 'react';
import "react-toastify/dist/ReactToastify.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import PropertiesPage from './pages/PropertiesPage';
import { ToastContainer } from 'react-bootstrap';
import NotFound from './components/NotFound';

const App=()=> {
  return (
    <>
      <Router>
        <Header />
        <main className='py-3'>
          <Routes>
            <Route path='/' element={<HomePage />} />
            <Route path='/properties' element={<PropertiesPage />} />
            <Route path='*' element={<NotFound />} />
          </Routes>
      <ToastContainer  theme="dark"/>
        </main>
      </Router>
    </>
  );
}

export default App;
