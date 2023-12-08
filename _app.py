from common.env import DEV_MODE
from common.dev import ConsoleShortcuts
import common.router as router
import os

def compile_ts_to_js(file_name: str) -> None:
    if not (file_name.endswith('ts')):
        return
    command = f"tsc {file_name}"
    result = os.system(command)
    backslash = "\\"
    file_name_end = file_name.split(backslash)[-1]
    
    if result == 0:
        print(f"{ConsoleShortcuts.log()} {file_name_end} -> {file_name_end.replace('.ts', '.js')}")
    else:
        print(f"{ConsoleShortcuts.error()} Error during compilation of {file_name}")

if __name__ == "__main__":
    if DEV_MODE:
        print(f"{ConsoleShortcuts.log()} Starting compilation of all TypeScript files in /static/scripts")
        for root, dirs, files in os.walk("./static/scripts"):
            for file in files:
                compile_ts_to_js(f"{root}/{file}")
        print(f"{ConsoleShortcuts.ok()} Finished compiling all files, preparing to launch the server")

    app = router.start_app()
    app.run(debug=DEV_MODE, use_reloader=False)