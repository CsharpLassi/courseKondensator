# Übungsaufgaben

# Berechnung von Kapazitäten aus den Fertigungsmaße

1. Alumnium-Elektrolytkondensatoren werden oft, aufgrund ihrer hohen Kapazität, für die Spannungsstabilisierung eingesetzt. Aluminiumoxid besitzt eine relative Permittivität von $\epsilon_r = 9,6$. Berechnen Sie die Kapazität eines Alumnium-Elektrolytkondensatoren. ($A = 3 \text{mm}^2$ und $d= 1,4 \text{nm}$ )

   [] $2 \text{nF}$

   [x] $0,18 \mu\text{F}$

   [] $3 \text{mF}$

   

2. Ein Folienkondensator wird aus einer, mit Metall bedampften, Kunststofffolie hergestellt. Durch die Folie können nicht die Abstände erreicht werden, wie beim Elektrolytkondensatoren. Berechne Sie die Kapazität für einen Folienkondensator aus PET( $\epsilon_r = 3,3$, $A = 3 \text{mm}^2$ und $d= 700 \text{nm}$)

   [x] $0,125 \text{nF}$

   [x] $125 \text{pF}$

   [] $20 \text{nF}$

3. Berechnen Sie welche Fläche notwendig wäre, um ein Folienkondensator aus PET ($\epsilon_r = 3,3$) mit einer Kapazität von $1 \text{F}$. Der Abstand wieder $d= 700 \text{nm}$.

   [] ca. $1 \text{m}^2$

   [x] ca. $0,1 \text{km}^2$

   [] ca. $100 \text{m}^2$

# Berechnen von Ladungen

4. Ein Kondensator kann eine bestimmte Menge an Ladung in Abhängigkeit der Spannung halten. **Supercaps** gehören zu den Kondensatoren mit der größten Ladungsdichte. Nachteil sie können meisten nur Spannungen von wenigen Volt aushalten. Berechnen Sie die Ladung für ein Supercap mit $0,22 \text{F}$ und $5,5 \text{V}$.

   [] $1 \text{mC}$

   [x] $1,21 \text{C}$

   [] $0,99 \mu \text{C}$

5. Berechnen Sie Ladung für einen Alumnium-Elektrolytkondensatoren mit $0,18 \mu\text{F}$ und $5,5 \text{V}$.

   [] $1 \text{mC}$

   [] $1,21 \text{C}$

   [x] $0,99 \mu \text{C}$

# Kenngrößen vom RC-Glied

Die häufigste Anwendung eines Kondensators ist die Anwendung als Tiefpass. 

![Tiefpass](https://upload.wikimedia.org/wikipedia/commons/e/e8/Tiefpass.svg)

Von Fleshgrinder - Eigenes Werk, Gemeinfrei, https://commons.wikimedia.org/w/index.php?curid=8054477

6. Berechnen Sie von einem Tiefpass die Zeitkonstante $\tau$ für eine Kondensator mit der Kapazität von $220 \mu \text{F}$ und einem Widerstand von $100 \text{k}\Omega$.

   [] $2,2 \text{s}$

   [x] $22 \text{s}$

   [] $220 \text{ms}$

7. Die Zeitkonstante gibt ihnen an wie schnell ein Kondensator geladen wird. Nach wie vielen Zeiteinheiten ist der Kondensator voll geladen.

   [] $1\tau$

   [] $3\tau$

   [x] $5\tau$

In den nachfolgenden Aufgaben benötigen Sie folgendes Diagramm:

![Ladekurve](../Python/output/charge_curve.png)

8. Bestimmen Sie aus dem Diagramm die Zeitkonstante $\tau$.

   [x] $2 \text{s}$

   [] Die Konstante lässt sich nicht aus dem Diagramm ablesen

   [] $10 \text{s}$

10. Bestimmen Sie den Widerstand, wenn der Kondensator eine Kapazität von $220 \mu \text{F}$ hat.

    [x] ca. $10 \text{k}\Omega$

    [] ca. $4,7 \text{k}\Omega$

    [] Der Widerstandswert lässt sich nicht ermitteln.