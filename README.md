XENONnT S2-only data release
============================

XENON Collaboration, 2026

The repository contains data from the paper
  * Aprile E., _et al._ (XENON collaboration), [Light Dark Matter Search with 7.8 Tonne-Year of Ionization-Only Data in XENONnT](https://arxiv.org/abs/2601.11296) (2026)

The data release allows researchers to compute dark matter search result for a custom model using XENONnT ionization-only data. Please cite our paper if you do so. For further questions and comments, please contact [Shenyang Shi](ss6109@columbia.edu) and [Yongyu Pan](yongyu.pan@lpnhe.in2p3.fr).

Contents
---------

  * `example_analysis.ipynb`: An example showing how to produce templates on the observable for a custom signal model, and build the statistical inference. Note that the systematic uncertainties, including the charge yield uncertainty, cathode background uncertainty, are not demonstrated in the example analysis. But the data release still contains them in the `data` folder.
  * `response`: The response matrix from a monoenergetic nuclear recoil energy to the observable cS2 for science run 0/1/2, in events / (bin tonne year).
  * `data`: background templates and observed events.
  * `limits`: Dark matter limit data points in Fig 4 of the paper.
  * `fig`: Figures showing the reponse matrices.
  * `s2_only_statistical_model.yaml`: Alea configs to build the statistical model, considering the systematic uncertainties and nuisance parameters.

