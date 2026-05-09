import { LoaderCircle } from "lucide-react";

type LoaderProps = {
  text?: string;
};

export function Loader({
  text = "Loading...",
}: LoaderProps) {
  return (
    <div className="flex flex-col items-center justify-center gap-4 py-10">
      <LoaderCircle className="h-8 w-8 animate-spin text-primary" />

      <p className="text-sm text-muted-foreground">
        {text}
      </p>
    </div>
  );
}