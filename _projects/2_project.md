---
layout: page
title: assembly theory
description: measuring selection and causal depth in molecules, spectra, and planetary atmospheres
img: assets/img/assembly_theory.svg
importance: 2
category: projects
related_publications: true
---

Complexity measures are easy to invent and hard to trust. Almost all of them are defined on a *representation* — a
string, a compressed file, a graph descriptor — so the number you get out depends on how you chose to write the object
down. Assembly theory takes a different route. It asks how many steps are needed to **build** an object from its
elementary parts, allowing anything already made along the way to be reused, and it insists that this number be
measurable in a laboratory rather than merely computable from a model.

Two quantities do the work. The **assembly index** of an object is the minimum number of causal joins required to
construct it from its units, and its **copy number** is how many indistinguishable instances of it are present in a
sample. Together they define the assembly of an ensemble,

$$
A = \sum_{i,\; n_i > 1} e^{a_i} \frac{n_i}{N_T},
$$

where the sum runs over distinguishable object types and $$N_T$$ is the total number of objects observed. The index
measures causal depth; the copy number measures whether some mechanism keeps producing that depth. Neither alone is
diagnostic. Their conjunction is, because the number of possible objects grows at least exponentially with assembly
index, so an undirected process is exponentially unlikely to make the *same* deep object many times over.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/assembly_theory.svg" title="The assembly index and copy number plane" alt="Copy number plotted against assembly index. A shaded region at low assembly index is bounded by a line falling exponentially, marking what undirected chemistry can populate. A threshold near assembly index 15 and a detection limit near ten thousand copies mark off a region reachable only through selection." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Without selection, copy number falls at least exponentially with assembly index, so deep objects are never abundant.
    The joint observation of a high assembly index <em>and</em> a high copy number is the signature that cannot be
    reached by undirected chemistry.
</div>

My own work is on the part of this that has to actually run: the algorithms that compute the index, the software that
makes it usable outside the group that invented it, the curated chemical spaces to test it against, and the
spectroscopic pipelines that measure it on samples rather than on structures.

## What the index measures, and why it can be measured at all

An assembly space is a set of objects together with a rule saying which pairs may be joined into which products. Units
are the objects that are not the product of any join, and every object in the space must be reachable from the units in
finitely many steps. For molecules the objects are graphs with coloured vertices (atoms) and coloured edges (bonds), a
join identifies a non-trivial subset of same-coloured vertices between two fragments, and the units come out as single
bonds. Nothing about that definition refers to how the molecule was actually made.

That is the point. Environmental and historical constraints — which catalyst, which cell, which geochemical setting —
are usually unknown and always context-dependent, but the bonds in a molecule are there in the object itself. Because
the elementary steps are physical, the index is accessible to instruments: tandem mass spectrometry, NMR, and infrared
spectroscopy all give handles on it, and they agree. This is what separates assembly theory from complexity measures
that only exist on paper. It also separates it from machine-learning approaches to life detection, which have to be
trained on known biology and inherit its assumptions {% cite slocombe2024measuring %}.

It is a genuinely different quantity from the chemical complexity scores it is often compared against. Böttcher and
Bertz indices count structural features — branching, rings, connectivity patterns — whereas the assembly index counts
the minimum contingent information required to put the object together. Reaction grammars describe mechanism on kinetic
timescales; the assembly index accumulates causation over evolutionary ones. Entropy captures the distribution of
microstates but says nothing about the pathway. And unlike compression-based measures, it does not depend on how the
data were encoded or labelled.

Spaces defined this way nest, and the nesting is what carries the notion of selection. The assembly universe contains
everything any joining operation could produce, including structures that violate valence; the assembly possible is the
subset reachable by physically valid joins; and an assembly contingent is a single resource-bound, time-bound
trajectory through it — a history. What an instrument recovers from a sample is an assembly observed, one contingent
space among the many that could have been realised. How strongly a system prefers particular routes through this
structure is parameterised directly: unbiased exploration sits at α = 1, and smaller values mean sharper preference for
specific construction paths.

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

The empirical anchor for all of this is a threshold. Marshall and colleagues computed assembly indices across 2.5
million organic compounds and measured them by tandem mass spectrometry on biological, abiotic, taphonomic, and blinded
samples. Above a molecular assembly index (MA) of about 15 — at copy numbers above the tandem MS detection threshold of
roughly 10⁴ — such molecules turned up only in samples of biological origin. No false positives.

That single number is what makes assembly theory operational for astrobiology. It provides a life-detection test that
does not presuppose which chemistry life is made of, only that whatever made the molecule had to select a deep pathway
and then repeat it. The molecules do not have to be identified, and the sample does not have to resemble anything on
Earth.

## Computing it is the bottleneck

Calculating an assembly index is NP-hard, and this is the practical obstacle to using the theory on anything large.
Early implementations were bespoke: an initial calculator in Go, later work in C++, more recently in Rust. They were
scattered across papers, mostly limited to covalently bonded molecules, and each imposed a substantial barrier to entry.

AssemblyCPP-v5, the C++ calculator that does the heavy lifting for us, gets its speed from two things. During the
enumeration of duplicatable subgraphs, fragments are stored as Boolean edge-lists against the parent graph and hashed,
so both fragments and multi-piece assembly states can be memoised — dynamic programming over previously seen
structures. On top of that, the search tree is pruned by a branch-and-bound heuristic: searching fragments in
decreasing order of size lets you bound the achievable index using an addition chain conditional on the largest
fragment that can be taken, and the current version tightens this by accounting for the second-largest fragment as
well, applying the bound both before and after fragmentation.

