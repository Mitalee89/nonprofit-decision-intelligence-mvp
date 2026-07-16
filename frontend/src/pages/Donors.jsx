import { useEffect, useState } from "react";

import EntityTable from "../components/EntityTable";
import EntityForm from "../components/EntityForm";
import Loader from "../components/Loader";
import ErrorBanner from "../components/ErrorBanner";

import {
    getDonors,
    createDonor,
    updateDonor,
    deleteDonor,
} from "../api/donorApi";

export default function Donors() {
    const [donors, setDonors] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const [editingDonor, setEditingDonor] =
        useState(null);

    useEffect(() => {
        loadDonors();
    }, []);

    async function loadDonors() {
    try {
        setLoading(true);
        setError("");

        const response = await getDonors();

        console.log("Response:", response);
        console.log("Success:", response.success);
        console.log("Data:", response.data);
        console.log("Is Array:", Array.isArray(response.data));

        if (response.success) {
            setDonors(response.data);
        } else {
            setDonors([]);
        }
    } catch (err) {
        console.error(err);
        setError("Unable to load donors");
        setDonors([]);
    } finally {
        setLoading(false);
    }
}

    async function handleSave(formData) {
        try {
            if (editingDonor) {
                await updateDonor(
                    editingDonor.id,
                    formData
                );
            } else {
                await createDonor(formData);
            }

            setEditingDonor(null);

            await loadDonors();
        } catch (err) {
            console.error(err);
            setError("Unable to save donor");
        }
    }

    async function handleDelete(id) {
        if (!window.confirm("Delete donor?"))
            return;

        try {
            await deleteDonor(id);

            await loadDonors();
        } catch (err) {
            console.error(err);
            setError("Unable to delete donor");
        }
    }

    return (
        <div className="space-y-6">

            <h1 className="text-3xl font-bold">
                Donors
            </h1>

            <ErrorBanner message={error} />

            <EntityForm
                fields={[
                    {
                        name: "name",
                        label: "Name",
                        type: "text",
                    },
                    {
                        name: "email",
                        label: "Email",
                        type: "email",
                    },
                    {
                        name: "city",
                        label: "City",
                        type: "text",
                        required: false,
                    },
                    {
                        name: "interests",
                        label: "Interests",
                        type: "text",
                        required: false,
                    },
                    {
                        name: "preferred_cause",
                        label: "Preferred Cause",
                        type: "text",
                        required: false,
                    },
                    {
                        name: "capacity",
                        label: "Capacity",
                        type: "number",
                    },
                ]}
                initialValues={editingDonor || {}}
                isEditing={editingDonor !== null}
                onCancel={() =>
                    setEditingDonor(null)
                }
                buttonLabel={
                    editingDonor
                        ? "Update Donor"
                        : "Create Donor"
                }
                onSubmit={handleSave}
            />

            {loading ? (
                <Loader />
            ) : (
                <EntityTable
                    columns={[
                        {
                            key: "name",
                            label: "Name",
                        },
                        {
                            key: "email",
                            label: "Email",
                        },
                        {
                            key: "city",
                            label: "City",
                        },
                        {
                            key: "preferred_cause",
                            label: "Preferred Cause",
                        },
                        {
                            key: "capacity",
                            label: "Capacity",
                        },
                    ]}
                    data={donors}
                    onDelete={handleDelete}
                    onEdit={(row) =>
                        setEditingDonor(row)
                    }
                />
            )}

        </div>
    );
}