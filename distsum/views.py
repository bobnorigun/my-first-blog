from django.shortcuts import render

# Create your views here.
import csv, io
from django.contrib import messages
from .models import Mylocation
import os, re, math

def distsum(request):
	template = "distsum/fileupload.html"
	data = Mylocation.objects.all()
	loca_count = Mylocation.objects.count()
	prompt = {'order': 'lat,lon', 'loca_count': loca_count}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, '잘못된 파일')

	data_set = csv_file.read().decode('UTF-8')

	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=','):
		_, created = Mylocation.objects.update_or_create(
			lat=column[0],
			lon=column[1]
		)
	context = {}

	return render(request, template, context)

def calc_dist(lat1, lon1, lat2, lon2):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	delta_lat = lat2 - lat1
	delta_lon = lon2 - lon1

	a = ((math.sin(delta_lat/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin(delta_lon/2))**2)
	c = 2 * math.atan2(a**0.5, (1-a)**0.5)

	earth_radius = 6371

	return float(earth_radius * c)

"""아래 수작업으로 불러 온 좌표값들을 자동으로 생성하고 결과값을 뽑아내는 공식을 만들고 싶어요!!!"""

def caldistview(request):
	q = Mylocation.objects.get(pk=1)
	q1 = float(q.lat)
	q2 = float(q.lon)
	r = Mylocation.objects.get(pk=2)
	r1 = float(r.lat)
	r2 = float(r.lon)
	s = Mylocation.objects.get(pk=3)
	s1 = float(s.lat)
	s2 = float(s.lon)
	t = Mylocation.objects.get(pk=4)
	t1 = float(t.lat)
	t2 = float(t.lon)
	u = Mylocation.objects.get(pk=5)
	u1 = float(u.lat)
	u2 = float(u.lon)
	v = Mylocation.objects.get(pk=6)
	v1 = float(v.lat)
	v2 = float(v.lon)
	w = Mylocation.objects.get(pk=7)
	w1 = float(w.lat)
	w2 = float(w.lon)
	x = Mylocation.objects.get(pk=8)
	x1 = float(x.lat)
	x2 = float(x.lon)
	y = Mylocation.objects.get(pk=9)
	y1 = float(y.lat)
	y2 = float(y.lon)
	z = Mylocation.objects.get(pk=10)
	z1 = float(z.lat)
	z2 = float(z.lon)
	a = Mylocation.objects.get(pk=11)
	a1 = float(a.lat)
	a2 = float(a.lon)
	b = Mylocation.objects.get(pk=12)
	b1 = float(b.lat)
	b2 = float(b.lon)
	c = Mylocation.objects.get(pk=13)
	c1 = float(c.lat)
	c2 = float(c.lon)
	d = Mylocation.objects.get(pk=14)
	d1 = float(d.lat)
	d2 = float(d.lon)
	e = Mylocation.objects.get(pk=15)
	e1 = float(e.lat)
	e2 = float(e.lon)
	f = Mylocation.objects.get(pk=16)
	f1 = float(f.lat)
	f2 = float(f.lon)
	g = Mylocation.objects.get(pk=17)
	g1 = float(g.lat)
	g2 = float(g.lon)
	h = Mylocation.objects.get(pk=18)
	h1 = float(h.lat)
	h2 = float(h.lon)
	i = Mylocation.objects.get(pk=19)
	i1 = float(i.lat)
	i2 = float(i.lon)
	j = Mylocation.objects.get(pk=20)
	j1 = float(j.lat)
	j2 = float(j.lon)
	k = Mylocation.objects.get(pk=21)
	k1 = float(k.lat)
	k2 = float(k.lon)
	l = Mylocation.objects.get(pk=22)
	l1 = float(l.lat)
	l2 = float(l.lon)

	mydist = calc_dist(q1, q2, r1, r2) + calc_dist(s1, s2, r1, r2) + calc_dist(s1, s2, t1, t2) + calc_dist(u1, u2, t1, t2) + calc_dist(u1, u2, v1, v2) + calc_dist(w1, w2, v1, v2) + calc_dist(w1, w2, x1, x2) + calc_dist(x1, x2, y1, y2) + calc_dist(y1, y2, z1, z2) + calc_dist(a1, a2, z1, z2) + calc_dist(a1, a2, b1, b2) + calc_dist(c1, c2, b1, b2) + calc_dist(c1, c2, d1, d2) + calc_dist(e1, e2, d1, d2) + calc_dist(e1, e2, f1, f2) + calc_dist(g1, g2, f1, f2) + calc_dist(g1, g2, h1, h2) + calc_dist(i1, i2, h1, h2) + calc_dist(i1, i2, j1, j2) + calc_dist(k1, k2, j1, j2) + calc_dist(k1, k2, l1, l2) 
	fdist = round(mydist,2)
	return render(request, 'distsum/out.html', {'distance': fdist})