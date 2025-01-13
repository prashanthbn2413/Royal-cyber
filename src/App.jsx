import  { useEffect } from 'react';
import './App.css';
import NavBar from './NavBar';
import Card from './Card';
import products from './productData'; // Import the product data
import ChatbotButton from './ChatbotButton';

function App() {
  // Set the background color of the body to black when the component mounts
  useEffect(() => {
    document.body.style.backgroundColor = "black";

    // Cleanup: Reset body background color when the component unmounts
    return () => {
      document.body.style.backgroundColor = "";
    };
  }, []);

  return (
    <>
      <NavBar />
      <div className="product-cards">
        {/* Loop through products and render a Card for each product */}
        {products.map((product) => (
          <Card key={product.id} productId={product.id} />
        ))}
      </div>
      <ChatbotButton />
    </>
  );
}

export default App;
