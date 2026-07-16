import { useEffect, useState } from "react";

import EntityForm from "../components/EntityForm";
import EntityTable from "../components/EntityTable";
import Loader from "../components/Loader";
import ErrorBanner from "../components/ErrorBanner";

import {
    getDonations,
    createDonation,
    updateDonation,
    deleteDonation,
} from "../api/donationApi";

import { getDonors } from "../api/donorApi";
import { getFunds } from "../api/fundApi";

import {
    formatCurrency,
    formatDateTime,
} from "../utils/formatters";

export default function Donations() {

    const [donations, setDonations] = useState([]);
    const [donors, setDonors] = useState([]);
    const [funds, setFunds] = useState([]);

    const [editingDonation, setEditingDonation] =
        useState(null);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    useEffect(() => {
        loadPage();
    }, []);

    async function loadPage() {

        try {

            setLoading(true);
            setError("");

            const [
                donationRes,
                donorRes,
                fundRes,
            ] = await Promise.all([
                getDonations(),
                getDonors(),
                getFunds(),
            ]);

            if (donationRes.success)
                setDonations(donationRes.data);

            if (donorRes.success)
                setDonors(donorRes.data);

            if (fundRes.success)
                setFunds(fundRes.data);

        } catch (err) {

            console.error(err);

            setError("Unable to load donations");

        } finally {

            setLoading(false);

        }

    }

    async function handleSave(formData) {

        try {

            if (editingDonation) {

                await updateDonation(
                    editingDonation.id,
                    formData
                );

            } else {

                await createDonation(formData);

            }

            setEditingDonation(null);

            await loadPage();

        } catch (err) {

            console.error(err);

            setError("Unable to save donation");

        }

    }

    async function handleDelete(id) {

        if (!window.confirm("Delete Donation?"))
            return;

        try {

            await deleteDonation(id);

            await loadPage();

        } catch (err) {

            console.error(err);

            setError("Unable to delete donation");

        }

    }

    return (

        <div className="space-y-6">

            <h1 className="text-3xl font-bold">
                Donations
            </h1>

            <ErrorBanner message={error} />

            <EntityForm

                fields={[

                    {
                        name: "donor_id",
                        label: "Donor",
                        type: "select",
                        options: donors.map(d => ({
                            value: d.id,
                            label: d.name,
                        })),
                    },

                    {
                        name: "fund_id",
                        label: "Campaign / Fund",
                        type: "select",
                        options: funds.map(f => ({
                            value: f.id,
                            label: `${f.name} (Fund)`,
                        })),
                    },

                    {
                        name: "amount",
                        label: "Donation Amount",
                        type: "number",
                    },

                ]}

                initialValues={editingDonation || {}}

                isEditing={editingDonation !== null}

                onCancel={() =>
                    setEditingDonation(null)
                }

                buttonLabel={
                    editingDonation
                        ? "Update Donation"
                        : "Create Donation"
                }

                onSubmit={handleSave}

            />

            {loading ? (

                <Loader />

            ) : (

                <EntityTable

                    columns={[

                        {
                            key: "donor_id",
                            label: "Donor",
                            render: (row) =>
                                donors.find(
                                    d => d.id === row.donor_id
                                )?.name ?? row.donor_id,
                        },

                        {
                            key: "fund_id",
                            label: "Fund",
                            render: (row) =>
                                funds.find(
                                    f => f.id === row.fund_id
                                )?.name ?? row.fund_id,
                        },

                        {
                            key: "amount",
                            label: "Amount",
                            render: (row) =>
                                formatCurrency(row.amount),
                        },

                        {
                            key: "donated_at",
                            label: "Received On",
                            render: (row) =>
                                formatDateTime(row.donated_at),
                        },

                        {
                            key: "status",
                            label: "Status",
                        },

                    ]}

                    data={donations}

                    onEdit={(row) =>
                        setEditingDonation(row)
                    }

                    onDelete={handleDelete}

                />

            )}

        </div>

    );

}