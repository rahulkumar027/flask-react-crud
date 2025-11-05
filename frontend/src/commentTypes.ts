export type Comment = {
  id: number;
  task_id: number;
  body: string;
  author: string;
  created_at: string;
  updated_at: string;
};

export type CommentCreate = {
  body: string;
  author?: string;
};

export type CommentUpdate = Partial<CommentCreate>;
