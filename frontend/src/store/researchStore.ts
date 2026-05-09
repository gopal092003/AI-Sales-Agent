import { create } from "zustand";

import type { ResearchResponse } from "@/services/research.service";

// =========================================================
// TYPES
// =========================================================

type ResearchState = {
  result: ResearchResponse["data"] | null;

  loading: boolean;

  error: string | null;

  setLoading: (
    loading: boolean
  ) => void;

  setResult: (
    result: ResearchResponse["data"] | null
  ) => void;

  setError: (
    error: string | null
  ) => void;

  reset: () => void;
};

// =========================================================
// STORE
// =========================================================

export const useResearchStore =
  create<ResearchState>((set) => ({
    result: null,

    loading: false,

    error: null,

    setLoading: (loading) =>
      set({
        loading,
      }),

    setResult: (result) =>
      set({
        result,
      }),

    setError: (error) =>
      set({
        error,
      }),

    reset: () =>
      set({
        result: null,
        loading: false,
        error: null,
      }),
  }));