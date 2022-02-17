function minMax(arr) {
	let max=-1000;
	let min=10000;
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