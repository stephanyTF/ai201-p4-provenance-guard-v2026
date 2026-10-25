"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "It makes my heart melt to watch cats “making biscuits” on my social media feed. Basically “making biscuits” is when cats look like they’re kneading their pillows, stuffed toys, and even their owners. I learned it's a sign of affection but it’s also very cute to watch!",
            "Nahh it’s all good. I don’t want to pressure u to join if u can’t. Your health and school are an absolute priority!! Ahh noo. No sleep? It’s must been a long week for u. Hope ur able to take some power naps when u can so u can get thru your assignments. But ik self care and staying on top of school work and everything else is hard.",
            "The key to writing identity in an essay while maintaining professionalism is to pretend that I was telling a story to a live audience. Nothing else fits in this role better than a speaker at graduation orating anecdotes and advice. Hence, I was delighted that the genre Summer Bridge Writing Lab would focus on would be Commencement speeches. During those five weeks, I reviewed the familiar rhetorical strategies but learned how rhetorical was utilized in a new way in speeches. For instance, in the readings of AGWR Ch 1 “Introducing Rhetoric and Genre” written by Rebecca Schultz, I was reminded of what truly is rhetorical which is basically, “any text or piece of music, or image ... created by someone, to communicate something to someone else” (1)",
            "No matter how ironed their clothes may be, the anthropomorphic beasts in Reynard the Fox can not smooth out animalistic impulses, leaving a perceptible wrinkle in their logic. As loyal civilians, the Bear and the Cat are sent to retrieve the delinquent fox, Reynard. Yet they are still animals with natural desires including Reynard the Fox who true to his nature is cunning enough to manipulate the animals’ instinct to escape the law.",
            "First the introduction, establishes the importance of studying child development for the future of society. Then the essay leads into the focus of the topic of child development researched by Jean William Fritz Piaget. Supporting body paragraphs each discuss the four stages of child development, the counter argument that the theory was not inclusive of all children due to different biological traits, and finally the rebuttal that a nurturing home environment would support Piaget theory of child development.",
            "A vole seeks a wife in the highest position. He starts with the sun, believing he will wed with the daughter of the strongest being. Yet the sun insists his position is not the most powerful and admits a lower position, the clouds which has more power in blocking his sunlight. As the vole moves down the levels, he is told there is another of “higher” power that rests below them. In the vole’s goal of ascending the classes, he is ironically descending back to his original place to find the daughter of the “highest” is to marry.",
            "Even Though she seems to be gesturing to the fish, the image is self-reflective in making the woman the real prize which catches more than a plastic fish but the male gaze. The objectification of women can also be seen in the other picture of a woman whose body is outstretched upright with her limbs cutting out of the picture and her main body within the frame.",
            "From Donaldson's lecture, Tom Regan’s quote brings up new ethics of care where humans extend their empathy and moral consideration for non-human beings. It’s been historically debated by many philosophers whether animals have rational thought and if its presence should be what defines their moral consciousness. Critical philosophers like Aristotle or Descartes assumed animals lacked rational reasoning and thus also failed the same moral rights or the capability to generate the same authentic emotions on a human level.",
            "However, more sympathetic debaters such as Tom Regan compares the rationality of an animal to those of infants or patients with Alzheimer's, thereby arguing that since society guards the moral rights of these human figures then the same should be applied to animals. Rationality or human-level reasoning may be seen as a bias anthropocentric measurement of the value of life since it's not inclusive of nonhuman species. Animal ethics of care protects the right to live life the way one desires and is not restricted to only humans but extends to the rights of animals."
            
        ],
    },
    {
        "name": "Distinguishable",
        "criterion": 2,
        # A clearly-AI and clearly-human text score difference should be 
        # at least .5
        "texts": [
            "Few feline habits are as endearing, or as puzzling, as kneading. A cat settles onto a soft blanket and begins pressing its paws rhythmically into the fabric, one after the other, often purring with half-closed eyes. Although the behavior looks like a quirk, it has deep roots in a cat's biology and early life.  Kneading likely combines several motives: nostalgia, instinct, territory, and comfort.",
            "Nahh it's all good. I don't want to pressure u to join if u can’t. Your health and school are an absolute priority!! Ahh noo. No sleep? It’s must been a long week for u. Hope ur able to take some power naps when u can so u can get thru your assignments. But ik self care and staying on top of school work and everything else is hard.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "Few feline habits are as endearing, or as puzzling, as kneading. A cat settles onto a soft blanket and begins pressing its paws rhythmically into the fabric, one after the other, often purring with half-closed eyes. Although the behavior looks like a quirk, it has deep roots in a cat's biology and early life.  Kneading likely combines several motives: nostalgia, instinct, territory, and comfort.",
            "Nahh it's all good. I don't want to pressure u to join if u can’t. Your health and school are an absolute priority!! Ahh noo. No sleep? It’s must been a long week for u. Hope ur able to take some power naps when u can so u can get thru your assignments. But ik self care and staying on top of school work and everything else is hard.",
            "Have you seen on your social media feed or heard a few cat owners exclaim, “Aww my cats are making biscuits!”. Making biscuits or kneading are one of the few feline habits that can be seen as not just endearing but even puzzling. A cat settles onto a soft blanket and begins pressing its paws rhythmically into the fabric, one after the other, often purring with half-closed eyes. Although the behavior might seem quirky, it's deeply rooted in a cat's biology and early life.  Kneading likely stems from several motives: nostalgia, instinct, territory, and comfort."
        ],
    },
      
    {
        "name": "Handling Invalid Text",
        "criterion": 5,
        #  Missing and/or empty text should always avoid scoring and request the user again to submit a non empty text while an enormous text should also be avoided to score and instead notify the user to shorten their content
        "texts": [
            "",
            ".",
            "borderline.",
    
        ],
    },




    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    # {
    #     "name": "bad input",
    #     "criterion": 3,
    #     "bodies": [
    #         {"text": "", "creator_id": "eval_bad_empty"},
    #         {"creator_id": "eval_bad_missing"},          # no text field at all
    #         {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
    #         {"text": None, "creator_id": "eval_bad_null"},
    #     ],
    # },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.


    ## Criterion 4 (appeals) is NOT included here. 
    #  Run python run_appeals.py separately; it submits, appeals, then checks the audit log.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
