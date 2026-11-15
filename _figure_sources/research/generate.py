#!/usr/bin/env python3
"""Create conceptual research illustrations with the local VectorCraft CLI.

Run from any directory: python3 _figure_sources/research/generate.py
Native documents and SVGs are regenerated; no scientific data are represented.
"""
import json
import math
from pathlib import Path
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parent
OUTPUT = SOURCE.parents[1] / 'assets/img/research'
BG, INK, MUTED = '#f3f6f8', '#253c50', '#647687'
TEAL, PURPLE, GOLD, PALE = '#16746e', '#7453a4', '#b16b2e', '#dae5eb'


class Figure:
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.cmd('file.new', name=f'Research: {name}', width=720, height=360,
                 units='Points', colorMode='rgb', backgroundContents='white')
        self.rect(0, 0, 720, 360, BG)

    def cmd(self, command, **params):
        index = len(self.commands)
        self.commands.append({'command': command, 'params': params})
        return f'${index}.id'

    def paint(self, obj, fill=None, stroke=None, width=3):
        self.cmd('paint.setFill', id=obj, **({'color': fill} if fill else {'none': True}))
        self.cmd('paint.setStroke', id=obj, **({'color': stroke} if stroke else {'none': True}))
        if stroke:
            self.cmd('stroke.set', id=obj, weight=width, cap='round', join='round')
        return obj

    def text(self, x, y, text, size=25, color=INK, bold=False):
        obj = self.cmd('text.create', x=x, y=y, text=text, size=size,
                       font='Liberation Sans', style='Bold' if bold else 'Regular',
                       color=color, justify='center')
        self.cmd('paint.setStroke', id=obj, none=True)

    def line(self, x1, y1, x2, y2, color=MUTED, width=3, arrow=False):
        obj = self.paint(self.cmd('shape.line', x1=x1, y1=y1, x2=x2, y2=y2), stroke=color, width=width)
        if arrow:
            self.cmd('stroke.set', id=obj, endArrow='Triangle', arrowAlign='tip')
            self.cmd('stroke.setAdvanced', id=obj, arrowScale=[55, 55])

    def rect(self, x, y, w, h, fill=None, stroke=None, width=3):
        return self.paint(self.cmd('shape.rectangle', x=x, y=y, width=w, height=h), fill, stroke, width)

    def dot(self, x, y, r=9, fill=TEAL, stroke=None):
        return self.paint(self.cmd('shape.ellipse', x=x-r, y=y-r, width=2*r, height=2*r), fill, stroke)

    def path(self, points, color=TEAL, width=4, closed=False):
        return self.paint(self.cmd('path.create', anchors=[{'x':x,'y':y} for x,y in points], closed=closed),
                          stroke=color, width=width)

    def chain(self, points, color=TEAL, dots=True):
        self.path(points, color, 4)
        if dots:
            for x,y in points:
                self.dot(x,y,8,color)

    def save(self):
        OUTPUT.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='research-figures-') as tmp:
            commands = Path(tmp) / 'commands.json'
            commands.write_text(json.dumps(self.commands))
            result = subprocess.run(['vectorcraft-cli', '--safe-mode', 'run', '--commands', str(commands),
                                     '--export', str(SOURCE / f'{self.name}.vectorcraft'),
                                     '--export', str(OUTPUT / f'{self.name}.svg')],
                                    capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stderr + result.stdout[-3000:])
            for line in result.stdout.splitlines():
                record = json.loads(line)
                if record.get('error') or record.get('ok') is False:
                    raise RuntimeError(line)
            print(f'Created {self.name}')


f = Figure('polymers')
for x,label in [(122,'Chemistry'),(360,'Material'),(598,'Breakdown')]:
    f.text(x,55,label,bold=True)
f.chain([(42+i*26,180+(-1)**i*22) for i in range(7)])
f.line(231,180,257,180,arrow=True)
f.rect(280,105,160,150,stroke=PALE,width=2)
for j,col in enumerate([TEAL,PURPLE,GOLD,TEAL]):
    f.chain([(293+i*12,125+j*34+12*math.sin(i*.8+j)) for i in range(12)],col,False)
f.line(464,180,490,180,arrow=True)
f.chain([(530,145),(552,170),(578,150)],TEAL)
f.chain([(603,205),(630,179),(655,200)],PURPLE)
f.chain([(549,224),(576,240)],GOLD)
f.text(122,307,'Repeat units',22,MUTED)
f.text(360,307,'Many chains',22,MUTED)
f.text(598,307,'Smaller fragments',22,MUTED)
f.save()

