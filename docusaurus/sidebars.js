/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    {
      type: "doc",
      id: "index",
      label: "プロジェクト概要",
    },
    {
      type: "doc",
      id: "getting-started",
      label: "開発ガイド",
    },
    {
      type: "doc",
      id: "api-reference",
      label: "API リファレンス",
    },
    {
      type: "category",
      label: "議事録",
      items: ["meeting-notes/2025-06"],
    },
  ],
};

module.exports = sidebars;
