// @ts-check
const { themes } = require("prism-react-renderer");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "社内プロジェクト文書",
  tagline: "プロジェクト Orbit の技術文書・運用ガイド",

  url: "https://your-internal-domain.example",
  baseUrl: "/",

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "ja",
    locales: ["ja"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: "./sidebars.js",
          routeBasePath: "/",
          // バージョン管理を有効にする場合は以下をコメント解除
          // lastVersion: "current",
          // versions: {
          //   current: { label: "v2.0 (最新)" },
          // },
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: "プロジェクト Orbit",
        items: [
          { to: "/", label: "ドキュメント", position: "left" },
          {
            href: "https://github.com/your-org/project-orbit",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        copyright: `© ${new Date().getFullYear()} 開発チーム — 社内限定`,
      },
      prism: {
        theme: themes.github,
        darkTheme: themes.dracula,
        additionalLanguages: ["bash", "json", "yaml"],
      },
    }),
  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
        language: ["ja"],
        docsRouteBasePath: "/",
      },
    ],
  ],
};

module.exports = config;
