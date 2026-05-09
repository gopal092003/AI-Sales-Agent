import { api } from "@/services/api";

// =========================================================
// TYPES
// =========================================================

export interface ResearchPayload {
  company: string;
}

export interface ResearchResponse {
  success: boolean;

  data: {
    company: {
      name: string;
      website?: string;
      industry?: string;
      summary?: string;
      business_model?: string;
      icp_fit?: boolean;
    };

    hiring_signals: string[];

    growth_signals: string[];

    tech_stack: {
      frontend: string[];
      backend: string[];
      cloud: string[];
      analytics: string[];
    };

    pain_points: string[];

    lead_score: number;

    qualification: string;

    outreach: {
      cold_email: string;
      linkedin_message: string;
      follow_up_message: string;
    };
  };
}

// =========================================================
// RESEARCH SERVICE
// =========================================================

export async function runResearch(
  payload: ResearchPayload
): Promise<ResearchResponse> {
  const response = await api.post(
    "/research",
    payload
  );

  return response.data;
}