f = Figure('simulation')
f.text(197,55,'Molecular environment',bold=True)
f.text(550,55,'Reaction path',bold=True)
for i in range(16):
    angle=i*math.tau/16
    x,y=197+125*math.cos(angle),184+95*math.sin(angle)
    f.dot(x,y,7,PALE)
    f.line(x,y,x+16*math.sin(angle),y+16*math.cos(angle),PALE,3)
f.dot(197,184,63,'#e3eeed',TEAL)
f.chain([(166,191),(190,164),(221,185)],TEAL)
f.dot(190,164,10,GOLD)
f.text(197,315,'Detailed reacting region',22,MUTED)
f.line(344,184,392,184,arrow=True)
pts=[(418+i*2.5,218-92*math.sin(math.pi*i/100)**2) for i in range(101)]
f.path(pts,PURPLE,5)
f.dot(418,218,10,TEAL)
f.dot(668,218,10,GOLD)
f.text(428,260,'Before',22,MUTED)
f.text(654,260,'After',22,MUTED)
f.text(550,315,'Connecting arrangements',22,MUTED)
f.save()

f = Figure('biochemistry')
f.text(180,55,'Reaction networks',bold=True)
f.text(530,55,'Protein structures',bold=True)
pts=[(67,190),(125,128),(143,230),(204,181),(238,105),(278,241),(304,158)]
for a,b in [(0,1),(0,2),(1,3),(2,3),(3,4),(3,5),(4,6),(5,6)]:
    f.line(*pts[a],*pts[b],MUTED,3)
for i,(x,y) in enumerate(pts):
    f.dot(x,y,13,[TEAL,PURPLE,GOLD][i%3])
f.chain([(426+i*27,123+(-1)**i*8) for i in range(9)],TEAL)
f.line(534,148,534,185,arrow=True)
curve=[(535+64*math.sin(t)*math.cos(t*.4),245+42*math.cos(t)) for t in [i*.09 for i in range(120)]]
f.path(curve,PURPLE,5)
f.text(180,320,'Connected chemistry',22,MUTED)
f.text(530,320,'Sequence and shape',22,MUTED)
f.save()

f = Figure('assembly')
for x,parts,product,step in [(124,'A + B','AB','1 join'),(360,'AB + C','ABC','2 joins'),(596,'ABC + ABC','ABCABC','3 joins')]:
    f.text(x,63,step,25,INK,True)
    f.text(x,128,parts,28,MUTED)
    f.line(x,150,x,187,arrow=True)
    width=len(product)*32
    for i,letter in enumerate(product):
        col={'A':TEAL,'B':PURPLE,'C':GOLD}[letter]
        f.rect(x-width/2+i*32,210,30,48,col)
        f.text(x-width/2+i*32+15,243,letter,25,'#ffffff',True)
f.text(360,320,'Build a fragment, then reuse it',25,INK)
f.save()

f = Figure('dna')
f.text(178,55,'A base pair',bold=True)
f.text(548,55,'A different pairing pattern',bold=True)
for x,proton_left in [(178,True),(548,False)]:
    f.rect(x-117,110,72,135,'#e3eeed',TEAL)
    f.rect(x+45,110,72,135,'#eae5f2',PURPLE)
    for yy in [147,207]:
        for xx in range(int(x-38),int(x+38),14):
            f.line(xx,yy,xx+5,yy,MUTED,2)
    f.dot(x-25 if proton_left else x+25,147,12,GOLD)
    f.text(x,289,'Proton on the left' if proton_left else 'Proton on the right',22,MUTED)
f.line(329,174,390,174,arrow=True)
f.text(360,335,'A small rearrangement can change hydrogen bonding',23,INK)
f.save()

f = Figure('surfaces')
f.text(180,55,'Motion at interfaces',bold=True)
f.text(548,55,'Light and materials',bold=True)
for row in range(3):
    for col in range(5):
        cx=72+col*42
        cy=195+row*19*math.sqrt(3)+(col%2)*19*math.sqrt(3)/2
        f.path([(cx+28*math.cos(i*math.pi/3),cy+19*math.sin(i*math.pi/3)) for i in range(6)],MUTED,2,True)
f.line(150,131,132,111,TEAL,5)
f.line(150,131,172,113,TEAL,5)
f.dot(150,131,14,PURPLE)
f.dot(132,111,8,TEAL)
f.dot(172,113,8,TEAL)
f.line(198,143,266,143,TEAL,4,True)
for x in [465,540,615]:
    f.path([(x,108),(x-12,132),(x+4,147),(x-10,176)],GOLD,4)
    f.line(x-10,176,x-17,191,GOLD,4,True)
for y,col in [(211,TEAL),(233,PURPLE),(255,MUTED)]:
    f.rect(435,y,230,18,col)
f.text(180,323,'Water on a surface',22,MUTED)
f.text(548,323,'Solar absorbers',22,MUTED)
f.save()
