export interface Lead {
  id: number;

  company_name: string;

  company_url?: string;

  industry?: string;

  company_summary?: string;

  lead_score: number;

  qualification?: string;

  hiring_signals?: string;

  growth_signals?: string;

  tech_stack?: string;

  is_contacted: boolean;

  created_at: string;

  updated_at: string;
}

export interface LeadScore {
  company_name: string;

  lead_score: number;

  qualification: string;
}

export interface LeadListResponse {
  total: number;

  items: Lead[];
}