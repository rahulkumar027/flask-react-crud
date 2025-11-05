import { useEffect, useState } from "react";
import { api } from "./api";

interface Task {
  id: number;
  title: string;
  description?: string;
}

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTitle, setNewTitle] = useState("");

  // ✅ Fetch all tasks
  const loadTasks = async () => {
    try {
      const res = await api.get("/tasks");
      setTasks(res.data.items || []);
    } catch (err) {
      console.error(err);
    }
  };

  // ✅ Add a new task
  const addTask = async () => {
    if (!newTitle.trim()) return;
    await api.post("/tasks", { title: newTitle });
    setNewTitle("");
    loadTasks();
  };

  // ✅ Delete a task
  const deleteTask = async (id: number) => {
    await api.delete(`/tasks/${id}`);
    loadTasks();
  };

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "system-ui" }}>
      <h2>📝 Task Manager</h2>

      <div style={{ marginBottom: 20 }}>
        <input
          type="text"
          placeholder="New task title"
          value={newTitle}
          onChange={(e) => setNewTitle(e.target.value)}
          style={{ padding: 8, width: 250 }}
        />
        <button onClick={addTask} style={{ marginLeft: 10, padding: "8px 16px" }}>
          ➕ Add Task
        </button>
      </div>

      {tasks.length === 0 ? (
        <p>No tasks found.</p>
      ) : (
        <ul>
          {tasks.map((t) => (
            <li key={t.id} style={{ marginBottom: 8 }}>
              {t.title}
              <button
                onClick={() => deleteTask(t.id)}
                style={{
                  marginLeft: 10,
                  background: "#e33",
                  color: "#fff",
                  border: "none",
                  padding: "4px 8px",
                  borderRadius: 4,
                  cursor: "pointer",
                }}
              >
                🗑️ Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}


