import axios from "axios";

import { API_BASE_URL } from "@/lib/constants";

// =========================================================
// AXIOS INSTANCE
// =========================================================

export const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,

  headers: {
    "Content-Type": "application/json",
  },

  timeout: 30000,
});

// =========================================================
// RESPONSE INTERCEPTOR
// =========================================================

api.interceptors.response.use(
  (response) => response,

  (error) => {
    const message =
      error?.response?.data?.detail ||
      error?.message ||
      "Something went wrong";

    return Promise.reject(
      new Error(message)
    );
  }
);