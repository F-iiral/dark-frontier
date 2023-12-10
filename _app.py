from common.env import DEV_MODE
from common.dev import ConsoleShortcuts
import common.router as router
import os
import time

def get_file_modification_time(file_path: str) -> float:
    return os.path.getmtime(file_path)

def compile_ts_to_js(file_name: str) -> None:
    if not (file_name.endswith('ts')):
        return
    
    ts_file_modification_time = get_file_modification_time(file_name)
    js_file_name = file_name.replace('.ts', '.js')
    file_name_end = os.path.basename(file_name)

    if os.path.exists(js_file_name):
        js_file_modification_time = get_file_modification_time(js_file_name)
        if ts_file_modification_time < js_file_modification_time:
            print(f"{ConsoleShortcuts.log()} <#> {file_name_end} -> {file_name_end.replace('.ts', '.js')}")
            return
    
    command = f"tsc {file_name} --lib es2015,dom --target es5"
    result = os.system(command)
    
    if result == 0:
        print(f"{ConsoleShortcuts.log()} </> {file_name_end} -> {file_name_end.replace('.ts', '.js')}")
    else:
        print(f"{ConsoleShortcuts.error()} Error during compilation of {file_name}")

if __name__ == "__main__":
    if DEV_MODE:
        print(f"{ConsoleShortcuts.log()} Starting compilation of modified TypeScript files in /static/scripts")
        for root, dirs, files in os.walk("./static/scripts"):
            for file in files:
                file_path = f"{root}/{file}"
                compile_ts_to_js(file_path)
        print(f"{ConsoleShortcuts.ok()} Finished compiling modified files, preparing to launch the server")

    app = router.start_app()
    app.run(debug=DEV_MODE, use_reloader=False)
