# Data dictionary

The processed result tables use the following common fields:

- `method`: evaluated method or model variant.
- `shield`: whether the task-progress reservation shield is enabled.
- `grid`: construction grid size.
- `dyads`: number of human–machine dyads.
- `return_mean`, `return_std`: mean and standard deviation of cumulative return.
- `makespan_mean`, `makespan_std`: mean and standard deviation of makespan.
- `waiting_mean`, `waiting_std`: mean and standard deviation of waiting actions.
- `collision_mean`, `collision_std`: mean and standard deviation of collision events.
- `rework_mean`, `rework_std`: mean and standard deviation of rework operations.
- `bits_mean`, `bits_std`: mean and standard deviation of communication bits.

Tables that are already formatted for manuscript viewing may also contain compact `mean ± std` strings.
