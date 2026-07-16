export default function EntityTable({
  columns,
  data,
  onDelete,
  onEdit,
}) {
  return (
    <div className="overflow-x-auto bg-white rounded-lg shadow">
      <table className="min-w-full">

        <thead className="bg-gray-100">
          <tr>

            {columns.map((column) => (
              <th
                key={column.key}
                className="px-4 py-3 text-left font-semibold"
              >
                {column.label}
              </th>
            ))}

            <th className="px-4 py-3">
              Actions
            </th>

          </tr>
        </thead>

        <tbody>

          {data.length === 0 ? (

            <tr>

              <td
                colSpan={columns.length + 1}
                className="text-center py-6 text-gray-500"
              >
                No Records Found
              </td>

            </tr>

          ) : (

            data.map((row) => (

              <tr
                key={row.id}
                className="border-b hover:bg-gray-50"
              >

                {columns.map((column) => (

                  <td
                    key={column.key}
                    className="px-4 py-3"
                  >

                    {column.render
                      ? column.render(row)
                      : row[column.key]}

                  </td>

                ))}

                <td className="px-4 py-3 space-x-2">

                  <button
                    onClick={() => onEdit && onEdit(row)}
                    className="bg-yellow-500 text-white px-3 py-1 rounded"
                  >
                    Edit
                  </button>

                  <button
                    onClick={() => onDelete(row.id)}
                    className="bg-red-600 text-white px-3 py-1 rounded"
                  >
                    Delete
                  </button>

                </td>

              </tr>

            ))

          )}

        </tbody>

      </table>
    </div>
  );
}