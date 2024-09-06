from ..ComfyUI_IPAdapter_plus.IPAdapterPlus import IPAdapterSimple, IPAdapterInsightFaceLoader, IPAdapterFaceID

class IPAdapterApply(IPAdapterSimple):
    pass

class IPAdapterApplyEncoded(IPAdapterApply):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ipadapter": ("IPADAPTER", ),
                "embeds": ("EMBEDS",),
                "model": ("MODEL", ),
                "weight": ("FLOAT", { "default": 1.0, "min": -1, "max": 3, "step": 0.05 }),
                "weight_type": (["original", "linear", "channel penalty"], ),
            },
            "optional": {
                "attn_mask": ("MASK",),
            }
        }

class InsightFaceLoader(IPAdapterInsightFaceLoader):
    pass

class IPAdapterApplyFaceID(IPAdapterFaceID):
    pass

NODE_CLASS_MAPPINGS = {
    "IPAdapterApply": IPAdapterApply,
    "IPAdapterApplyEncoded": IPAdapterApplyEncoded,
    "IPAdapterApplyFaceID": IPAdapterApplyFaceID, # reback
    "InsightFaceLoader": InsightFaceLoader, # reback
    "IPAdapterFaceIDBatch": "IPAdapter FaceID Batch"}