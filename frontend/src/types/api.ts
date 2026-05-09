export interface ApiResponse<T> {
  success: boolean;
  message?: string;
  data: T;
}

export interface ApiErrorResponse {
  success: boolean;
  detail?: string;
  message?: string;
}

export interface PaginationResponse<T> {
  total: number;
  items: T[];
}

export type ApiStatus =
  | "idle"
  | "loading"
  | "success"
  | "error";