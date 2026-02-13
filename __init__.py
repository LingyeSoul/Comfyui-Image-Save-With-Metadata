"""
Image Save With Metadata - ComfyUI Custom Node
A standalone node for saving images with custom metadata support.

Author: Extracted from WAS Node Suite
License: Same as WAS Node Suite
"""

from .image_save_node import ImageSaveWithMetadata

NODE_CLASS_MAPPINGS = {
    "Image Save With Metadata": ImageSaveWithMetadata,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Image Save With Metadata": "Image Save With Metadata",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
