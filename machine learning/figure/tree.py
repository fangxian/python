#clust-->merge old clusts create the new clust

def getheight(clust):
	if clust.left==None and clust.right==None:
		return 1
	return getheight(clust.left)+getheight(clust.right)
def getdepth(clust):
	if clust.left==None and clust.right==None:
		return 0
	return max(getdepth(clust.left),getdepth(clust.right))+clust.distance

def drawdendrogram(clust,labels,jpeg='cluster.jpeg'):
	h=getheight(clust)*20
	w=1200
	depth=getdepth(clust)
	scaling=float(w-150)/depth

	img=Image.new('RGB',(w,h),(255,255,255))
	draw=ImageDraw.Draw(img)

	draw.line((0,h/2,10,h/2),fill=(255,0,0))
	drawnode(draw,clust,10,(h/2),scaling,labels)
	img.save(jpeg,'JPEG')

def drawnode(draw,clust,x,y,scaling,labels):
	if clust.id < 0:
		h1 = getheight(clust.left) * 20
		h2 = getheight(clust.right) * 20
		top = y-(h1 + h2)/2
		bottom = y + (h1 + h2)/2
		#ll == clust.distance * scaling
		draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))
		draw.line((x,top+h1/2,x+11,top+h1/2),fill=(255,0,0))
		draw.line((x,bottom-h2/2,x+11,bottom-h2/2),fill=(255,0,0))
		drawnode(draw,clust.left,x+11,top+h1/2,scaling,labels)
		drawnode(draw,clust.right,x+11,bottom-h2/2,scaling,labels)
	else:
		draw.text((x+5,y-7),labels[clust.id],(0,0,0))