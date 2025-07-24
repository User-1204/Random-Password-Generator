import gui, logic

# Build GUI and get variables
root, settings, result_var, strength_var, strength_bar = gui.create_gui({
    'generate': lambda: logic.generate_password(settings, result_var, strength_var, strength_bar),
    'copy': lambda: logic.copy_to_clipboard(result_var),
    'export': lambda: logic.export_to_file(result_var)
})

# Run the app
root.mainloop()
