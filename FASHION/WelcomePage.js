import React from 'react';
import './WelcomePage.css';
import {Link} from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css"
const WelcomePage = () => {
  return (
    <div className="welcome-container">
      <div className="content">
        <h1>Welcome to Fashion Fusion</h1>
        <p>Discover the latest trends and styles</p>
        <Link to="login">
        <button className="get-started-button">Get Started</button>
        </Link>
      </div>
    </div>
  );
};

export default WelcomePage;
