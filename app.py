#import module
import streamlit as st

#Title
st.title("Tugas Project Pemrograman Fungsional")
st.markdown("""Anggota :""")
st.markdown(":blue[Latifah Nurrohmah       (21102124)]:girl:")
st.markdown(":blue[Kelvin Fauzian Setiawan (21102127)]:boy:")
st.markdown(":blue[Dimas Teguh Ramadhani   (21102145)]:boy:") 
st.markdown(":blue[Septya Andini Putri     (21102177)]:girl:")
st.header("Itertools")
st.text("""Modul itertools adalah library standar yang mengandung beberapa fungsi
yang berguna dalam pemrograman fungsional. fungsinya untuk membantu bekerja 
dengan iterables berulang. """)
st.text("""Itertools terbagi menjadi 2 yaitu
- Using infinite iterators yang meliputi
  - count()
  - cycle()
  - repeat()
- Using the finite iterators yang meliputi
  - accumulate()
  - chain()
  - compress()
  - combinations()
  - permutations()
  - groupby()""")

st.header("Dibawah ini adalah contoh beberapa studi kasus yang menggunakan fungsi fungsi dari itertools")

## Count

st.subheader("Using Infinite Iterators - count()")
st.text("")
#code block
code ='''import itertools

# Studi kasus: Menghitung berapa banyak uang yang diperlukan untuk membeli mainan
prices = [5, 10, 15, 20, 25]
budget = 100

# fungsi itertools
toys = itertools.count(1)

# money spent di set dari 0
money_spent = 0

# fungsi agar budget mainan sampai mendekati cukup
for price in prices:
    if money_spent + price > budget:
        break
    money_spent += price
    print(f"Beli mainan ke-{next(toys)} seharga {price}, Total belanja: {money_spent}")

# Output mainan yang dibeli dan jumlah uang tersisa
print(f"Jumlah mainan yang dibeli: {next(toys) - 1}")
print(f"Sisa uang: {budget - money_spent}")'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''Beli mainan ke-1 seharga 5, Total belanja: 5
Beli mainan ke-2 seharga 10, Total belanja: 15
Beli mainan ke-3 seharga 15, Total belanja: 30
Beli mainan ke-4 seharga 20, Total belanja: 50
Jumlah mainan yang dibeli: 4
Sisa uang: 50'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus yang menghitung berapa banyak uang yang diperlukan untuk membeli mainan. tools :green[_itertools.count(1)_] digunakan untuk menghitung berapa banyak mainan yang dapat dibeli, dengan meng-generate count infinit dari mainan yang dapat dibeli.")

## Cycle

st.subheader("Using Infinite Iterators - cycle()")
#Code Block
code ='''import itertools
import time

# Studi kasus: Menunjukkan angka secara berulang dari 1 sampai 4
numbers = [1, 2, 3, 4]

# Menggunakan itertools.cycle() untuk menunjukkan angka secara berulang
for number in itertools.cycle(numbers):
    print(number)
    time.sleep(1)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''1
2
3
4
1
2
3
4
...'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus yang menunjukkan angka secara berulang dari 1 sampai 4 tanpa henti sejauh program berjalan. tools :green[_itertools.cycle()_] digunakan untuk menunjukkan angka secara berulang.")

## Repeat

st.subheader("Using Infinite Iterators - repeat()")
#Code Block
code ='''import itertools

# Studi kasus: Mencetak 10 kali "Selamat Datang"
for i in itertools.repeat("Selamat Datang", 10):
    print(i)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang
Selamat Datang'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus mencetak 'Selamat Datang' sebanyak 10 kali. tools :green[_itertools.repeat()_] digunakan untuk mengulang kata sebanyak x kali")

## accumulate

st.subheader("Using Finite Iterators - accumulate()")

#code block
code ='''import itertools

# Studi kasus: Mencari jumlah acak dari angka 1 sampai 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mencari jumlah acak dari angka
cumulative_sum = list(itertools.accumulate(numbers))
print(cumulative_sum)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus menggunakan :green[_itertools.accumulate()_] untuk mencari jumlah acak dari angka dengan paramater 1-10.")

## chain

st.subheader("Using Finite Iterators - chain()")

#code block
code ='''import itertools

# Studi kasus: Menggabungkan beberapa daftar angka menjadi satu daftar
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
numbers3 = [9, 10, 11, 12]

# Menggabungkan beberapa daftar menjadi satu daftar
combined_numbers = list(itertools.chain(numbers1, numbers2, numbers3))
print(combined_numbers)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus menggabungkan beberapa daftar angka menjadi satu daftar dengan menggunakan tools :green[_itertools.chain()_]")

## compress

st.subheader("Using Finite Iterators - compress()")

#code block
code ='''import itertools

# Studi kasus: Mencari nama hari yang hari libur kelas N ITTP semester 3
days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
weekends = [False, False, False, False, True, True, True]

