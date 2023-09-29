import React, {useEffect} from 'react'
import './home.scss'
import { useNavigate} from "react-router-dom";
import { useAuth } from "../../context/AuthContext";


const Home = () => {
  const navigate = useNavigate();
  useEffect(()=>{
    if (localStorage.getItem("token")===null){
      navigate("/login")
    }

  },[])
  return (
    <div className='home'>
      <h1><span>TEST</span> data</h1>
    </div>
  )
}

export default Home