import React from 'react';
import './CasualWear.css';

const DressBox = ({ imageSrc, title, description }) => (
  <div className="dress-box">
    <div className="image-container">
      <img src={imageSrc} alt={title} />
    </div>
    <h2>{title}</h2>
    <p>{description}</p>
  </div>
);

const CasualWear = () => {
  return (
    <div>
      <header>
        <h1 className="app-name">Casual - Wear</h1>
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
          imageSrc="https://i.pinimg.com/736x/b7/0f/b4/b70fb41bcc928c50009a8345de719a00.jpg"
          title="Light Blue Denim Dress"
          description="A comfortable and stylish denim dress for casual occasions."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/originals/24/4e/72/244e72b98cce17bf281b40a02c3f3f0e.jpg"
          title="Striped T-shirt Dress"
          description="A striped t-shirt dress perfect for a relaxed day out."
        />
        <DressBox
          imageSrc="https://i.pinimg.com/736x/b0/a9/0f/b0a90f3a9387706c762ebf2c4a77ffce.jpg"
          title="Khaki Shorts and Tee"
          description="Casual khaki shorts paired with a classic white t-shirt."
        />
        <DressBox
          imageSrc="https://guysworld.in/wp-content/uploads/2019/03/91M3nnPXttL._UL1500_.jpg"
          title="Pink Casual"
          description="Perfect casual wear for the meetings."
        />
        <DressBox
          imageSrc="https://daccordshirts.com/wp-content/uploads/2016/04/5894-brown-tan.jpg"
          title="Brown shirt"
          description="Classic for a match."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/51yvxMGTn7L._SX679_.jpg"
          title="Black Casual"
          description="Black casual combines timeless elegance with contemporary comfort."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/71cisR6ybEL._SY550_.jpg"
          title="Regular fit shirt"
          description="A regular fit shirt offers a classic and comfortable silhouette that suits a variety of occasions."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/61o6YUP7SwL._SX679_.jpg"
          title="Be Active casual Shirt"
          description="BE ACTIVE Men's offers a range of stylish and functional activewear designed for modern lifestyles."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/61ZbKLlt0sL._SY679_.jpg"
          title="Stripped Slim"
          description="Discover effortless sophistication with our Striped Slim collection."
        />
        <DressBox
          imageSrc="https://m.media-amazon.com/images/I/71iwZkuZFOL._SY679_.jpg"
          title="Opaque checked"
          description="Elevate your wardrobe with our Opaque Checked collection."
        />
      </div>
    </div>
  );
};

export default CasualWear;
