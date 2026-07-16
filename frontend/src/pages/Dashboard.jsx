import { useEffect, useState } from "react";

import DashboardCard from "../components/DashboardCard";
import Loader from "../components/Loader";
import ErrorBanner from "../components/ErrorBanner";

import { getCampaigns } from "../api/campaignApi";
import { getDonors } from "../api/donorApi";
import { getDonations } from "../api/donationApi";
import { getGrants } from "../api/grantApi";
import { getFunds } from "../api/fundApi";

import { formatCurrency } from "../utils/formatters";

export default function Dashboard() {

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [stats, setStats] = useState({
    campaigns: 0,
    donors: 0,
    funds: 0,
    grants: 0,
    donations: 0,
    totalRaised: 0,
    fundBalance: 0,
  });

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {

    try {

      setLoading(true);
      setError("");

      const [
        campaignRes,
        donorRes,
        donationRes,
        grantRes,
        fundRes,
      ] = await Promise.all([
        getCampaigns(),
        getDonors(),
        getDonations(),
        getGrants(),
        getFunds(),
      ]);

      const funds = fundRes.success ? fundRes.data : [];

      setStats({

        campaigns: campaignRes.success
          ? campaignRes.data.length
          : 0,

        donors: donorRes.success
          ? donorRes.data.length
          : 0,

        donations: donationRes.success
          ? donationRes.data.length
          : 0,

        grants: grantRes.success
          ? grantRes.data.length
          : 0,

        funds: funds.length,

        totalRaised: funds.reduce(
          (sum, fund) =>
            sum + Number(fund.total_received),
          0
        ),

        fundBalance: funds.reduce(
          (sum, fund) =>
            sum + Number(fund.balance),
          0
        ),

      });

    } catch (err) {

      console.error(err);

      setError("Unable to load dashboard");

    } finally {

      setLoading(false);

    }

  }

  if (loading) {
    return <Loader />;
  }

  return (

    <div className="space-y-6">

      <h1 className="text-3xl font-bold">
        Dashboard
      </h1>

      <ErrorBanner message={error} />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

        <DashboardCard
          title="Campaigns"
          value={stats.campaigns}
        />

        <DashboardCard
          title="Donors"
          value={stats.donors}
        />

        <DashboardCard
          title="Funds"
          value={stats.funds}
        />

        <DashboardCard
          title="Grants"
          value={stats.grants}
        />

        <DashboardCard
          title="Donations"
          value={stats.donations}
        />

        <DashboardCard
          title="Total Raised"
          value={formatCurrency(stats.totalRaised)}
        />

        <DashboardCard
          title="Fund Balance"
          value={formatCurrency(stats.fundBalance)}
        />

        <DashboardCard
          title="AI Recommendations"
          value="Coming Soon"
        />

      </div>

    </div>

  );

}