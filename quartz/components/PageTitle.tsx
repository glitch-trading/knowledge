import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const PageTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <h2 class={classNames(displayClass, "page-title")}>
      <a href={baseDir}>
        <img src={`${baseDir}/static/icon.gif`} alt={cfg.pageTitle} class="page-logo" />
      </a>
    </h2>
  )
}

PageTitle.css = `
.page-title {
  margin: 0;
}

.page-logo {
  height: 150px;
  width: auto;
  display: block;
  border-radius: 0;
  margin: 0;
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
