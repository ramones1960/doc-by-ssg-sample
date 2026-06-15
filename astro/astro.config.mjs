// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
  integrations: [
    starlight({
      title: "社内プロジェクト文書",
      description: "プロジェクト Orbit の技術文書・運用ガイド",
      // 表示言語を日本語に
      defaultLocale: "root",
      locales: {
        root: { label: "日本語", lang: "ja" },
      },
      social: {
        github: "https://github.com/your-org/project-orbit",
      },
      // サイドバー構成
      sidebar: [
        { label: "プロジェクト概要", link: "/" },
        { label: "開発ガイド", link: "/getting-started/" },
        { label: "API リファレンス", link: "/api-reference/" },
        {
          label: "議事録",
          items: [{ label: "2025 年 6 月", link: "/meeting-notes/2025-06/" }],
        },
      ],
      // Starlight は標準で全文検索（Pagefind）を内蔵
    }),
  ],
});
