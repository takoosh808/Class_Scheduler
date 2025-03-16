import React,{useState} from "react"
import {BrowserRouter, Route, Routes} from "react-router-dom"
import ClassSearch from '../ClassSearch/ClassSearch'
import Drop from '../Drop/Drop'
import Enroll from '../Enroll/Enroll'
import Header from '../Header/Header'
import Login from "../Login/Login"
import Sidebar from '../Sidebar/Sidebar'
import ShoppingCart from '../ShoppingCart/ShoppingCart'
import ViewClasses from "../ViewClasses/ViewClasses"
import WeeklySchedule from "../WeeklySchedule/WeeklySchedule"
import useToken from './useToken'

import './App.css'


function App() {
  const {token,setToken} = useToken();


  if(!token){
    return <Login setToken={setToken}/>
  }
  
  return (
    <BrowserRouter>
      <Header title="Shopping Cart"/>
      <Sidebar />
      <main>
        <Routes>
          <Route path="/shopping-cart" element={<ShoppingCart />}/>
          <Route path="/weekly-schedule" element={<WeeklySchedule />} />
          <Route path="/view-classes" element={<ViewClasses />}/>
          <Route path="/class-search" element={<ClassSearch/>} />
          <Route path="/enroll" element={<Enroll />} />
          <Route path="/drop" element={<Drop />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App
