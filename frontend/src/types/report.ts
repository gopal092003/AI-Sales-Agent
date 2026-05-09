export interface Report {
  id: number;

  lead_id: number;

  company_overview?: string;

  pain_points?: string;

  opportunity_areas?: string;

  outreach_strategy?: string;

  cold_email?: string;

  linkedin_message?: string;

  follow_up_message?: string;

  generated_by: string;

  created_at: string;

  updated_at: string;
}

export interface SalesIntelligenceReport {
  company_name: string;

  industry?: string;

  company_summary?: string;

  lead_score: number;

  qualification: string;

  hiring_signals: string[];

  growth_signals: string[];

  tech_stack: string[];

  pain_points: string[];

  opportunity_areas: string[];

  cold_email?: string;

  linkedin_message?: string;

  follow_up_message?: string;
}