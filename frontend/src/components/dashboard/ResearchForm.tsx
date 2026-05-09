"use client";

import { useState } from "react";
import { Search, Sparkles } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { useResearch } from "@/hooks/useResearch";

import { normalizeUrl } from "@/lib/utils";

export function ResearchForm() {
  const [company, setCompany] =
    useState("");

  const {
    runResearch,
    loading,
    error,
  } = useResearch();

  async function handleSubmit(
    e: React.FormEvent<HTMLFormElement>
  ) {
    e.preventDefault();

    if (!company.trim()) {
      return;
    }

    try {
      await runResearch({
        company: normalizeUrl(company),
      });
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="rounded-3xl border border-border bg-card p-6 shadow-sm">
      <div className="mb-6">
        <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-border px-3 py-1 text-xs text-muted-foreground">
          <Sparkles className="h-3 w-3" />
          AI Multi-Agent Research
        </div>

        <h2 className="text-2xl font-bold">
          Company Intelligence Research
        </h2>

        <p className="mt-2 text-sm text-muted-foreground">
          Analyze companies using AI-powered
          research, enrichment, lead scoring,
          and outreach generation.
        </p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="space-y-4"
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <Input
            placeholder="Enter company website (e.g. stripe.com)"
            value={company}
            onChange={(e) =>
              setCompany(e.target.value)
            }
            className="h-12"
          />

          <Button
            type="submit"
            disabled={
              loading || !company.trim()
            }
            className="h-12 px-6"
          >
            {loading ? (
              <>
                <Sparkles className="h-4 w-4 animate-pulse" />
                Researching...
              </>
            ) : (
              <>
                <Search className="h-4 w-4" />
                Analyze
              </>
            )}
          </Button>
        </div>

        {error && (
          <div className="rounded-xl border border-red-500/20 bg-red-500/10 p-3 text-sm text-red-500">
            {error}
          </div>
        )}
      </form>
    </div>
  );
}