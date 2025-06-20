import React from 'react';
import './styles.css';

const DressBox = ({ imageSrc, title, description }) => (
  <div className="dress-box">
    <div className="image-container">
      <img src={imageSrc} alt={title} />
    </div>
    <h2>{title}</h2>
    <p>{description}</p>
  </div>
);

const BusinessCasualPage = () => {
  return (
    <div>
      <header>
        <h1 className="app-name">Business - Casual</h1>
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
      <div className="container">
        <DressBox
          imageSrc="https://i.pinimg.com/originals/a9/f3/7d/a9f37d161e3167627c8bccd3f1d17380.jpg"
          title="Blazer and Chinos"
          description="A tailored blazer paired with classic chinos for a smart-casual look."
        />
        <DressBox
          imageSrc="https://cdn.shopify.com/s/files/1/0048/3714/6714/files/White-toweling-cloth-polo-shirt-with-dark-blue-trousers.jpg"
          title="Polo Shirt and Trousers"
          description="A stylish polo shirt combined with tailored trousers for a professional yet relaxed ensemble."
        />
        <DressBox
          imageSrc="https://www.beyoung.in/blog/wp-content/uploads/2021/06/rugged-jeans-min-768x922.jpg"
          title="Button-Up Shirt and Jeans"
          description="A button-up shirt tucked into dark jeans for a versatile business casual outfit."
        />
        {/* Add more DressBox components as needed */}
      </div>
    </div>
  );
};

export default BusinessCasualPage;
