import React, { useEffect } from 'react'
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Header.css'


async function getUser(id){
    const response =  await fetch('http://localhost:8000/api/getuser/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({id}),
    });
    return response.json();
}
export default function Header({title="title"}) {
    const [name,setName] = useState('')
    const navigate = useNavigate();

    useEffect(()=>{
        const tokenData = JSON.parse(sessionStorage.getItem('token'));
        const id = tokenData?.token;
        if (id){
            getUser(id).then(data=>{
                if(data.user){
                    setName(data.user)
                }
                else{
                    setName("Guest User");
                }
            });
        }
    },[]);

    function handleHamburgerClick(){
        console.log("Menu clicked");
    }
    function handleBasketClick(){
        console.log("Navigating to '/shopping-cart'");
        navigate('/shopping-cart')
    }
    function handleProfileClick(){
        console.log("Profile clicked");
        // console.log(`Name ${getUser(id)}`);
    }
  return (
    <div id="header" className="container-fluid ">
        <div className="row main-line">
            <div className="col-lg-auto">
                <span className="int-icon icon-menu" onClick={e=>{
                    e.stopPropagation();
                    handleHamburgerClick();
                    }}></span>
            </div>
            <div className="col-lg-10">
                <h1>{title}</h1>
            </div>
            <div className="col-lg">
                <span className="int-icon icon-basket" onClick={e=>{
                    e.stopPropagation();
                    handleBasketClick();
                }}></span>
                <span className="int-icon icon-user" onClick={e=>{
                    e.stopPropagation();
                    handleProfileClick();
                }}></span>
            </div>
            
        </div>
        <div className="row">
            <b className="user-text">Logged in as user: {name}</b>
        </div>
    </div>
  )
}
