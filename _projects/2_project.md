---
layout: page
title: Assembly theory
description: what the construction of a molecule can tell us about the chemistry that made it
img: assets/img/assembly_theory.svg
importance: 2
category: projects
related_publications: true
---

How much can a molecule tell us about the processes that made it? That question becomes especially interesting when
we're looking for life in unfamiliar chemistry. Assembly theory approaches it by asking how many steps are needed to
**build** an object from elementary parts, allowing fragments already made along the way to be reused.

The minimum number of causal joins is the object's **assembly index**. Its **copy number** tells us how many
indistinguishable instances are present in a sample. Finding many copies of an object that takes a long sequence of
joins to build is evidence that some process repeatedly selects that construction pathway.

Together, these quantities define the assembly of an ensemble,

$$
A = \sum_{i,\; n_i > 1} e^{a_i} \frac{n_i}{N_T},
$$

where $$a_i$$ is the assembly index, $$n_i$$ is the copy number, and $$N_T$$ is the total number of objects observed.
The sum runs over distinguishable object types with more than one copy. The number of possible objects grows at least
exponentially with assembly index, so repeatedly making the same complex object becomes increasingly unlikely through
an undirected process. This is why we need both the index and the abundance.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/assembly_theory.svg" title="The assembly index and copy number plane" alt="Copy number plotted against assembly index. A shaded region at low assembly index is bounded by a line falling exponentially, marking what undirected chemistry can populate. A threshold near assembly index 15 and a detection limit near ten thousand copies mark off a region reachable only through selection." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Assembly index describes how much construction an object requires; copy number describes its abundance.
    In this framework, a high value of both is a signature of selection, because undirected chemistry becomes
    exponentially less likely to produce many copies as the index increases.
</div>

My contribution is largely practical. I work on algorithms for calculating assembly indices, software that other
researchers can use, chemical databases for testing the theory, and ways to estimate the index from spectra.
These are the steps needed to take an idea about molecular construction and apply it to a sample in the laboratory.

## What the index measures, and why it can be measured at all

An assembly space specifies a set of objects and the rules for joining them. Its elementary units cannot themselves
be made by a join, and every other object must be reachable from those units in a finite number of steps. For
molecules, we use graphs with coloured vertices for atoms and coloured edges for bonds. A join identifies a
non-trivial subset of same-coloured vertices between two fragments, and the elementary units are single bonds.

This definition doesn't require us to know the molecule's actual synthesis history. We may have no record of the
catalysts, cells, or geochemical conditions involved, but we can examine the bonds in the molecule we have.
Tandem mass spectrometry, NMR, and infrared spectroscopy provide routes to measuring its assembly index. Agreement
between these methods is central to treating the index as a measurable physical quantity
{% cite slocombe2024measuring %}. It also makes the approach useful for life detection without training a model on
examples of known biology.

The distinction from other complexity measures is in what we count. Böttcher and Bertz indices describe structural
features such as branching, rings, and connectivity. Assembly index describes the minimum contingent information
needed to construct the object. Reaction grammars address mechanisms on kinetic timescales; assembly theory considers
construction histories over evolutionary ones. Entropy describes the distribution of microstates, while compression
measures depend on how an object is encoded. Assembly index instead depends on the specified objects and joining rules.

The theory describes selection through nested spaces. The **assembly universe** contains everything a joining
operation could produce, even structures that violate valence. The **assembly possible** restricts this to physically
valid joins. An **assembly contingent** follows one history through that space, constrained by time and resources;
the **assembly observed** is the part recovered from a sample. A parameter, α, describes the preference for particular
construction paths: α = 1 gives unbiased exploration, and smaller values give stronger preferences.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/assembly_pathway.svg" title="Reuse lowers the assembly index" alt="Two assembly pathways for strings of equal length: abcabc is built in three joins because the intermediate abc is reused, whereas abcdef requires five joins because nothing in it repeats." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Two strings of the same length with different assembly indices. Because the virtual object <code>abc</code> can be
    reused once it exists, <code>abcabc</code> takes three joins; <code>abcdef</code> repeats nothing and takes five.
    The intermediates on the shortest path are causally necessary but need not be independently observable.
</div>

## The threshold

An important experimental result comes from Marshall and colleagues. They computed assembly indices for 2.5 million
organic compounds and used tandem mass spectrometry to examine biological, abiotic, taphonomic, and blinded samples.
Above a molecular assembly index (MA) of about 15, and at copy numbers above the detection threshold of roughly 10⁴,
the molecules they detected came only from samples of biological origin. There were no false positives in that study.

For astrobiology, the attraction is that the test doesn't require us to identify each molecule or assume that life
elsewhere uses familiar terrestrial chemistry. It looks for evidence of a construction pathway being selected and
repeated often enough to leave a measurable population.

## Computing it is the bottleneck

Calculating an assembly index is NP-hard, so finding an exact answer becomes difficult as objects grow. Early
calculators were spread across separate projects in Go, C++, and Rust, mostly for covalently bonded molecules.
Making these methods easier to use has been a substantial part of my work.

