##      Discourse structure                    # 

Discourse or text generally has multiple clauses or sentences. The parts of discourse are interrelated and form a coherent whole that clearly expresses a meaning. Since communication mostly takes place
in discourse (text), research in language sciences cannot simply confine itself to words and sentences. Discourse in the wider sense underlies disciplines such as law, religion, politics, science amongst others. **Discourse structure**, like syntax, concerns the ways in which discourse units are brought together to form a coherent discourse. Discourse structure mostly concerns the logical and topological interrelations of discourse units (or elementary discourse units, EDUs). Discourse structure reflects the thematic organization of the text at various levels of granularity and it constrains semantic interpretations. **Discourse relation** is the semantic or logical meaning of the connections between discourse units. It is a central concern in discourse structure. The processing of discourse structure is thus a crucial part of research in linguistics, especially that concerning natural language processing. The study of the processing of discourse structure is particularly helpful when it comes to seeing how humans comprehend language in a real-world context.

# The python scripts 

The code in the folder (PDTB2dep) can convert the PDTB annotations into discourse dependency information

The following is about some possible explorations based on discourse dependency. 
# Theories of discourse structure

Researchers have developed many different theories of discourse and these reflect many and various perspectives on textual coherence. 

## 1) RST 
(Rhetorical Structure Theory, Mann and Thompson (1988))
is one influential approach in this field. It describes textual coherence
using the rhetorical relations between EDUs and postulates a hierarchical tree structure. 

## 2) D-LTAG theory 
(a lexicalized Tree Adjoining Grammar for discourse) argues that discourse relations can be lexicalized (Webber, 2004). Based on the fact that discourse connectives signal discourse
relations (e.g., “because, although, when”), this theory treats two discourse units as linked by a connective, which means that one discourse unit and the connective together constitute a dependency
relation.

## 3) SDRT
(Segmented Discourse Representation Theory, (Asher et al., 2003)), combines dynamic semantics with a discourse structure defined
via rhetorical relations between segments. These approaches to discourse structure thus reflect their different areas of focus

# Cite:
```
@inproceedings{sun2022constructing,
  title={Constructing the Corpus of Chinese Textual ‘Run-on’Sentences (CCTRS): Discourse Corpus Benchmark with Multi-layer Annotations},
  author={Sun, Kun and Wang, Rong},
  booktitle={Proceedings of the 5th International Conference on Natural Language and Speech Processing (ICNLSP 2022)},
  pages={265--276},
  year={2022}
}
```
# Discourse corpora

1) Using an RST framework, the structure of a text can be depicted as a tree with three fundamental components: (i) discourse units, (ii) the nuclearity status of the discourse units, and (iii) RST relations.
RST corpora (such as the RST discourse treebank. RST-DT) was established.

2) The Penn Discourse Treebank (PDTB 3.0), annotates English discourse structures following the D-LTAG. But because the D-LTAG looks at each relation individually and disregards most of the surrounding structures, it does not take into account the global structure of the text. This approach is used in shallow discourse parsing.

3) A number of discourse corpora have been established according to the SDRT, such as the Parallel Meaning Bank, and the STAC corpus. 

4) Although there is a lack of consensus on how to represent discourse structure, in a number of studies, the dependency structure is taken as a common structure that the other structures can be converted to. Successes can be found that RST relations have been converted into dependency relations in numerous studies.

5) More importantly, a number of discourse corpora were established following the PDTB, RST and SDRT respectively in different languages.

# Discourse Sources in mutiple languages

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## PDTB-style corpora across languages


