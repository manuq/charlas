from __future__ import unicode_literals
from collections import namedtuple
import csv

# Cosas para graficos
import matplotlib.pyplot as plt

Respuesta = namedtuple('Respuesta', [
    'timestamp',
    'edad_laboral',
    'floss',
    'floss_leader',
    'ocupado',
    'ocupado_por_floss',
    'edad_floss',
    'contrata',
    'contrata_por_floss'])

r = []
with open('respuestas.csv', 'r') as fd:
    reader = csv.reader(fd)
    resultados = [Respuesta(
        x[0],
        int(x[1]) if x[1] else 0,
        x[2]=='Si',
        x[3]=='Si' and x[2]=='Si',  # Corregir para lideres que no hacen FLOSS porque FOO
        x[4]=='Si',
        x[5]=='Si',
        int(x[6]) if x[6] else 0,
        x[7]=='Si',
        x[8]=='Si',
        ) for x in list(reader)[1:]]

print "Respuestas:", len(resultados)
c_floss = len([x for x in resultados if x.floss])
print "Gente que esta en FLOSS:", c_floss
c_no_floss = len([x for x in resultados if not x.floss])
print "Gente que no esta en FLOSS:", c_no_floss
c_lider = len([x for x in resultados if x.floss_leader])
print "Gente que lidera FLOSS:", c_lider

print "--------------"

print "Gente con trabajo:", len([x for x in resultados if x.ocupado])
print "Gente sin trabajo:", len([x for x in resultados if not x.ocupado])

c_ocup_no_floss = len([x for x in resultados if x.ocupado and not x.floss])
print "Porcentaje de ocupacion en no FLOSS: %.2f%%" % ((100.*c_ocup_no_floss)/c_no_floss)

c_ocup_floss = len([x for x in resultados if x.ocupado and x.floss])
print "Porcentaje de ocupacion en FLOSS: %.2f%%" % ((100.*c_ocup_floss)/c_floss)

c_ocup_lider = len([x for x in resultados if x.ocupado and x.floss_leader])
print "Porcentaje de ocupacion en lideres FLOSS: %.2f%%" % ((100.*c_ocup_lider)/c_lider)

print "--------------"

#x1 = [x.edad_laboral for x in resultados if not x.floss]
#x2 = [x.edad_laboral for x in resultados if x.floss]
#x3 = [x.edad_laboral for x in resultados if x.floss_leader]
#plt.hist([x1, x2, x3], normed=1, range=(0,25))
#plt.hist([x.edad_floss for x in resultados if x.floss], normed=1, facecolor='b', alpha=.5)
#plt.hist(, normed=1, facecolor='r', alpha=.2, range=(0,25))
#plt.xlabel('Edad Laboral')
#plt.title('Hace cuanto trabaja la gente? [no-floss/floss/lideres]')
#plt.show()

print "Cuando contratas te sirve si el candidato hace FLOSS?"
print "SI:", len([x for x in resultados if x.contrata_por_floss])
print "NO:", len([x for x in resultados if not x.contrata_por_floss])

print "EPA"

print "Claro, no todo el mundo contrata :-)"
print "Cuantos contratan?"
print len([x for x in resultados if x.contrata])
print "Cuando contratas (si lo haces) te sirve si el candidato hace FLOSS?"
c1 = len([x for x in resultados if x.contrata and x.contrata_por_floss])
c2 = len([x for x in resultados if x.contrata and not x.contrata_por_floss])
print "SI:", c1, "%.2f%%" % (100.*c1/(c2+c1))
print "NO:", c2, "%.2f%%" % (100.*c2/(c2+c1))

print "EPA!"

print "Cuando contratas te sirve si el candidato hace FLOSS aunque hayas dicho que no contratas?"
print "SI:", len([x for x in resultados if not x.contrata and x.contrata_por_floss])

print "Si contratas y haces FLOSS, te sirve que el candidato haga FLOSS?"
c1 = len([x for x in resultados if x.contrata and x.contrata_por_floss and x.floss])
c2 = len([x for x in resultados if x.contrata and not x.contrata_por_floss and x.floss])
print "SI:", c1, "%.2f%%" % (100.*c1/(c2+c1))
print "NO:", c2, "%.2f%%" % (100.*c2/(c2+c1))

print "Si contratas y NO haces FLOSS, te sirve que el candidato haga FLOSS?"
c1 = len([x for x in resultados if x.contrata and x.contrata_por_floss and not x.floss])
c2 = len([x for x in resultados if x.contrata and not x.contrata_por_floss and not x.floss])
print "SI:", c1, "%.2f%%" % (100.*c1/(c2+c1))
print "NO:", c2, "%.2f%%" % (100.*c2/(c2+c1))


print "Per jodere nomas... cuantos de los lideres de proyectos FLOSS contratan otra gente?"
c1 = len([x for x in resultados if x.contrata and x.contrata_por_floss and x.floss_leader])
c2 = len([x for x in resultados if x.contrata and not x.contrata_por_floss and x.floss_leader])
print c1, "de", c1+c2, "%.2f%%" % (100.*c1/(c2+c1))

c1 = len([x for x in resultados if x.contrata])
c2 = len([x for x in resultados if not x.contrata])
print "Comparado con %.2f%% del total de la encuesta" % (100.*c1/(c2+c1)),
c1 = len([x for x in resultados if x.floss])
c2 = len([x for x in resultados if not x.floss])
print "y %.2f%% de los que hacen FLOSS" % (100.*c1/(c2+c1))
