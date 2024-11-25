import React from "react";
import styled from "styled-components";

const StyledFooter = styled.footer`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: white;
  color: #6C9CEA;
//   border-top: 2px solid #6C9CEA;
  margin: 0 20px; /* Add margin to the left and right of the footer */
  
  .left-section {
    font-size: 14px;
  }

  .right-section {
    display: flex;
    align-items: center;

    a {
      margin-left: 20px;
      color: #6C9CEA;
      font-weight: bold;
      text-decoration: none;
      transition: color 0.3s;

      &:hover {
        color: #4A83C1; /* Darker hover effect */
      }
    }
  }
`;


const Footer = () => {
  return (
    <StyledFooter>
      <div className="left-section">
        <p>&copy; {new Date().getFullYear()} Automata. All rights reserved.</p>
      </div>
      <div className="right-section">
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </div>
    </StyledFooter>
  );
};

export default Footer;
