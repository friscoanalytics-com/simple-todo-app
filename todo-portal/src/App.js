import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8095/todos";

function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");

  // Fetch todos on component mount
  useEffect(() => {
    fetchTodos();
  }, []);

  // Fetch all todos
  const fetchTodos = async () => {
    try {
      const response = await axios.get(API_URL);
      setTodos(response.data);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  // Add a new todo
  const addTodo = async () => {
    if (!title.trim()) return;

    try {
      const newTodo = { title, completed: false };
      await axios.post(API_URL, newTodo);
      setTitle(""); 
      fetchTodos(); 
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  // Update a todo
  const toggleTodo = async (id, completed) => {
    try {
      const updatedTodo = {
        title: todos.find(t => t.id === id).title, 
        completed: !completed
      };
      await axios.put(`${API_URL}/${id}`, updatedTodo);
      fetchTodos(); 
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  // Delete a todo
  const deleteTodo = async (id) => {
    try {
      await axios.delete(`${API_URL}/${id}`);
      fetchTodos(); 
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  return (
    <div className="App" style={{ padding: "2rem" }}>
      <h1>To-Do App</h1>

      <div>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a new task"
          style={{ padding: "0.5rem", width: "200px", marginRight: "1rem" }}
        />
        <button onClick={addTodo} style={{ padding: "0.5rem 1rem" }}>Add</button>
      </div>

      <ul style={{ listStyleType: "none", padding: 0, marginTop: "1rem" }}>
        {todos.map((todo) => (
          <li key={todo.id} style={{ margin: "0.5rem 0" }}>
            <span
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
                marginRight: "1rem",
                cursor: "pointer"
              }}
              onClick={() => toggleTodo(todo.id, todo.completed)}
            >
              {todo.title}
            </span>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
