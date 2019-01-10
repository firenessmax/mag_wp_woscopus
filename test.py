import sys

datos = [
	{
		"authors":"asdfasdfasdf",
		"title":"titulos y la wea xD",
		"year":2099,
		"source":"blablabla",
		"pagerange":"57-90",
		"index":{"doi":"10.1021/acs.cgd.7b00569"},
		"vol":18
	},
	{
		"authors":"asdfasdfasdf",
		"title":"titulos y la wea xD",
		"year":2099,
		"source":"blablabla",
		"pagerange":"57-90",
		"index":{"doi":"10.1021/acs.cgd.7b00569"},
		"vol":18
	},
	{
		"authors":"asdfasdfasdf",
		"title":"titulos y la wea xD",
		"year":2099,
		"source":"blablabla",
		"pagerange":"57-90",
		"index":{"doi":"10.1021/acs.cgd.7b00569"},
		"vol":18
	}
]
if len(sys.argv)==2:
	if sys.argv[1]=="mmarin":
		print "<h3>Publicaciones</h3>"
		print "<ul>"
		#TODO: hacer que se ve bonito
		for au in datos:
			print "<li><span>{authors}({year}). {title} <i>{source}</i>, <i>{volume}</i>, {pagerange}. {index}</span></li>".format(
					authors=au['authors'],
					year=au['year'],
					title=au['title'],
					source=au['source'],
					volume=au['vol'],
					pagerange=au['pagerange'],
					index=", ".join([k+': '+v for k,v in au['index'].items()])
				)
		print "</ul>"
	else:
		print "<span>No hay datos<span>"
else:
	print "<span>ERROR<span>"