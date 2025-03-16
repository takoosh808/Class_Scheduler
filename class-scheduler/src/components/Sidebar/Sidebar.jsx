import React from 'react'
import { useNavigate } from 'react-router-dom';
import './Sidebar.css'

export default function Sidebar() {
    let numCards = 0;
  return (
    <aside id="aside">
        <Card key={numCards++} icon="calendar" text="Weekly Schedule" path="/weekly-schedule"/>
        <Card key={numCards++} icon="people" text="View Classes" path="/view-classes"/>
        <Card key={numCards++} icon="magnifier" text="Class Search" path="/class-search"/>
        <Card key={numCards++} icon="cursor" text="Enroll for Classes" path="/enroll"/>
        <Card key={numCards++} icon="close" text="Drop Classes" path="/drop"/>
    </aside>
  )
}

function Card({icon, text, path}) {
    const navigate = useNavigate();

    function handleClick(){
        console.log(`Navigating to ${path}`);
        navigate(path);
    }

  return (
    <div className="card row" onClick={e=>{
        e.stopPropagation();
        handleClick();
        }}>
        <span >
            <i style={{fontSize:"30px"}} className={"icon-"+icon}></i>
            <h3 style={{float:"right"}}>{text}</h3>
        </span>
        
    </div>
  )
}
