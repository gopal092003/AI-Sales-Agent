import { z } from "zod";

// =========================================================
// COMPANY RESEARCH
// =========================================================

export const companyResearchSchema = z.object({
  company: z
    .string()
    .min(2, "Company name or URL is required")
    .max(500, "Input is too long"),
});

export type CompanyResearchInput =
  z.infer<typeof companyResearchSchema>;

// =========================================================
// OUTREACH
// =========================================================

export const outreachSchema = z.object({
  company_name: z
    .string()
    .min(2, "Company name is required"),

  industry: z.string().optional(),

  company_summary: z.string().optional(),

  lead_score: z.number().min(0).max(100),

  pain_points: z.array(z.string()),

  hiring_signals: z.array(z.string()),

  growth_signals: z.array(z.string()),

  tech_stack: z.array(z.string()),
});

export type OutreachInput =
  z.infer<typeof outreachSchema>;

// =========================================================
// HELPERS
// =========================================================

export function isValidUrl(
  value: string
): boolean {
  try {
    new URL(value);
    return true;
  } catch {
    return false;
  }
}