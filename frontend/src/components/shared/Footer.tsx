import Link from "next/link";

export function Footer() {
  return (
    <footer className="border-t border-border">
      <div className="container-width flex flex-col gap-6 py-10 md:flex-row md:items-center md:justify-between">
        {/* LEFT */}
        <div>
          <h3 className="text-lg font-semibold">
            AI Sales Intelligence Agent
          </h3>

          <p className="mt-2 max-w-md text-sm text-muted-foreground">
            AI-native multi-agent platform for
            company research, lead scoring,
            hiring signal detection, and
            personalized outreach generation.
          </p>
        </div>

        {/* RIGHT */}
        <div className="flex flex-col gap-3 text-sm text-muted-foreground">
          <Link
            href="/"
            className="transition hover:text-foreground"
          >
            Home
          </Link>

          <Link
            href="/dashboard"
            className="transition hover:text-foreground"
          >
            Dashboard
          </Link>

          <Link
            href="/reports"
            className="transition hover:text-foreground"
          >
            Reports
          </Link>
        </div>
      </div>

      {/* BOTTOM */}
      <div className="border-t border-border py-4">
        <div className="container-width flex flex-col items-center justify-between gap-2 text-xs text-muted-foreground md:flex-row">
          <p>
            © {new Date().getFullYear()} AI Sales
            Intelligence Agent
          </p>

          <p>
            Built with Next.js, FastAPI, and AI
            Agents
          </p>
        </div>
      </div>
    </footer>
  );
}