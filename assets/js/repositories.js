(() => {
  const catalogue = document.getElementById("code-catalogue");
  if (!catalogue) return;

  const search = catalogue.querySelector(".code-search");
  const input = document.getElementById("code-search-input");
  const clear = document.getElementById("code-search-clear");
  const status = document.getElementById("code-search-status");
  const empty = catalogue.querySelector(".code-empty");
  const groups = [...catalogue.querySelectorAll(".code-group")];
  const projects = [...catalogue.querySelectorAll(".code-project")];
  const normalise = (value) =>
    value
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase();
  const searchable = new Map(projects.map((project) => [project, normalise(project.dataset.search)]));

  const filter = () => {
    const query = normalise(input.value.trim());
    const words = query.split(/\s+/).filter(Boolean);
    let visible = 0;

    projects.forEach((project) => {
      project.hidden = !words.every((word) => searchable.get(project).includes(word));
      if (!project.hidden) visible += 1;
    });

    groups.forEach((group) => {
      const count = [...group.querySelectorAll(".code-project")].filter((project) => !project.hidden).length;
      group.hidden = count === 0;
      group.querySelector(".code-group-count").textContent = count;
    });

    empty.hidden = visible !== 0;
    clear.disabled = input.value.length === 0;
    status.textContent = query ? `Showing ${visible} of ${projects.length} repositories.` : `Showing all ${projects.length} repositories.`;
  };

  input.addEventListener("input", filter);
  clear.addEventListener("click", () => {
    input.value = "";
    filter();
    input.focus();
  });

  // Topic links always reveal their destination, even after a search.
  catalogue.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", () => {
      input.value = "";
      filter();
    });
  });

  filter();
  search.hidden = false;
})();
