import React from 'react'
import './Login.css'

export default function Login({token}) {
  return (
    <div id="loginWrapper">
        <form className="loginForm">
            <label>
                <h3>Username</h3>
                <input id="username" type="text" />
            </label>
            <label >
                <h3>Password</h3>
                <input id="password" type="password" />
            </label>
            <div className="submitLogin">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>
  )
}
