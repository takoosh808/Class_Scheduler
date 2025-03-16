import React,{useState} from "react"
import {BrowserRouter, Route, Routes} from "react-router-dom"
import ClassSearch from './components/ClassSearch/ClassSearch'
import Drop from './components/Drop/Drop'
import Enroll from './components/Enroll/Enroll'
import Header from './components/Header/Header'
import Login from "./components/Login/Login"
import Sidebar from './components/Sidebar/Sidebar'
import ShoppingCart from './components/ShoppingCart/ShoppingCart'
import ViewClasses from "./components/ViewClasses/ViewClasses"
import WeeklySchedule from "./components/WeeklySchedule/WeeklySchedule"

import './App.css'

function App() {
  //Next step is adding the login system
  // const [token, setToken]=useState();
  // if(!token){
  //   return <Login token={token}/>
  // }
  
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
