import React from 'react';
import styled from 'styled-components';

const ChatButtonContainer = styled.div`
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: transparent;
  color: #6C9CEA;
  font-size: 50px;
  cursor: pointer;
  transition: color 0.3s;
  
  &:hover {
    color: #4A83C1;
  }
`;

const ChatButton = ({ toggleChat }) => {
  return (
    <ChatButtonContainer onClick={toggleChat}>
      <i className="fa-brands fa-facebook-messenger"></i>
    </ChatButtonContainer>
  );
};

export default ChatButton;
