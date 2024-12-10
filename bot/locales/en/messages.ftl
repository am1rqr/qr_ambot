menu = <b>🏠 Welcome! You are in the main menu.</b>
settings = <b>⚙️ Your settings:</b>

           <b><i>▫️Cell size: {$box_size}</i></b>
           <b><i>🔲 Border width: {$border}</i></b>
           <b><i>🎨 Fill color: {$fill_color}</i></b>
           <b><i>🖼 Background color: {$back_color}</i></b>
           <b><i>📎 File format: {$file_format}</i></b>

           <i>👇 Choose a parameter to change:</i>

change_size =
    {$change_type ->
        [box_size] <i>✍️ Enter the cell size:</i>
        [border] <i>✍️ Enter the border width:</i>
    }