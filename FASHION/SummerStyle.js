import React from 'react';
import './SummerStyle.css'

const DressBox = ({ imageSrc, title, description }) => (
  <div className="dress-box">
    <div className="image-container">
      <img src={imageSrc} alt={title} />
    </div>
    <h2>{title}</h2>
    <p>{description}</p>
  </div>
);

const Header = () => (
  <header>
    <h1 className="app-name">Summer Attire</h1>
    <nav>
      <a href="dresspage.html">Home</a> | 
      <a href="casual-wear.html">Casual Wear</a> | 
      <a href="formal-attire.html">Formal Attire</a> | 
      <a href="business-casual.html">Business Casual</a> | 
      <a href="tuxedo.html">Tuxedo</a> | 
      <a href="summer-style.html">Summer Style</a> | 
      <a href="streetwear.html">Modern Suits</a> | 
      <a href="athleisure.html">Athleisure</a>
    </nav>
  </header>
);

const SummerStylePage = () => {
  return (
    <div>
      <Header />
      <div className="container">
        <DressBox
          imageSrc="https://images.shoefabs.com/pp-9323d4a9/l/a57126f14da1de/Enjoybuy-Mens-Summer-Linen-Henley-Shirts-Short-Sleeve-Banded-Collar-Casual-Beach-Shirt-Tops-White-White-a57126f14da1de.jpg"
          title="Lightweight Linen Shirt"
          description="Cool and breathable, perfect for hot summer days."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/c3/01/b1/c301b101302ef5b8adc30ccfcc1b5dbd.jpg"
          title="Flowy Sundress"
          description="Airy and comfortable, ideal for summer outings."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/56/a4/36/56a436f294a4d172cf7f2f21ca89bde0.png"
          title="Shorts and Tank Top"
          description="Casual and stylish, great for beach or casual gatherings."
        />
        {/* Add more DressBox components as needed */}
      </div>
    </div>
  );
};

export default SummerStylePage;
