// import React from 'react';
import './Card.css'; // Import the CSS file for styling
import products from './productData'; // Import the product data

function Card({ productId }) {
    // Find the product by ID from the products array
    const product = products.find((item) => item.id === productId);

    // If product not found, return null or a placeholder
    if (!product) {
        return <div>Product not found</div>;
    }

    return (
        <>
            <div className="cards-container">
                <div className="card">
                    <img src={product.image} alt={product.name} className="card-image" />
                    <div className="card-details">
                        <h5 className="card-name">{product.name}</h5>
                        <p>{product.description}</p>
                    </div>
                </div>
            </div>
            

        </>

    );
}

export default Card;
