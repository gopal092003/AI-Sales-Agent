import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    status: "ok",
    service: "AI Sales Intelligence Frontend",
    timestamp: new Date().toISOString(),
  });
}