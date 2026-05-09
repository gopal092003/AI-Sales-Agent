import type { Metadata } from "next";
import { Inter } from "next/font/google";

import { QueryProvider } from "@/providers/QueryProvider";

import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AI Sales Intelligence Agent",
  description:
    "AI-native sales intelligence platform for company research, lead scoring, and personalized outreach generation.",
};

type RootLayoutProps = {
  children: React.ReactNode;
};

export default function RootLayout({
  children,
}: RootLayoutProps) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
    >
      <body
        className={`${inter.className} bg-background text-foreground antialiased`}
      >
        <QueryProvider>
          {children}
        </QueryProvider>
      </body>
    </html>
  );
}