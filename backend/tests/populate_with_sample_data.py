#!/usr/bin/env python
# encoding: utf-8

import sys
sys.path.append("..")
sys.path.append(".")
from config import *
from helpers.basics import load_config
from helpers.logger import Logger
from helpers.db_helpers import * 


# Script 
import datetime
if "log" not in globals():
  log = Logger.init_logger('SAMPLE_DATA_%s'%(cfg.language_code), load_config())

# clear db 

species_col.remove()
publications_col.remove()
samples_col.remove()
mappings_col.remove()
measurements_col.remove()



#### Melon 


# species 

melon={
	"full_name":"Cucumis Melo",
	"abbrev_name":"C. melo",
	"aliases":["cucumis_melo","melon"],
	"taxid":3656, # taxURL: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3656
	"wikipedia":"http://en.wikipedia.org/wiki/Muskmelon",
	"preferred_id":"icugi_unigene",
	"classification":{
		"top_level":"Eukaryotes",
		"kingdom":	"Plantae",
		"unranked": ["Angiosperms","Eudicots","Rosids"],
		"order":	"Cucurbitales",
		"family":	"Cucurbitaceae",
		"genus":	"Cucumis",
		"species":	"C. melo",
	}
}

species_col.insert(melon)

m_canon={
	"full_name":"Monosporascus Cannonballus",
	"abbrev_name":"M. canonballus",
	"aliases":["monosporascus_cannonballus"],
	"taxid":155416,
	"classification":{
		"top_level":"Eukaryotes",
		"kingdom":	"Fungi",
		"phylum":	"Ascomycota",
		"class":	"Sordariomycetes",
		"subclass":	"Sordariomycetidae",
		"order":	"Sordariales",
		"family":	"Incertae sedis",
		"genus":	"Monosporascus",
		"species": "M. cannonballus"
	},
	"wikipedia":"http://en.wikipedia.org/wiki/Monosporascus_cannonballus"
}

species_col.insert(m_canon)

cmv={
	"full_name":"Cucumber mosaic virus",
	"wikipedia":"http://en.wikipedia.org/wiki/Cucumber_mosaic_virus",
	"aliases":['cmv'],
	"classification":{
		"top_level":"viruses",
		"group":"Group IV ((+)ssRNA)",
		"order":"Unassigned",
		"family":"Bromoviridae",
		"genus":"Cucumovirus",
		"species":"Cucumber mosaic virus",
	}
	
}

species_col.insert(cmv)



## publication 

melon_pub={
	"doi":"10.1186/1471-2164-10-467",
	"url":"http://www.biomedcentral.com/1471-2164/10/467",
	"first_author":"Albert Mascarell-Creus",
	"pmid":19821986, # http://www.ncbi.nlm.nih.gov/pubmed/19821986
	# rest can be populated automatically 
}

publications_col.insert(melon_pub)
## mapping 


mapping_table={
	"data_file":"mappings/1471-2164-13-601-s7.xls",
	"src":"est_unigen",
	"tgt":"icugi_unigene",
	"url":"http://www.biomedcentral.com/content/supplementary/1471-2164-13-601-s7.xls",
	"doi":"10.1186/1471-2164-13-601-s7",
	"key":"est_2_unigene",
	# parser config 
		# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":3,
		"column_keys":['idx','est_unigen','sequence','icugi_unigene'],
		"sheet_index":0,
	}
}
mappings_col.insert(mapping_table)


## samples 


