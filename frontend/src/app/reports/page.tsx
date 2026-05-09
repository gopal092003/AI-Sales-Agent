"use client";

import Link from "next/link";
import {
  FileText,
  ArrowRight,
} from "lucide-react";

import { Footer } from "@/components/shared/Footer";
import { Loader } from "@/components/shared/Loader";
import { Navbar } from "@/components/shared/Navbar";
import { PageContainer } from "@/components/shared/PageContainer";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "@/components/ui/badge";

import { useReports } from "@/hooks/useReports";

import {
  formatDateTime,
  truncate,
} from "@/lib/formatters";

export default function ReportsPage() {
  const {
    data,
    isLoading,
    error,
  } = useReports();

  return (
    <main className="min-h-screen bg-background">
      <Navbar />

      <PageContainer className="space-y-8">
        {/* HEADER */}
        <section>
          <h1 className="text-4xl font-bold tracking-tight">
            Intelligence Reports
          </h1>

          <p className="mt-3 text-muted-foreground">
            Browse generated sales
            intelligence reports and AI
            outreach insights.
          </p>
        </section>

        {/* LOADING */}
        {isLoading && (
          <Card className="rounded-3xl p-10">
            <Loader text="Loading reports..." />
          </Card>
        )}

        {/* ERROR */}
        {error && (
          <Card className="rounded-3xl border-red-500/20 bg-red-500/10 p-6">
            <p className="text-sm text-red-500">
              Failed to load reports.
            </p>
          </Card>
        )}

        {/* EMPTY */}
        {!isLoading &&
          !error &&
          !data?.data?.length && (
            <Card className="rounded-3xl p-10 text-center">
              <FileText className="mx-auto h-10 w-10 text-muted-foreground" />

              <h2 className="mt-4 text-xl font-semibold">
                No reports yet
              </h2>

              <p className="mt-2 text-sm text-muted-foreground">
                Run company research from
                the dashboard to generate
                reports.
              </p>
            </Card>
          )}

        {/* REPORTS */}
        {data?.data?.length ? (
          <div className="grid gap-6 lg:grid-cols-2">
            {data.data.map((report) => (
              <Link
                key={report.id}
                href={`/reports/${report.id}`}
              >
                <Card className="rounded-3xl transition hover:border-primary hover:shadow-md">
                  <CardHeader>
                    <div className="flex items-center justify-between gap-4">
                      <CardTitle className="line-clamp-1">
                        Report #{report.id}
                      </CardTitle>

                      <ArrowRight className="h-5 w-5 text-muted-foreground" />
                    </div>
                  </CardHeader>

                  <CardContent className="space-y-4">
                    <Badge variant="secondary">
                      {report.generated_by}
                    </Badge>

                    {report.company_overview && (
                      <p className="text-sm leading-7 text-muted-foreground">
                        {truncate(
                          report.company_overview,
                          180
                        )}
                      </p>
                    )}

                    <div className="text-xs text-muted-foreground">
                      Created{" "}
                      {formatDateTime(
                        report.created_at
                      )}
                    </div>
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>
        ) : null}
      </PageContainer>

      <Footer />
    </main>
  );
}