function minMax(arr) {
	let max=parseInt(Math.random()*-1000000000);
	let min=parseInt(Math.random()*1000000000)	;
	arr.forEach((element)=>{
		if(element<min)
			{
				min=element
			}
		if(max<element)
			{
				max=element
			}
	})
	let object =[min,max]
	return object;
}