samples={
	"src_pub":19821986, # Any field from the pub, doi, pmid, first author etc. 
	"species":"C. melo", # any abbrev name, key or full name, 
	"name":"Transcriptomics of infection of C. melo",
	"comments":[
		{"content":"""
Excerpt from the article related to strains : 

The material used for the transcriptomic profile analyses came from three different C. melo accessions: the line T-111, which corresponds to a Piel de Sapo breeding line, the Tendral variety (Semillas Fitó, Barcelona, Spain), and the pat81 accession of C. melo L. ssp. agrestis (Naud.) Pangalo maintained at the germplasm bank of COMAV (COMAV-UPV, Valencia, Spain). Seeds of T-111 were germinated at 30°C for two days and plants were grown in a greenhouse in peat bags, drip irrigated, with 0.25-m spacing between plants. Fruits were collected 15 and 46 days after pollination and mesocarp tissues were used for RNA extractions. Roots from pat81 plants were mock treated or inoculated with 50 colony-forming units (CFU) of M.c. per gram of sterile soil and harvested 14 days after inoculation. Cotyledons from var. Tendral, mock treated or mechanically inoculated with CMV, were harvested 3 days post inoculation. Plant growth and infections were done as described in González-Ibeas et al. [1].
		""","author":"hayssam","date":datetime.datetime.now()}
	],
	"assay":{
		"type":"micro-array",
		"design":"http://www.ebi.ac.uk/arrayexpress/files/A-MEXP-1675/A-MEXP-1675.adf.txt"
	},
	"deposited":{
		"repository":"http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-2334/",
		"sample_description_url":"http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-2334/samples/",
		"experimental_meta_data":"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?query=melogen_melo_v1"

	},
	# xls parser configuration, are propagated to all entries in  "experimental_results",
	"xls_parsing":{
		"n_rows_to_skip":4,
		"column_keys":['idx','est_unigen','length','description','fold_change'],
		"sheet_index":0,
		"id_type":"est_unigen"
	},
	"experimental_results":[
		{
			"data_file":"Cucumis/cucumis_melo/transcriptomics/micro_array/no_infection/condition_15d_VS_46d/1471-2164-10-467-S1.XLS",
			"conditions":["15d","46d"],
			"contrast":"46d VS 15d",
			"type":"contrast",
			"variety":"T-111"
		},
		{
			"data_file":"Cucumis/cucumis_melo/transcriptomics/micro_array/monosporascus_cannonballus/1471-2164-10-467-S2.XLS",
			"conditions":["non infected",{
				"infected":True,
				"infection_agent":"monosporascus_cannonballus",
				"label":"Infected with M. canonballus"
				}
			],
			"contrast":"inoculated VS non infected",
			"type":"contrast",
			"variety":"pat81"
		},
		{
			"data_file":"Cucumis/cucumis_melo/transcriptomics/micro_array/cucumber_mosaic_virus/1471-2164-10-467-S3.XLS",
			"conditions":["non infected",{
				"infected":True,
				"infection_agent":"Cucumber mosaic virus",
				"label":"Infected with CMV"
				}
			],
			"contrast":"inoculated VS non infected",
			"type":"contrast",
			"variety":"Tendral"
			
		}
	]

}

samples_col.insert(samples)



#### Prunus 




prunus={
	"full_name":"Prunus Domestica",
	"abbrev_name":"P. domestica",
	"aliases":["prunus_domestica","prunus"],
	"taxid":3758, # taxURL: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3656
	"wikipedia":"http://en.wikipedia.org/wiki/Prunus_domestica",
	"preferred_id":"unigene",
	"classification":{
		"top_level":"Eukaryotes",
		"kingdom":	"Plantae",
		"unranked":	["Angiosperms","Eudicots","Rosids"],
		"order":	"Rosales",
		"family":	"Rosaceae",
		"genus":	"Prunus",
		"subgenus":	"Prunus",
		"section":	"Prunus",
		"species":	"P. domestica",
	}
}

species_col.insert(prunus)


prunus_pub={
	"doi":"10.1371/journal.pone.0100477",
	"url":"http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0100477",
	"first_author":"Bernardo Rodamilans",
	"title":"Transcriptomic Analysis of Prunus domestica Undergoing Hypersensitive Response to Plum Pox Virus Infection",
	"pmid":24959894, # http://www.ncbi.nlm.nih.gov/pubmed/24959894
	# rest can be populated automatically 
}

publications_col.insert(prunus_pub)

ppox={
	"full_name":"Plum pox",
	"wikipedia":"http://en.wikipedia.org/wiki/Plum_pox",
	"aliases":['sharka','ppv'],
	"classification":{
		"top_level":"viruses",
		"group": "Group IV ((+)ssRNA)",
		"family": "Potyviridae",
		"genus": "Potyvirus",
		"species": "Plum pox virus"
	}
	
}

species_col.insert(ppox)

