import React, { useState, useEffect } from 'react';
import { codeService } from '../services/api';
import NavBar from '../components/NavBar';
import CodeInput from '../components/CodeInput';
import Suggestions from '../components/Suggestions';
import History from '../components/History';

const MainPage = () => {
  const [code, setCode] = useState("");
  const [language, setLanguage] = useState("python");
  const [suggestions, setSuggestions] = useState("");
  const [history, setHistory] = useState([]);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const response = await codeService.getHistory();
      setHistory(response.data);
    } catch (error) {
      console.error('Error loading history:', error);
    }
  };

  const handleDeleteHistory = async (id) => {
    try {
      await codeService.deleteHistory(id);
      setHistory(history.filter(item => item.id !== id));
    } catch (error) {
      console.error('Error deleting history:', error);
    }
  };

  const handleOptimize = async () => {
    try {
      const response = await codeService.optimize(code, language);
      setSuggestions(response.data.suggestions || "No suggestions returned.");
      loadHistory();
    } catch (error) {
      console.error('Error optimizing code:', error);
    }
  };

  return (
    <div>
      <NavBar />
      <div className="page-container">
        <CodeInput 
          code={code}
          setCode={setCode}
          language={language}
          setLanguage={setLanguage}
          onGenerate={handleOptimize}
        />
        <Suggestions suggestions={suggestions} />
        <History 
          history={history}
          onDelete={handleDeleteHistory}
        />
      </div>
    </div>
  );
};

export default MainPage; 