"use client";

import {
  Brain,
  Building2,
  LineChart,
  Sparkles,
} from "lucide-react";

import { Card } from "@/components/ui/card";

const activities = [
  {
    title: "Company Research Completed",
    description:
      "Website content and metadata analyzed.",
    icon: Building2,
  },
  {
    title: "Hiring Signals Detected",
    description:
      "Careers pages and hiring activity identified.",
    icon: Brain,
  },
  {
    title: "Lead Scoring Finished",
    description:
      "ICP fit and growth signals evaluated.",
    icon: LineChart,
  },
  {
    title: "Outreach Generated",
    description:
      "AI-generated personalized messaging completed.",
    icon: Sparkles,
  },
];

export function ActivityTimeline() {
  return (
    <Card className="rounded-3xl p-6">
      <div className="mb-6">
        <h3 className="text-xl font-semibold">
          Agent Activity Timeline
        </h3>

        <p className="mt-1 text-sm text-muted-foreground">
          Multi-agent workflow execution
        </p>
      </div>

      <div className="space-y-6">
        {activities.map((activity, index) => (
          <div
            key={activity.title}
            className="flex gap-4"
          >
            {/* ICON */}
            <div className="relative flex flex-col items-center">
              <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-border bg-muted">
                <activity.icon className="h-5 w-5" />
              </div>

              {index !==
                activities.length - 1 && (
                <div className="mt-2 h-full w-px bg-border" />
              )}
            </div>

            {/* CONTENT */}
            <div className="pb-8">
              <h4 className="font-medium">
                {activity.title}
              </h4>

              <p className="mt-1 text-sm text-muted-foreground">
                {activity.description}
              </p>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
}