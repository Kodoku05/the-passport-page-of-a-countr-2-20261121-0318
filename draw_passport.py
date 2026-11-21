"""Deterministic, offline passport artwork. Pillow is needed only to rebuild."""
from PIL import Image, ImageDraw, ImageFont
import math, random, hashlib, json
from pathlib import Path
S=3
W=H=1024
im=Image.new('RGB',(W*S,H*S),'#d7d4cc')
d=ImageDraw.Draw(im)
NAVY='#263f4a'; INK='#283e45'; MUTED='#697b7e'; PAPER='#f2eee2'; TEAL='#365f60'
FONT='/usr/share/fonts/truetype/dejavu/'
def font(n,kind='sans'):
    names={'sans':'DejaVuSans.ttf','bold':'DejaVuSans-Bold.ttf','serif':'DejaVuSerif.ttf','mono':'DejaVuSansMono.ttf'}
    return ImageFont.truetype(FONT+names[kind],round(n*S))
def text(x,y,s,n=12,kind='sans',fill=INK,anchor=None):
    d.text((x*S,y*S),s,font=font(n,kind),fill=fill,anchor=anchor,stroke_width=0)
def line(coords,fill=INK,width=1): d.line([(int(x*S),int(y*S)) for x,y in coords],fill=fill,width=max(1,int(width*S)))
def rect(box,fill=None,outline=None,width=1,r=0):
    b=tuple(int(v*S) for v in box)
    if r:d.rounded_rectangle(b,radius=int(r*S),fill=fill,outline=outline,width=int(width*S))
    else:d.rectangle(b,fill=fill,outline=outline,width=int(width*S))
