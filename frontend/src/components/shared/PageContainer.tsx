import { cn } from "@/lib/utils";

type PageContainerProps = {
  children: React.ReactNode;
  className?: string;
};

export function PageContainer({
  children,
  className,
}: PageContainerProps) {
  return (
    <div
      className={cn(
        "container-width py-8 md:py-10",
        className
      )}
    >
      {children}
    </div>
  );
}