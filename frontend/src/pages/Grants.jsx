import { useEffect, useState } from "react";

import EntityForm from "../components/EntityForm";
import EntityTable from "../components/EntityTable";
import Loader from "../components/Loader";
import ErrorBanner from "../components/ErrorBanner";
import { formatCurrency } from "../utils/formatters";

import {
    getGrants,
    createGrant,
    updateGrant,
    deleteGrant,
} from "../api/grantApi";

export default function Grants() {

    const [grants, setGrants] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const [editingGrant, setEditingGrant] =
        useState(null);

    useEffect(() => {
        loadGrants();
    }, []);

    async function loadGrants() {

        try {

            setLoading(true);
            setError("");

            const response = await getGrants();

            if (response.success) {
                setGrants(response.data);
            } else {
                setGrants([]);
            }

        } catch (err) {

            console.error(err);

            setError("Unable to load grants");

            setGrants([]);

        } finally {

            setLoading(false);

        }

    }

    async function handleSave(formData) {

        try {

            if (editingGrant) {

                await updateGrant(
                    editingGrant.id,
                    formData
                );

            } else {

                await createGrant(formData);

            }

            setEditingGrant(null);

            await loadGrants();

        } catch (err) {

            console.error(err);

            setError("Unable to save grant");

        }

    }

    async function handleDelete(id) {

        if (!window.confirm("Delete Grant?"))
            return;

        try {

            await deleteGrant(id);

            await loadGrants();

        } catch (err) {

            console.error(err);

            setError("Unable to delete grant");

        }

    }

    return (

        <div className="space-y-6">

            <h1 className="text-3xl font-bold">
                Grants
            </h1>

            <ErrorBanner message={error} />

            <EntityForm

                fields={[

                    {
                        name: "title",
                        label: "Grant Title",
                        type: "text",
                    },

                    {
                        name: "organization",
                        label: "Organization",
                        type: "text",
                    },

                    {
                        name: "amount",
                        label: "Amount",
                        type: "number",
                        render: (row) => formatCurrency(row.amount),
                    },

                    {
                        name: "eligibility",
                        label: "Eligibility",
                        type: "text",
                        required: false,
                    },

                    {
                        name: "deadline",
                        label: "Deadline",
                        type: "date",
                    },

                ]}

                initialValues={editingGrant || {}}

                isEditing={editingGrant !== null}

                onCancel={() =>
                    setEditingGrant(null)
                }

                buttonLabel={
                    editingGrant
                        ? "Update Grant"
                        : "Create Grant"
                }

                onSubmit={handleSave}

            />

            {loading ? (

                <Loader />

            ) : (

                <EntityTable

                    columns={[

                        {
                            key: "title",
                            label: "Title",
                        },

                        {
                            key: "organization",
                            label: "Organization",
                        },

                        {
                            key: "amount",
                            label: "Amount",
                            render: (row) => formatCurrency(row.amount),
                        },

                        {
                            key: "deadline",
                            label: "Deadline",
                        },

                        {
                            key: "status",
                            label: "Status",
                        },

                    ]}

                    data={grants}

                    onEdit={(row) =>
                        setEditingGrant(row)
                    }

                    onDelete={handleDelete}

                />

            )}

        </div>

    );

}