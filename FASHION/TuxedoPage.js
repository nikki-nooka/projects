import React from 'react';
import './TuxedoPage.css';

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
    <h1 className="app-name">Tuxedo Dress</h1>
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

const TuxedoPage = () => {
  return (
    <div>
      <Header />
      <div className="container">
        <DressBox
          imageSrc="https://cdn11.bigcommerce.com/s-h5szxdw1y0/images/stencil/1280x1280/products/1443/1202/yhst-130746406128729_2271_354672486__39569.1530286840.jpg?c=2&imbypass=on"
          title="Classic Black Tuxedo"
          description="Elegant and timeless, perfect for formal occasions."
        />
        <DressBox
          imageSrc="https://gentwith.com/wp-content/uploads/2019/03/Aalvert-Slim-Fit-Tuxedo-%E2%80%93-White-3.jpeg"
          title="Slim-Fit Tuxedo Suit"
          description="Modern and sophisticated, ideal for a contemporary look."
        />
        <DressBox
          imageSrc="https://i.etsystatic.com/24454145/r/il/4aed3b/2564080306/il_794xN.2564080306_d338.jpg"
          title="Velvet Tuxedo Jacket"
          description="Luxurious and stylish, stands out for special events."
        />
        {/* Add more DressBox components as needed */}
      </div>
    </div>
  );
};

export default TuxedoPage;
