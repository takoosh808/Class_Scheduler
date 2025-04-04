import React from 'react'
import { useNavigate,useLocation } from 'react-router-dom';
import './Header.css'
import './Profile/Profile.jsx'
import { Profile } from './Profile/Profile.jsx';


export default function Header({name="name"}) {
    const navigate = useNavigate();
    const location = useLocation();
    const title = getTitle(location.pathname)
    function handleHamburgerClick(){
        console.log("Menu clicked");
    }
    function handleBasketClick(){
        console.log("Navigating to '/shopping-cart'");
        navigate('/shopping-cart')
    }
    function getTitle(path){
        let newPath = path.replace(/[-]/g," ");
        newPath = newPath.replace(/[//]/g,"")
        return newPath.charAt(0).toUpperCase() + newPath.slice(1);

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
                <Profile name="User1"/>
            </div>
            
        </div>
        <div className="row">
            <b className="user-text">Logged in as user: {name}</b>
        </div>
    </div>
  )
}
