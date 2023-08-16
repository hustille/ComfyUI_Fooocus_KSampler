from .sampler.nodes import KSamplerWithRefiner

NODE_CLASS_MAPPINGS = {
    "KSampler With Refiner (Fooocus)": KSamplerWithRefiner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KSamplerWithRefiner" : "KSampler With Refiner (Fooocus)"
}


print("\033[34mFooocus combined KSampler: \033[92mloaded\033[0m")
