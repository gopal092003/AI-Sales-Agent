"use client";

import { useMutation } from "@tanstack/react-query";

import {
  runResearch,
  type ResearchPayload,
} from "@/services/research.service";

import { useResearchStore } from "@/store/researchStore";

export function useResearch() {
  const {
    result,
    loading,
    error,
    setLoading,
    setResult,
    setError,
  } = useResearchStore();

  const mutation = useMutation({
    mutationFn: (
      payload: ResearchPayload
    ) => runResearch(payload),

    onMutate: () => {
      setLoading(true);
      setError(null);
    },

    onSuccess: (data) => {
      setResult(data.data);
    },

    onError: (err: Error) => {
      setError(
        err.message ||
          "Failed to run research"
      );
    },

    onSettled: () => {
      setLoading(false);
    },
  });

  return {
    result,
    loading,
    error,
    runResearch: mutation.mutateAsync,
  };
}