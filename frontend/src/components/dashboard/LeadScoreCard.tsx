"use client";

import { Award, TrendingUp } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { useResearchStore } from "@/store/researchStore";

import {
  formatScore,
  getLeadBadgeVariant,
} from "@/lib/utils";

export function LeadScoreCard() {
  const { result } = useResearchStore();

  if (!result) {
    return null;
  }

  return (
    <Card className="rounded-3xl">
      <CardHeader className="flex flex-row items-center justify-between space-y-0">
        <div>
          <CardTitle>
            Lead Intelligence Score
          </CardTitle>

          <p className="mt-1 text-sm text-muted-foreground">
            AI-generated qualification score
          </p>
        </div>

        <div className="rounded-2xl bg-primary/10 p-3">
          <TrendingUp className="h-6 w-6" />
        </div>
      </CardHeader>

      <CardContent>
        <div className="flex items-center justify-between">
          {/* SCORE */}
          <div>
            <div className="flex items-end gap-2">
              <h2 className="text-5xl font-bold">
                {formatScore(
                  result.lead_score
                )}
              </h2>
            </div>

            <p className="mt-2 text-sm text-muted-foreground">
              Calculated using ICP fit,
              hiring activity, growth
              signals, and tech stack.
            </p>
          </div>

          {/* QUALIFICATION */}
          <div className="flex flex-col items-end gap-3">
            <Badge
              variant={getLeadBadgeVariant(
                result.qualification
              )}
              className="px-3 py-1 text-sm"
            >
              {result.qualification}
            </Badge>

            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <Award className="h-4 w-4" />
              AI Qualified Lead
            </div>
          </div>
        </div>

        {/* PROGRESS */}
        <div className="mt-8">
          <div className="mb-2 flex items-center justify-between text-xs text-muted-foreground">
            <span>Lead Score</span>

            <span>
              {Math.round(
                result.lead_score
              )}
              %
            </span>
          </div>

          <div className="h-3 overflow-hidden rounded-full bg-muted">
            <div
              className="h-full rounded-full bg-primary transition-all duration-700"
              style={{
                width: `${Math.min(
                  result.lead_score,
                  100
                )}%`,
              }}
            />
          </div>
        </div>
      </CardContent>
    </Card>
  );
}