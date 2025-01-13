import React, { useState } from 'react';
import './ChatbotButton.css'; // For styling the floating button

function ChatbotButton() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleChatbot = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      {/* Floating button */}
      <button className="chatbot-button" onClick={toggleChatbot}>
        Order Here
      </button>

      {/* Chatbot iframe */}
      {isOpen && (
        <div className="chatbot-container">
         <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/0004d96c-c620-43a3-a085-9013c207406b"></iframe>
        </div>
      )}
    </div>
  );
}

export default ChatbotButton;
