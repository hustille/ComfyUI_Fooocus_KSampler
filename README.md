# ComfyUI_Fooocus_KSampler
The KSampler from [Fooocus](https://github.com/lllyasviel/Fooocus) as a ComfyUI node

## Nodes

### KSamplerWithRefiner
On the surface basically two KSamplerAdvanced combined, therefore two input sets for base/refiner model and prompt.

- _refiner_switch_step_ controls when the models are switched, like _end_at_step_/_start_at_step_ with two discrete samplers.
- _sharpness_ does some local sharpening with a gaussian filter without changing the overall image too much. Useful range seems to go up to 20 or so.

## Note
There is some magic beyond just encapsulating two samplers into one. This patches basic ComfyUI behaviour - don't use together with other samplers. Or perhaps do? Other samplers might profit from those changes ... ymmv.

## Known issues
It doesn't work ... Well, the example setup obviously does, at least for me. But anything nontrivial, like e.g. Controlnet and batch jobs, results in errors. I'd appreciate if somebody who actually understands the math would take a look at it
