import React from 'react';
import './FormalAttirePage.css';

const DressBox = ({ imageSrc, title, description }) => (
  <div className="dress-box">
    <div className="image-container">
      <img src={imageSrc} alt={title} />
    </div>
    <h2>{title}</h2>
    <p>{description}</p>
  </div>
);

const FormalAttirePage = () => {
  return (
    <div>
      <header>
        <h1 className="app-name">Formal - Attire</h1>
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
          imageSrc="https://i.pinimg.com/originals/72/7c/7c/727c7c4f77c3a3916e7c09b97f51a7f6.jpg"
          title="Black Tie Suit"
          description="Elegant and classic black tie suit for formal events."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/90/72/1a/90721a3f799c9d7a3aa35e8f5786f667.jpg"
          title="Tuxedo with Bow Tie"
          description="Sophisticated tuxedo ensemble with a stylish bow tie."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/62/c4/92/62c492dc0fdb484d789986eb42c4d758.jpg"
          title="Navy Blue Suit"
          description="Stylish navy blue suit for formal occasions."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/61XnPWdRAWL._SY679_.jpg"
          title="Black and Grey"
          description="Stylish black for formal occasions."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/7136T3IfsOL._SY550_.jpg"
          title="Creame"
          description="Creame for formal occasions."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/51OEhDURrZL._SY550_.jpg"
          title="White and Black"
          description="Black and White for special cases."
        />
      </div>
    </div>
  );
};

export default FormalAttirePage;
