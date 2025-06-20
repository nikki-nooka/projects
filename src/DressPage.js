import React from 'react';
import './DressPage.css';

const styles = {
  body: {
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#f8f8f8',
    margin: 0,
    padding: 0,
  },
  header: {
    backgroundColor: '#333',
    color: '#fff',
    textAlign: 'center',
    padding: '20px 0',
  },
  container: {
    maxWidth: '1000px',
    margin: '20px auto',
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '20px',
  },
  dressBox: {
    backgroundColor: '#fff',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    padding: '20px',
    borderRadius: '8px',
    textAlign: 'center',
  },
  imageContainer: {
    width: '100%',
    height: '200px',
    overflow: 'hidden',
    borderRadius: '8px',
  },
  image: {
    width: '100%',
    height: '100%',
    objectFit: 'cover',
    borderRadius: '8px',
  },
  dressTitle: {
    color: '#333',
    fontSize: '1.5em',
    marginTop: '10px',
  },
  dressDescription: {
    color: '#666',
    fontSize: '1em',
    marginTop: '8px',
  },
};

const dresses = [
  {
    title: 'Casual Wear',
    image: 'https://m.media-amazon.com/images/I/61bCDqUNmYL._SY879_.jpg',
    description: 'Relaxed and stylish for everyday outings.',
    link: 'CasualWear.js',
  },
  {
    title: 'Formal Attire',
    image: 'https://s-media-cache-ak0.pinimg.com/originals/c0/5a/4a/c05a4a8b56894b618023a58e5308cb3c.jpg',
    description: 'Elegant and sophisticated for special occasions.',
    link: 'formal-attire.js',
  },
  {
    title: 'Sporty Look',
    image: 'https://i.pinimg.com/736x/47/06/f6/4706f6fe7efb8495b86053611ae70923.jpg',
    description: 'Active wear for sports and outdoor activities.',
    link: 'sporty-look.js',
  },
  {
    title: 'Business Casual',
    image: 'https://i.pinimg.com/originals/e2/39/d6/e239d6e9011839eee56c790ac7bce69e.jpg',
    description: 'Smart and relaxed for work and casual outings.',
    link: 'business-casual.js',
  },
  {
    title: 'Tuxedo',
    image: 'https://i.pinimg.com/originals/42/1a/57/421a5747224f1a8b83c7796b5a5a86d4.jpg',
    description: 'Classic formal wear for black-tie events.',
    link: 'tuxedo.js',
  },
  {
    title: 'Summer Style',
    image: 'http://www.thedaycollections.com/wp-content/uploads/2017/07/summer-men-outfit-1.jpg',
    description: 'Breezy and comfortable for hot summer days.',
    link: 'summer-style.js',
  },
  {
    title: 'Streetwear',
    image: 'https://nextluxury.com/wp-content/uploads/cool-chekered-jacker-street-style-outfit.jpg',
    description: 'Casual and trendy urban fashion.',
    link: 'streetwear.js',
  },
  {
    title: 'Modern Suit',
    image: 'https://www.simonjersey.com/images/contemporary-mens-black-modern-fit-suit-p1177-123230_image.jpg',
    description: 'Sleek and contemporary suit style.',
    link: 'modern-suit.js',
  },
  {
    title: 'Athleisure',
    image: 'https://vitruvianmagazine.com/wp-content/uploads/2018/04/Athleisure-pic-7.jpg',
    description: 'Combining athletic and casual wear for versatility.',
    link: 'athleisure.js',
  },
];

const DressPage = () => (
  <div style={styles.body}>
    <header style={styles.header}>
      <h1 className="app-name">Fashion Fusion</h1>
    </header>
    <div style={styles.container}>
      {dresses.map((dress, index) => (
        <div key={index} style={styles.dressBox}>
          <div style={styles.imageContainer}>
            <img src={dress.image} alt={dress.title} style={styles.image} />
          </div>
          <h2 style={styles.dressTitle}>{dress.title}</h2>
          <a href={dress.link} className="dress-link">Click here!!</a>
          <p style={styles.dressDescription}>{dress.description}</p>
        </div>
      ))}
    </div>
  </div>
);

export default DressPage;
