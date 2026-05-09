"use client";

import { useQuery } from "@tanstack/react-query";

import {
  getReportById,
  getReports,
} from "@/services/reports.service";

// =========================================================
// GET ALL REPORTS
// =========================================================

export function useReports() {
  return useQuery({
    queryKey: ["reports"],

    queryFn: getReports,
  });
}

// =========================================================
// GET SINGLE REPORT
// =========================================================

export function useReport(
  reportId: number
) {
  return useQuery({
    queryKey: ["report", reportId],

    queryFn: () =>
      getReportById(reportId),

    enabled: !!reportId,
  });
}