The formal side matters too, since much of the confusion around assembly theory has come from imprecise definitions.
Work with Gage Siebert and colleagues sets out assembly spaces rigorously and develops fast methods for *approximating*
assembly indices where exact computation is out of reach {% cite siebert2026assembly %} — which, given NP-hardness, is
the regime most interesting applications live in.

## AssemblyTheoryTools

AssemblyTheoryTools (ATT) is the software layer over all of this {% cite slocombe2026assemblytheorytools %}. It is a
Python package that wraps the fast C++ and Rust calculators, handles their input and output, and exposes assembly
theory through an interface that assumes Python and nothing more specialised.

The scope is deliberately wider than chemistry. Molecules come in as SMILES, InChI, mol files, RDKit objects, or
anything ASE or RDKit can read; strings come in directly, directed or undirected; and anything else that can be encoded
as a coloured graph comes in through NetworkX. Every calculation returns three things — the index, the list of virtual
objects on the shortest path, and the directed graph showing how they combined — which is what makes downstream
analysis possible rather than just index lookup. Joint assembly spaces let you ask what a *set* of objects costs to
co-assemble, typically far less than the sum of the individual indices, since intermediates are shared.

Beyond calculation, the package explores assembly space: reconstructing pathways, enumerating the neighbourhood of
structures reachable by a single join, and generating new objects from the assembly pool of an input molecule under
valence constraints. This is the mode used for drug discovery, where deconstructing known actives into pathways and
recombining fragments along them yields candidates that keep the parent's efficacy with different structure. Through
ASE it also hooks into electronic-structure calculations, so properties can be attached to objects along a pathway.
Calculations parallelise across cores and onto clusters; the package installs from pip or conda and runs on Linux,
Windows, and macOS.

## Measuring it on spectra instead of structures

Computing the index needs the structure. Measuring it does not, and that is the more useful direction for anything you
might find on another planet.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/assembly_metrology.svg" title="Three routes to the same assembly index" alt="A molecular graph, an infrared spectrum, and a tandem mass spectrometry fragment tree all converging on a single assembly index value, via graph search, peak counting, and recursion over the fragment tree respectively." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    The assembly index is the same quantity whether it is computed from a molecular graph or measured spectroscopically.
    Agreement between the routes is what gives it the status of a metrological quantity rather than a descriptor.
</div>

**Infrared.** The number of peaks in the fingerprint region tracks the assembly index linearly, a relationship rooted
in the molecule's quantum state. Validating this against the Chemotion IR repository means smoothing real spectra
before peak-finding — noise inflates the count badly — then fitting predicted against graph-computed indices across the
database.

**Tandem mass spectrometry.** Fragmentation reveals a molecule's constructive hierarchy directly, so an MS/MS tree can
be read backwards as an assembly pathway. Without fragmentation data the best you can do is a mass approximation,
MA ≈ 0.047 × MW − 0.4, fitted across more than 16 million PubChem molecules; it degrades for heavy atoms like bromine
and iodine, for molecules with repeating units, and for exactly the heavy molecules that make good biosignatures, since
the bounds on MA diverge with mass. The recursive algorithm does better by walking the fragment tree from the parent
ion down, matching daughter masses to plausible join operations at each level and recursing. A branch terminates either
on a single element, contributing nothing, or on an ion with no observed daughters, where the mass approximation fills
in. The reported index is the shortest constructive route found through the whole tree. On a 297 Da phosphonate ester
with a graph-computed index of 14, the recursive estimate returns about 13, from spectra alone.

## Beyond molecules

The formalism generalises, but not for free. The molecular case works because chemical bonds are simultaneously the
physical constraints that record causation *and* the things instruments can see. Carry the same bond-by-bond
construction over to a long peptide or a genome and it stops being informative — there you want units and joins that
sit where the constraints actually are, at peptide bonds or higher-level motifs or modular subunits.

The real difficulty is not encoding an object as a graph, which is usually easy. It is finding domains where the
symmetries and repeated motifs an assembly calculator detects correspond to something functionally meaningful and
measurable, rather than to an artefact of how the data were labelled or coarse-grained. Validated substrates so far are
molecules, planetary atmospheres, and periodic solid-state materials.

Atmospheres are where I have been most involved in pushing past the molecular case. An exoplanet atmosphere is observed
spectroscopically and never resolved into individual molecules, which is precisely the regime where a
measurable-without-identification complexity scale is worth having — you can ask whether the mixture shows evidence of
chemical selection without knowing what is in it {% cite janin2025searching %}. The mission-relevant version of that
argument, aimed at the Habitable Worlds Observatory, is set out in {% cite walker2026searching %}.

## Chemical space to test against

None of the above is testable without well-curated chemistry to run it on. CBR-db is a curated biochemical reaction
database built for this kind of analysis {% cite slocombe2026cbrdb %}: over 18,000 compounds with associated KEGG
reactions, cleaned so that every entry parses into a chemical graph. Surveying assembly indices across it shows the
shape of biochemical space — a lower bound on the index that grows logarithmically with molecular weight against an
upper bound that grows linearly, with the gap between them opening up as molecules get large enough to contain
recursive substructure.

## Related threads

The same interest in what selection leaves behind in chemistry runs through work on the emergence of molecular chirality
from metabolic network structure {% cite malloy2025emergence %}, and on the deep-time stability of proteome elemental
composition across cellular and viral life {% cite benites2026deeptime %}.

## Software

AssemblyTheoryTools and CBR-db are open source and actively maintained at
[ELIFE-ASU/assemblytheorytools](https://github.com/ELIFE-ASU/assemblytheorytools) and
[ELIFE-ASU/CBRdb](https://github.com/ELIFE-ASU/CBRdb), with tutorials covering installation, assembly-index
computation, assembly-space construction, and the spectroscopic pipelines described above.
