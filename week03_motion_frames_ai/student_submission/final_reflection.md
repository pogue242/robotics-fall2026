# Final reflection

Respond to any or all of these prompts:

1. What did this activity make you think about regarding your own interests in robotics, computing, engineering, or related work?
2. How did this activity affect your motivation to do similar kinds of work in the future?
3. What value do you see in connecting technical or computing work with human, ethical, or societal considerations?
4. What stood out to you about the activity, and why?
5. Is there anything else you would like to share about your experience with the activity?

## Response

The part that stood out to me the most was how something could be correct mathematically and still not work correctly when run it. My original values used a forward speed of 0.12 m/s, an angular speed of 0.40 rad/s, and a duration of about 1.96 seconds. Those values do produce a 0.30 m radius and 45 degree turn. All of the automated tests passed as well. However, when running in Gazebo, the robot moved outside of the allowed position tolerance. The simulator has things like acceleration and signal timing error that can change the final result.

_Word count: 97_
