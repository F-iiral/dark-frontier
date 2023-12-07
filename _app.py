from common.env import DEV_MODE
from common.dev import ConsoleShortcuts
import common.router as router
import os

def compile_ts_to_js(file_name: str) -> None:
    if not (file_name.endswith('ts')):
        return
    ts_file_path = f"./static/scripts/{file_name}"
    command = f"tsc {ts_file_path}"
    result = os.system(command)
    
    if result == 0:
        print(f"{ConsoleShortcuts.log()} {file_name} -> {file_name.replace('.ts', '.js')}")
    else:
        print(f"{ConsoleShortcuts.error()} Error during compilation of {file_name}")

if __name__ == "__main__":
    if DEV_MODE:
        print(f"{ConsoleShortcuts.log()} Starting compilation of all TypeScript files in /static/scripts")
        for file in os.listdir("./static/scripts"):
            compile_ts_to_js(file)

    app = router.start_app()
    app.run(debug=DEV_MODE, use_reloader=False)