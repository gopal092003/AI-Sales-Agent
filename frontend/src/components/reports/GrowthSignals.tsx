"use client";

import { TrendingUp } from "lucide-react";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type GrowthSignalsProps = {
  signals: string[];
};

export function GrowthSignals({
  signals,
}: GrowthSignalsProps) {
  if (!signals?.length) {
    return null;
  }

  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <TrendingUp className="h-5 w-5" />
          Growth Signals
        </CardTitle>
      </CardHeader>

      <CardContent>
        <div className="space-y-4">
          {signals.map((signal) => (
            <div
              key={signal}
              className="rounded-2xl border border-border bg-muted/30 p-4"
            >
              <p className="text-sm leading-6">
                {signal}
              </p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}