We use AssemblyCPP-v5 as one of the fast calculators. It stores fragments as hashed Boolean edge-lists relative to the
parent graph, allowing it to reuse results for fragments and multi-piece assembly states it has already encountered.
It also uses a branch-and-bound search to discard routes that cannot improve the answer. Searching larger fragments
first gives a bound based on an addition chain; accounting for the second-largest fragment tightens that bound.
The bound is applied both before and after fragmentation.

When exact computation is out of reach, useful approximations become essential. My work with Gage Siebert and
colleagues develops fast approximation methods alongside rigorous definitions of assembly spaces
{% cite siebert2026assembly %}.

## AssemblyTheoryTools

AssemblyTheoryTools (ATT) brings the C++ and Rust calculators into a common Python interface and handles their input
and output {% cite slocombe2026assemblytheorytools %}. You can supply molecules as SMILES, InChI, mol files, RDKit
objects, or other formats supported by ASE or RDKit. It also accepts directed or undirected strings, and coloured
graphs through NetworkX.

The output includes the index, the virtual objects on the shortest path, and a directed graph of how they combine.
That lets you inspect the construction pathway as well as its length. Joint assembly spaces extend the calculation
to sets of objects: sharing intermediates can make their combined assembly much cheaper than building each separately.

The package can also reconstruct pathways, enumerate structures one join away, and generate new objects from an input
molecule's assembly pool while respecting valence constraints. In drug-discovery applications, these pathways are used
to recombine fragments from known active molecules into candidates with different structures that retain the parent's
efficacy. The ASE connection lets us calculate electronic-structure properties along a pathway.
Calculations can run across cores and on clusters; the package is available through pip or conda for Linux, Windows,
and macOS.

## Measuring it on spectra instead of structures

For an unfamiliar sample, we may have a spectrum long before we know which molecules are present. Estimating assembly
index directly from that spectrum makes the approach useful in situations where identifying every structure is impractical.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/assembly_metrology.svg" title="Three routes to the same assembly index" alt="A molecular graph, an infrared spectrum, and a tandem mass spectrometry fragment tree all converging on a single assembly index value, via graph search, peak counting, and recursion over the fragment tree, respectively." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Graph calculations and spectroscopic measurements approach the same assembly index from different directions.
    Comparing their results lets us test how well the measurements recover the quantity defined by the theory.
</div>

**Infrared.** The number of peaks in the fingerprint region has a linear relationship with assembly index, rooted in
the molecule's quantum state. To test this against the Chemotion IR repository, we smooth the spectra before counting
peaks, because noise can inflate the count. We then compare the predicted indices with those calculated from molecular graphs.

**Tandem mass spectrometry.** An MS/MS fragmentation tree can be read backwards as a possible assembly pathway.
If fragmentation data are unavailable, a mass-based estimate, MA ≈ 0.047 × MW − 0.4, provides a starting point.
That fit uses more than 16 million PubChem molecules, but becomes less reliable for heavy atoms such as bromine and
iodine, repeating units, and large molecules, where the bounds on MA spread apart.

The recursive approach follows the tree from the parent ion, matching daughter masses to plausible joins. A branch
ends at a single element, which contributes nothing, or at an ion with no observed daughters, where we use the mass
estimate. The reported index is the shortest construction route found through the tree. For a 297 Da phosphonate
ester with a graph-computed index of 14, this method estimates about 13 using spectra alone.

## Beyond molecules

Applying assembly theory to other systems requires care in choosing the units and joining rules. Chemical bonds work
well for molecules because they record physical constraints and can be probed experimentally. For a long peptide or
a genome, useful units may instead lie at the level of peptide bonds, larger motifs, or modular subunits.

The patterns found by a graph algorithm need to correspond to something physically meaningful and measurable.
Otherwise, the result may reflect how we labelled or simplified the data. Work so far has examined molecules,
planetary atmospheres, and periodic solid-state materials.

I've been particularly involved in the atmospheric work. We observe an exoplanet's atmosphere through spectra, without
resolving its individual molecules. Assembly measures offer a way to look for chemical selection in the mixture
without first identifying every component {% cite janin2025searching %}. We discuss how this could inform observations
with the Habitable Worlds Observatory in {% cite walker2026searching %}.

## Chemical space to test against

Testing these ideas takes a reliable set of molecules and reactions. Our CBR-db database contains over 18,000
compounds with associated KEGG reactions, cleaned so that each entry can be read as a chemical graph
{% cite slocombe2026cbrdb %}.

Across this biochemical space, the lower bound on assembly index grows logarithmically with molecular weight, while
the upper bound grows linearly. The widening gap reflects the scope for larger molecules to reuse substructures in
their assembly pathways.

## Related threads

Related collaborations look at how metabolic network structure can give rise to molecular chirality
{% cite malloy2025emergence %}, and why the elemental composition of proteomes remains so consistent across cellular
and viral life over deep time {% cite benites2026deeptime %}.

## Software

You can find the open-source code for AssemblyTheoryTools and CBR-db at
[ELIFE-ASU/assemblytheorytools](https://github.com/ELIFE-ASU/assemblytheorytools) and
[ELIFE-ASU/CBRdb](https://github.com/ELIFE-ASU/CBRdb). Both are actively maintained, with tutorials covering installation,
assembly-index calculations, assembly spaces, and the spectroscopic methods described above.
