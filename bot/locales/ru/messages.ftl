menu = <b>🏠 Добро пожаловать! Вы находитесь в главном меню.</b>
settings = <b>⚙️ Ваши настройки:</b>

           <b><i>▫️Размер клетки: {$box_size}</i></b>
           <b><i>🔲 Ширина границы: {$border}</i></b>
           <b><i>🎨 Цвет заполнения: {$fill_color}</i></b>
           <b><i>🖼 Цвет фона: {$back_color}</i></b>
           <b><i>📎 Формат файла: {$file_format}</i></b>

           <i>👇 Выберите параметр для изменения:</i>

change_size =
    {$change_type ->
        [box_size] <i>✍️ Введите размер клетки:</i>
        [border] <i>✍️ Введите ширину границы:</i>
    }