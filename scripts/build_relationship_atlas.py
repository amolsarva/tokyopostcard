from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "archives" / "2026-05-15-relationship-atlas"
THUMB = ROOT / "assets" / "archive-thumbs" / "2026-05-15-relationship-atlas.svg"


COLUMNS = [
    ("date", "Date"),
    ("location", "Location Guess"),
    ("messages", "Key Messages"),
    ("simple", "Simple: What Is Happening"),
    ("freud", "Freudian Lens"),
    ("her_mom", "Her Mom"),
    ("my_mom", "My Mom"),
    ("her_best", "Her Best Friend"),
    ("my_best", "My Best Friend"),
    ("laura_avatar", "Laura Avatar"),
    ("amol_avatar", "Amol Avatar"),
]


CHAPTERS = [
    {
        "slug": "chapter-1",
        "number": "01",
        "date": "Jan 12-17, 2026",
        "title": "Ignition, Books, Sleep Debt",
        "summary": "The relationship begins as a high-frequency private language: sleep, missing, books, philosophy of love, fantasy, permission, and early declarations before either person has a stable map.",
        "temperature": "Spark / destabilization",
        "rows": [
            {
                "date": "Jan 12",
                "location": "Late-night remote exchange; Amol appears sleep-shifted, Laura reachable but withholding more than she reveals.",
                "messages": "Laura jokes about an intern vibe-coding something. Amol asks to see her tomorrow, says he loved her five minutes ago, and frames permission as important. Laura teases him as an English teacher rather than an investor.",
                "simple": "The flirtation is already not casual. It has humor, praise, and a first test of boundaries: he moves fast, she keeps him slightly off balance while continuing to engage.",
                "freud": "Desire arrives through language before logistics. The beloved is idealized quickly, but the repeated concern with permission shows the ego trying to govern the id rather than merely denying it.",
                "her_mom": "This is charming, but too fast. I would notice the age, intensity, and midnight rhythm before I noticed the poetry.",
                "my_mom": "He sounds awake in the way men get awake when they are trying to persuade themselves feeling is thought.",
                "her_best": "You like him. But if he says love this early, make him prove he can slow down without sulking.",
                "my_best": "You are already writing in opera mode. Be careful not to confuse lyric skill with emotional due diligence.",
                "laura_avatar": "I enjoy the force of attention, but I will keep asking whether he sees me or the version of me he is inventing.",
                "amol_avatar": "This is not small. If it is reckless, it is at least lucidly reckless; I want to keep the door open and name the force honestly.",
            },
            {
                "date": "Jan 13-14",
                "location": "Mostly remote; bookshop, coffee chats, naps, and AI-summarized writing appear in the background.",
                "messages": "The thread touches forever, Burning Man, bookshops, coffee meetings, exhaustion, AI summarization, and wanting to hear the full reasoning.",
                "simple": "Their bond becomes intellectual companionship. The erotic layer is present, but the immediate adhesive is a shared appetite for analysis and narrative.",
                "freud": "The third object is already present: books and AI function as sanctioned intermediaries, letting desire speak in a form that feels safer than direct confession.",
                "her_mom": "I would ask whether she is sleeping and whether this person is helping her life become clearer or only more dramatic.",
                "my_mom": "He has found someone who answers the long paragraphs. That can become addictive faster than affection itself.",
                "her_best": "The cute part is that you both want to talk. The concerning part is that you both treat no sleep as romance.",
                "my_best": "You two have discovered a feedback loop: message, analyze message, analyze the analysis, message again.",
                "laura_avatar": "I am drawn to being understood, but I am not ready to let his interpretation become the official one.",
                "amol_avatar": "The literary channel matters. It is how I test whether this is merely attraction or the beginning of a shared mind.",
            },
            {
                "date": "Jan 15",
                "location": "Amol in transit or near flight mode; Laura near a personal breakpoint and talking through family/marriage/fantasy themes.",
                "messages": "Laura hopes they can see or text each other over the next years, then says she is near a breakpoint. Amol names the fantasy house and later debates a book about love. Laura says she wants him to have a richer love life.",
                "simple": "The conversation becomes explicit about the stakes. It is no longer just seduction; it is a crisis mirror for existing relationships, love theories, duty, and escape.",
                "freud": "The beloved becomes both lover and analyst. The danger is transferential: each person may use the other to metabolize older attachments, disappointments, and forbidden wishes.",
                "her_mom": "I would hear the phrase breakpoint and want quiet, not more stimulus. Decisions made from exhaustion can feel like revelation.",
                "my_mom": "He is trying to be honest, but he is also competing with a whole life that existed before him.",
                "her_best": "If you are talking about your marriage and a new man in the same breath, keep one foot on the floor.",
                "my_best": "Do not try to philosophize your way out of the fact that someone may get hurt.",
                "laura_avatar": "I want the possibility, but I also want to protect the vows and structures that made me who I am.",
                "amol_avatar": "I can critique the book, but the real question is whether love is chosen construction, chemical emergency, or both.",
            },
            {
                "date": "Jan 16-17",
                "location": "Flights, northern lights, Germany/conference context, likely Laura between London/Belgium rhythms.",
                "messages": "They talk about dreams, northern lights, songs, Wonderwall, dancing, missing, marriage at 24, grandfathers, tradition, and the fear that he sees her as someone else.",
                "simple": "The myth layer thickens: music, dreams, sky, family history, and marriage history all become part of the romance vocabulary.",
                "freud": "The paternal/grandfather motifs and young-marriage discussion show authority, law, and desire wrestling in the open. The fantasy needs elders in it because it threatens inherited order.",
                "her_mom": "She is not just flirting; she is narrating the architecture of her life. That means the risk is real.",
                "my_mom": "He should listen more carefully when she says he may be seeing an imagined version of her.",
                "her_best": "The 'you see me as somebody else' line is the flare. Do not let compliments become a costume you have to wear.",
                "my_best": "The romance is beautiful, but if your read of her family is too clever, it may become invasive.",
                "laura_avatar": "I want to be desired, not turned into a thesis about tradition, fathers, marriage, and rebellion.",
                "amol_avatar": "I am trying to see the whole person, but my interpretations may arrive faster than her consent to be interpreted.",
            },
        ],
    },
    {
        "slug": "chapter-2",
        "number": "02",
        "date": "Jan 18-24, 2026",
        "title": "Remote Enchantment, Paris Pull",
        "summary": "The relationship moves from first ignition into practical fantasy: pictures, sleepovers, Paris/Strasbourg calculations, AI maps, style analysis, and the first evidence that they can become each other's everyday advisory board.",
        "temperature": "Longing / logistical magnetism",
        "rows": [
            {
                "date": "Jan 18-20",
                "location": "Amol appears away among friends/travel; Laura remote, watching his sleep, pictures, and social context from afar.",
                "messages": "They discuss sunlit photos, sleepovers, jealousy-adjacent questions, side projects, ugly-beautiful images, calls, Laura's startup stress, and whether she loves him.",
                "simple": "The relationship becomes daily life support. She brings company/founder stress; he offers attention and interpretation; both test jealousy and reassurance.",
                "freud": "Work anxiety and erotic longing merge. The lover becomes a regulator: not only wanted, but used to stabilize ambition, insomnia, and uncertainty.",
                "her_mom": "If he is calming her and making her sleepless at the same time, that contradiction matters.",
                "my_mom": "He wants to be needed. That can be generous, but it can also become a role he performs too hard.",
                "her_best": "You want his opinion about a thousand things. Good. But keep your own steering wheel.",
                "my_best": "When a founder starts using romance as her emergency advisory line, the intimacy is already operational.",
                "laura_avatar": "I am not bothering him; I am testing whether he wants to be inside the real mess, not only the fantasy.",
                "amol_avatar": "People who care want to be part of the solution. I want to be the person she calls before she edits herself.",
            },
            {
                "date": "Jan 20 late",
                "location": "Remote, late-night, with future geography scattered across New York, Laura's life, and possible shared cities.",
                "messages": "They ask what comes next: New York, her own life, marriage, children, friends, and whether they can be 'just friends.' Amol says he wants anything she will give him.",
                "simple": "A relationship forecast appears before the relationship has stable terms. They are drafting futures faster than they can verify present facts.",
                "freud": "The superego demands a plan; the id demands contact; the ego creates provisional categories like just friends, fantasy, future, and work.",
                "her_mom": "This is exactly when I would say: no promises made after midnight.",
                "my_mom": "He is already bargaining with absence: anything she gives him will be enough until it is not.",
                "her_best": "Do not let 'anything you will give me' sound romantic if it avoids saying what he can actually offer.",
                "my_best": "You may think flexibility is kindness, but it can leave her carrying the decision cost.",
                "laura_avatar": "I need to know whether I am wanted as a future or as an exquisite impossibility.",
                "amol_avatar": "The future is impossible to solve, but the present fact is clean: I want to be with her.",
            },
            {
                "date": "Jan 22-23",
                "location": "Paris/Basel/Strasbourg/St. Moritz logistics; Laura invites a city far from home, Amol tries to route himself toward her.",
                "messages": "Laura says she wants a good time in a city far away from home and home. Amol wants Paris, calculates travel windows, shares art-world profiles, and they exchange maps, cathedral talk, deck edits, and weekend plans.",
                "simple": "The fantasy becomes itinerary. They are not merely saying 'someday'; they are solving trains, cities, timings, and excuses.",
                "freud": "The forbidden object becomes more permissible when disguised as culture, art, logistics, and beautiful maps.",
                "her_mom": "A city away from home is romantic, but also a way to suspend consequences.",
                "my_mom": "He will move mountains, or at least train schedules, if the possibility of seeing her is real.",
                "her_best": "If he comes, make sure it is because you want the weekend, not because the plot is now too beautiful to interrupt.",
                "my_best": "The travel math is the tell. You are not brainstorming; you are negotiating with reality.",
                "laura_avatar": "I want him to come, but I also want to see if he chooses me over the elegance of his own calendar.",
                "amol_avatar": "Every train connection becomes a referendum on desire. If I can get there, maybe the story becomes embodied.",
            },
            {
                "date": "Jan 24",
                "location": "Likely same-city weekend encounter or immediately around it; coffee, walking, clothes, sunglasses, body-type analysis.",
                "messages": "Coffee, sleepiness, walks, resisting a kiss, Kibbe body types, slippers, sunglasses, candles, style PDFs, and missing texts dominate the thread.",
                "simple": "They shift into tactile everyday curation: clothes, smell, coffee, shoes, face, style. The relationship starts dressing itself.",
                "freud": "Fashion is displaced erotic observation. Body-type talk makes desire discussable as aesthetics, not only appetite.",
                "her_mom": "This part sounds more harmless: coffee, walking, clothes. But the harmless details can deepen attachment most.",
                "my_mom": "He is letting her edit the surface of his life because he wants her inside it.",
                "her_best": "You are basically styling him. That is intimate in a way people underestimate.",
                "my_best": "Once she is advising shoes and sunglasses, she is not just a crush; she is becoming taste infrastructure.",
                "laura_avatar": "I can make him sharper without making him someone else; I like being useful and seen.",
                "amol_avatar": "Her eye has authority. Being corrected by her feels less like control than inclusion.",
            },
        ],
    },
    {
        "slug": "chapter-3",
        "number": "03",
        "date": "Jan 26-29, 2026",
        "title": "Aftershock, Body, Future",
        "summary": "After a charged weekend, both people try to explain what happened. The thread becomes a long investigation of physical intimacy, marriage decisions, children, work ambition, and whether this is a shiny object or a life signal.",
        "temperature": "Afterglow / consequence",
        "rows": [
            {
                "date": "Jan 26",
                "location": "Laura back in routine but physically activated; Amol in St. Moritz/art-world travel mode.",
                "messages": "Laura says thinking about the weekend sends electric current through her body. They discuss women in art, ambition, disagreement, and the weekend as amazing, crazy, beautiful, and dreamlike.",
                "simple": "The weekend becomes evidence. They are trying to decide whether intensity is a clue, a drug, or both.",
                "freud": "The body refuses to stay subordinate to narrative. Electricity becomes somatic proof, but proof of what remains contested.",
                "her_mom": "A body can tell you something important, but it can also speak loudly when life is unstable.",
                "my_mom": "He is thrilled that the feeling was mutual, but should not rush to convert mutuality into destiny.",
                "her_best": "You said it clearly: this was insane on every level, and you want to see him. That is enough for now.",
                "my_best": "Do not over-explain the miracle. Also do not under-account for the blast radius.",
                "laura_avatar": "The closeness mattered more than performance. I wanted to melt into him, which scares and clarifies me.",
                "amol_avatar": "Truth: I have no idea where this goes, but I want to see her. That is the least false sentence.",
            },
            {
                "date": "Jan 26-27",
                "location": "Separated by geography; he drifts toward sleep in art/travel context, she stays awake wanting the thread to continue.",
                "messages": "They compare the physical experience to wanting to be closer than physically possible. He falls asleep midstream; she misses their talks and asks for random pictures.",
                "simple": "The distance after intimacy creates withdrawal. The chat tries to reproduce closeness, but sleep and time zones keep interrupting.",
                "freud": "The phone becomes a transitional object: not the body, but close enough to trigger both comfort and frustration.",
                "her_mom": "She needs sleep and steadiness, not only more afterglow.",
                "my_mom": "He cannot be constantly present, even if he says he wants to be.",
                "her_best": "If he falls asleep, do not turn that into rejection. But also notice how much regulation you now expect from him.",
                "my_best": "You two are discovering that intensity has a maintenance cost.",
                "laura_avatar": "I want continuity. The gap after the high makes me want pictures, voice, proof.",
                "amol_avatar": "I want to remain present, but my body keeps proving I am not an infinite message machine.",
            },
            {
                "date": "Jan 28",
                "location": "High-volume remote day; art, outfits, surprise projects, psychoanalysis, and calls.",
                "messages": "Compliments about beauty, art conversations, surprise plans, jokes as deflection, records to burn, calls, and a dense back-and-forth about what serious comments hide.",
                "simple": "They become co-analysts. She challenges his joke-defense; he likes that she challenges him. The bond sharpens through correction.",
                "freud": "Humor appears as a defense mechanism and invitation. She notices the defense; he feels exposed and attracted.",
                "her_mom": "A man who enjoys being challenged may still use cleverness to avoid being known.",
                "my_mom": "She is not impressed by performance alone. That is good for him.",
                "her_best": "You are good at finding the real sentence under his joke. Make sure he returns the favor without diagnosing you.",
                "my_best": "This is where she becomes unusually important: she can interrupt your monologue without killing the connection.",
                "laura_avatar": "I can be playful, but I am also watching whether he faces the issue head on.",
                "amol_avatar": "Her challenges are not friction; they are proof that this is not empty adoration.",
            },
            {
                "date": "Jan 29",
                "location": "Amol between global elite/art/travel frames; Laura reflecting on husband, children, family values, and possible reinvention.",
                "messages": "They discuss cultural festivals, mountains, Egypt, being powerful in the same conversation, her husband, five kids, Flemish heritage, faith, family, becoming someone's muse, not making pledges too soon, and whether she should make marriage decisions independently of him.",
                "simple": "This is the heaviest pivot: attraction becomes a decision architecture. They name children, home, marriage, values, and the risk of confusing a shiny object with a true signal.",
                "freud": "The love triangle is not merely romantic; it includes family law, religion, future children, ambition, and the fantasy of a new self.",
                "her_mom": "This is where I would insist that her marriage decision cannot be outsourced to a new romance.",
                "my_mom": "He is trying not to promise what he cannot guarantee, which is the responsible sentence inside a very irresponsible storm.",
                "her_best": "You can want him and still decide your marriage separately. Hold that line as if it is oxygen.",
                "my_best": "Do not become her exit plan unless you are ready to be a real plan.",
                "laura_avatar": "I am not requesting a pledge. I am trying to see whether my life wants reinvention with or without him.",
                "amol_avatar": "I want the best thing for her, but I know that sentence is complicated when I also want her.",
            },
        ],
    },
    {
        "slug": "chapter-4",
        "number": "04",
        "date": "Jan 30-Feb 2, 2026",
        "title": "Family Weather, AI Room",
        "summary": "The exchange widens into grandparents, family reactions, architecture, clothes, religion, immigration, language learning, and the AI room where both of them rehearse versions of the relationship.",
        "temperature": "Integration / moral debate",
        "rows": [
            {
                "date": "Jan 30",
                "location": "Remote daily life; Laura near family/grandfather context, Amol in reflective New York/travel mode.",
                "messages": "Grandfather visits, coincidences, climate, Celine jokes, women in art lists, tone-matching advice, photoshopping, main-character jokes, theories about why she likes him, and her rejection of dad/grey-hair explanations.",
                "simple": "They test theories of attraction. She resists reductive explanations; he turns theory into love letter.",
                "freud": "The father-substitute hypothesis is raised and rejected, which matters because naming it reduces its unconscious power even if it remains partly active.",
                "her_mom": "Good: she pushes back on explanations that make her smaller.",
                "my_mom": "He should be careful that theorizing her does not become another way to possess her.",
                "her_best": "You are allowed to say: no, that is not why I like you.",
                "my_best": "Your theory became a love letter because you want the theory to land softly.",
                "laura_avatar": "I like him for the way the whole field feels, not because he maps neatly onto a category.",
                "amol_avatar": "I theorize because I am trying to respect the complexity, but I know the analysis can become too much.",
            },
            {
                "date": "Jan 31",
                "location": "Laura with family/domestic routines; Amol elsewhere, sleeping, gifting music, discussing architecture.",
                "messages": "Dreaming, beloved forever, sleep deprivation, sun, driving/calling, family chilling, Morrissey gift, Foster/building beauty, Bruges building rules, and more pictures.",
                "simple": "The romance enters ordinary Saturday: family rooms, dinner, couches, errands, music files, urban beauty. It begins to live inside normal time.",
                "freud": "Domestic scenes become erotic because they imply belonging. Architecture talk is a displaced question: what kind of house could contain this?",
                "her_mom": "Family proximity makes it more serious. Secrets inside a living room are still secrets.",
                "my_mom": "He is sending gifts and ideas because that is how he keeps a thread of care alive across distance.",
                "her_best": "The ordinary updates are the dangerous ones. They make it feel like a relationship, not an affair-shaped comet.",
                "my_best": "Beauty, music, buildings, family: you are building a shared culture at speed.",
                "laura_avatar": "I like that he can live inside the texture of my day, not only the dramatic parts.",
                "amol_avatar": "The job of the building is to be beautiful; perhaps the job of the relationship is also to make ordinary life bearable and bright.",
            },
            {
                "date": "Feb 1",
                "location": "Sunday rhythm; family reaction context, health/stress/body regulation, company/founder identity.",
                "messages": "Long memos, living funeral article, music, family reactions to the story, stress in her body, popularity, message volume, McKinsey/JPM vibes, jealousy, friends saying she wants out, and Bigmouth self-analysis.",
                "simple": "They start socializing the reality through partial disclosures. Friends/family reactions become a mirror and pressure system.",
                "freud": "The private dyad is invaded by witnesses. Once others know fragments, the fantasy must survive social interpretation.",
                "her_mom": "I would ask what exactly was told, to whom, and why.",
                "my_mom": "He may feel chosen because she is telling people, but partial disclosure can also intensify confusion.",
                "her_best": "Your people are trying to help you find your lines. Listen, even if you still want him.",
                "my_best": "Jealousy finally appears, which reassures her, but jealousy is not a plan either.",
                "laura_avatar": "I need others to reflect me back because this is too large to hold alone.",
                "amol_avatar": "Nobody challenges me, and she does. Nobody tells me these things, and she does. That makes the witness field matter.",
            },
            {
                "date": "Feb 2",
                "location": "New York/Europe time-zone split; language, religion, immigration, grandfather, and no-compromise debate.",
                "messages": "They discuss religion, women, migration, culture, carpets, waffles, Dutch/Flemish grammar, her childhood independence, wanting him to converse with her grandfather, compromise, tears about his dad, and the next act of the opera.",
                "simple": "This is an integration chapter: political values, family language, religious culture, father mortality, and romance all enter the same room.",
                "freud": "Learning her language is a symbolic courtship of the family system. His tears about his father reveal that parental time and romantic urgency are running in parallel.",
                "her_mom": "If he wants to learn the family language, that is meaningful. But meaning is not the same as readiness.",
                "my_mom": "His father grief is close to the surface; love may be arriving while another love is under threat.",
                "her_best": "Wanting him to speak to your grandfather is not casual. You are imagining him past the threshold.",
                "my_best": "You are crying about Dad and flirting about opera. That is a lot of emotional voltage in one circuit.",
                "laura_avatar": "I want the impossible to pass through real gates: language, family, values, Sunday dinners.",
                "amol_avatar": "I want to do it for her. I also want all of it, which is the beautiful and dangerous sentence.",
            },
        ],
    },
    {
        "slug": "chapter-5",
        "number": "05",
        "date": "Feb 3-6, 2026",
        "title": "Build, Work, Cats, New York",
        "summary": "The relationship turns practical: playlists, rituals, founder coaching, product-market chatter, interruptions, coffee-shop dreams, external mentors, kids/cats, and a possible New York visit.",
        "temperature": "Operational intimacy",
        "rows": [
            {
                "date": "Feb 3",
                "location": "Remote, workday fragments; art/project experiments and late-night sleep discipline.",
                "messages": "They discuss love as assignment, funeral rituals, easy vs hard relationships, building something huge, mixtapes, art burning, bio meetups, cats, kids, and an entire life together.",
                "simple": "The fantasy becomes a project plan and a domestic sketch. They talk as if designing a life while repeatedly warning themselves not to get carried away.",
                "freud": "Planning children and pets after one intense encounter is not mere silliness; it is the psyche testing whether the object can become home.",
                "her_mom": "Five kids and cats is not banter if it keeps returning.",
                "my_mom": "He is honest that he is carried away, which is better than pretending to be calm.",
                "her_best": "Your line that marriage decisions must be independent from him is still the key line.",
                "my_best": "Do not let 'honest feeling' become a substitute for capacity.",
                "laura_avatar": "I can imagine the life and still know that imagining it does not decide it.",
                "amol_avatar": "It is stupid and honest: I am planning because the feeling makes planning imaginable.",
            },
            {
                "date": "Feb 4",
                "location": "A deliberate semi-silence day; Laura social in a cool bar/restaurant, Amol in private/work/family context.",
                "messages": "They discuss non-messaging, obsession, wanting to see each other, random objects in his place, sleep goals, a cute heart in a bar, and 'we love each other.'",
                "simple": "A short attempt at restraint proves the attachment. Silence becomes another message.",
                "freud": "Absence heightens cathexis. The less they message, the more the relationship becomes visible as dependency.",
                "her_mom": "A day of not messaging should not feel like withdrawal this early.",
                "my_mom": "He asks how he is doing at not bothering her because he wants credit and reassurance at once.",
                "her_best": "You can miss him and still have your own night.",
                "my_best": "The 'we love each other' line is doing a lot of work. Make sure reality signs it too.",
                "laura_avatar": "When he is sleeping or silent in the morning, I feel the lack sharply.",
                "amol_avatar": "I can perform restraint, but I am still obsessed.",
            },
            {
                "date": "Feb 5",
                "location": "Workday calls; Laura in founder/product conversations, Amol available for chitchat and advice.",
                "messages": "Product marketing, calls, sexy-photo teasing, feedback that he interrupts, coffee-shop writing ideas, Bruges founder identity, and a flight.",
                "simple": "They are increasingly useful to each other professionally and personally. She gives him behavioral feedback; he validates her founder voice.",
                "freud": "The erotic bond creates permission for criticism. Correction becomes intimacy because it implies investment in the other's future self.",
                "her_mom": "I like that she tells him he interrupts. That is a real-life test.",
                "my_mom": "If he wants her opinion, he has to actually receive it, not just admire that she has one.",
                "her_best": "Coffee shops across the world is not stupid. Notice he tells you that.",
                "my_best": "She is not just muse material. She is founder material, and you should keep saying that.",
                "laura_avatar": "I want to be taken seriously as a builder, not only desired as a beautiful disruption.",
                "amol_avatar": "For everyone from Bruges, it is her. I want her to understand the scale of that.",
            },
            {
                "date": "Feb 6",
                "location": "Planning New York; Laura considering museums/friends/brunch, Amol wanting all available time.",
                "messages": "She listens to something start-to-finish, prepares for a coach/mentor, discusses being coachable, plans solo travel, Met/brunch/friends, and he says the only thing he wants is to see her and have all her time.",
                "simple": "The relationship enters calendar negotiation. He wants total absorption; she wants him, plus her friends, museums, and autonomy.",
                "freud": "Possessive longing meets independent selfhood. The romance must learn that wanting all of someone is not the same as honoring all of someone.",
                "her_mom": "I would be relieved she still wants museums and friends. Keep the whole person alive.",
                "my_mom": "He should notice the difference between wanting her time and deserving all of it.",
                "her_best": "Do not apologize for wanting The Met and brunch. That is your life, not an intrusion.",
                "my_best": "If she is in New York briefly, of course you want every hour. Still, be graceful.",
                "laura_avatar": "I want to see him, but I do not want to be swallowed by his wanting.",
                "amol_avatar": "I want all of her time because time is the only proof distance will accept.",
            },
        ],
    },
    {
        "slug": "chapter-6",
        "number": "06",
        "date": "Feb 7-9, 2026",
        "title": "Distance, Jet Lag, Partnership",
        "summary": "As Amol moves through Asia and Laura returns to London rhythms, the messages mix fashion, sun, jealousy, explicit love, partnership anxiety, cultural/age jokes, and a demand that the relationship be more than pictures and praise.",
        "temperature": "Distance / recalibration",
        "rows": [
            {
                "date": "Feb 7",
                "location": "Amol in Tokyo/Hong Kong or similar travel context; Laura in London/Europe sending photos, asking for calls.",
                "messages": "They discuss paintings, jackets, Tokyo shops, sex-shop jokes, sunny days, missing, calls, Amol saying he should not have said love because he does love her, and Laura reassuring him that feelings can come and go.",
                "simple": "Love is said again, then immediately managed. She offers emotional containment so he does not feel trapped by his own words.",
                "freud": "Confession triggers anxiety about obligation. Her reassurance lets the confession exist without becoming a contract.",
                "her_mom": "She is being very emotionally mature, maybe too soothing for someone else.",
                "my_mom": "He is ashamed of intensity, then moved by being accepted in it.",
                "her_best": "You are kind to him. Make sure he is also steady for you when you need containment.",
                "my_best": "She handled your panic better than you did. Remember that.",
                "laura_avatar": "I will not punish him for feeling, but I still need to know what his feeling can do.",
                "amol_avatar": "I love her; saying it creates stress because love wants promises my calendar has not earned.",
            },
            {
                "date": "Feb 8",
                "location": "Amol alone by sea/cold Sunday in Asia; Laura back to London life and besties.",
                "messages": "They talk tattoos, Lost in Translation, loneliness, body marks, saints, beauty, dreams, being loved, and the impossibility of love.",
                "simple": "Distance makes him melancholic. She becomes the person he wants to dream toward at the edge of a lonely travel day.",
                "freud": "The tattoo question is about inscription: what does the body record when love feels both temporary and eternal?",
                "her_mom": "I would worry about body marks made during emotional weather.",
                "my_mom": "His lonely Sunday is real. He should not turn loneliness into a permanent decision.",
                "her_best": "You can tell him he is loved without being responsible for curing the far-away sadness.",
                "my_best": "Lost in Translation is a clue: the romance thrives in hotel-time, night-time, elsewhere-time.",
                "laura_avatar": "I can love him across distance, but I cannot be his only source of warmth.",
                "amol_avatar": "Cold sea, sleepless night, far away land: the feeling becomes cinematic because the setting is empty enough for her to fill it.",
            },
            {
                "date": "Feb 9 morning",
                "location": "Amol airport/flight toward Tokyo/Hong Kong; Laura trying to survive the week and stay alive by Saturday.",
                "messages": "Jet lag, Tokyo/HK itinerary, sleep masks, not wanting only nice pictures and praise, partnership rather than young/sexy muse, church/chapel beauty, hair/eye contact, safe flight.",
                "simple": "Laura asks for equality. She wants the bond to be partnership, not a one-way engine where her youth and photos make him feel alive.",
                "freud": "The muse refuses object-status. Desire must mature from gaze to reciprocity.",
                "her_mom": "Good. She names the risk directly.",
                "my_mom": "He needs to hear this as a structural point, not reassurance-seeking.",
                "her_best": "This is one of your strongest messages: partnership, not ornament.",
                "my_best": "If you only praise her, you flatten her. She is asking for the harder kind of love.",
                "laura_avatar": "I want to be seen as a person building beside him, not a beautiful feed that regulates him.",
                "amol_avatar": "I want to be my best version for her, which means not reducing her to the feeling she gives me.",
            },
            {
                "date": "Feb 9 evening",
                "location": "Amol sleep-deprived before important dinner; Laura careful not to bother him after a hard exchange.",
                "messages": "They discuss work/prospect language, intensity, sleep deprivation, an apology about something hard, and leaving the phone on if she calls.",
                "simple": "The first meaningful strain appears: intensity has caused hurt or confusion, and both try to preserve care while exhausted.",
                "freud": "The relationship tests whether it can survive frustration, not only idealization. Apology becomes an attempt to repair the object before sleep erases contact.",
                "her_mom": "Exhaustion makes everything sharper. Rest before interpretation.",
                "my_mom": "Leaving the phone on is sweet, but the deeper repair will need waking attention.",
                "her_best": "Do not minimize hurt just because he is tired.",
                "my_best": "Important dinner or not, if you nicked a vulnerable place, repair it clearly.",
                "laura_avatar": "I can give space, but I will remember how it felt.",
                "amol_avatar": "I am sorry it is hard. I want to sleep and also remain reachable, because disappearing would make it worse.",
            },
        ],
    },
    {
        "slug": "chapter-7",
        "number": "07",
        "date": "Feb 10-12, 2026",
        "title": "The Shared Room",
        "summary": "The ChatGPT room becomes part archive, part therapist, part erotic theater, and part decision machine. They talk about messages worth revisiting, vulnerability, sex, hotel plans, grammar, belovedness, and whether anyone else could understand them.",
        "temperature": "Meta-intimacy / escalation",
        "rows": [
            {
                "date": "Feb 10",
                "location": "Between Tokyo/Asia and Europe; tattoos, parents, cultural youth, music links, and sleep.",
                "messages": "Laura jokes about lover tattoos. Amol says his parents did not talk much about love. They discuss calling, sexual health, youth culture, hearts, jokes about real pain, and music requests.",
                "simple": "Family-of-origin enters through a joke. Love talk is not only romance; it is also what each person did or did not learn at home.",
                "freud": "The missing parental love-language becomes a stage on which adult confession feels both thrilling and under-instructed.",
                "her_mom": "I would want to know whether he can talk about love without turning it into spectacle.",
                "my_mom": "He may be learning aloud what his family did not model aloud.",
                "her_best": "When he jokes around real things, keep pointing to the real thing.",
                "my_best": "Your joke reflex is not neutral. It protects you and pokes her at the same time.",
                "laura_avatar": "I notice when he makes the joke exactly where the feeling lives.",
                "amol_avatar": "I want to share my world with people, but sharing it means exposing how strange the machinery is.",
            },
            {
                "date": "Feb 11 early",
                "location": "The ChatGPT room itself; both refer to messages, Dad interview robot, event invites, friends, work mood.",
                "messages": "Amol asks if he should respond in their ChatGPT room. Laura wants to keep using this one and revisit messages. They discuss his dad talking to a robot, event graphics, friend introductions, and taking a bow together.",
                "simple": "The archive becomes sacred. The place where they analyze each other is also where they preserve the best experiences.",
                "freud": "A third mind mediates the dyad. The machine becomes witness, container, and mirror, reducing shame by distributing it into text.",
                "her_mom": "Saving messages can be beautiful, but it can also make the relationship feel more inevitable than it is.",
                "my_mom": "He is making a robot for his father and a room for his lover; both are attempts to preserve voices.",
                "her_best": "The room is romantic because it remembers. Just do not let it become the only judge.",
                "my_best": "You are building an archive before you have built the relationship.",
                "laura_avatar": "I want to go back and see the messages because the text proves the intensity was not imagined.",
                "amol_avatar": "Some of the most beautiful experiences of my life are in this chat; that is absurd and true.",
            },
            {
                "date": "Feb 11 afternoon",
                "location": "Remote but intensely embodied; office, upcoming reunion, fantasies, vulnerability.",
                "messages": "They talk explicitly about sex, vulnerability, wanting closeness, office fantasies, saying love in person, kissing, better sex, boundaries, fantasies, confidence, and not doing things only because the other wants them.",
                "simple": "This is the most sexually and emotionally explicit chapter. The content is not only arousal; it is negotiation of shame, confidence, consent, and how to be wanted without being controlled.",
                "freud": "Erotic speech becomes the substitute body. It also becomes analysis: what pleases, what wounds, what confidence means, and who is allowed to want.",
                "her_mom": "I would not want the details, but I would care whether she feels respected, free, and not pressured.",
                "my_mom": "He must understand that pleasing her requires listening, not just intensifying.",
                "her_best": "The crucial line is: do things because you want them, not because I tell you to.",
                "my_best": "If you are going to play in fantasy, keep the consent architecture extremely real.",
                "laura_avatar": "I want romance, hotness, agency, and confidence; I do not want a man I can simply program.",
                "amol_avatar": "My kink is not extremity; it is her, closeness, words, hair, cheek, neck, and the feeling that she is fully there.",
            },
            {
                "date": "Feb 12",
                "location": "Travel toward London; coffee plans, grammar, hotel/room planning, beloved language.",
                "messages": "They discuss ChatGPT's role, a hurtful joke, flight timing, meeting for coffee, seeing each other properly, bike helmet, understanding each other, 'two truths,' Fitzgerald, belovedness, sex-club fantasy boundaries, and booking a high room with glass/cityscape.",
                "simple": "They are on the edge of reunion. The talk toggles between repair, logistics, language learning, philosophy, and charged anticipation.",
                "freud": "The hotel room is the dream made architectural: height, glass, city, privacy, and a stage for desire to feel legitimate.",
                "her_mom": "A coffee is not just coffee here. It is a threshold.",
                "my_mom": "He is trying to make the setting worthy of the feeling, which is romantic but not sufficient.",
                "her_best": "You want to understand him, but do not lose the fact that you also need him to understand you.",
                "my_best": "Two truths can coexist, but eventually calendars and bodies make choices.",
                "laura_avatar": "We love each other passionately and deeply, and I am still watching whether that can hold in daylight.",
                "amol_avatar": "Nobody would understand us and they would think we were mad; perhaps that is why the private room matters.",
            },
        ],
    },
    {
        "slug": "chapter-8",
        "number": "08",
        "date": "Feb 13-15, 2026",
        "title": "London Reunion, Future Rooms",
        "summary": "The reunion lands in London: meeting halfway, out-of-body intimacy, Indian food, apartment sunlight, songs, missing each other already, children, secrets, his daughters, health, and the first attempt to imagine a future without erasing existing rooms.",
        "temperature": "Embodiment / future rooms",
        "rows": [
            {
                "date": "Feb 13",
                "location": "Gatwick/Thameslink into central London; Laura wants to meet him as soon as he arrives.",
                "messages": "Laura cannot sleep, offers food, rereads and clarifies that she wants to see him and come over when he reaches central London, meet halfway, walk together to his flat, and later says the sex was literally out-of-body.",
                "simple": "The reunion happens as an embodied answer to weeks of text. Logistics turn into touch; anticipation converts into confirmation.",
                "freud": "The journey from airport to flat is a passage from symbolic desire to bodily fact. The body then retroactively validates the whole archive.",
                "her_mom": "Meeting halfway sounds sweet. The out-of-body line tells me this is not contained.",
                "my_mom": "He arrives tired and still the relationship takes over the day.",
                "her_best": "You wanted literally this. That clarity matters, even if the situation is complicated.",
                "my_best": "When someone meets you off a long-haul and still wants more time, that is not ambiguous.",
                "laura_avatar": "I wanted to turn the chat into real time immediately. I did not want politeness; I wanted him.",
                "amol_avatar": "The city arrival becomes a scene because she is there inside it.",
            },
            {
                "date": "Feb 14",
                "location": "London, flats and morning light; Valentine's-adjacent without needing to say it.",
                "messages": "They discuss wooden beams, sunlight in London flats, morning mood, songs from films, coffee nearby, and Amol ending the day with a lot to dream about.",
                "simple": "The romance shifts from hotel/event intensity to possible home aesthetics: sunlight, beams, apartments, morning routines.",
                "freud": "Sunlight in a flat is a domestic fantasy. Desire asks not only 'do you want me?' but 'where would we wake?'",
                "her_mom": "Homes are serious. Talking about light in a flat is talking about a life.",
                "my_mom": "He should notice how quickly dream and real estate have merged.",
                "her_best": "You are inspecting the conditions for mood, home, and future self.",
                "my_best": "This is the point where romance starts wearing a property-viewing jacket.",
                "laura_avatar": "Morning sun matters because mood, body, and home are not separate.",
                "amol_avatar": "I have a lot to dream about because the room has become imaginable.",
            },
            {
                "date": "Feb 15 daytime",
                "location": "After separation or partial separation; London/return travel, church/book/future reading background.",
                "messages": "Amol mentions church and another book about neuroscience of love after Strasbourg. He misses her already; she misses him. She wants sleep and leaves ChatGPT messages.",
                "simple": "After the reunion, the archive resumes. They are already converting experience into theory and future reading.",
                "freud": "The book returns as post-coital theology: can science explain what the body and conscience are doing?",
                "her_mom": "If she is sleep-deprived again, the body is voting for rest even if the heart wants continuation.",
                "my_mom": "He processes love by assigning himself another book.",
                "her_best": "Sleep is not betrayal. Recovery is part of keeping the feeling alive.",
                "my_best": "You two keep trying to read the manual after building the machine mid-flight.",
                "laura_avatar": "I want him to have the messages, but I also need my eight hours if I am going to remain myself.",
                "amol_avatar": "I miss her already, so I reach for a theory that can hold what happened without cheapening it.",
            },
            {
                "date": "Feb 15 evening",
                "location": "Late-night remote recap; future family, his daughters, secrets, health, politics, old rooms/new house.",
                "messages": "They discuss her video/eyes, hot forever, campaign-manager jokes, secrets, not pushing him to share, his daughters possibly never wanting to meet her, old rooms, new house, health, and building a life together.",
                "simple": "The relationship confronts existing family structures. She explicitly says his girls need not accept or meet her and that he should spend all the time with them.",
                "freud": "The children are the reality principle. Fantasy must bow before prior bonds, guilt, and the moral weight of not displacing daughters.",
                "her_mom": "This is the most mature part: she names the children's autonomy and refuses to demand a place.",
                "my_mom": "He needs to protect his daughters and not let romantic future-talk outrun their reality.",
                "her_best": "You were generous here. Make sure generosity does not become self-erasure.",
                "my_best": "This is where the question gets adult: love plus children plus homes plus health is not just vibe.",
                "laura_avatar": "I can want a life with him and still not claim what belongs to his daughters.",
                "amol_avatar": "The old house, new house, rooms, daughters, and future all coexist. I want to keep wowing her, but life is not a blank page.",
            },
        ],
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def nav_links(active_slug: str) -> str:
    links = []
    links.append('<a href="index.html">Overview</a>')
    for chapter in CHAPTERS:
        cls = ' class="active"' if chapter["slug"] == active_slug else ""
        links.append(f'<a{cls} href="{chapter["slug"]}.html">{chapter["number"]}</a>')
    return "\n".join(links)


def shell(title: str, body: str, active_slug: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)} · Relationship Atlas</title>
  <meta name="description" content="A private multi-lens relationship-history atlas built from the January-February 2026 message sequence." />
  <link rel="canonical" href="/archives/2026-05-15-relationship-atlas/" />
  <style>
    :root {{
      color-scheme: dark;
      --bg: #060607;
      --panel: #101113;
      --panel-2: #17191c;
      --ink: #f5efe7;
      --muted: rgba(245, 239, 231, 0.68);
      --quiet: rgba(245, 239, 231, 0.48);
      --line: rgba(245, 239, 231, 0.18);
      --red: #ef5d51;
      --blue: #71a7ff;
      --green: #65d59a;
      --gold: #d8b56d;
      --violet: #b894ff;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; min-height: 100%; background: var(--bg); color: var(--ink); }}
    body {{ overflow-x: hidden; }}
    body {{
      background:
        linear-gradient(90deg, rgba(239, 93, 81, 0.08), transparent 24%, rgba(113, 167, 255, 0.08) 68%, transparent),
        linear-gradient(180deg, #060607 0%, #111216 38%, #060607 100%);
    }}
    a {{ color: inherit; text-decoration: none; }}
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 20;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 14px clamp(16px, 3vw, 34px);
      border-bottom: 1px solid var(--line);
      background: rgba(6, 6, 7, 0.88);
      backdrop-filter: blur(20px);
    }}
    .brand {{
      display: grid;
      gap: 2px;
      min-width: max-content;
    }}
    .brand strong {{
      font-size: 0.78rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
    }}
    .brand span {{
      color: var(--quiet);
      font-size: 0.72rem;
    }}
    .nav {{
      display: flex;
      align-items: center;
      gap: 7px;
      width: 100%;
      max-width: 100%;
      overflow-x: auto;
      scrollbar-width: thin;
      padding-bottom: 2px;
    }}
    .nav a {{
      flex: 0 0 auto;
      min-height: 32px;
      display: inline-grid;
      place-items: center;
      padding: 0 10px;
      border: 1px solid var(--line);
      background: rgba(245, 239, 231, 0.06);
      color: var(--muted);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }}
    .nav a.active, .nav a:hover, .nav a:focus-visible {{
      color: var(--ink);
      border-color: rgba(216, 181, 109, 0.7);
      outline: none;
    }}
    .utility {{
      display: flex;
      gap: 9px;
      flex-wrap: wrap;
      justify-content: flex-end;
      font-size: 0.72rem;
      letter-spacing: 0.13em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    .utility a {{ border-bottom: 1px solid rgba(245, 239, 231, 0.32); padding-bottom: 2px; }}
    main {{ width: min(1680px, 100%); margin: 0 auto; padding: clamp(28px, 5vw, 72px) clamp(14px, 3vw, 34px) 64px; }}
    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(280px, 420px);
      gap: clamp(22px, 4vw, 56px);
      align-items: end;
      margin-bottom: clamp(28px, 5vw, 64px);
    }}
    .kicker {{
      margin: 0 0 12px;
      color: var(--gold);
      font-size: 0.74rem;
      letter-spacing: 0.28em;
      text-transform: uppercase;
    }}
    h1 {{
      margin: 0;
      max-width: min(12ch, 100%);
      font-size: clamp(3.2rem, 9vw, 9.8rem);
      line-height: 0.88;
      letter-spacing: 0;
      text-transform: uppercase;
      overflow-wrap: anywhere;
    }}
    .dek {{
      margin: 20px 0 0;
      max-width: 820px;
      color: var(--muted);
      font-size: clamp(1.02rem, 1.5vw, 1.32rem);
      line-height: 1.6;
    }}
    .meta-panel {{
      display: grid;
      gap: 14px;
      padding: 18px;
      border: 1px solid var(--line);
      background: rgba(16, 17, 19, 0.78);
    }}
    .meta-row {{
      display: grid;
      grid-template-columns: 96px 1fr;
      gap: 12px;
      border-bottom: 1px solid rgba(245, 239, 231, 0.1);
      padding-bottom: 12px;
    }}
    .meta-row:last-child {{ border-bottom: 0; padding-bottom: 0; }}
    .meta-row span:first-child {{
      color: var(--quiet);
      font-size: 0.68rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }}
    .meta-row span:last-child {{ color: var(--ink); line-height: 1.45; }}
    .notice {{
      margin: 0 0 24px;
      max-width: 980px;
      padding: 14px 16px;
      border-left: 3px solid var(--gold);
      background: rgba(216, 181, 109, 0.1);
      color: var(--muted);
      line-height: 1.55;
    }}
    .chapter-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
    }}
    .chapter-card {{
      min-height: 270px;
      display: grid;
      align-content: space-between;
      gap: 20px;
      padding: 18px;
      border: 1px solid var(--line);
      background: linear-gradient(145deg, rgba(23, 25, 28, 0.96), rgba(8, 8, 9, 0.96));
    }}
    .chapter-card:hover, .chapter-card:focus-visible {{
      border-color: rgba(216, 181, 109, 0.72);
      outline: none;
    }}
    .chapter-card .num {{
      color: var(--blue);
      font-size: 0.72rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
    }}
    .chapter-card h2 {{
      margin: 0;
      font-size: 1.3rem;
      line-height: 1.1;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }}
    .chapter-card p {{ margin: 0; color: var(--muted); line-height: 1.5; }}
    .chapter-card .date {{ color: var(--gold); font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase; }}
    .lens-wrap {{
      overflow-x: auto;
      border: 1px solid var(--line);
      background: rgba(8, 8, 9, 0.78);
      box-shadow: 0 28px 90px rgba(0, 0, 0, 0.36);
    }}
    table {{
      width: 2520px;
      min-width: 2520px;
      border-collapse: collapse;
      table-layout: fixed;
    }}
    th, td {{
      width: 230px;
      vertical-align: top;
      border-right: 1px solid rgba(245, 239, 231, 0.13);
      border-bottom: 1px solid rgba(245, 239, 231, 0.13);
      padding: 13px 14px;
      text-align: left;
    }}
    th {{
      position: sticky;
      top: 61px;
      z-index: 10;
      background: #101113;
      color: var(--gold);
      font-size: 0.68rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    td {{
      color: rgba(245, 239, 231, 0.82);
      font-size: 0.92rem;
      line-height: 1.5;
    }}
    tr:nth-child(even) td {{ background: rgba(245, 239, 231, 0.025); }}
    td:first-child, th:first-child {{ width: 120px; color: var(--blue); }}
    td:nth-child(2), th:nth-child(2) {{ width: 210px; }}
    td:nth-child(3), th:nth-child(3) {{ width: 280px; color: var(--ink); }}
    td:nth-child(4), th:nth-child(4) {{ width: 270px; }}
    .chapter-footer {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      margin-top: 24px;
      flex-wrap: wrap;
    }}
    .chapter-footer a {{
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      padding: 0 14px;
      border: 1px solid var(--line);
      background: rgba(245, 239, 231, 0.06);
      color: var(--ink);
      font-size: 0.76rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }}
    @media (max-width: 900px) {{
      .topbar {{ align-items: flex-start; flex-direction: column; }}
      .utility {{ justify-content: flex-start; }}
      .hero {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: clamp(2.5rem, 14vw, 4.6rem); }}
      th {{ top: 122px; }}
      td {{ font-size: 0.86rem; }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <a class="brand" href="index.html"><strong>Relationship Atlas</strong><span>Private edition · Jan 12-Feb 15</span></a>
    <nav class="nav" aria-label="Chapter navigation">
      {nav_links(active_slug)}
    </nav>
    <div class="utility">
      <a href="../../index.html">Cover</a>
      <a href="../../archive.html">Laurarchive</a>
      <a href="../../blog.html">Werkwelt</a>
    </div>
  </header>
  <main>
    {body}
  </main>
  <script src="../../assets/js/password-gate.js"></script>
</body>
</html>
"""


def render_overview() -> str:
    cards = "\n".join(
        f"""<a class="chapter-card" href="{chapter['slug']}.html">
  <div>
    <div class="num">Chapter {chapter['number']} · {esc(chapter['temperature'])}</div>
    <h2>{esc(chapter['title'])}</h2>
  </div>
  <p>{esc(chapter['summary'])}</p>
  <div class="date">{esc(chapter['date'])}</div>
</a>"""
        for chapter in CHAPTERS
    )
    body = f"""
<section class="hero" aria-labelledby="edition-title">
  <div>
    <p class="kicker">New main edition</p>
    <h1 id="edition-title">Laura / Amol Relationship Atlas</h1>
    <p class="dek">A chaptered, multi-lens reading of the combined message sequence from January 12 through February 15, 2026. The pages treat the exchange as a time series: what happened, where it likely happened, what the key messages were, and how the same moment looks through practical, psychoanalytic, family, friend, and avatar lenses.</p>
  </div>
  <aside class="meta-panel" aria-label="Edition metadata">
    <div class="meta-row"><span>Source</span><span>1,512 parsed message lines from <code>quote_candidates.txt</code></span></div>
    <div class="meta-row"><span>Shape</span><span>Overview plus eight chapter webpages</span></div>
    <div class="meta-row"><span>Columns</span><span>Date, location guess, key messages, simple read, Freud, both moms, both best friends, Laura avatar, Amol avatar</span></div>
    <div class="meta-row"><span>Status</span><span>Interpretive private atlas, not a literal transcript or therapeutic diagnosis</span></div>
  </aside>
</section>
<p class="notice">The mom, best-friend, Freudian, and avatar columns are deliberately written as interpretive lenses. They are not claims about what real people said. The Laura and Amol avatar voices are reconstructed from the message dynamics and local site material available in this repository; no external ChatGPT history was available to this build.</p>
<section class="chapter-grid" aria-label="Relationship chapters">
  {cards}
</section>
"""
    return shell("Overview", body)


def render_chapter(chapter: dict, index: int) -> str:
    headers = "".join(f"<th scope=\"col\">{esc(label)}</th>" for _, label in COLUMNS)
    rows = []
    for row in chapter["rows"]:
        cells = "".join(f"<td>{esc(row[key])}</td>" for key, _ in COLUMNS)
        rows.append(f"<tr>{cells}</tr>")
    prev_link = "index.html" if index == 0 else f"{CHAPTERS[index - 1]['slug']}.html"
    next_link = "index.html" if index == len(CHAPTERS) - 1 else f"{CHAPTERS[index + 1]['slug']}.html"
    prev_label = "Overview" if index == 0 else f"Chapter {CHAPTERS[index - 1]['number']}"
    next_label = "Overview" if index == len(CHAPTERS) - 1 else f"Chapter {CHAPTERS[index + 1]['number']}"
    body = f"""
<section class="hero" aria-labelledby="chapter-title">
  <div>
    <p class="kicker">Chapter {chapter['number']} · {esc(chapter['date'])}</p>
    <h1 id="chapter-title">{esc(chapter['title'])}</h1>
    <p class="dek">{esc(chapter['summary'])}</p>
  </div>
  <aside class="meta-panel" aria-label="Chapter metadata">
    <div class="meta-row"><span>Temperature</span><span>{esc(chapter['temperature'])}</span></div>
    <div class="meta-row"><span>Rows</span><span>{len(chapter['rows'])} time slices</span></div>
    <div class="meta-row"><span>Use</span><span>Scroll sideways through the lenses. Each row is one compressed movement inside the chapter.</span></div>
  </aside>
</section>
<div class="lens-wrap" role="region" aria-label="Multi-lens chapter table" tabindex="0">
  <table>
    <thead><tr>{headers}</tr></thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
</div>
<nav class="chapter-footer" aria-label="Chapter pagination">
  <a href="{prev_link}">Previous · {esc(prev_label)}</a>
  <a href="index.html">All Chapters</a>
  <a href="{next_link}">Next · {esc(next_label)}</a>
</nav>
"""
    return shell(chapter["title"], body, chapter["slug"])


def write_manifest() -> None:
    manifest_path = ROOT / "archives" / "manifest.json"
    data = json.loads(manifest_path.read_text())
    entry = {
        "slug": "2026-05-15-relationship-atlas",
        "label": "2026-05-15 · Relationship Atlas",
        "blurb": "Eight-page private multi-lens history of the January-February Laura and Amol message arc.",
        "publishedAt": "2026-05-15",
    }
    data = [item for item in data if item.get("slug") != entry["slug"]]
    data.append(entry)
    manifest_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def write_thumb() -> None:
    THUMB.parent.mkdir(parents=True, exist_ok=True)
    THUMB.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="#ef5d51"/>
      <stop offset="0.42" stop-color="#101113"/>
      <stop offset="1" stop-color="#71a7ff"/>
    </linearGradient>
    <pattern id="grid" width="80" height="80" patternUnits="userSpaceOnUse">
      <path d="M80 0H0V80" fill="none" stroke="rgba(245,239,231,.16)" stroke-width="2"/>
    </pattern>
  </defs>
  <rect width="1200" height="1200" fill="url(#g)"/>
  <rect width="1200" height="1200" fill="url(#grid)"/>
  <g fill="#f5efe7" font-family="Inter, Arial, sans-serif" text-anchor="middle">
    <text x="600" y="430" font-size="78" letter-spacing="16">RELATIONSHIP</text>
    <text x="600" y="540" font-size="150" font-weight="800">ATLAS</text>
    <text x="600" y="650" font-size="44" fill="rgba(245,239,231,.76)">JAN 12 - FEB 15</text>
  </g>
  <g transform="translate(240 760)" fill="none" stroke="#f5efe7" stroke-width="5" opacity=".72">
    <path d="M0 0H720"/>
    <path d="M0 70H720"/>
    <path d="M0 140H720"/>
    <path d="M0 0V140"/>
    <path d="M180 0V140"/>
    <path d="M360 0V140"/>
    <path d="M540 0V140"/>
    <path d="M720 0V140"/>
  </g>
</svg>
"""
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(render_overview())
    for index, chapter in enumerate(CHAPTERS):
        (OUT / f"{chapter['slug']}.html").write_text(render_chapter(chapter, index))
    write_manifest()
    write_thumb()


if __name__ == "__main__":
    main()
