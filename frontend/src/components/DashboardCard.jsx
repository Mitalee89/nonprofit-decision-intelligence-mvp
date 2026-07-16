export default function DashboardCard({
  title,
  value,
}) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition-shadow">

      <div className="text-sm text-gray-500 uppercase tracking-wide">
        {title}
      </div>

      <div className="mt-3 text-3xl font-bold text-gray-900">
        {value}
      </div>

    </div>
  );
}