import pathlib

class Path:

    def verify_path(self, path: pathlib.Path):
        path = pathlib.Path(path)
        path.touch(exist_ok=True, parents=True)

if __name__ == "__main__":
    p = Path()
    p.verify_path("C:\\Users\\Imuvi\\Desktop\\testefolder\\folder")
