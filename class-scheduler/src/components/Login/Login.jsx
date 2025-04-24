import React, {useState} from 'react'
import PropTypes from 'prop-types';
import './Login.css'

async function loginUser(credentials){
    console.log(credentials)
    return fetch('http://localhost:8000/api/login/',{
        method:'POST',
        headers:{
            'Content-Type' : 'application/json'
        },
        body:JSON.stringify(credentials)
    })
    .then(data=>data.json())
}



export default function Login({setToken}) {
    const [id,setId] = useState();
    const [password, setPassword] = useState();
    const [invalidPassword, setInvalidPassword] = useState(false);
    const handleSubmit = async e=>{
        e.preventDefault();
        const token = await loginUser({
            id,
            password
        });
        setToken(token);
        if(token?.error == 'Invalid password'){
            setInvalidPassword(true);
        }
    }

  return (
    <div id="loginWrapper">

        <h1 className="col-lg-auto"id="signInText">Sign in</h1>
        <form className="loginForm" onSubmit={handleSubmit}>
            <div className="loginInput">
                <label className="row">
                    <h3>Student ID</h3>
                    <input id="student-id" type="text" onChange={e=>setId(e.target.value)} placeholder='Mulch T. Booger'/>
                </label>
                <label className="row">
                    <h3>Password</h3>
                    <input id="password" type="password" onChange={e=>setPassword(e.target.value)} placeholder=''/>
                </label>
            </div>
            <div className="submitLogin">
                <button className="col-xl-10"type="submit">Submit</button>
            </div>
        </form>
        <div className='invalid_password' style={{display: invalidPassword ? 'flex': 'none'}}>
            <p>Invalid username or password!</p>
        </div>
        <div className="forgotContainer">
            <a href="http://youtube.com/" target="_blank" rel="noopener noreferrer">Forgot User ID?</a>
            <a href="http://youtube.com/" target="_blank" rel="noopener noreferrer">Forgot Password?</a>

        </div>
    </div>
  )
}

Login.propTypes={
    setToken: PropTypes.func.isRequired
}