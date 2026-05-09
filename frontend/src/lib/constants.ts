// =========================================================
// APP
// =========================================================

export const APP_NAME =
  "AI Sales Intelligence Agent";

export const APP_DESCRIPTION =
  "AI-native platform for company research, lead scoring, and personalized outreach generation.";

// =========================================================
// API
// =========================================================

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ||
  "http://localhost:8000";

// =========================================================
// ROUTES
// =========================================================

export const ROUTES = {
  HOME: "/",
  DASHBOARD: "/dashboard",
  REPORTS: "/reports",
} as const;

// =========================================================
// LEAD QUALIFICATIONS
// =========================================================

export const LEAD_QUALIFICATIONS = {
  HIGH: "High Priority",
  MEDIUM: "Medium Priority",
  LOW: "Low Priority",
} as const;

// =========================================================
// LEAD SCORE THRESHOLDS
// =========================================================

export const HIGH_PRIORITY_THRESHOLD = 80;

export const MEDIUM_PRIORITY_THRESHOLD = 50;

// =========================================================
// FEATURE FLAGS
// =========================================================

export const FEATURES = {
  REPORTS:
    process.env
      .NEXT_PUBLIC_ENABLE_REPORTS === "true",

  OUTREACH:
    process.env
      .NEXT_PUBLIC_ENABLE_OUTREACH === "true",

  DASHBOARD:
    process.env
      .NEXT_PUBLIC_ENABLE_DASHBOARD ===
    "true",
};

// =========================================================
// QUERY KEYS
// =========================================================

export const QUERY_KEYS = {
  REPORTS: ["reports"],
  LEADS: ["leads"],
  RESEARCH: ["research"],
} as const;