/* import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App */

import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/v1/tasks/", {
      headers: {
        // Authorization: "Token your_api_token_here",
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("API Response:", data); // Debugging: See the response format
        setTasks(data);
      })
      .catch((err) => {
        console.error("Error fetching tasks:", err);
        setError(err.message);
      });
  }, []);

  return (
    <div className="App">
      <h1>Task List</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {tasks.length > 0 ? (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong> <br />
              期限: {task.due_date || "未設定"} <br />
              頻度: {task.frequency_label || "日"} <br />
              状態: {task.is_completed ? "完了" : "未着手"}
              <br />
              {task.memo && <span>メモ: {task.memo}</span>}
            </li>
          ))}
        </ul>
      ) : (
        <p>タスクがありません。</p>
      )}
    </div>
  );
}

export default App;
