// =========================================================
// DATE FORMATTERS
// =========================================================

export function formatDateTime(
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

export function formatRelativeTime(
  value: string | Date
): string {
  const date =
    typeof value === "string"
      ? new Date(value)
      : value;

  const now = new Date();

  const diffMs =
    now.getTime() - date.getTime();

  const minutes = Math.floor(
    diffMs / (1000 * 60)
  );

  const hours = Math.floor(
    diffMs / (1000 * 60 * 60)
  );

  const days = Math.floor(
    diffMs / (1000 * 60 * 60 * 24)
  );

  if (minutes < 1) {
    return "Just now";
  }

  if (minutes < 60) {
    return `${minutes} min ago`;
  }

  if (hours < 24) {
    return `${hours} hr ago`;
  }

  return `${days} day ago`;
}

// =========================================================
// SCORE FORMATTERS
// =========================================================

export function formatLeadScore(
  score: number
): string {
  return `${Math.round(score)}/100`;
}

export function getLeadScoreLabel(
  score: number
): string {
  if (score >= 80) {
    return "High Priority";
  }

  if (score >= 50) {
    return "Medium Priority";
  }

  return "Low Priority";
}

// =========================================================
// TEXT FORMATTERS
// =========================================================

export function truncate(
  text: string,
  maxLength: number = 120
): string {
  if (!text) {
    return "";
  }

  if (text.length <= maxLength) {
    return text;
  }

  return `${text.slice(0, maxLength)}...`;
}

export function capitalize(
  value: string
): string {
  if (!value) {
    return "";
  }

  return (
    value.charAt(0).toUpperCase() +
    value.slice(1)
  );
}

export function formatList(
  values: string[]
): string {
  if (!values?.length) {
    return "N/A";
  }

  return values.join(", ");
}