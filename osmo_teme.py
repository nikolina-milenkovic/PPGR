import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backend_bases import PickEvent

tacke = []

def onclick(event):
  global tacke
  if len(tacke) < 7:
    if event.xdata is not None and event.ydata is not None:
      x, y = event.xdata, event.ydata
      tacke.append([int(x), int(y),1])
      if len(tacke) == 7:
        print(f"Odabrane su tacke: {tacke}")
        fig.canvas.mpl_disconnect(cid)



img = mpimg.imread('rubikova_kocka_temena.jpg')

fig, ax = plt.subplots()
ax.imshow(img)
plt.title("Odaberite redom 7 tacaka (preskocite br. 4)")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()


def afinize(teme):
  if teme[2] == 0:
    raise ValueError("Poslednja koordinata je nula.") 
  return [teme[0]/teme[2], teme[1]/teme[2], 1]

def osmoteme(tacka):
  P1 = tacke[0]
  P2 = tacke[1]
  P3 = tacke[2]
  P5 = tacke[3]
  P6 = tacke[4]
  P7 = tacke[5]
  P8 = tacke[6]

  Xb1 = np.array(afinize(np.cross(np.cross(P2, P6), np.cross(P1, P5))))
  Xb2 = np.array(afinize(np.cross(np.cross(P2, P6), np.cross(P7, P3))))
  Xb3 = np.array(afinize(np.cross(np.cross(P7, P3), np.cross(P5, P1))))

  Xb = [(Xb1[0] + Xb2[0] + Xb3[0])/3, (Xb1[1] + Xb2[1] + Xb3[1])/3, (Xb1[2] + Xb2[2] + Xb3[2])/3]

  Yb1 = np.array(afinize(np.cross(np.cross(P2, P1), np.cross(P6, P5))))
  Yb2 = np.array(afinize(np.cross(np.cross(P2, P1), np.cross(P7, P8))))
  Yb3 = np.array(afinize(np.cross(np.cross(P7, P8), np.cross(P6, P5))))

  Yb = [(Yb1[0] + Yb2[0] + Yb3[0])/3, (Yb1[1] + Yb2[1] + Yb3[1])/3, (Yb1[2] + Yb2[2] + Yb3[2])/3]

  Zb1 = np.array(afinize(np.cross(np.cross(P6, P7), np.cross(P2, P3))))
  Zb2 = np.array(afinize(np.cross(np.cross(P6, P7), np.cross(P5, P8))))
  Zb3 = np.array(afinize(np.cross(np.cross(P2, P3), np.cross(P5, P8))))

  Zb = [(Zb1[0] + Zb2[0] + Zb3[0])/3, (Zb1[1] + Zb2[1] + Zb3[1])/3, (Zb1[2] + Zb2[2] + Zb3[2])/3]

  p41 = np.array(afinize(np.cross(np.cross(Xb, P8), np.cross(Yb, P3))))
  p42 = np.array(afinize(np.cross(np.cross(Xb, P8), np.cross(Zb, P1))))
  p43 = np.array(afinize(np.cross(np.cross(Yb, P3), np.cross(Zb, P1))))

  P4 = np.array([(p41[0] + p42[0] + p43[0])/3, (p41[1] + p42[1] + p43[1])/3, (p41[2] + p42[2] + p43[2])/3])

  return np.round(P4).astype(int)

print(osmoteme(tacke))