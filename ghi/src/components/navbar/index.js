import React, { useEffect, useState } from 'react'
import { FaBars } from 'react-icons/fa'
import {IconContext} from 'react-icons/lib'
import { animateScroll as scroll } from 'react-scroll';
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
  const [scrollNav, setScrollNav] = useState(false);

  const changeNav = () => {
    if (window.scrollY >= 80) {
      setScrollNav(true);
    } else {
      setScrollNav(true);
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', changeNav)
  }, []);

  const toggleHome = () => {
    scroll.scrollToTop();
  };

  return (
    <>
      <Nav scrollNav={scrollNav}>
        <NavbarContainer>
          <NavLogo onClick={toggleHome} to='/'>
          TeamTable
          </NavLogo>
          <MobileIcon onClick={toggle}>
            <FaBars />
          </MobileIcon>
          <NavMenu>
            <NavItem>
              <NavLinks 
                to="about"
                smooth={true}
                duration={100}
                spy={true}
                exact='true'
                // offset={-100}
              >
                About Us
              </NavLinks>
            </NavItem>
            <NavItem>
            <NavLinks 
              to="discover"
              smooth={true}
              duration={100}
              spy={true}
              exact='true'
              // offset={-80}
            >
              Discover
            </NavLinks>
            </NavItem>
            <NavItem>
            <NavLinks 
              to="services"
              smooth={true}
              duration={100}
              spy={true}
              exact='true'
              // offset={-80}
            >
            Services
            </NavLinks>
            </NavItem>
          </NavMenu>
          <NavButton>
            <NavBtnLink to="signup">Sign Up</NavBtnLink>
          </NavButton>
          <NavButton>
            <NavBtnLink to="signin">Sign In</NavBtnLink>
          </NavButton>
        </NavbarContainer>
      </Nav>
    </>
  )
}

export default NavBar