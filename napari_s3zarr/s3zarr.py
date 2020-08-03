from napari_plugin_engine import napari_hook_implementation
import dask.array as da


@napari_hook_implementation
def napari_get_reader(path):
    if not isinstance(path, str):
        return
    if path.startswith("s3:") and path.endswith(".zarr"):
        return reader_function


def reader_function(path):
    return [(da.from_zarr(path, storage_options={"anon": True}),)]
