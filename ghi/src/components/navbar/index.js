import React from 'react'
import { FaBars } from 'react-icons/fa'
import { 
  Nav, 
  NavbarContainer, 
  NavLogo, 
  MobileIcon, 
  NavMenu, 
  NavItem, 
  NavLinks,
  NavButton,
  NavBtnLink, 
} from './NavbarElements';

const NavBar = ({toggle}) => {

  return (
    <>
      <Nav>
        <NavbarContainer>
          <NavLogo>TeamTable</NavLogo>
          <MobileIcon onClick={toggle}>
            <FaBars />
          </MobileIcon>
          <NavMenu>
            <NavItem>
              <NavLinks to="about">About Us</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to="discover">Discover</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to="services">Services</NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks to="/signup">Sign Up</NavLinks>
            </NavItem>
          </NavMenu>
          <NavButton>
            <NavBtnLink to="signin">Sign In</NavBtnLink>
          </NavButton>
        </NavbarContainer>
      </Nav>


    </>
  )
}

export default NavBar