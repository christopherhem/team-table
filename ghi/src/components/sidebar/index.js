import React from 'react'
import {
  SidebarContainer,
  Icon,
  CloseIcon,
  SidebarWrapper,
  SidebarMenu,
  SidebarLink,
  SidebarLinkR,
  SideBtnWrap,
  SidebarRoute
} from './SidebarElements';



const Sidebar = ({ isOpen, toggle }) => {
  return (
    <SidebarContainer isOpen={isOpen} onClick={toggle}>
      <Icon onClick={toggle}>
        <CloseIcon />
      </Icon>
      <SidebarWrapper>
        <SidebarMenu>
          <SidebarLink to="about" onClick={toggle}>About Us</SidebarLink>
          <SidebarLink to="discover" onClick={toggle}>Discover</SidebarLink>
          <SidebarLink to="product" onClick={toggle}>Our Product</SidebarLink>
          <SidebarLinkR to="signup" onClick={toggle}>Sign Up</SidebarLinkR>
        </SidebarMenu>
        <SideBtnWrap>
          <SidebarRoute to="/signin">
            Sign In
          </SidebarRoute>
        </SideBtnWrap>
      </SidebarWrapper>
    </SidebarContainer>
  )
}

export default Sidebar;