|         language  |corpus name    |size |genre |link|              
|----------------|-------------|------------------|--------------|---------------|
|Chinese | Chinese Discourse Treebank | 70K words |newspaper|https://catalog.ldc.upenn.edu/LDC2014T21|
|Chinese | TED-CDB |72 texts | talks|https://github.com/wanqiulong0923/TED-CDB|
|Czech | Prague Discourse Treebank | 50K sentences |newspaper|https://ufal.mff.cuni.cz/pdit2.0| 
|English | Penn Discourse Treebank |one million words |newspaper|https://catalog.ldc.upenn.edu/LDC2019T05|
|English |TED-MDB | 6 texts | TED talks|https://github.com/MurathanKurfali/Ted-MDB-Annotations|
|English | BioDRB | 112K words | Biomedical articles|https://github.com/syeedibnfaiz/BioDRB|
|French |DisFrEn | 16K words | spoken genres|NA|
|German | Potsdam Commentary Corpus | 44K words | newspaper|http://angcl.ling.uni-potsdam.de/resources/pcc.html|
|German, Polish, Russian,Portuguese, and Turkish (parallel corpora by translation)| TED-MDB |6 texts |TED talks |https://github.com/MurathanKurfali/Ted-MDB-Annotations|
|Hindi | Hindi Discourse Relation Bank | 400K words |newspaper |NA|
|Italian | Luna Corpus | 25K words | dialogue|NA|
|Modern Standard Arabic | Leeds Arabic DTB |166K words|newspaper|NA|
|Iranian |Persian Discourse Treebank |30,000 sentences | NA|NA|
|Turkish |METU-TDB Corpus | 500K words | different genres|https://ii.metu.edu.tr/metu-corpora-research-group|


## RST-style corpora across languages



|         language  |corpus name    |size |genre |link|              
|----------------|-------------|------------------|--------------|---------------|
|Basque|`  RST Basque Treebank          |15.5K words            | abstracts| http://ixa2.si.ehu.eus/diskurtsoa/en/|
|Chinese          |Macro Chinese Discourse Treebank            |720 texts           |newspaper|https://figshare.com/s/250474dba44e4161b040|
|Chinese   |Chinese/Spanish Treebank`|100 texts|different genres|http://ixa2.si.ehu.eus/rst/zh/index.php|
|Chinese   |‘Run-on’ sentences`|500 texts|fiction|https://github.com/fivehills/CCTRS-corpus-|
|Dutch |Dutch RUG Corpus | 6K words | several written genres|http://www.let.rug.nl/vannoord/alp/Alpino/|
|English|RST Discourse Treebank| 176K words |newspaper|https://catalog.ldc.upenn.edu/LDC2002T07|
|English |GUM | 176K words | different genres |https://corpling.uis.georgetown.edu/gum/|
|English | SciDTB  | 1.3K texts | scientific abstracts|https://github.com/PKU-TANGENT/SciDTB|
|German | Potsdam Commentary Corpus |44K words| newspaper|http://angcl.ling.uni-potsdam.de/resources/pcc.html|
|Portuguese|CST News| 47K words| newspaper|https://sites.icmc.usp.br/taspardo/sucinto/cstnews.html|
|Spanish |  RST Spanish Treebank | 52K words | written science|http://www.corpus.unam.mx/rst/index_en.html|

> **Note:** The **Potsdam** is annoated by RST and PDTB.


## SDRT-style corpora across languages


|         language  |corpus name    |size |genre |link|              
|----------------|-------------|------------------|--------------|---------------|
|English | STAC | 1081 dialogues | multiparty dialogues|https://www.irit.fr/STAC/corpus.html|
|English | Molweni |10K dialogues | multiparty dialogues|https://github.com/HIT-SCIR/Molweni|
|English | Parallel Meaning Bank| 10 documents | NA|https://pmb.let.rug.nl/|
|French |ANNODIS |NA |NA|http://redac.univ-tlse2.fr/corpus/annodis/me_download/index_en.html|
|German, Dutch and Italian(parallel corpora by translation) | Parallel Meaning Bank |10 documents in each language |spoken genres|https://github.com/HIT-SCIR/Molweni|

## Dependency corpora across languages

|         language  |corpus name    |size |genre |link|              
|----------------|-------------|------------------|--------------|---------------|
|English | SciDTB |1355 texts | ACL paper abstracts |https://github.com/PKU-TANGENT/SciDTB|
|English | Molweni | 10K dialogues |multiparty dialogues |https://github.com/HIT-SCIR/Molweni|
|English | COVID19-DTB | 300 documents | medical articles|https://github.com/norikinishida/biomedical-discourse-treebanks|



> **Note:** The **Molweni** is annoated by SRDT and depedency.
>  **Note:** The **CCR** (Cognitive Coherence Relation) is a unified framework useful in cognitive studies, and **QAD** (question and answer) is another framework particularly useful in conversation and dialogues.


