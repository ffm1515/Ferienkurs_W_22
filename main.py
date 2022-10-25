from browser import document, window, alert
import random 
 
def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)
  
  def setup():
    p.createCanvas(450,400)
    p.background(0,255,255)
    p.rectMode(p.CENTER)

    # Die >fill<Methode gibt an, welche Farbe fortan zum 
    # Zeichnen verwendet wird.
    # Als Parameter werden RGB-Werte übergeben oder 1 Parameter 
    # für den Grauten.
    # RGB-Werte sind auf >farb-tabelle.de< zu finden.
    p.fill(30,144,255)
    p.circle(210,160,50)
    p.fill(191,239,255)
    p.rect(210, 160, 120, 40)
    p.fill(64,224,208)
    p.circle(210,160,30)
    p.rect(210,160,100,20)
    p.circle(210,160,20)
    p.rect(210,160,10)
    p.textSize(50)
    p.fill(1)
    p.text('Willkommen!!!', 70, 250)
    
  p.setup = setup
    
myp5 = window.p5.new(sketch)
