import { useEffect, useState } from "react";

export default function EntityForm({
    fields,
    onSubmit,
    buttonLabel = "Save",
    initialValues = {},
    onCancel,
    isEditing = false,
}) {
  const buildInitialState = () => {
    const state = {};

    fields.forEach((field) => {
      state[field.name] =
        initialValues[field.name] ?? "";
    });

    return state;
  };

  const [formData, setFormData] = useState(
    buildInitialState()
  );

  useEffect(() => {
    setFormData(buildInitialState());
  }, [initialValues]);

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    await onSubmit(formData);

    setFormData(buildInitialState());
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow rounded-lg p-5 space-y-4"
    >
      {fields.map((field) => (
        <div key={field.name}>
          <label className="block mb-1 font-medium">
            {field.label}
          </label>

        {field.type === "select" ? (

          <select
              name={field.name}
              value={formData[field.name]}
              onChange={handleChange}
              className="border rounded w-full p-2"
              required={field.required ?? true}
          >
              <option value="">
                  Select...
              </option>

              {field.options?.map(option => (

                  <option
                      key={option.value}
                      value={option.value}
                  >
                      {option.label}
                  </option>

              ))}

          </select>

      ) : (

          <input
              type={field.type}
              name={field.name}
              value={formData[field.name]}
              onChange={handleChange}
              className="border rounded w-full p-2"
              required={field.required ?? true}
          />

      )}
        </div>
      ))}

      <div className="flex gap-3">

    <button
        type="submit"
        className="bg-blue-600 text-white px-5 py-2 rounded hover:bg-blue-700"
    >
        {buttonLabel}
    </button>

    {isEditing && (
        <button
            type="button"
            onClick={onCancel}
            className="bg-gray-500 text-white px-5 py-2 rounded hover:bg-gray-600"
        >
            Cancel
        </button>
    )}

</div>
    </form>
  );
}