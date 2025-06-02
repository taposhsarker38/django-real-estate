import React from 'react'
import { Button,Container } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom';
const HomePage = () => {
    const navigate = useNavigate();

  const handleViewProperties = () => {
    navigate('/properties');
  };

  return (
    <>
        <header className='masthead main-bg-image'>
            <Container className='px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center'>
                <div className='d-flex justify-content-center'>
                    <div className='text-center'>
                        <h1 className='mx-auto my-0 text-uppercase'>Real Estate</h1>
                        <h2 className='text-white-50 mx-auto mt-2 mb-5'>A place to buy and sell properties</h2>
                        <Button onClick={handleViewProperties} variant='primary' className='js-scroll-trigger'>View Properties</Button>
                       
                    </div>
                </div>
            </Container>
            
        </header>
    </>
  )
}

export default HomePage