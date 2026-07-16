import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Campaigns from "./pages/Campaigns";
import Donors from "./pages/Donors";
import Donations from "./pages/Donations";
import Grants from "./pages/Grants";
import Workflow from "./pages/Workflow";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/campaigns" element={<Campaigns />} />
        <Route path="/donors" element={<Donors />} />
        <Route path="/donations" element={<Donations />} />
        <Route path="/grants" element={<Grants />} />
        <Route path="/workflow" element={<Workflow />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;