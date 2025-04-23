import React from 'react'
import './ShoppingCart.css'

export default function ShoppingCart() {
  return (
    <div id="shopping-container">
      <h3 style={{color:"var(--button-primary)"}}>Your shopping cart:</h3>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Select</th>
            <th scope="col">Course ID</th>
            <th scope="col">Description</th>
            <th scope="col">Day/Time</th>
            <th scope="col">Room</th>
            <th scope="col">Instructor</th>
            <th scope="col">Credits</th>
          </tr>
        </thead>

      </table>
    </div>
  )
}