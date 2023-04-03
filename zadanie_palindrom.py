
#funkcja sprawdzająca ,czy dane słowo jest palindromem 
def fPalindrom(x):
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        if x[i] != x[n-1-i]: #jezeli znak po przeciwnej stronie (w tej samej kolejnosci od konca) nie bedzie taki sam
            return False #zwroc false
    return True; #jezeli nie napotkano problemow, zwroc true
polindrom = "kajak"
print("kajak " + ("jest " if(fPalindrom(polindrom)) else "nie jest ") + "palindromem")