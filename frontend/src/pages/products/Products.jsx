import React, {useEffect} from "react";
import "./products.scss";
import { useNavigate} from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const Products = () => {
  const navigate = useNavigate();
  const { token, login } = useAuth();
  useEffect(()=>{
    
    if (token===''){
      navigate("/login")
    }

  },[])
  return <div className="products">Products</div>;
};

export default Products;
