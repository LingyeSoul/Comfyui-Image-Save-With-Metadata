# ComfyUI Image Save With Metadata

A standalone ComfyUI custom node for saving images with custom metadata support.

## Origin

This node is extracted from [WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui) - specifically the Image Save node, with additional functionality for saving custom metadata.

## Custom Metadata

The key feature added to this node is the ability to embed custom metadata into your saved images. You can provide a JSON object in the `custom_metadata` field:

```json
{
  "author": "Your Name",
  "model": "SDXL",
  "custom_field": "any value"
}
```

For PNG files, custom metadata is stored as PNG text chunks. For WebP files, it's stored in EXIF data.



## License

Same license as WAS Node Suite.
