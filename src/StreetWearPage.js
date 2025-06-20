import React from 'react';
import './StreetWear.css';


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
    <h1 className="app-name">StreetWear - Attire</h1>
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

const StreetwearPage = () => {
  return (
    <div>
      <Header />
      <div className="container">
        <DressBox
          imageSrc="https://i.styleoholic.com/2022/04/a-relaxed-summer-look-with-a-white-t-shirt-a-light-blue-denim-jacket-black-pants-and-white-sneakers.jpg"
          title="Graphic T-Shirt and Denim Jacket"
          description="Casual and edgy, perfect for urban environments."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/40/3e/22/403e224c0f3f38a7fd5beff25e106148.jpg"
          title="Hoodie and Cargo Pants"
          description="Comfortable and stylish, ideal for a laid-back street look."
        />
        <DressBox
          imageSrc="https://www.outfittrends.com/wp-content/uploads/2018/04/jogger-Set.jpg"
          title="Sneakers and Joggers"
          description="Sporty and cool, great for an active streetwear vibe."
        />
        {/* Add more DressBox components as needed */}
      </div>
    </div>
  );
};

export default StreetwearPage;
