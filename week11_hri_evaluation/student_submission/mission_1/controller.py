"""Complete decide() using the transition requirements in the Lab 10 guide."""
# This whole block disappeared for some reason

def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]

    if kind == "CANCEL" and (phase == "CLARIFY" or phase == "CONFIRM" or phase == "EXECUTING" or phase == "WAIT_READY") :
        return "cancel"  # TODO Mission 1. Cancel before processing active work.

    if kind in ("REQUEST", "CORRECT"):
        if kind == "REQUEST" and (phase == "IDLE" or phase == "CLARIFY" or phase == "CONFIRM" or phase == "RECOVERY" or phase == "CANCELLED"):
           if target == "red" or target == "blue":
              return "select"
           return "clarify"
        if kind == "CORRECT" and (phase == "CLARIFY" or phase == "CONFIRM" or phase == "EXECUTING" or phase == "WAIT_READY"):
           if target == "red" or target == "blue":
              return "select"
        return "hold"  # TODO Mission 1. Clarify an unnamed target and guard when a request may replace it.

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if phase == "WAIT_READY" and kind == "READY":
        return "release"

    if kind == "TIMEOUT" and phase == "WAIT_READY" :
        return "timeout"  # TODO Mission 1. Enter recovery from a waiting state.

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    return "hold"