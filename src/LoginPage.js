//login.js
import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

const LoginPage = () => {
  return (
    <div>
    <div style={{ backgroundColor: '#d3f9d8', minHeight: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      
      <Container style={{ backgroundColor: '#ffffff', padding: '30px', borderRadius: '10px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
        <center>
        
          <Row className="justify-content-center">
            
            <Col md={6} className="text-center">
              <h2 style={{ color: '#343a40', marginBottom: '30px' }}>Login</h2>
              <Form>
                <Form.Group controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>
    
                <Form.Group controlId="formBasicPassword">
                  <Form.Label>Password</Form.Label>
                  <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                <Link to="dress">
                <Button variant="info" type="submit" style={{ backgroundColor: '#17a2b8', borderColor: '#17a2b8' }}>
                  LOGIN
                </Button>
                </Link>
              </Form>
              <p className="mt-3" style={{ color: '#6c757d', fontSize: '0.9rem' }}>Don't have an account? <Link to="/signup" style={{ color: '#007bff', textDecoration: 'none', fontWeight: 'bold' }}>Sign up now</Link></p>
            </Col>
          </Row>
        </center>
      </Container>
    </div>
    </div>
  );
};

export default LoginPage;