"use client";

import { ActivityTimeline } from "@/components/dashboard/ActivityTimeline";
import { CompanyCard } from "@/components/dashboard/CompanyCard";
import { LeadScoreCard } from "@/components/dashboard/LeadScoreCard";
import { ResearchForm } from "@/components/dashboard/ResearchForm";
import { TechStackCard } from "@/components/dashboard/TechStackCard";

import { Footer } from "@/components/shared/Footer";
import { Loader } from "@/components/shared/Loader";
import { Navbar } from "@/components/shared/Navbar";
import { PageContainer } from "@/components/shared/PageContainer";

import { GrowthSignals } from "@/components/reports/GrowthSignals";
import { HiringSignals } from "@/components/reports/HiringSignals";
import { OutreachSection } from "@/components/reports/OutreachSection";
import { PainPoints } from "@/components/reports/PainPoints";

import { useResearchStore } from "@/store/researchStore";

export default function DashboardPage() {
  const { result, loading } =
    useResearchStore();

  return (
    <main className="min-h-screen bg-background">
      <Navbar />

      <PageContainer className="space-y-8">
        {/* HERO */}
        <section>
          <div className="max-w-3xl">
            <h1 className="text-4xl font-bold tracking-tight">
              AI Sales Intelligence Dashboard
            </h1>

            <p className="mt-3 text-muted-foreground">
              Research companies, detect
              hiring signals, analyze tech
              stacks, and generate
              personalized outreach using
              multi-agent AI workflows.
            </p>
          </div>
        </section>

        {/* RESEARCH FORM */}
        <ResearchForm />

        {/* LOADING */}
        {loading && (
          <div className="rounded-3xl border border-border bg-card p-10">
            <Loader text="Running multi-agent intelligence pipeline..." />
          </div>
        )}

        {/* RESULTS */}
        {result && !loading && (
          <div className="space-y-8">
            {/* TOP GRID */}
            <div className="grid gap-8 lg:grid-cols-3">
              <div className="space-y-8 lg:col-span-2">
                <CompanyCard />

                <TechStackCard />
              </div>

              <div className="space-y-8">
                <LeadScoreCard />

                <ActivityTimeline />
              </div>
            </div>

            {/* SIGNALS */}
            <div className="grid gap-8 lg:grid-cols-2">
              <HiringSignals
                signals={
                  result.hiring_signals
                }
              />

              <GrowthSignals
                signals={
                  result.growth_signals
                }
              />
            </div>

            {/* PAIN POINTS */}
            <PainPoints
              painPoints={
                result.pain_points
              }
            />

            {/* OUTREACH */}
            <OutreachSection
              outreach={result.outreach}
            />
          </div>
        )}
      </PageContainer>

      <Footer />
    </main>
  );
}