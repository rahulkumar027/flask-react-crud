import { useEffect, useState } from "react";
import { api } from "../api";
import type { Comment, CommentCreate, CommentUpdate } from "../commentTypes";

type Props = { taskId: number };

export default function CommentsPanel({ taskId }: Props) {
  const [items, setItems] = useState<Comment[]>([]);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [newBody, setNewBody] = useState("");
  const [newAuthor, setNewAuthor] = useState("Rahul");

  const log = (...a: any[]) => console.log("[CommentsPanel]", ...a);

  const load = async () => {
    setLoading(true);
    setErr(null);
    try {
      log("GET /tasks/%d/comments", taskId);
      const res = await api.get(`/tasks/${taskId}/comments`);
      setItems(res.data.items ?? []);
      log("Loaded", res.data);
    } catch (e: any) {
      const msg = e?.response?.data?.message || e.message;
      setErr("Load failed: " + msg);
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { load(); }, [taskId]);

  const create = async () => {
    const payload: CommentCreate = {
      body: newBody.trim(),
      author: newAuthor.trim() || "Anonymous",
    };
    if (!payload.body) return;

    try {
      setLoading(true);
      setErr(null);
      log("POST /tasks/%d/comments", taskId, payload);
      await api.post(`/tasks/${taskId}/comments`, payload);
      setNewBody("");
      await load();
    } catch (e: any) {
      const msg = e?.response?.data?.message || e.message;
      setErr("Create failed: " + msg);
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const update = async (id: number, patch: CommentUpdate) => {
    try {
      setLoading(true);
      setErr(null);
      log("PATCH /comments/%d", id, patch);
      await api.patch(`/comments/${id}`, patch);
      await load();
    } catch (e: any) {
      const msg = e?.response?.data?.message || e.message;
      setErr("Update failed: " + msg);
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const remove = async (id: number) => {
    try {
      setLoading(true);
      setErr(null);
      log("DELETE /comments/%d", id);
      await api.delete(`/comments/${id}`);
      await load();
    } catch (e: any) {
      const msg = e?.response?.data?.message || e.message;
      setErr("Delete failed: " + msg);
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="grid gap-3">
      <div className="flex items-center gap-2">
        <span style={{fontSize: 22}}>💬</span>
        <h2 className="text-2xl font-semibold">Task #{taskId} Comments</h2>
      </div>

      {/* creator */}
      <div className="flex gap-2 items-center">
        <input
          value={newBody}
          onChange={(e) => setNewBody(e.target.value)}
          placeholder="Write a comment…"
          className="border rounded px-3 py-2 flex-1"
        />
        <input
          value={newAuthor}
          onChange={(e) => setNewAuthor(e.target.value)}
          placeholder="Author"
          className="border rounded px-3 py-2 w-40"
        />
        <button
          onClick={create}
          disabled={!newBody.trim() || loading}
          className="bg-black text-white px-3 py-2 rounded disabled:opacity-50"
        >
          Add
        </button>
      </div>

      {loading && <p>Loading…</p>}
      {err && <p className="text-red-500">{err}</p>}

      <ul className="grid gap-2">
        {items.map((c) => (
          <CommentRow key={c.id} c={c} onUpdate={update} onDelete={remove} />
        ))}
      </ul>
    </div>
  );
}

function CommentRow({
  c,
  onUpdate,
  onDelete,
}: {
  c: Comment;
  onUpdate: (id: number, patch: CommentUpdate) => Promise<void> | void;
  onDelete: (id: number) => Promise<void> | void;
}) {
  const [isEditing, setIsEditing] = useState(false);
  const [body, setBody] = useState(c.body);
  const [author, setAuthor] = useState(c.author);

  const save = async () => {
    await onUpdate(c.id, {
      body: body.trim(),
      author: author.trim() || "Anonymous",
    });
    setIsEditing(false);
  };

  return (
    <li className="border rounded p-3 bg-white text-black">
      {isEditing ? (
        <div className="grid gap-2">
          <input
            className="border rounded px-2 py-1"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
          />
          <textarea
            className="border rounded px-2 py-1"
            value={body}
            onChange={(e) => setBody(e.target.value)}
          />
          <div className="flex gap-2">
            <button onClick={save} className="bg-black text-white px-3 py-1 rounded">Save</button>
            <button onClick={() => setIsEditing(false)} className="px-3 py-1 rounded border">Cancel</button>
          </div>
        </div>
      ) : (
        <div className="grid gap-1">
          <div className="text-sm text-gray-600">
            {new Date(c.created_at).toLocaleString()}
          </div>
          <div><strong>{c.author}</strong>: {c.body}</div>
          <div className="flex gap-2 mt-1">
            <button onClick={() => setIsEditing(true)} className="px-3 py-1 rounded border">Edit</button>
            <button onClick={() => onDelete(c.id)} className="px-3 py-1 rounded border border-red-500 text-red-600">Delete</button>
          </div>
        </div>
      )}
    </li>
  );
}
