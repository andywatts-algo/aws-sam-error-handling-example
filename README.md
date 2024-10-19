# Step Function Error Handling Example

## Components

### Lambdas
* [RandomError](random_error/app.py)
* [LogInput](log_input/app.py)

### Step Function
* [statemachine.asl.json](statemachine.asl.json)

#### Steps
1. Start with RandomError lambda which fails 50% of the time
2. If RandomError succeeds, then LogInput lambda is called
3. If RandomError fails, then the state machine will retry RandomError 2 more times for a total of 3 attempts
4. After 3 attempts, the failure is bubbled up to the step function and the execution fails.




