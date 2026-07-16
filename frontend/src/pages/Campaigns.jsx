import { useEffect, useState } from "react";

import EntityTable from "../components/EntityTable";
import EntityForm from "../components/EntityForm";
import Loader from "../components/Loader";
import ErrorBanner from "../components/ErrorBanner";
import { formatCurrency } from "../utils/formatters";

import {
  getCampaigns,
  createCampaign,
  updateCampaign,
  deleteCampaign,
} from "../api/campaignApi";

export default function Campaigns() {
  const [campaigns, setCampaigns] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [editingCampaign, setEditingCampaign] =
  useState(null);

  useEffect(() => {
    loadCampaigns();
  }, []);

  async function loadCampaigns() {
    try {
      setLoading(true);
      setError("");

    const response = await getCampaigns();

    if (response.success) {
        setCampaigns(response.data);
    } else {
        setCampaigns([]);
    }
    } catch (err) {
      console.error(err);
      setError("Unable to load campaigns");
      setCampaigns([]);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate(formData) {
  try {
    if (editingCampaign) {
      await updateCampaign(
        editingCampaign.id,
        formData
      );
    } else {
      await createCampaign(formData);
    }

    setEditingCampaign(null);

    await loadCampaigns();
  } catch (err) {
    console.error(err);
    setError("Unable to save campaign");
  }
}

  async function handleDelete(id) {
    if (!window.confirm("Delete this campaign?")) return;

    try {
      await deleteCampaign(id);

      await loadCampaigns();
    } catch (err) {
      console.error(err);
      setError("Unable to delete campaign");
    }
  }

  return (
    <div className="space-y-6">

      <h1 className="text-3xl font-bold">
        Campaigns
      </h1>

      <ErrorBanner message={error} />

      <EntityForm
        initialValues={editingCampaign || {}}
        isEditing={editingCampaign !== null}
        onCancel={() => setEditingCampaign(null)}
        buttonLabel={
          editingCampaign
            ? "Update Campaign"
            : "Create Campaign"
        }
        fields={[
          {
            name: "name",
            label: "Campaign Name",
            type: "text",
          },
          {
            name: "description",
            label: "Description",
            type: "text",
            required: false,
          },
          {
            name: "goal_amount",
            label: "Goal Amount",
            type: "number",
          },
          {
            name: "start_date",
            label: "Start Date",
            type: "date",
          },
          {
            name: "end_date",
            label: "End Date",
            type: "date",
          },
        ]}
        onSubmit={handleCreate}
      />

      {loading ? (
        <Loader />
      ) : (
        <EntityTable
          columns={[
            {
              key: "name",
              label: "Campaign",
            },
            {
              key: "goal_amount",
              label: "Goal Amount",
              render: (row) => formatCurrency(row.goal_amount),
            },
            {
              key: "amount_raised",
              label: "Raised",
              render: (row) => formatCurrency(row.goal_amount),
            },
            {
              key: "status",
              label: "Status",
            },
          ]}
          data={campaigns}
          onDelete={handleDelete}
          onEdit={(row) => setEditingCampaign(row)}
        />
      )}
    </div>
  );
}