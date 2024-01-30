# Maine Biosciences Visualization

Maine is a low population dense region where education and industry are highly dispersed. Often, information is siloed within institutions and connections between are weak. Traditionally, ecosystem development projects concentrate on the “existence” of institutions across regions. In today’s knowledge economy, there is a need to extract the knowledge within these institutions for stakeholders. Where can I gain training to lead me to the next step? What
organization has the knowledge I need to advance my idea or product? Where can I access the talent I need to grow my business. To address this need, we propose to begin the first step in mapping a Maine knowledge map with a focus on educational pipeline. What is the knowledge and geographical roadmap for talent
development from the K-12 system to doctoral programs. Our team will explore the degree and non-degree space for life science education in the state and map these opportunities into a searchable data visualization tool. This project will:

1. Offer a first order visualization of bioscience talent in the state.
2. Provide students with a path for furthering their education in bioscience in the state.
3. Identify gaps of education and training in Maine for the bioscience industry.
4. Offer a framework for creating a larger bioscience knowledge map of Maine.

## Existing work
One student team has created this [web app](https://cs7290.github.io/bioscience/) (the GitHub for this is [here](https://github.com/cs7290/bioscience) which uses [this Observable notebook](https://observablehq.com/@class/bio-science-data-visualization-part-2@820).

Aileen has been coalescing data [here](https://docs.google.com/spreadsheets/d/1ErL4QeamLyZVcTHMMgVyM6g1Zgt1aiN6RtcGppz_XqM/edit#gid=0), whereas the student has been using the following datasets:
- [companies](https://docs.google.com/spreadsheets/d/e/2PACX-1vQEi4WHuBLMmfMxC42GLZoKo6aHLFRMTMejbcIeAu_Pk099O7hglas-K2hiGxiw65nJ7fJJMV_LMiOV/pub?gid=0&single=true&output=csv)
- [companies to streams](https://docs.google.com/spreadsheets/d/e/2PACX-1vQEi4WHuBLMmfMxC42GLZoKo6aHLFRMTMejbcIeAu_Pk099O7hglas-K2hiGxiw65nJ7fJJMV_LMiOV/pub?gid=2102318967&single=true&output=csv)
- [streams](https://docs.google.com/spreadsheets/d/e/2PACX-1vQEi4WHuBLMmfMxC42GLZoKo6aHLFRMTMejbcIeAu_Pk099O7hglas-K2hiGxiw65nJ7fJJMV_LMiOV/pub?gid=1696986308&single=true&output=csv)
- [stream to universities](https://docs.google.com/spreadsheets/d/e/2PACX-1vQEi4WHuBLMmfMxC42GLZoKo6aHLFRMTMejbcIeAu_Pk099O7hglas-K2hiGxiw65nJ7fJJMV_LMiOV/pub?gid=180963330&single=true&output=csv)
- [universities](https://docs.google.com/spreadsheets/d/e/2PACX-1vQEi4WHuBLMmfMxC42GLZoKo6aHLFRMTMejbcIeAu_Pk099O7hglas-K2hiGxiw65nJ7fJJMV_LMiOV/pub?gid=1811364362&single=true&output=csv)

I aggregated these datasets in agg.ipynb and started visualizing them in vis.ipynb. I also wrote some code to scrape US New & World Report to try to back-fill some of the missing university data.



