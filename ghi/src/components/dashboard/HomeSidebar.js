import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { Link, NavLink } from 'react-router-dom';
import {
  ProSidebar,
  Menu,
  MenuItem,
  SubMenu,
  SidebarHeader,
  SidebarFooter,
  SidebarContent
} from 'react-pro-sidebar';
import {
  FaUser,
  FaAngleDoubleLeft,
  FaAngleDoubleRight,
  FaPeopleArrows,
  FaCalendarDay,
  FaHome,
  FaPencilAlt,
  FaSignOutAlt
} from 'react-icons/fa';
import { useSignOutMutation } from '../../store/UsersApi';

function SignOutButton() {
  const navigate = useNavigate();
  const [signOut, { data }] = useSignOutMutation();

  useEffect(() => {
    if (data) {
      navigate('/');
    }
  }, [data, navigate]);

  return (
    <Link
      className="sidebar-btn"
      style={{ cursor: 'pointer' }}
      onClick={signOut} 
    >
      <FaSignOutAlt />
      <span>Logout</span>
    </Link>
  );
}

const HomeSidebar = ({
  image,
  collapsed,
  toggled,
  handleToggleSidebar,
  handleCollapsedChange
}) => {
  return (
    <ProSidebar
      collapsed={collapsed}
      toggled={toggled}
      onToggle={handleToggleSidebar}
      breakPoint="md"
    >
      <SidebarHeader>
        <Menu iconShape="circle">
          {collapsed ? (
            <MenuItem
              icon={<FaAngleDoubleRight />}
              onClick={handleCollapsedChange}
            ></MenuItem>
          ) : (
            <MenuItem
              suffix={<FaAngleDoubleLeft />}
              onClick={handleCollapsedChange}
            >
              <div
                style={{
                  padding: '9px',
                  textTransform: 'uppercase',
                  fontWeight: 'bold',
                  fontSize: 15,
                  letterSpacing: '1px'
                }}
              >
                Team Table
              </div>
            </MenuItem>
          )}
        </Menu>
      </SidebarHeader>
      {/* Content */}
      <SidebarContent>
        <Menu iconShape="circle">
          <MenuItem
            icon={<FaHome />}
            suffix={<span className="badge red">NEW</span>}
          >
            My Home
            <NavLink to="/" />
          </MenuItem>
          <MenuItem
            icon={<FaPeopleArrows />}
            suffix={<span className="badge red">NEW</span>}
          >
            Teams
            <NavLink to="/team" />
          </MenuItem>
          {/* <MenuItem icon={<FaGem />}>Components </MenuItem> */}
          <MenuItem icon={<FaCalendarDay />}>
            My Events <Link to="/events" />
          </MenuItem>
          <SubMenu
            suffix={<span className="badge yellow">3</span>}
            title={'Create Event'}
            icon={<FaPencilAlt />}
          >
            <MenuItem>Cover</MenuItem>
            <MenuItem>Swap</MenuItem>
            <MenuItem>Availability</MenuItem>
          </SubMenu>
          {/* <SubMenu
            prefix={<span className="badge gray">3</span>}
            title={'With Prefix'}
            icon={<FaHeart />}
          >
            <MenuItem>Submenu 1</MenuItem>
            <MenuItem>Submenu 2</MenuItem>
            <MenuItem>Submenu 3</MenuItem>
          </SubMenu>
          <SubMenu title={'Multi Level'} icon={<FaList />}>
            <MenuItem>Submenu 1 </MenuItem>
            <MenuItem>Submenu 2 </MenuItem>
            <SubMenu title={'Submenu 3'}>
              <MenuItem>Submenu 3.1 </MenuItem>
              <MenuItem>Submenu 3.2 </MenuItem>
            </SubMenu> */}
          {/* </SubMenu> */}
        </Menu>
      </SidebarContent>
      {/* Footer */}
      <SidebarFooter style={{ textAlign: 'center' }}>
        <div className="sidebar-btn-wrapper" style={{ padding: '16px' }}>
          <Link
            className="sidebar-btn"
            style={{ cursor: 'pointer' }}
            to="/profile"
          >
            <FaUser />
            <span>My Account</span>
          </Link>
          <SignOutButton />
        </div>
      </SidebarFooter>
    </ProSidebar>
  );
};

export default HomeSidebar;
