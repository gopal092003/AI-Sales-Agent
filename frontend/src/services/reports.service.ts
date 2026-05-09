import { api } from "@/services/api";

import type { Report } from "@/types/report";

// =========================================================
// TYPES
// =========================================================

interface ReportsResponse {
  success: boolean;
  count: number;
  data: Report[];
}

interface ReportResponse {
  success: boolean;
  data: Report;
}

// =========================================================
// GET ALL REPORTS
// =========================================================

export async function getReports(): Promise<ReportsResponse> {
  const response = await api.get("/reports");

  return response.data;
}

// =========================================================
// GET REPORT BY ID
// =========================================================

export async function getReportById(
  reportId: number
): Promise<ReportResponse> {
  const response = await api.get(
    `/reports/${reportId}`
  );

  return response.data;
}