export default function ErrorBanner({
  message,
}) {
  if (!message) return null;

  return (
    <div className="bg-red-100 border border-red-400 text-red-700 rounded p-3 mb-4">
      {message}
    </div>
  );
}