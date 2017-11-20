![raw canonical github image link](https://github.com/cmoscardi/PUI2017_ch3183/raw/master/HW8_ch3183/HW8_Screenshot.png)


#### CLARITY: is the plot easy to read? is it clear or confusing, are the quantities being visualized ambiguous?
I was not entirely clear on what was going on until reading the captions. I would put the "Figure1: ..." caption at the top, as the title.

I think the juxtaposition is messy. I would consider plotting inbound and outbound on two plots adjacent to each other - this may make reading more clear. I think the color scheme may also help here...

Units: I find the choice of 00 - 23 confusing for time, but this probably depends on the reader. What timeframe are the average counts taken over? (e.g. weekdays vs. weekends probably have different patterns).

#### ESTHETIC: beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?

I think the bars are quite narrow - I find bar charts easier to read when the bars are wider. One way to make these bars wider would be...

There's basically no data between 1AM - 5AM, so I'd consider omitting those hours. They take up space but provide little information. Because there are so few trips in that time range, I don't think it would be dishonest, provided you mention this choice in the caption.

The red/blue feels like 3D glasses, which give me a headache and is uncomfortable on my eyes. It may contribute to why I find this plot unclear.

Why is the balance change plot in greyscale? I'd probably use a color there too. What would be really cool would be one color when there's a net increase, and another color when there's a net decrease. You could even use color to highlight magnitude.


#### HONESTY: is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?
I think this plot is honest. It takes averages at each hour across some timeframe - that timeframe is unknown, which is mostly confusing but could also distort the visualization depending on the choice and the viewer's expectation. Given that the caption indicates we should notice commuter patterns, including weekend days may distort that pattern.