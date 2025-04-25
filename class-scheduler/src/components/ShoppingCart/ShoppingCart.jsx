import React, { useState, useEffect } from 'react';
import './ShoppingCart.css';
import axios from 'axios';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);
  const studentId = localStorage.getItem("student_id");

  const handleRemoveFromCart = (courseId) => {
    const studentId = localStorage.getItem("student_id");
    console.log(studentId);
    console.log(courseId);
    console.log(cartItems)
    axios.post("http://localhost:8000/api/cart/remove/", {
      student_id: studentId, // or your context variable
      course_id: courseId
    })
    .then(res => {
      alert("Removed from cart.");
      setCartItems(prev => prev.filter(item => item.id_number !== courseId));
    })
    .catch(err => {
      console.error("Remove failed:", err);
      alert("Failed to remove course from cart.");
    });
  };

  const handleEnroll = (courseId) => {
    axios.post("http://localhost:8000/api/enroll/", {
      student_id: localStorage.getItem("student_id"),
      course_id: courseId
    })
    .then(response => {
      const message = response.data.message || "Enrolled successfully.";
      alert(message);
      setCartItems(prev => prev.filter(item => item.id_number !== courseId));
    })
    .catch(error => {
      if (error.response) {
        const message = error.response.data.message || error.response.data.error || "Enrollment failed.";
        alert(`${message}`);
      } else {
        alert("Network error or server unavailable.");
      }
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
              <th>Instructor</th>
              <th>Time</th>
              <th>Date</th>
              <th>Location</th>
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
                  <td>{item.instructor}</td>
                  <td>{item.time}</td>
                  <td>{item.date}</td>
                  <td>{item.location}</td>
                  <td>{item.quantity}</td>
                  <td>
                  {cartItems.length > 0 && (
                    <button className="submit" onClick={() => handleEnroll(item.id_number)}>Enroll in Courses</button>
                  )}
                  </td>
                  <td>
                  <button
                      className="submit"
                      onClick={() => handleRemoveFromCart(item.id_number)}
                    >
                      Remove
                    </button>
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