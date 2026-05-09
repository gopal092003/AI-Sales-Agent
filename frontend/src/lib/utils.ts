import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merge Tailwind + conditional class names safely.
 */
export function cn(
  ...inputs: ClassValue[]
) {
  return twMerge(clsx(inputs));
}

/**
 * Format date into readable text.
 */
export function formatDate(
  value: string | Date
): string {
  const date =
    typeof value === "string"
      ? new Date(value)
      : value;

  return new Intl.DateTimeFormat("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}

/**
 * Truncate long text safely.
 */
export function truncateText(
  text: string,
  maxLength: number = 120
): string {
  if (!text) {
    return "";
  }

  if (text.length <= maxLength) {
    return text;
  }

  return (
    text.slice(0, maxLength).trim() + "..."
  );
}

/**
 * Convert score into percentage string.
 */
export function formatScore(
  score: number
): string {
  return `${Math.round(score)}/100`;
}

/**
 * Get lead priority color classes.
 */
export function getLeadBadgeVariant(
  qualification?: string
):
  | "success"
  | "warning"
  | "destructive"
  | "secondary" {
  switch (qualification) {
    case "High Priority":
      return "success";

    case "Medium Priority":
      return "warning";

    case "Low Priority":
      return "destructive";

    default:
      return "secondary";
  }
}

/**
 * Normalize URL input.
 */
export function normalizeUrl(
  value: string
): string {
  if (!value) {
    return "";
  }

  const trimmed = value.trim();

  if (
    trimmed.startsWith("http://") ||
    trimmed.startsWith("https://")
  ) {
    return trimmed;
  }

  return `https://${trimmed}`;
}