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
  const [isLoading, setIsLoading] = useState(false);

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
    if (!code.trim()) {
      setSuggestions("Please enter some code first.");
      return;
    }

    setIsLoading(true);
    setSuggestions("Analyzing your code and generating optimization suggestions...");

    try {
      const response = await codeService.optimizeCode(code, language);
      if (response.data) {
        setSuggestions(response.data.suggestions || response.data.optimized_code || "No suggestions returned.");
        await loadHistory();  // Reload history
      } else {
        setSuggestions("No response received from the server.");
      }
    } catch (error) {
      console.error('Error optimizing code:', error);
      setSuggestions("Error: " + (error.response?.data?.message || error.message || "Failed to optimize code"));
    } finally {
      setIsLoading(false);
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
          isLoading={isLoading}
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