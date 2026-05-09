"use client";

import { TriangleAlert } from "lucide-react";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

type PainPointsProps = {
  painPoints: string[];
};

export function PainPoints({
  painPoints,
}: PainPointsProps) {
  if (!painPoints?.length) {
    return null;
  }

  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <TriangleAlert className="h-5 w-5" />
          Potential Pain Points
        </CardTitle>
      </CardHeader>

      <CardContent>
        <div className="space-y-4">
          {painPoints.map((point) => (
            <div
              key={point}
              className="rounded-2xl border border-border bg-muted/30 p-4"
            >
              <p className="text-sm leading-6">
                {point}
              </p>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}