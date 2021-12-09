Link do repozytorium Github: https://github.com/GabrielaWielgus/Warcaby.git

Opis zadania:

- Okno z siatką przysicków 8x8 oraz przyciskiem do resetowania gry.
- Przyciski reprezentując pola plaszy do gry w warcaby. Pola z pionkami gracza 2 -
  przycisk z tekstem "B". Damki oznaczane są dodatkową literą d("Cd", "Bd").
- Nad planszą wyświetlana jest informacja "Tura gracza 1" lub "Tura gracza 2".
- Gracz wybiera pionka (tekst pola zmienia się z "C" na "[C]" lub z "B" na "[B]", a
  potem pole na które chce wykonać ruch. Jeśli ruch jest dozwolony, pionek jest przestawiany,
  jeśli nie to wyświtlany jest komunikat "ruch niedozwolony".
- Zasady jak w warcabach, dowolny wariant. Zwykłe pionki i damki mają być obiekatami dwóch
  różnych klas dziedziczących po klasie Pionek.
- Gdy gra się kończy, wyświetlane jest okienko z napisem "Wygrał gracz 1" lub "Wygrał gracz 2",
  zależnie kto wygrał grę. Możliwe jest zresetowanie planszy bez zamykania głownego okna.

Testy:

1. Wykonanie po dwa ruchy przez każdego z graczy.
2. Niepowodzenie błędnego ruchu pionkiem.
3. Wykonanie bicia pojedynczego pionka.
4. Wykonanie bicia przynajmniej dwóch pionków.
5. Zamiana pionka w damkę.
6. Bicie damką.
7. Wygrana gracza grającego czarnymi pionkami.
8. Rozpoczęcie nowej gry po zwycięstwie jednego z graczy.

Wskazane jest przygotowanie specjalnych początkowych rozstawień pionków dla testów 
d,e,f,g,h. (4,5,6,7,8)