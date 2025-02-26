import ttkbootstrap as ttk
import menus.main_menu as mm


WINDOW_BG = 'lightgrey'

#create app window
app = ttk.Window(title= 'GT Learning Tool')
app.config(background = WINDOW_BG)
#starts the window maximised
app.state('zoomed')
#sets the window icon
app.iconbitmap("icon/gt_icon.ico")

mm.drawMenu(app)

app.mainloop()