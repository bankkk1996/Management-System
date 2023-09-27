import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./menu.scss";
import { menu } from "../../data";
import HomeOutlined from "@mui/icons-material/HomeOutlined";
import GroupOutlined from "@mui/icons-material/GroupOutlined";

const Menu = () => {

  const getIcon = (value) => {
    switch (value) {
      case "home":
        return <HomeOutlined />;
      case "group":
        return <GroupOutlined />;
      default:
        return null; // Return null or another default component for unsupported values
    }
  };

  return (
    <div className="menu">
      {menu.map((item) => (
        <div className="item" key={item.id}>
          <span className="title">{item.title}</span>
          {item.listItems.map((listItem) => (
            <Link to={listItem.url} className={listItem.class} key={listItem.id} >
              {getIcon(listItem.icon)}
              <span className="listItemTitle">{listItem.title}</span>
            </Link>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Menu;
