"use client";

import {
  Cloud,
  Code2,
  Database,
  Globe,
} from "lucide-react";

import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { useResearchStore } from "@/store/researchStore";

type TechSectionProps = {
  title: string;
  items: string[];
  icon: React.ElementType;
};

function TechSection({
  title,
  items,
  icon: Icon,
}: TechSectionProps) {
  if (!items?.length) {
    return null;
  }

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-2">
        <Icon className="h-4 w-4 text-muted-foreground" />

        <h4 className="text-sm font-medium">
          {title}
        </h4>
      </div>

      <div className="flex flex-wrap gap-2">
        {items.map((item) => (
          <Badge
            key={item}
            variant="secondary"
          >
            {item}
          </Badge>
        ))}
      </div>
    </div>
  );
}

export function TechStackCard() {
  const { result } = useResearchStore();

  if (!result) {
    return null;
  }

  const tech = result.tech_stack;

  const hasTech =
    tech.frontend.length ||
    tech.backend.length ||
    tech.cloud.length ||
    tech.analytics.length;

  if (!hasTech) {
    return null;
  }

  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Code2 className="h-5 w-5" />
          Technology Stack
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-6">
        <TechSection
          title="Frontend"
          items={tech.frontend}
          icon={Globe}
        />

        <TechSection
          title="Backend"
          items={tech.backend}
          icon={Database}
        />

        <TechSection
          title="Cloud & Infrastructure"
          items={tech.cloud}
          icon={Cloud}
        />

        <TechSection
          title="Analytics"
          items={tech.analytics}
          icon={Code2}
        />
      </CardContent>
    </Card>
  );
}