"use client";

import { useParams } from "next/navigation";

import { Footer } from "@/components/shared/Footer";
import { Loader } from "@/components/shared/Loader";
import { Navbar } from "@/components/shared/Navbar";
import { PageContainer } from "@/components/shared/PageContainer";

import { CompanyOverview } from "@/components/reports/CompanyOverview";
import { OutreachSection } from "@/components/reports/OutreachSection";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

import { useReport } from "@/hooks/useReports";

export default function ReportDetailPage() {
  const params = useParams();

  const reportId = Number(params.id);

  const {
    data,
    isLoading,
    error,
  } = useReport(reportId);

  const report = data?.data;

  return (
    <main className="min-h-screen bg-background">
      <Navbar />

      <PageContainer className="space-y-8">
        {/* HEADER */}
        <section>
          <h1 className="text-4xl font-bold tracking-tight">
            Intelligence Report
          </h1>

          <p className="mt-3 text-muted-foreground">
            Detailed AI-generated sales
            intelligence insights and
            outreach recommendations.
          </p>
        </section>

        {/* LOADING */}
        {isLoading && (
          <Card className="rounded-3xl p-10">
            <Loader text="Loading report..." />
          </Card>
        )}

        {/* ERROR */}
        {error && (
          <Card className="rounded-3xl border-red-500/20 bg-red-500/10 p-6">
            <p className="text-sm text-red-500">
              Failed to load report.
            </p>
          </Card>
        )}

        {/* REPORT */}
        {report && (
          <div className="space-y-8">
            <CompanyOverview
              company={{
                name:
                  report.generated_by ||
                  "Company",

                summary:
                  report.company_overview ||
                  "",

                business_model:
                  report.outreach_strategy ||
                  "",
              }}
            />

            <OutreachSection
              outreach={{
                cold_email:
                  report.cold_email,

                linkedin_message:
                  report.linkedin_message,

                follow_up_message:
                  report.follow_up_message,
              }}
            />

            {(report.pain_points ||
              report.opportunity_areas) && (
              <Card className="rounded-3xl">
                <CardContent className="space-y-6 p-6">
                  {report.pain_points && (
                    <div>
                      <h3 className="mb-3 text-lg font-semibold">
                        Pain Points
                      </h3>

                      <p className="text-sm leading-7 text-muted-foreground">
                        {report.pain_points}
                      </p>
                    </div>
                  )}

                  {report.opportunity_areas && (
                    <div>
                      <h3 className="mb-3 text-lg font-semibold">
                        Opportunity Areas
                      </h3>

                      <p className="text-sm leading-7 text-muted-foreground">
                        {
                          report.opportunity_areas
                        }
                      </p>
                    </div>
                  )}
                </CardContent>
              </Card>
            )}
          </div>
        )}
      </PageContainer>

      <Footer />
    </main>
  );
}