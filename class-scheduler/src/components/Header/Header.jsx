import React from 'react'
import { useNavigate } from 'react-router-dom';
import './Header.css'


export default function Header({title="title"}) {
    const navigate = useNavigate();
    function handleHamburgerClick(){
        console.log("Menu clicked");
    }
    function handleBasketClick(){
        console.log("Navigating to '/shopping-cart'");
        navigate('/shopping-cart')
    }
    function handleProfileClick(){
        console.log("Profile clicked");
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
            <b className="user-text">Logged in as user: User1</b>
        </div>
    </div>
  )
}
