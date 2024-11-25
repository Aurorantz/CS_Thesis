import React, { useState } from 'react';
import styled from 'styled-components';

const ChatWindowContainer = styled.div`
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  background-color: white;
  border: 1px solid #6C9CEA;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 10px;
  z-index: 1000;
  animation: fadeIn 0.3s ease-in-out;

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
`;

const ChatHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const CloseButton = styled.button`
  background-color: transparent;
  border: none;
  color: #6C9CEA;
  font-size: 20px;
  cursor: pointer;
`;

const ChatBody = styled.div`
  margin-top: 10px;
  max-height: 300px;
  overflow-y: auto;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  display: flex;
  flex-direction: column-reverse;
`;

const Message = styled.div`
  display: flex;
  margin: 5px 0;
  justify-content: ${({ sender }) => (sender === 'user' ? 'flex-end' : 'flex-start')};
  align-items: flex-end;
  max-width: 80%;
`;

const MessageContent = styled.div`
  background-color: ${({ sender }) => (sender === 'user' ? '#6C9CEA' : '#ddd')};
  color: ${({ sender }) => (sender === 'user' ? 'white' : 'black')};
  padding: 8px 15px;
  border-radius: 10px;
  max-width: 70%;
`;

const Timestamp = styled.div`
  font-size: 12px;
  color: #888;
  margin-left: 10px;
`;

const ChatFooter = styled.div`
  display: flex;
  margin-top: 10px;
`;

const Input = styled.input`
  width: 80%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const SendButton = styled.button`
  width: 15%;
  padding: 8px;
  border: none;
  background-color: #6C9CEA;
  color: white;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #4A83C1;
  }
`;

const ChatWindow = ({ messages, userInput, handleInputChange, handleSendMessage, toggleChat }) => {
  return (
    <ChatWindowContainer>
      <ChatHeader>
        <h3>Chat with Us!</h3>
        <CloseButton onClick={toggleChat}>X</CloseButton>
      </ChatHeader>
      <ChatBody>
        <div className="message-list">
          {messages.map((msg, index) => (
            <Message key={index} sender={msg.sender}>
              <MessageContent sender={msg.sender}>
                {msg.text}
              </MessageContent>
              <Timestamp>{msg.timestamp.toLocaleTimeString()}</Timestamp>
            </Message>
          ))}
        </div>
      </ChatBody>
      <ChatFooter>
        <Input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="Type your message..."
        />
        <SendButton onClick={handleSendMessage}>Send</SendButton>
      </ChatFooter>
    </ChatWindowContainer>
  );
};

export default ChatWindow;
