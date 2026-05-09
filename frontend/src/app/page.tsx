import Link from "next/link";
import {
  ArrowRight,
  Brain,
  Building2,
  LineChart,
  Sparkles,
} from "lucide-react";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      {/* HERO */}
      <section className="border-b border-border">
        <div className="container-width section-spacing">
          <div className="grid items-center gap-12 lg:grid-cols-2">
            <div>
              <div className="mb-4 inline-flex items-center rounded-full border border-border px-4 py-1 text-sm text-muted-foreground">
                AI-Native Sales Intelligence Platform
              </div>

              <h1 className="max-w-3xl text-5xl font-bold tracking-tight sm:text-6xl">
                Automate company research,
                lead scoring, and outreach.
              </h1>

              <p className="mt-6 max-w-2xl text-lg text-muted-foreground">
                AI-powered multi-agent system for
                company intelligence, hiring signal
                detection, tech stack analysis, and
                personalized outreach generation.
              </p>

              <div className="mt-8 flex flex-wrap gap-4">
                <Link
                  href="/dashboard"
                  className="inline-flex items-center gap-2 rounded-xl bg-primary px-6 py-3 text-sm font-medium text-primary-foreground transition hover:opacity-90"
                >
                  Open Dashboard
                  <ArrowRight className="h-4 w-4" />
                </Link>

                <Link
                  href="/reports"
                  className="inline-flex items-center gap-2 rounded-xl border border-border px-6 py-3 text-sm font-medium transition hover:bg-muted"
                >
                  View Reports
                </Link>
              </div>
            </div>

            {/* RIGHT PANEL */}
            <div className="glass rounded-3xl p-8">
              <div className="space-y-6">
                <div className="rounded-2xl border border-border bg-background/80 p-5">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm text-muted-foreground">
                        Lead Score
                      </p>

                      <h3 className="mt-1 text-3xl font-bold">
                        87/100
                      </h3>
                    </div>

                    <div className="rounded-xl bg-primary/10 p-3">
                      <LineChart className="h-6 w-6" />
                    </div>
                  </div>
                </div>

                <div className="rounded-2xl border border-border bg-background/80 p-5">
                  <div className="flex items-start gap-4">
                    <div className="rounded-xl bg-primary/10 p-3">
                      <Building2 className="h-5 w-5" />
                    </div>

                    <div>
                      <h4 className="font-semibold">
                        Company Intelligence
                      </h4>

                      <p className="mt-1 text-sm text-muted-foreground">
                        Detect hiring trends,
                        growth signals, and
                        company expansion
                        patterns automatically.
                      </p>
                    </div>
                  </div>
                </div>

                <div className="rounded-2xl border border-border bg-background/80 p-5">
                  <div className="flex items-start gap-4">
                    <div className="rounded-xl bg-primary/10 p-3">
                      <Brain className="h-5 w-5" />
                    </div>

                    <div>
                      <h4 className="font-semibold">
                        AI Outreach
                      </h4>

                      <p className="mt-1 text-sm text-muted-foreground">
                        Generate personalized
                        cold emails and LinkedIn
                        outreach using real-time
                        company intelligence.
                      </p>
                    </div>
                  </div>
                </div>

                <div className="rounded-2xl border border-border bg-background/80 p-5">
                  <div className="flex items-start gap-4">
                    <div className="rounded-xl bg-primary/10 p-3">
                      <Sparkles className="h-5 w-5" />
                    </div>

                    <div>
                      <h4 className="font-semibold">
                        Multi-Agent Workflow
                      </h4>

                      <p className="mt-1 text-sm text-muted-foreground">
                        Research, enrichment,
                        scoring, and outreach
                        agents working together
                        autonomously.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section>
        <div className="container-width section-spacing">
          <div className="mb-12 max-w-2xl">
            <h2 className="text-3xl font-bold tracking-tight">
              Built for AI-native GTM workflows
            </h2>

            <p className="mt-4 text-muted-foreground">
              Designed to simulate real-world AI
              SDR systems used in modern startups.
            </p>
          </div>

          <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
            {features.map((feature) => (
              <div
                key={feature.title}
                className="rounded-2xl border border-border p-6 transition hover:bg-muted/40"
              >
                <feature.icon className="h-6 w-6" />

                <h3 className="mt-4 text-lg font-semibold">
                  {feature.title}
                </h3>

                <p className="mt-2 text-sm text-muted-foreground">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}

const features = [
  {
    title: "Company Research",
    description:
      "Extract business intelligence from company websites automatically.",
    icon: Building2,
  },
  {
    title: "Lead Scoring",
    description:
      "Score leads using hiring signals, ICP fit, and growth indicators.",
    icon: LineChart,
  },
  {
    title: "AI Outreach",
    description:
      "Generate personalized outreach messages using LLM workflows.",
    icon: Sparkles,
  },
  {
    title: "Multi-Agent System",
    description:
      "Research, enrichment, scoring, and outreach agents working together.",
    icon: Brain,
  },
];