import React from 'react';
import { Container, Nav, Navbar, NavDropdown } from 'react-bootstrap';
import { GiHouse } from 'react-icons/gi';

import { useNavigate } from 'react-router-dom';

const Header = () => {
const navigate = useNavigate();

const handleViewHome = () => {
navigate('/');
};
const handleViewProperties = () => {
navigate('/properties');
};
  return (
    <header>
      <Navbar fixed='top' expand="lg" bg='dark' variant='dark'  collapseOnSelect>
        <Container>
            <Navbar.Brand onClick={handleViewHome}><GiHouse className='nav-icon'/> Real Estate</Navbar.Brand>
          
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav" className='justify-content-end'>
            <Nav className="ml-auto">
                <Nav.Link onClick={handleViewHome}>Home</Nav.Link>
                <Nav.Link onClickCapture={handleViewProperties}>Properties</Nav.Link>
              <Nav.Link href="#link">Link</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;