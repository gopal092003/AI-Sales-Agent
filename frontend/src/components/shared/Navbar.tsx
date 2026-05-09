"use client";

import Link from "next/link";
import { BrainCircuit } from "lucide-react";

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-md">
      <div className="container-width flex h-16 items-center justify-between">
        {/* LOGO */}
        <Link
          href="/"
          className="flex items-center gap-2"
        >
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-primary-foreground">
            <BrainCircuit className="h-5 w-5" />
          </div>

          <div>
            <p className="text-sm font-semibold leading-none">
              AI Sales Intelligence
            </p>

            <p className="text-xs text-muted-foreground">
              Multi-Agent SDR System
            </p>
          </div>
        </Link>

        {/* NAVIGATION */}
        <nav className="hidden items-center gap-6 md:flex">
          <Link
            href="/"
            className="text-sm text-muted-foreground transition hover:text-foreground"
          >
            Home
          </Link>

          <Link
            href="/dashboard"
            className="text-sm text-muted-foreground transition hover:text-foreground"
          >
            Dashboard
          </Link>

          <Link
            href="/reports"
            className="text-sm text-muted-foreground transition hover:text-foreground"
          >
            Reports
          </Link>
        </nav>

        {/* CTA */}
        <Link
          href="/dashboard"
          className="rounded-xl bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition hover:opacity-90"
        >
          Launch App
        </Link>
      </div>
    </header>
  );
}