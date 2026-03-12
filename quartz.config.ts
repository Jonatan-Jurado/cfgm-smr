import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Apuntes CFGM SMR",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "es-ES", // Cambiado a español para tus apuntes
    baseUrl: "cfgm-smr", // Asegúrate de que NO tenga '/' al final
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#f5f0fa",        // Fondo claro lavanda
          lightgray: "#e0d6eb",    // Bordes suaves
          gray: "#9882ab",         // Texto secundario
          darkgray: "#4a3b5c",     // Texto principal
          dark: "#2d2140",         // Títulos
          secondary: "#875faf",    // Púrpura royal (enlaces)
          tertiary: "#a78bba",     // Púrpura claro (hover)
          highlight: "rgba(135, 95, 175, 0.12)",
          textHighlight: "#d9c7f0aa",
        },
        darkMode: {
          light: "#1a1520",        // Fondo oscuro púrpura
          lightgray: "#2d2438",    // Bordes
          gray: "#6e5a80",         // Texto secundario
          darkgray: "#c8b8d8",     // Texto principal
          dark: "#e8daf0",         // Títulos
          secondary: "#b8a7c5",    // Lavanda (enlaces)
          tertiary: "#a78bfa",     // Púrpura brillante (hover)
          highlight: "rgba(167, 139, 250, 0.15)",
          textHighlight: "#7c3aed55",
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
          light: "github-light",
          dark: "github-dark",
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
    ],
  },
}

export default config
