"use client";

import {
  Mail,
  MessageSquare,
  Reply,
} from "lucide-react";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Textarea } from "@/components/ui/textarea";

type OutreachSectionProps = {
  outreach: {
    cold_email?: string;
    linkedin_message?: string;
    follow_up_message?: string;
  };
};

type OutreachCardProps = {
  title: string;
  content?: string;
  icon: React.ElementType;
};

function OutreachCard({
  title,
  content,
  icon: Icon,
}: OutreachCardProps) {
  if (!content) {
    return null;
  }

  return (
    <div className="rounded-2xl border border-border bg-muted/30 p-5">
      <div className="mb-4 flex items-center gap-2">
        <Icon className="h-4 w-4 text-muted-foreground" />

        <h4 className="font-medium">
          {title}
        </h4>
      </div>

      <Textarea
        readOnly
        value={content}
        className="min-h-[180px] resize-none border-0 bg-background"
      />
    </div>
  );
}

export function OutreachSection({
  outreach,
}: OutreachSectionProps) {
  return (
    <Card className="rounded-3xl">
      <CardHeader>
        <CardTitle>
          AI-Generated Outreach
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-6">
        <OutreachCard
          title="Cold Email"
          content={outreach.cold_email}
          icon={Mail}
        />

        <OutreachCard
          title="LinkedIn Message"
          content={
            outreach.linkedin_message
          }
          icon={MessageSquare}
        />

        <OutreachCard
          title="Follow-Up Message"
          content={
            outreach.follow_up_message
          }
          icon={Reply}
        />
      </CardContent>
    </Card>
  );
}