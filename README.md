# ComfyUI_Fooocus_KSampler
The KSampler from [Fooocus](https://github.com/lllyasviel/Fooocus) as a ComfyUI node

## Nodes

### KSamplerWithRefiner
Basically, two KSamplerAdvanced combined, therefore two input sets for base/refiner model and prompt. Additionally there is _refiner_switch_step_, which controls when the models are switched.

## Note
This patches basic ComfyUI behaviour - don't use together with other samplers. Or perhaps do? Other samplers might profit from those changes ... ymmv.
