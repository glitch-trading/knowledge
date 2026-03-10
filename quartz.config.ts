import { QuartzConfig } from "./quartz/cfg";
import * as Plugin from "./quartz/plugins";

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Glitch Knowledge Base",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "knowledge.glitch.trading",
    ignorePatterns: [".obsidian", "templates"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#09090D",
          lightgray: "#2f334d",
          gray: "#444a73",
          darkgray: "#a9b8e8",
          dark: "#c8d3f5",
          secondary: "#82aaff",
          tertiary: "#c3e88d",
          highlight: "rgba(252, 167, 234, 0.12)",
          textHighlight: "rgba(255, 199, 119, 0.25)",
        },
        darkMode: {
          light: "#09090D",
          lightgray: "#2f334d",
          gray: "#444a73",
          darkgray: "#a9b8e8",
          dark: "#c8d3f5",
          secondary: "#82aaff",
          tertiary: "#c3e88d",
          highlight: "rgba(252, 167, 234, 0.12)",
          textHighlight: "rgba(255, 199, 119, 0.25)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "material-theme-palenight",
          dark: "material-theme-palenight",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
};

export default config;