def ellipse(box,fill,outline=None,width=1): d.ellipse(tuple(int(v*S) for v in box),fill=fill,outline=outline,width=int(width*S))
def poly(points,fill):d.polygon([(int(x*S),int(y*S)) for x,y in points],fill=fill)
# A closed, neutral surface and the real thickness of a small booklet.
for i in range(20,0,-1): rect((25-i*.5,133-i*.2,999+i*.5,894+i*.8),fill=(199+i//3,197+i//3,190+i//3),r=18)
rect((22,130,1001,894),fill='#203a47',r=17)
for i in range(5):rect((30+i,138+i*2,994-i,883-i*2),fill='#d6d2c5',outline='#bdbfaf',r=12)
rect((36,145,511,875),fill=PAPER,r=10)
rect((513,145,988,875),fill='#f1ecdf',r=10)
# Fine security waves, clipped to the printed area; no attention-grabbing ornament.
for left,right in [(48,500),(526,976)]:
    for row in range(154,866,9):
        pts=[(x,row+3*math.sin(x*.05+row*.08)+1.5*math.sin(x*.13)) for x in range(left,right+1,2)]
        line(pts,fill='#e4e3d5',width=.38)
# Translucent binding shadow, with stitches.
for x in range(493,530):
    v=int(237-30*math.exp(-((x-512)/7)**2))
    line([(x,151),(x,868)],fill=(v,v-3,v-13),width=1)
for y in range(180,860,52):line([(511,y),(511,y+12)],fill='#a4a99f',width=.65)
# Small state device: an island, three seas, a navigational star.
cx=274
poly([(cx,170),(cx+19,177),(cx+17,199),(cx,211),(cx-17,199),(cx-19,177)],NAVY)
poly([(cx,176),(cx+2,183),(cx+8,185),(cx+2,187),(cx,193),(cx-2,187),(cx-8,185),(cx-2,183)],PAPER)
for yy in (196,200):line([(cx-10,yy),(cx-5,yy-1),(cx,yy+1),(cx+5,yy-1),(cx+10,yy)],PAPER,.7)
text(274,222,'REPUBLIC OF KALVERRA',21,'serif',anchor='mt')
text(274,254,'PASSPORT / PASSEPORT',15,'bold',anchor='mt')
line([(59,286),(487,286)],MUTED,.7)
text(61,296,'Type / Type',8,fill=MUTED);text(61,310,'P',12,'bold')
text(172,296,'Code / Code',8,fill=MUTED);text(172,310,'KAL',12,'bold')
text(318,296,'Passport no. / N° de passeport',8,fill=MUTED);text(318,310,'KA0047281',13,'bold')
# Duotone engraved document portrait, drawn entirely from geometric shapes.
rect((61,341,218,554),fill='#d9e1de',outline='#94a8a6',width=.7,r=3)
for yy in range(345,554,5):line([(64,yy),(215,yy)],'#c4d1cf',.35)
# Shoulders, wool jacket, shirt, neck, ears, and angular face planes.
poly([(65,554),(69,514),(94,500),(116,490),(161,490),(187,505),(214,523),(215,554)],'#536c73')
poly([(101,498),(124,486),(155,488),(176,503),(158,554),(117,554)],'#a5b6b6')
poly([(122,468),(121,494),(139,510),(158,490),(156,461)],'#8b9f9f')
poly([(119,491),(137,509),(119,524),(107,499)],'#d3ded9')
poly([(159,491),(138,509),(158,524),(174,500)],'#c4d2cd')
poly([(138,509),(145,521),(141,554),(132,554),(132,520)],'#3d5963')
poly([(98,500),(114,514),(106,531),(119,554),(91,554)],'#3f5b66')
poly([(179,502),(164,515),(170,532),(158,554),(191,554)],'#405d67')
ellipse((100,405,114,441),'#95a9a7');ellipse((165,405,177,441),'#8b9f9e')
poly([(109,380),(122,364),(150,364),(166,381),(170,416),(163,454),(153,474),(137,482),(121,473),(110,454),(105,417)],'#b7c6c1')
poly([(148,382),(164,388),(165,422),(156,441),(160,456),(147,474),(137,480),(155,473),(166,448),(171,413),(164,381)],'#8ca3a3')
poly([(113,413),(118,438),(127,451),(122,463),(112,449),(107,425)],'#a0b3af')
# Hair: graying, combed to one side, no cartoon outlines.
poly([(105,418),(101,400),(104,380),(112,366),(131,358),(155,361),(170,375),(175,398),(169,421),(162,398),(160,383),(148,382),(135,387),(118,385),(112,398),(112,419)],'#516b73')
for i in range(13):line([(108+i*4,378+(i%3)),(121+i*3.4,367+(i%4)),(145+i*1.4,369+i*.7)],'#94a8a9',.6)
# Brow, eyes, cheekbones, nose and natural mouth.
line([(115,410),(123,407),(130,409)],'#506870',1.2)
line([(145,409),(153,407),(161,410)],'#506870',1.2)
line([(116,416),(122,414),(128,416)],'#526b71',.8)
line([(146,416),(152,414),(159,416)],'#526b71',.8)
ellipse((121,414,123,417),'#344e59');ellipse((151,414,153,417),'#344e59')
line([(138,414),(134,435),(139,439),(144,437)],'#718c91',.8)
line([(125,451),(135,449),(142,450),(151,449)],'#6c8589',.85)
line([(132,455),(144,455)],'#94aaa9',.7)
line([(119,430),(125,433)],'#8ca3a3',.6)
# Fine engraved modeling on the shadow side, cheek and forehead.
for yy in range(390,407,3):
    line([(151,yy),(160,yy+2)],'#9eafad',.35)
for yy in range(422,443,2):
    line([(154,yy),(163-(yy-422)*.15,yy+2)],'#8da4a4',.4)
for yy in range(447,468,3):
    line([(115+(yy-447)*.25,yy),(122+(yy-447)*.2,yy+2)],'#9aafaa',.4)
for yy in range(441,473,3):
    line([(155-(yy-441)*.14,yy),(162-(yy-441)*.34,yy-2)],'#7e989c',.45)
for yy in range(523,552,3):
    line([(75,yy),(101,yy-10)],'#81989d',.45)
    line([(183,yy),(207,yy-8)],'#82999d',.45)
text(139,539,'K A L',7,'mono',fill='#d5e1db',anchor='mt')
# Biographical hierarchy: small bilingual labels, uniform value baselines.
def field(x,y,label,value,n=12):
    text(x,y,label,8,fill=MUTED);text(x,y+14,value,n,'bold')
field(234,340,'Surname / Nom','SOLBERG',15)
field(234,389,'Given names / Prénoms','EIRIK',15)
field(234,438,'Nationality / Nationalité','KALVERRAN',12)
field(234,487,'Date of birth / Date de naissance','02 JUN 1988',12)
field(61,570,'Place of birth / Lieu de naissance','PORT ANSELM',12)
field(358,570,'Sex / Sexe','M',12)
field(61,619,'Date of issue / Date de délivrance','14 MAR 2024',12)
field(292,619,'Date of expiry / Date d’expiration','14 MAR 2034',12)
field(61,669,'Authority / Autorité','PASSPORT OFFICE · PORT ANSELM',11)
text(61,718,'Holder’s signature / Signature du titulaire',8,fill=MUTED)
# Restrained handwritten signature, not a typographic faux-script.
line([(255,746),(264,729),(261,747),(276,734),(269,745),(285,742),(291,731),(286,746),(304,741),(312,730),(308,744),(324,737),(337,741),(353,732),(347,744),(370,738)],'#5a6970',.9)
line([(61,762),(487,762)],MUTED,.7)
# ICAO TD3 check digits, including the composite digit.
def cd(s):
    def val(c):return 0 if c=='<' else int(c) if c.isdigit() else ord(c)-55
    return str(sum(val(c)*[7,3,1][i%3] for i,c in enumerate(s))%10)
number='KA0047281';birth='880602';expiry='340314';personal='<'*14
mrz1=('P<KAL'+'SOLBERG<<EIRIK').ljust(44,'<')
mrz2=number+cd(number)+'KAL'+birth+cd(birth)+'M'+expiry+cd(expiry)+personal+cd(personal)
mrz2+=cd(mrz2[:10]+mrz2[13:20]+mrz2[21:43])
assert len(mrz1)==len(mrz2)==44
rect((52,778,496,846),fill='#eee9da')
text(60,788,mrz1,15.7,'mono');text(60,815,mrz2,15.7,'mono')
text(61,857,'KAL / P / 2024',7,'mono',fill=MUTED)
text(482,857,'02',8,'mono',fill=MUTED,anchor='rt')
# Visa page. The page number and document number repeat as security printing.
text(752,180,'VISAS / VISAS',18,'serif',anchor='mt')
line([(542,213),(962,213)],MUTED,.6)
text(543,224,'KA0047281',9,'mono',fill=MUTED)
text(960,224,'03',10,'mono',fill=MUTED,anchor='rt')
# Stamps are separate raster plates so their rotations never disturb the grid.
def stamp(x,y,country,port,date,action,angle=0):
    plate=Image.new('RGBA',(205*S,132*S),(0,0,0,0));p=ImageDraw.Draw(plate)
    col=(57,91,93,235)
    p.rounded_rectangle((5*S,5*S,200*S,127*S),radius=6*S,outline=col,width=2*S)
    p.rounded_rectangle((9*S,9*S,196*S,123*S),radius=3*S,outline=col,width=1*S)
    def st(yy,s,n,kind='sans'):p.text((102*S,yy*S),s,font=font(n,kind),fill=col,anchor='mt')
    st(17,country,13,'bold');st(39,port,9)
    p.line((18*S,58*S,187*S,58*S),fill=col,width=S)
    st(64,date,18,'mono');st(96,action+'  ·  SEA  /  01',9,'bold')
    plate=plate.rotate(angle,Image.Resampling.BICUBIC,expand=True)
    im.paste(plate,(round((x+102)*S-plate.width/2),round((y+66)*S-plate.height/2)),plate)
stamp(541,273,'ÍSLAND / ICELAND','SEYÐISFJÖRÐUR','06 JUN 2024','ENTRY',-3)
stamp(755,291,'ÍSLAND / ICELAND','SEYÐISFJÖRÐUR','14 JUN 2024','EXIT',3)
stamp(541,446,'NORGE / NORWAY','BERGEN','03 SEP 2025','ENTRY',2)
stamp(755,463,'NORGE / NORWAY','BERGEN','12 SEP 2025','EXIT',-3)
# Official domestic maritime endorsement: geographic character in ordinary paperwork.
rect((547,642,959,820),fill='#e2e4d8',outline='#829996',width=.8,r=2)
rect((547,642,959,671),fill='#506d70',r=1)
text(559,650,'KALVERRA · MARITIME ENDORSEMENT',10,'bold',fill='#f1f0df')
text(559,684,'No. M / 240314 / 7281',10,'mono')
text(559,706,'On return by sea, the holder must register',10)
text(559,722,'with the harbourmaster within 48 hours.',10)
text(559,738,'Fishing vessel crews may register aboard.',10,'bold')
line([(559,760),(946,760)],'#9aa9a1',.6)
text(559,770,'Issued: Port Anselm · 14 MAR 2024',9)
text(559,787,'Valid to: 14 MAR 2034 · Passport KA0047281',9)
# Paid fee handstamp alongside page footer, subordinate to travel stamps.
text(548,840,'PAID 400 KR · CONSULAR FEE',9,'mono',fill=TEAL)
text(548,858,'PASSPORT OFFICE / PORT ANSELM',7,'sans',fill=MUTED)
text(960,858,'03',8,'mono',fill=MUTED,anchor='rt')
# Subpixel paper grain is deterministic and deliberately barely visible.
im=im.resize((1024,1024),Image.Resampling.LANCZOS)
rng=random.Random(7281)
pixels=im.load()
for yy in range(146,875):
    for xx in range(37,988):
        if 500<xx<525:continue
        delta=rng.choice((-1,0,0,0,1))
        if delta:pixels[xx,yy]=tuple(max(0,min(255,c+delta)) for c in pixels[xx,yy])
im.save('entry.png',optimize=True)
print(json.dumps({'mrz':[mrz1,mrz2],'size':Path('entry.png').stat().st_size,'sha256':hashlib.sha256(Path('entry.png').read_bytes()).hexdigest()},indent=2))
