from collections import Counter

d1 = """Crowded Fire's ensemble produces poetic, bold theater created by new and contemporary artists. We seek to engage our community by producing adventurous work,innovative in structure, which addresses the diverse political and social concerns of our audiences. Crowded Fire provides Community Services by (i) developing, discovering,and presenting new theater that is innovative in both structure and content; (ii) privileging a plurality of voices and experiences on our stage through the selection of material by and about those in under-represented and/or disenfranchised communities; and (iii) supporting artists at all stages of their career. Mainstage Productions & Development: In 2022, Crowded Fire did development and pre-production work on one mainstage theatrical production, SHIPPING & HANDLING by Playwright-in-Residence Star Finch, which, due to a COVID delay, will have its world premiere in 2024. Plays by four other playwrights were developed and supported in the Matchbox R&D Lab throughout the year, with the support of our staff, guest artists, and Resident Artists.
"""

d2 = """This organization seeks to involve Asian American groups and individuals to go out to the fields and offer help to local shelters, hospitals, schools, senior centers, and other organizations or households. It intends to improve the quality of life for the ones with special needs, facilitate the communication amoung the people being helped and the ones offering the help, and develop their ability to understand, respond to, and respect the needs of others.
"""

h1 = """
artist, theater, creative, community, play
theater, artist,innovative, supporting, production
theater, diverse, community,  new, voices, under-represented
Theater, Acting, Community, Stage, Performance
community, theatre, creativity, artists, contemporary, bold
Theater, artists, community, service, production
ensemble, theater, concerns, services, production
Crowded, Fire, theater, COVID, artist
theater, innovative, diverse, artists, production, development, play
creation, development, social, theatrical, diversity
theater, artist, community, production, innovative, support
poetry, play, community, theatrical, voices
theater, address, concern, services, privileging, under-represented, supporting
community, theater, diverse, structure, representation
artist, theater, community, play, production
community, development, artist, audience, career
poet, theater, art, diverse, concern, service, voice, experience
community, creative, current, diverse, theater, representation
"""

h2 = """
Asian, volunteer, communication, serve, local
Asian, help, local, organizations, communication
Asian, help, improve, communication, people, develop, respect
Outreach, Needs, Asian, Public, Canvassing
Community, communication, understanding, improvement, facilitation
Asian, local, involve, special, help, others
Asian, needs, improve, communication, develop
outreach, help, quality, needs, communication
Asian, American, Community, help, local, improve, facilitate, develop
Asian, American, help, people, needs
Asian, help, organization, needs, local, improve
asian, assist, community, volunteer, organizations
Asian, help, improve, facilitate, communication, develope
Asian, service, people, sympathy, communication
Asian, shelter, hospital, school, senior, communication, help
help, needs, organization, local, Asian, American
Asian, help, local, improve, quality, life, develop, ability
Asian, service, help, organizations, volunteer, facilitation
"""

def countwords(h):
    """Count the words I copied and pasted in.
    """
    words = h.lower().replace(",", " ").split()
    return Counter(words)

w1 = countwords(h1)
w2 = countwords(h2)

# A good LLM prompt (question) to summarize d1 and d2 needs to produce
# values where w1 and w2 are large.
