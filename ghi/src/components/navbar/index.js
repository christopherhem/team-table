import React, { useEffect } from 'react'
import { FaBars } from 'react-icons/fa'
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
  FlexContainer,
} from './NavbarElements';

const NavBar = ({ toggle }) => {

  useEffect(() => {
    window.addEventListener('scroll', (e) => {
    })
  }, []);

  const toggleHome = () => {
    scroll.scrollToTop();
  };

  return (
    <>
      <Nav>
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
                offset={-100}
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
                offset={-80}
              >
                Discover
              </NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks
                to="product"
                smooth={true}
                duration={100}
                spy={true}
                exact='true'
                offset={-150}
              >
                Our Product
              </NavLinks>
            </NavItem>
          </NavMenu>
          <FlexContainer >
            <NavButton>
              <NavBtnLink to="signup">Sign Up</NavBtnLink>
            </NavButton>
            <NavButton>
              <NavBtnLink to="signin">Sign In</NavBtnLink>
            </NavButton>
          </FlexContainer>
        </NavbarContainer>
      </Nav>
    </>
  )
}

export default NavBar
