![оптимизированный фильтр](screenshots/filter_prof.png)
![старый фильтр](screenshots/filter_old_prof.png)
![оптимизированный фильтр с подстановкой ввода](screenshots/filter_with_filename_prof.png)

Новый фильтр работает быстрее, так как работа с индексами в цикле for медленнее матричных преобразований.
Работу нового фильтра удалось "ускорить", прописав параметры в коде. Профилировщик учитывает время пользовательского ввода.
![оригинальное изображение](Lenna.png)
![после обработки](screenshots/Lenna_convert.png)