// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// Add navigation, news, research and profile links.
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "Research in quantum biology, molecular simulation, chemical complexity, and machine learning.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-research",
          title: "Research",
          description: "Understanding molecules, from the materials we make to the chemistry of life.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-code",
          title: "Code",
          description: "Software I&#39;ve written and helped develop for molecular simulation, materials, and chemical complexity.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "My research career, teaching, and work in the wider scientific community.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-teaching",
          title: "Teaching",
          description: "Helping students and researchers put computational methods to work in physics and chemistry.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "news-i-co-chaired-the-quantum-biology-gordon-research-symposium-in-tuscany-with-jana-vuckovic-bringing-together-49-early-career-researchers-i-raised-22-000-to-support-attendance-by-underrepresented-and-minority-researchers-and-helped-to-shape-the-programme-more-about-my-scientific-community-work",
          title: 'I co-chaired the Quantum Biology Gordon Research Symposium in Tuscany with Jana Vuckovic,...',
          description: "",
          section: "News",},{id: "news-we-ve-released-a-new-version-of-cbr-db-our-curated-biochemical-reaction-database-for-studying-the-origins-of-biochemistry-the-code-and-data-are-available-to-explore-and-reuse",
          title: 'We’ve released a new version of CBR-db, our curated biochemical reaction database for...',
          description: "",
          section: "News",},{id: "news-our-paper-on-water-behaviour-on-two-dimensional-material-interfaces-is-out-in-nature-communications-we-examine-how-individual-water-molecules-move-on-hexagonal-boron-nitride-and-graphene",
          title: 'Our paper on water behaviour on two-dimensional material interfaces is out in Nature...',
          description: "",
          section: "News",},{id: "news-i-received-a-best-poster-prize-at-frontiers-and-challenges-in-quantum-biology-at-the-niels-bohr-institute-in-copenhagen-the-poster-with-marco-sacchi-explored-nuclear-quantum-effects-in-guanine-thymine-misincorporation-in-dna-polymerase-λ",
          title: 'I received a Best Poster prize at Frontiers and Challenges in Quantum Biology...',
          description: "",
          section: "News",},{id: "news-our-new-preprint-on-proteome-elemental-composition-with-l-felipe-benites-and-sara-walker-looks-at-the-elements-that-make-up-proteins-across-cellular-and-viral-life-we-find-striking-consistency-across-thousands-of-proteomes-and-explore-what-this-might-tell-us-about-the-origins-of-the-amino-acid-alphabet",
          title: 'Our new preprint on proteome elemental composition, with L. Felipe Benites and Sara...',
          description: "",
          section: "News",},{id: "news-i-ve-joined-the-scanlon-materials-theory-group-at-the-university-of-birmingham-as-a-group-leader-research-fellow-i-ll-be-working-with-david-scanlon-on-computational-chemistry-and-machine-learning-for-sustainable-polymers-with-a-focus-on-predicting-biodegradability-more-about-my-research-and-background",
          title: 'I’ve joined the Scanlon Materials Theory Group at the University of Birmingham as...',
          description: "",
          section: "News",},{id: "projects-proton-transfer-in-dna",
          title: 'Proton transfer in DNA',
          description: "Can the motion of a single proton change how DNA is copied?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project.html";
            },},{id: "projects-molecular-complexity-amp-assembly-theory",
          title: 'Molecular complexity &amp;amp; assembly theory',
          description: "What can a molecule’s construction tell us about the processes that made it?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project.html";
            },},{id: "projects-biochemical-origins-amp-proteins",
          title: 'Biochemical origins &amp;amp; proteins',
          description: "What patterns connect life’s reaction networks, molecular building blocks, and proteins?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/biochemical_origins.html";
            },},{id: "projects-molecular-simulation-amp-quantum-dynamics",
          title: 'Molecular simulation &amp;amp; quantum dynamics',
          description: "How do we follow reactions accurately while keeping their surroundings in the picture?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/molecular_simulation.html";
            },},{id: "projects-surfaces-amp-energy-materials",
          title: 'Surfaces &amp;amp; energy materials',
          description: "How do atomic interactions control motion on a surface and a material’s response to light?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/surfaces_materials.html";
            },},{id: "projects-sustainable-polymers",
          title: 'Sustainable polymers',
          description: "How can we connect a polymer’s chemistry to its useful properties and its fate after use?",
          section: "Projects",handler: () => {
              window.location.href = "/projects/sustainable_polymers.html";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6C.%73%6C%6F%63%6F%6D%62%65@%62%68%61%6D.%61%63.%75%6B", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/LouieSlocombe", "_blank");
        },
      },{
        id: 'social-gitlab',
        title: 'GitLab',
        section: 'Socials',
        handler: () => {
          window.open("https://gitlab.com/LouieSlocombe", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0002-6986-5526", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=JISRQewAAAAJ", "_blank");
        },
      },{
        id: 'social-work',
        title: 'Work',
        section: 'Socials',
        handler: () => {
          window.open("https://research.birmingham.ac.uk/en/persons/louie-slocombe/", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