# Menggunakan itertools.compress() untuk mencari nama hari libur
holidays = list(itertools.compress(days_of_week, weekends))

# Menampilkan nama hari libur
print("Hari libur:", holidays)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''Hari libur: ['Jumat', 'Sabtu', 'Minggu']'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus mencari nama hari libur, dengan menggunakan :green[_itertools.compress()_] untuk mencari nama hari libur pada variabel days_of_week")

## Combinations

st.subheader("Using Finite Iterators - Combinations()")

#Code Block
code ='''#import module
import itertools
# Studi kasus: Mencari kombinasi makanan yang bisa dipesan dari daftar menu restoran
menu = ['Pizza', 'Burger', 'Fried Rice', 'Spaghetti']
prices = [15000, 10000, 12000, 11000]
max_price = 28000
# Mencari semua kombinasi makanan yang memenuhi harga maksimal
for combo in itertools.combinations(menu, 3):
    if sum(prices[menu.index(x)] for x in combo) <= max_price:
        print(combo)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''('Pizza', 'Burger', 'Fried Rice')
('Pizza', 'Burger', 'Spaghetti')
('Pizza', 'Fried Rice', 'Spaghetti')
('Burger', 'Fried Rice', 'Spaghetti')'''
st.code(code, language='python')

st.markdown("""Program diatas adalah contoh studi kasus yang menggunakan itertools.combinations()
untuk mencari kombinasi makanan dari daftar menu restoran yang memenuhi harga maksimal suatu pesanan.
Tools :green[_itertools.combinations(menu, 3)_] digunakan untuk mencari semua kombinasi 
makanan dari daftar menu yang terdiri dari 3 item. Jika harga total kombinasi tersebut lebih kecil atau sama dengan harga maksimal,
maka kombinasi tersebut akan dicetak.""")

## permutations

st.subheader("Using Finite Iterators - permutations()")

#code block
code ='''import itertools

# Studi kasus: Mencari semua permutasi angka dari 1 sampai 4
numbers = [1, 2, 3, 4]

# Mencari semua permutasi angka
for perm in itertools.permutations(numbers):
    print(perm)'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)
(1, 3, 4, 2)
(1, 4, 2, 3)
(1, 4, 3, 2)
(2, 1, 3, 4)
(2, 1, 4, 3)
(2, 3, 1, 4)
(2, 3, 4, 1)
(2, 4, 1, 3)
(2, 4, 3, 1)
(3, 1, 2, 4)
(3, 1, 4, 2)
(3, 2, 1, 4)
(3, 2, 4, 1)
(3, 4, 1, 2)
(3, 4, 2, 1)
(4, 1, 2, 3)
(4, 1, 3, 2)
(4, 2, 1, 3)
(4, 2, 3, 1)
(4, 3, 1, 2)
(4, 3, 2, 1)'''
st.code(code, language='python')

st.markdown("Program diatas adalah contoh studi kasus mencari semua permutasi angka dari 1 sampai 4 dengan :green[_itertools.permutations_]")

## groupby

st.subheader("Using Finite Iterators - groupby()")

#code block
code ='''import itertools

# Studi kasus: Menghitung berapa banyak kemunculan tiap huruf dalam sebuah kalimat
sentence = "supercalifragilisticexpialidocious"

# Menghitung berapa banyak kemunculan tiap huruf
sorted_sentence = sorted(sentence)
result = [(letter, len(list(group))) for letter, group in itertools.groupby(sorted_sentence)]

# Menampilkan hasil
for letter, count in result:
    print(f"Huruf '{letter}' muncul sebanyak {count} kali")'''
st.code(code, language='python')

st.text("Maka output yang akan dihasilkan menjadi")
code ='''Huruf 'a' muncul sebanyak 4 kali
Huruf 'c' muncul sebanyak 4 kali
Huruf 'd' muncul sebanyak 2 kali
Huruf 'e' muncul sebanyak 1 kali
Huruf 'f' muncul sebanyak 1 kali
Huruf 'g' muncul sebanyak 2 kali
Huruf 'i' muncul sebanyak 7 kali
Huruf 'l' muncul sebanyak 4 kali
Huruf 'o' muncul sebanyak 2 kali
Huruf 'p' muncul sebanyak 2 kali
Huruf 'r' muncul sebanyak 2 kali
Huruf 's' muncul sebanyak 2 kali
Huruf 't' muncul sebanyak 2 kali
Huruf 'u' muncul sebanyak 2 kali
Huruf 'x' muncul sebanyak 2 kali'''
st.code(code, language='python')

st.markdown("Program ini adalah contoh studi kasus menghitung berapa banyak kemunculan tiap huruf dalam sebuah kalimat. dengan menggunakan sorted() untuk mengurutkan huruf dalam kalimat dan :green[_itertools.groupby()_] untuk mengelompokkan huruf yang sama pada studi kasus diatas.")

