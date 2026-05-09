"use client";

import { Building2, Globe2 } from "lucide-react";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type CompanyOverviewProps = {
  company: {
    name: string;
    website?: string;
    industry?: string;
    summary?: string;
    business_model?: string;
  };
};

export function CompanyOverview({
  company,
}: CompanyOverviewProps) {
  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Building2 className="h-5 w-5" />
          Company Overview
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-6">
        {/* NAME */}
        <div>
          <p className="text-sm text-muted-foreground">
            Company
          </p>

          <h2 className="mt-1 text-3xl font-bold">
            {company.name}
          </h2>
        </div>

        {/* WEBSITE */}
        {company.website && (
          <div className="flex items-start gap-3">
            <Globe2 className="mt-0.5 h-5 w-5 text-muted-foreground" />

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
          <div>
            <p className="text-sm text-muted-foreground">
              Industry
            </p>

            <p className="mt-1 font-medium">
              {company.industry}
            </p>
          </div>
        )}

        {/* SUMMARY */}
        {company.summary && (
          <div>
            <p className="mb-2 text-sm text-muted-foreground">
              Company Summary
            </p>

            <div className="rounded-2xl border border-border bg-muted/30 p-5">
              <p className="text-sm leading-7">
                {company.summary}
              </p>
            </div>
          </div>
        )}

        {/* BUSINESS MODEL */}
        {company.business_model && (
          <div>
            <p className="mb-2 text-sm text-muted-foreground">
              Business Model
            </p>

            <div className="rounded-2xl border border-border bg-muted/30 p-5">
              <p className="text-sm leading-7">
                {company.business_model}
              </p>
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
}