import React, { useState, useEffect } from 'react';
import './ShoppingCart.css';
import axios from 'axios';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);
  const studentId = localStorage.getItem("student_id");

  const handleEnroll = () => {
    axios.post("http://localhost:8000/api/enroll/", {
      student_id: localStorage.getItem("student_id")
    })
    .then(response => {
      alert("Enrollment successful!");
      setCartItems([]); // Clear the cart in frontend too
    })
    .catch(error => {
      console.error("Enrollment failed:", error);
      alert("Enrollment failed. Try again.");
    });
  };

  useEffect(() => {
    if (!studentId) return;

    axios.get(`http://localhost:8000/api/cart/${studentId}/`)
      .then(response => {
        setCartItems(response.data.cart || []);
      })
      .catch(error => {
        console.error("Error loading cart:", error);
      });
  }, [studentId]);

  return (
    <div>
      <h2 style={{ marginLeft: '300px', marginTop: '20px' }}>Your Cart</h2>

      <div className="cartWrapper">
        <table className="searchWrapper">
          <thead>
            <tr className="title">
              <th>Course</th>
              <th>SLN</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            {cartItems.length === 0 ? (
              <tr className="result">
                <td colSpan="3">Your cart is empty.</td>
              </tr>
            ) : (
              cartItems.map((item, index) => (
                <tr key={index} className="result">
                  <td>{item.course_name}</td>
                  <td>{item.id_number}</td>
                  <td>{item.quantity}</td>
                  <td>
                  {cartItems.length > 0 && (
                    <button className="submit" onClick={handleEnroll}>Enroll in Courses</button>
                  )}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Cart;
