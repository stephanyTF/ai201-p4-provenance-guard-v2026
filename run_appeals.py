import requests, audit, config

URL = f"http://{config.HOST}:{config.PORT}"
TEXTS = [
    "The professor and students had a difficult time trying to define quality. It was later realized quality may not be concretely defined but innately recognized. The inability to come to this conclusion without rationality or premeditated steps was the blockage for the professor’s understanding of it. The students' blockage were their incapability to regurgitate anything they learned from the class to approach the unfamiliar question. ", #human
    "The key to writing identity in an essay while maintaining professionalism is to pretend that I was telling a story to a live audience. Nothing else fits in this role better than a speaker at graduation orating anecdotes and advice. Hence, I was delighted that the genre Summer Bridge Writing Lab would focus on would be Commencement speeches. During those five weeks, I reviewed the familiar rhetorical strategies but learned how rhetorical was utilized in a new way in speeches. For instance, in the readings of AGWR Ch 1 “Introducing Rhetoric and Genre” written by Rebecca Schultz, I was reminded of what truly is rhetorical which is basically, “any text or piece of music, or image ... created by someone, to communicate something to someone else” (1)", #human
    "No matter how ironed their clothes may be, the anthropomorphic beasts in Reynard the Fox can not smooth out animalistic impulses, leaving a perceptible wrinkle in their logic. As loyal civilians, the Bear and the Cat are sent to retrieve the delinquent fox, Reynard. Yet they are still animals with natural desires including Reynard the Fox who true to his nature is cunning enough to manipulate the animals’ instinct to escape the law.", #human
    "Artificial intelligence has transformed the way we approach problem-solving in the modern world. By leveraging large datasets and advanced algorithms, these systems can identify patterns that would be difficult for humans to detect. Furthermore, the integration of machine learning into everyday applications has led to significant improvements in efficiency, accuracy, and user experience across a wide range of industries.", #AI
    "In conclusion, effective communication is a cornerstone of success in both personal and professional settings. It is essential to listen actively, express ideas clearly, and adapt one's message to the audience. By fostering open dialogue and mutual understanding, individuals can build stronger relationships, resolve conflicts constructively, and achieve their goals more effectively.", #AI
    "Climate change represents one of the most pressing challenges facing humanity today. Rising global temperatures, melting ice caps, and increasingly frequent extreme weather events underscore the urgent need for collective action. To address this multifaceted issue, governments, businesses, and individuals must work together to reduce greenhouse gas emissions, invest in renewable energy, and promote sustainable practices.", #AI
    "The once cornerstone of problem-solving we’ve known growing up has been entirely disrupted by Artificial intelligence’s exponential momentum. Patterns once elusive and time consuming to be picked up by even the keenest analyst, can be done almost instantly by systems equipped with large datasets and advanced algorithms. Furthermore, the integration of machine learning into everyday applications has led to significant improvements in efficiency, accuracy, and user experience across a wide range of industries.", #borderline
    "To summarize, effective communication is the key to success in both personal and professional settings. It is essential to listen actively, express ideas clearly, and adapt one's message to the audience. With open dialogue and mutual understanding, individuals can create stronger relationships, resolve conflicts, and achieve their goals more effectively.", #borderline
    "Climate change is one of the most pressing challenges facing humanity today. Increasing global temperatures, melting ice caps, and frequent extreme weather events underscore the urgent need for collective action. To resolve this, governments, businesses, and individuals must work together to reduce greenhouse gas emissions, invest in renewable energy, and promote sustainable practices.", #borderline

    ]  
# 10 texts: your own writing, AI text, borderline

for trial in range(1, 4):
    ok = 0
    for i, text in enumerate(TEXTS):
        cid_user = f"eval_appeal_{trial}_{i}"
        sub = requests.post(f"{URL}/submit", json={"text": text, "creator_id": cid_user}).json()
        cid = sub["content_id"]
        r = requests.post(f"{URL}/appeal", json={
            "content_id": cid, "creator_id": cid_user, "reasoning": "I wrote this myself."})
        log = audit.entries_for(cid)
        passed = (r.status_code == 200
                  and log[-1].get("status") == "under_review"
                  and any(e.get("event") == "appeal" for e in log)
                  and log[0].get("status") == "decided")
        ok += passed
    print(f"trial {trial}: {ok}/10")
