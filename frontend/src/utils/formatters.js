export const formatCurrency = (value) =>
  Number(value).toLocaleString("en-US", {
    style: "currency",
    currency: "USD",
  });

export const formatDate = (value) =>
  new Date(value).toLocaleDateString("en-US");

export const formatDateTime = (value) =>
  new Date(value).toLocaleString("en-US");