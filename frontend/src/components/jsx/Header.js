import React from "react";
import logo from "../../assets/logo.svg";
import styled from "styled-components";
import { NavLink } from "react-router-dom";  // Use NavLink for active link styling

const StyledHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: white;
  color: #6C9CEA;
  margin: 0 20px; /* Add margin on the left and right to create space between edges */

  /* Add top and bottom borders */
  // border-bottom: 2px solid #6C9CEA;

  /* Removed border-radius to remove rounded corners */

  .left-section {
    display: flex;
    align-items: center;

    img {
      width: 40px;
      height: auto;
      margin-right: 10px;
    }

    h3 {
      margin: 0;
      font-size: 24px;
    }

    nav {
      display: flex;
      margin-left: 20px;

      /* Style for nav items */
      .nav-item {
        margin: 0 15px;
        cursor: pointer;
        font-weight: bold;
        font-size: 18px; /* Increase font size */
        color: #D3D3D3; /* Default light gray color */
        text-decoration: none; /* Remove underline */
        transition: color 0.3s;

        &:hover {
          color: #6C9CEA; /* Primary color on hover */
        }

        &.active {
          color: #6C9CEA; /* Primary color when active */
        }
      }
    }
  }

  .right-section {
    display: flex;
    align-items: center;

    div {
      margin-left: 20px;
      cursor: pointer;
      font-weight: bold;
      transition: color 0.3s;

      &:hover {
        color: #6C9CEA;
      }
    }
  }
`;

const Header = () => {
  return (
    <StyledHeader>
      <div className="left-section">
        <img src={logo} alt="Logo" />
        <h3></h3>
        <nav>
          <NavLink
            to="#"
            className="nav-item"
            activeClassName="active"
          >
            <div>DFA</div>
          </NavLink>
          <NavLink
            to="#"
            className="nav-item"
            activeClassName="active"
          >
            <div>NFA</div>
          </NavLink>
          <NavLink
            to="#"
            className="nav-item"
            activeClassName="active"
          >
            <div>Regular Grammar</div>
          </NavLink>
        </nav>
      </div>
      <div className="right-section">
        <div>Đăng nhập</div>
        <div>Đăng ký</div>
      </div>
    </StyledHeader>
  );
};

export default Header;
