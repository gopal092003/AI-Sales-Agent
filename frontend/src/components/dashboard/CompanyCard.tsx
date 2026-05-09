"use client";

import {
  Building2,
  Globe,
  Layers3,
} from "lucide-react";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "@/components/ui/badge";

import { useResearchStore } from "@/store/researchStore";

export function CompanyCard() {
  const { result } = useResearchStore();

  if (!result) {
    return null;
  }

  const company = result.company;

  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Building2 className="h-5 w-5" />
          Company Intelligence
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-6">
        {/* COMPANY NAME */}
        <div>
          <p className="text-sm text-muted-foreground">
            Company
          </p>

          <h2 className="mt-1 text-2xl font-bold">
            {company.name}
          </h2>
        </div>

        {/* WEBSITE */}
        {company.website && (
          <div className="flex items-start gap-3">
            <Globe className="mt-0.5 h-5 w-5 text-muted-foreground" />

            <div>
              <p className="text-sm text-muted-foreground">
                Website
              </p>

              <a
                href={company.website}
                target="_blank"
                rel="noopener noreferrer"
                className="break-all text-sm font-medium hover:underline"
              >
                {company.website}
              </a>
            </div>
          </div>
        )}

        {/* INDUSTRY */}
        {company.industry && (
          <div className="flex items-start gap-3">
            <Layers3 className="mt-0.5 h-5 w-5 text-muted-foreground" />

            <div>
              <p className="text-sm text-muted-foreground">
                Industry
              </p>

              <Badge
                variant="secondary"
                className="mt-1"
              >
                {company.industry}
              </Badge>
            </div>
          </div>
        )}

        {/* SUMMARY */}
        {company.summary && (
          <div>
            <p className="mb-2 text-sm text-muted-foreground">
              Company Summary
            </p>

            <p className="text-sm leading-7 text-foreground/90">
              {company.summary}
            </p>
          </div>
        )}

        {/* BUSINESS MODEL */}
        {company.business_model && (
          <div>
            <p className="mb-2 text-sm text-muted-foreground">
              Business Model
            </p>

            <div className="rounded-2xl border border-border bg-muted/40 p-4 text-sm">
              {company.business_model}
            </div>
          </div>
        )}

        {/* ICP FIT */}
        <div className="flex items-center justify-between rounded-2xl border border-border bg-muted/40 p-4">
          <div>
            <p className="text-sm text-muted-foreground">
              ICP Fit
            </p>

            <p className="mt-1 font-medium">
              Ideal Customer Match
            </p>
          </div>

          <Badge
            variant={
              company.icp_fit
                ? "success"
                : "destructive"
            }
          >
            {company.icp_fit
              ? "Matched"
              : "Not Matched"}
          </Badge>
        </div>
      </CardContent>
    </Card>
  );
}