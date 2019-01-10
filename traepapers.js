
var data = [{"autores":"asdfasdfasdf", "titulo":"titulos y la wea xD","year":2099,"revista":"blablabla","pagerange":"57-90","doi":"10.1021/acs.cgd.7b00569","vol":18}];
papers = document.getElementById("papers");
for(k in data){
	parrafo= document.createElement("p");
	parrafo.innerHTML ="<span>"+
		data[k].autores+
		"("+data[k].year+"). "+
		data[k].titulo+
		" <i>"+data[k].revista+"</i>, <i>"+data[k].vol+"</i>, "+
		data[k].pagerange+
		". doi: "+data[k].doi+"</span>";
	papers.append(parrafo);
}