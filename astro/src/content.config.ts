import { defineCollection } from "astro:content";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema } from "@astrojs/starlight/schema";

// Starlight のドキュメントコレクション定義
export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};
