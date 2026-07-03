
from gui_functions import *

def show_page(name):
    """Raise the selected page."""
    pages[name].tkraise()


def open_page(name):
	page_callbacks = {
		"Main": gui_main,\
		"Add Players": gui_add_players,\
		"Add Teams": gui_add_teams,\
		"Create Match": gui_create_match,\
		"Start Match": gui_start_match,\
		"Insert Scorecard": gui_insert_scorecard,\
	}
	show_page(name)
	
	callback = page_callbacks.get(name)
	if callback:
		callback()

def gui_start():
	global pages
	
	root = tk.Tk()
	root.title("Cricket Management System")
	root.geometry("900x600")
	root.minsize(900, 600)
	
	# ----------------------------
	# Style
	# ----------------------------
	style = ttk.Style()
	style.theme_use("clam")
	
	root.configure(background="white")
	
	style.configure(
		"Nav.TButton",
		font=("Segoe UI", 10, "bold"),
		padding=(12, 8),
		
	)
	
	style.configure(
		"Page.TFrame",
		background="white"
	)
	
	style.configure(
		"Title.TLabel",
		font=("Segoe UI", 20, "bold"),
		background="white"
	)

	# ----------------------------
	# Top Navigation Bar
	# ----------------------------
	nav = ttk.Frame(root, padding=5)
	nav.grid(row=0, column=0, sticky="ew")
	root.rowconfigure(1, weight=1)
	root.columnconfigure(0, weight=1)
	
	tabs = [
		"Main",
		"Add Players",
		"Add Teams",
		"Create Match",
		"Start Match",
		"Insert Scorecard"
	]
	
    # Make every button take equal width
	for i in range(len(tabs)):
		nav.columnconfigure(i, weight=1)
	
	for col, tab in enumerate(tabs):
		btn = ttk.Button(
			nav,
			text=tab,
			style="Nav.TButton",
			command=lambda t=tab: open_page(t)
		)
		btn.grid(row=0, column=col, sticky="ew", padx=2)

	# ----------------------------
	# Main Content Area
	# ----------------------------
	container = ttk.Frame(root, style="Page.TFrame")
	container.grid(row=1, column=0, sticky="nsew")
	
	pages = {}
	
	for tab in tabs:
		frame = ttk.Frame(container, style="Page.TFrame")
		frame.place(relx=0, rely=0, relwidth=1, relheight=1)
		
		frame.rowconfigure(0, weight=1)
		frame.columnconfigure(0, weight=1)
		
		ttk.Label(
			frame,
			text=tab,
			style="Title.TLabel"
		).grid(row=0, column=0, pady=30)
		
		pages[tab] = frame
	
	
	show_page("Main")
	
	root.mainloop()


if __name__ == "__main__":
    gui_start()
