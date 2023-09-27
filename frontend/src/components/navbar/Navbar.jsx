import React from 'react'
import './navbar.scss'
import SearchOutlinedIcon from '@mui/icons-material/SearchOutlined';
import GridViewOutlinedIcon from '@mui/icons-material/GridViewOutlined';
import CropFreeOutlinedIcon from '@mui/icons-material/CropFreeOutlined';
import NotificationsNoneOutlinedIcon from '@mui/icons-material/NotificationsNoneOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import Badge from '@mui/material/Badge';

const Navbar = () => {
  return (
    <div className='navbar'>
      <div className="logo">
        <img src="logo.svg" alt="" />
        <span>Hoteladmin</span>
      </div>
      <div className="icons">
        <SearchOutlinedIcon className='icon'/>
        <GridViewOutlinedIcon className='icon' />
        <CropFreeOutlinedIcon className='icon'/>
        <Badge badgeContent={4} color='error'>
          <NotificationsNoneOutlinedIcon/>
        </Badge>
        <div className="user">
          <img src="https://img.freepik.com/free-photo/smart-attractive-asian-glasses-male-standing-smile-with-freshness-joyful-casual-blue-shirt-portrait-white-background_609648-1226.jpg?size=626&ext=jpg&ga=GA1.2.311963722.1695658358&semt=sph" alt="" />
          <span>John Doe</span>
        </div>
        <SettingsOutlinedIcon/>
      </div>
    </div>
  )
}

export default Navbar