# Zhenghao Xu - Academic Homepage

Source for <https://xu-zhenghao-zzz.github.io>, adapted directly from the real directory structure of [luost26/academic-homepage](https://github.com/luost26/academic-homepage). The site keeps the original Style A visual system and Jekyll data/collection conventions; it is not a separate generic Jekyll scaffold.

## Site structure

```text
Xu-zhenghao-zzz.github.io/
├── .github/workflows/pages.yml   # GitHub Pages deployment
├── _data/                        # profile, navigation, display, authors
├── _includes/                    # original template widgets
├── _layouts/                     # original template layouts
├── _publications/2026/           # manuscript records
├── assets/
│   ├── css/ and js/              # Style A assets
│   ├── images/                   # portrait and badge placeholders
│   └── pdf/cv.pdf                # replace-in-place CV placeholder
├── index.html                    # contact-first homepage
├── research.html                 # complete research portfolio
├── publications.html             # all public manuscript records
├── projects.html                 # selected/open-source projects
├── cv.html                       # stable CV landing page
├── _config.yml
├── Gemfile
└── TODO.md
```

There is intentionally no News or Blog navigation/content.

## Replace the placeholders

1. **Portrait:** overwrite `assets/images/photos/portrait-placeholder.svg` with a portrait, or change `portrait_url` in `_data/profile.yml`.
2. **CV:** overwrite `assets/pdf/cv.pdf`. Keep the filename to preserve every existing link.
3. **Project links:** replace the visible TODO text in `projects.html` after repositories are public.
4. **Paper links and authors:** edit files in `_publications/2026/`. Public author lists are intentionally omitted where the supplied manuscript was anonymous or the order was not confirmed.
5. Review every item in [TODO.md](TODO.md) before public launch.

## Local preview

Ruby is not bundled with this Windows workspace. On a machine with Ruby 3.2+ and Bundler:

```bash
bundle install
bundle exec jekyll serve
```

Open the URL printed by Jekyll (normally `http://127.0.0.1:4000`).

## Deploy to GitHub Pages

1. Create an empty public repository named `Xu-zhenghao-zzz.github.io` under the `Xu-zhenghao-zzz` account.
2. Commit this directory and push its `main` branch to that repository.
3. In GitHub, open **Settings -> Pages** and select **GitHub Actions** as the source.
4. The included workflow builds Jekyll with the template's `jekyll-email-protect` plugin and deploys the generated site.

The workspace repository intentionally has no push configured for the target account. Review the local preview and TODO list before adding a remote or pushing.

## Content policy used in this draft

- GRACE is listed as **Manuscript under revision**, with Zhenghao Xu's contribution limited to cross-topology generalization experiments and sensitivity analysis.
- RobustVidBench is listed only as **Manuscript**; no rejected or future venue is named.
- Anonymous/double-blind wireless manuscripts are listed conservatively as **Manuscript**, without venue or inferred author order.
- The patent is described only as a **Chinese Invention Patent Application** with the supplied application number and inventor order; no legal status is invented.
- Research summaries distinguish paper-level findings from Zhenghao Xu's confirmed personal contribution.

## License and acknowledgement

The upstream template is MIT licensed; its license is preserved in [LICENSE](LICENSE). The footer also retains attribution to `luost26/academic-homepage`.