prunus_samples={
	"src_pub":19821986, # Any field from the pub, doi, pmid, first author etc. 
	"species":"P. domestica", # any abbrev name, key or full name, 
	"strain":"JoJo",
	"name":"Transcriptomics of infection of P. domestica Jojo by PPV",
	"xp_page":{
	"content":"""
RNAseq from P.domestica cv Jojo infected and non-infected with PPV; 
====

3020 differentially expressed unigenes (2234 up- and 786 down-regulated); 154 potential resistance genes; 75 additional genes that might be good candidates based on literature findings.

paper:

[Transcriptomic Analysis of Prunus domestica Undergoing Hypersensitive Response to Plum Pox Virus Infection](#24959894)
url:
http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0100477

data linked with articles :

[journal.pone.0100477.s004.xls](#journal.pone.0100477.s004.xls)
Differentially expressed unigenes. The raw number of reads found on each sample is given in columns Jojo-W1, Jojo-W2, Jojo-W+PPV and Jojo-M+PPV. Fold changes between infected and non-infected samples and FDR values are detailed in columns FC and FDR, respectively. Column labeled Description expands on the details of each unigene, including length in nucleotides.
doi:10.1371/journal.pone.0100477.s004 (XLS)

[journal.pone.0100477.s005.xls](#journal.pone.0100477.s005.xls)
Differentially expressed unigenes found in PRGdb. The raw number of reads found on each sample is given in columns Jojo-W1, Jojo-W2, Jojo-W+PPV and Jojo-M+PPV. Fold changes between infected and non-infected samples and FDR values are detailed in columns FC and FDR, respectively. Column labeled Description expands on the details of each unigene, including length in nucleotides.
doi:10.1371/journal.pone.0100477.s005. Content of this table is the same as the content from table s004, but only genes found in PRGdb are included (156 genes)

[journal.pone.0100477.s006.xls](#journal.pone.0100477.s006.xls)
Genes possibly involved in plant defense not included in the PRGdb. Similarity to a known protein is given in the Homology column. The raw number of reads found on each sample is given in columns Jojo-W1, Jojo-W2, Jojo-W+PPV and Jojo-M+PPV. Fold changes between infected and non-infected samples and FDR values are detailed in columns FC and FDR, respectively. Column labeled Description expands on the details of each unigene, including length in nucleotides.
doi:10.1371/journal.pone.0100477.s006

[journal.pone.0100477.s007.xls](#journal.pone.0100477.s007.xls)
List of genes from PRGdb matched by more than one ‘Jojo’ unigene. Reference numbers of the matched genes are shown in the NCBI Match column. The raw number of reads found on each sample is shown in columns Jojo-W1, Jojo-W2, Jojo-W+PPV and Jojo-M+PPV. Fold changes between infected and non-infected samples is given in column FC. Column labeled Description expands on the details of each gene.
doi:10.1371/journal.pone.0100477.s007. Not included.
	"""},
	"assay":{"type":"RNA-Seq"},
	"xls_parsing":{
		"n_rows_to_skip":2,
		"column_keys":['idx',"unigene", "Sequence", "Jojo-W1", "Jojo-W2", "Jojo-W+PPV", "Jojo-M+PPV", "fold_change", "logFC", "logCPM", "PValue", "FDR", "Description", "AccPrunus", "DescPrunus", "AccNCBI", "DescNCBI", "AccPlants", "DescPlants", "AccPRG", "DescPRG"],
		"sheet_index":0,
		"id_type":"unigene" #**TODO** check ID type for prunus 
	},
	"experimental_results":[{
		"name":"journal.pone.0100477.s004.xls",
		"data_file":"Prunus/prunus_domestica/transcriptomics/rna-seq/plum_pox_virus/journal.pone.0100477.s004.xls",
		"description":"Differentially expressed unigenes",
		"type":"contrast",
		"conditions":[
			"non-infected",
			{"infected":True,"infection_agent":"ppv","label":"infected with PPV"}
		]
	}, {
		"name":"journal.pone.0100477.s005.xls",
		"data_file":"Prunus/prunus_domestica/transcriptomics/rna-seq/plum_pox_virus/journal.pone.0100477.s005.xls",
		"description":"Differentially expressed unigenes found in PRGdb",
		"type":"contrast",
		"conditions":[
			"non-infected",
			{"infected":True,"infection_agent":"ppv","label":"infected with PPV"}
		]
	}
	# , {
	# 	"name":"journal.pone.0100477.s006.xls",
	# 	"data_file":"Prunus/prunus_domestica/transcriptomics/rna-seq/plum_pox_virus/journal.pone.0100477.s006.xls",
	# 	"description":"Genes that might be involved in plant defense and are not included in the PRGdb",
	# 	"type":"contrast",
	# 	"conditions":[
	# 		"non-infected",
	# 		{"infected":True,"infection_agent":"ppv","label":"infected with PPV"}
	# 	],
	# 	"xls_parsing":{'column_keys':['idx',"Homology", "Jojo-W1", "Jojo-W2", "Jojo-W+PPV", "Jojo-M+PPV", "fold_change", "logFC", "logCPM", "PValue", "FDR", "Description"]}
	# }
	# Table S7 is weird in content
	# , {
	# 	"name":"journal.pone.0100477.s007.xls",
	# 	"data_file":"Prunus/prunus_domestica/transcriptomics/rna-seq/plum_pox_virus/journal.pone.0100477.s007.xls",
	# 	"description":"",
	# 	"conditions":[
	# 		"non-infected",
	# 		{"infected":True,"infection_agent":"ppv","label":"infected with PPV"}
	# 	]
	# }
	]
}

samples_col.insert(prunus_samples)


