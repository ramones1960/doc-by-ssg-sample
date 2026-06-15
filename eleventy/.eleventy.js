const markdownIt = require("markdown-it");
const markdownItAnchor = require("markdown-it-anchor");
const markdownItToc = require("markdown-it-table-of-contents");

module.exports = function (eleventyConfig) {
  // Markdown の設定
  const md = markdownIt({ html: true, linkify: true, typographer: true })
    .use(markdownItAnchor, { permalink: markdownItAnchor.permalink.headerLink() })
    .use(markdownItToc, { includeLevel: [2, 3] });
  eleventyConfig.setLibrary("md", md);

  // CSS・静的ファイルをそのままコピー
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/img");

  // 更新日時フィルタ
  eleventyConfig.addFilter("dateJa", (date) =>
    new Date(date).toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "long",
      day: "numeric",
    })
  );

  // コレクション：docs ディレクトリ内のページ
  eleventyConfig.addCollection("docs", (collectionApi) =>
    collectionApi.getFilteredByGlob("src/docs/**/*.md").sort((a, b) =>
      (a.data.order ?? 99) - (b.data.order ?? 99)
    )
  );

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
