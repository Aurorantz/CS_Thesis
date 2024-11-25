import React, { useState } from 'react';
import './App.css';
import Header from './components/jsx/Header'; // Importing the Header component
import Footer from './components/jsx/Footer'; // Importing the Footer component
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ChatButton from './components/jsx/ChatButton'; // Importing the ChatButton component
import ChatWindow from './components/jsx/ChatWindow'; // Importing the ChatWindow component

function App() {
  // State for toggling the chat window
  const [showChat, setShowChat] = useState(false);
  const [messages, setMessages] = useState([
    { text: "Hello, how can I assist you today?", sender: "bot", timestamp: new Date() }
  ]);
  const [userInput, setUserInput] = useState("");

  const toggleChat = () => {
    setShowChat(!showChat);
  };

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleSendMessage = () => {
    if (userInput.trim()) {
      const newMessages = [...messages, { text: userInput, sender: "user", timestamp: new Date() }];
      setMessages(newMessages);
      setUserInput("");
      
      // Simulate bot response after a short delay
      setTimeout(() => {
        setMessages(prevMessages => [
          ...prevMessages,
          { text: "Thank you for your message!", sender: "bot", timestamp: new Date() }
        ]);
      }, 1000);
    }
  };

  return (
    <Router>
      <div className="App">
        <Header />
        <div className="content">
          <Routes>
            <Route path="/" element={<h1>Welcome to My React App!</h1>} />
          </Routes>
        </div>
        <Footer />

        <ChatButton toggleChat={toggleChat} />

        {showChat && (
          <ChatWindow
            messages={messages}
            userInput={userInput}
            handleInputChange={handleInputChange}
            handleSendMessage={handleSendMessage}
            toggleChat={toggleChat}
          />
        )}
      </div>
    </Router>
  );
}

export default App;
