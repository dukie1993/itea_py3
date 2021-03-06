'''
Створити міні блог програму. Тобто запускаючи програму, 
користувачі можуть перечитувати статті. В програмі користувач може 
мати одну з таких ролей: EDITOR, VISITOR, ADMIN. Якщо користувач має 
роль VISITOR, то він може тільки читати статті. Якщо він має роль EDITOR, 
то він може додавати і читати статті. Якщо користувач ADMIN, то він може робити 
все, що йому заманеться. В програмі повинен бути як мінімум один декоратор, 
замикання. Розбити програму на модулі. Наприклад можна створити модуль actions, 
де будуть розміщені функції, які наприклад створюватимуть статті, чи показуватимуть 
їх. Можна створити модуль auth, в якому визначатиметься роль користувача під час запуску 
програми. Можна створити модуль utils, в якому будуть якісь допоміжні функції, що 
використовуватимуться в декількох модулях.
Всі статті зберігати у файлах у форматі json. Для файлів можна створити окрему папку media. 
Створити функціонал, за допомогою якого адмін зможе додавати нових користувачів. 
Тобто він може створювати нові паролі і нові імена користувачів, і записувати їх у файл. 
І коли новий користувач буде запускати програму і спробує увійти, то його дані перевіряти 
у такому файлі.
'''