# 🎤 Speaker script — Data Quality · RA 2026

> Wed 23 Sept 2026 · 9:00 → 12:00 · EN · ~40 slides · Eya Akrimi
>
> How to read this: **⏱** = target duration on that slide.
> Everything in *italics* is a cue (question to the room, live demo, joke).
> Everything else is what you can say — paraphrase freely, don't read it.

---

## 0 · The 30 minutes before you start

- ☕  Coffee. Water bottle on the desk.
- 🔌  Plug in your laptop. Second charger if you have one.
- 🖥️  Connect to the projector, mirror mode not extend.
- 🔊  Test audio if you have any video.
- 💻  Open in advance:
  - The deck in **presenter mode** on the projector
  - **Terminal** in `~/Documents/rootsacademy-2026-data-quality` (font size big!)
  - **VS Code** with `soda/checks_starter.yml` open
  - The repo page on **github.com** (in a tab)
  - **Slack** on mute
- 🧪  Run `soda scan -d avocados -c soda/configuration.yml soda/checks_starter.yml` once — confirm you get the expected fails.
- 🎯  Pin the deck link and the repo link in the RA Slack channel so people can copy without asking.
- 😌  Breathe. You know this stuff.

---

## 🗣️ THE SESSION

### Slide 1 — Title  ·  ⏱ 1 min

*Let people walk in, chat, settle. Start at 9:02 sharp — one late person is enough.*

> "Bonjour tout le monde, welcome. Today we're doing data quality — the topic every job description mentions and no one ever teaches you. By noon you'll have written your own DQ checks, run them, broken them on purpose, and hopefully argued with the person next to you about ownership. Let's go."

---

### Slide 2 — Who am I  ·  ⏱ 1 min

*This is your slide, keep it human.*

> "I'm Eya, data engineer at Dataroots. I live in Kessel-Lo just outside Leuven. I'm currently on a data governance project at RVA-ONEM where we're rolling out OpenMetadata — a data catalog with a data quality module — so this stuff isn't theoretical for me right now. I speak French, English and Arabic — please interrupt me in any of them."

*(Add anything specific about your background here.)*

---

### Slide 3 — Agenda  ·  ⏱ 1.5 min

*Walk them through the shape of the morning. Set expectations.*

> "Nine blocks. Three hours. Two of the blocks are non-negotiable: the coffee break at 10:15, and the hands-on at 11. Everything else we time-box loosely — if a question sends us on a tangent that's worth it, we take the tangent. If it isn't, I'll say so and we come back to it at the end."

**Ask:** *"Anyone here already worked with Soda, Great Expectations, or dbt tests? Just raise your hand."* (You'll get a sense of the room.)

---

### Slides 4 & 5 — Knowledge check  ·  ⏱ 3 min total

*Slide 4 is a self-quiz: "how many have you HEARD of?" Slide 5 is the same terms but "how many can you EXPLAIN?"*

> "Look at this word cloud for 30 seconds. Silently count how many you've at least heard of."

*Pause.*

> "Now the same words, different question — how many can you comfortably explain to a colleague?"

*Pause. Then click.*

> "The gap between column 1 and column 2 is what we're going to close this morning. By noon, everything here should be in column 2. If it isn't, ping me after."

---

### Slide 6 — Section 01: Why Data Quality  ·  ⏱ 30 sec

*Just read the section header and move on. Don't linger on section slides.*

> "First question: why do we even care?"

---

### Slide 7 — The cost of bad data (1× vs 10×)  ·  ⏱ 2 min

*Point at the green square, then the ten red ones.*

> "There's a well-known rule from IBM: fixing bad data downstream costs about 10× what it would have cost to prevent it at the source. Which means every hour you spend upstream on quality saves you ten hours of firefighting later. Or, more painfully: every time you skip a DQ check because you're in a rush, you're borrowing time from your future self at 10× interest."

**Personal anecdote you can drop in here** — a time DQ (or lack of it) cost you or your team real hours. Even a small one lands well.

---

### Slide 8 — Five reasons the business cares  ·  ⏱ 2 min

*Walk through the five cards. Don't read each one — pick two and give a real example.*

> "Five reasons the business — meaning the people who pay for your work — cares about DQ. I want to flag two."

> "**Compliance and risk** — GDPR, and now DORA and the AI Act — auditors will ask you 'how do you know your data is accurate?' A shrug is not an answer. Having documented, versioned DQ checks *is* the answer."

> "**Customer trust** — when a customer sees a wrong number on their invoice, they don't say 'oh, must be a data quality issue'. They say 'this company is sloppy'. One bad refund is worth 100 apology emails."

---

### Slide 9 — Three real stories  ·  ⏱ 3 min

*This is where you make it visceral. Do all three quickly.*

> "**Unity Software, 2022.** Ingested bad customer data from one partner. Their ad targeting model went off the rails. Stock dropped 30%, roughly 110 million dollars in revenue impact. The fix? A single DQ check on ingestion. The cost of not having it: their product team's entire next 6 months."

> "**Public Health England, October 2020.** During the peak of COVID. Someone was using the old Excel format that caps at 65,536 rows. Case counts got silently truncated. Roughly 16,000 COVID cases went unreported for a week. Contact tracing was blind. A row-count anomaly check would have caught it in seconds."

> "**Amazon hiring AI, 2018.** They trained a resume-screening model on 10 years of historical hires — which happened to be mostly male. The model learned to downrank women. They scrapped it after 4 years of engineering work. This one's important because the data quality problem wasn't in the pipeline — it was in the label. Sometimes the dirt is what you're trying to predict."

*Beat.*

> "Three different companies, three different sectors, one common thread: nobody was checking."

---

### Slide 10 — Section 02  ·  ⏱ 30 sec

> "OK, so we agree it matters. Now let's define it."

---

### Slide 11 — A working definition  ·  ⏱ 2 min

*Point at the green box.*

> "Data quality is the health of data at every stage in its life cycle. Two things I want you to notice about this definition. First: it's **measurable** — health is a thing you can put a number on, temperature, blood pressure. Second: it's ongoing. Not a project you finish."

*Point at the three things it is NOT.*

> "Three things DQ is not: it's not a one-time cleanup, it's not a metric on a dashboard nobody looks at, and — the most important one — it's not the analytics team's problem alone. Everyone who touches data owns some of it."

---

### Slide 12 — The six dimensions (overview)  ·  ⏱ 2 min

*Don't explain each one yet — just point at the grid and set up the next 6 slides.*

> "There's a standard taxonomy. Six dimensions. This isn't the only framework out there but it's the one you'll hear in every DQ conversation, in every tool's docs, in every job interview. Learn it. Completeness, uniqueness, validity, consistency, accuracy, timeliness. Let's take one slide each."

---

### Slides 13–18 — The six dimensions (one each)  ·  ⏱ ~2 min each, 12 min total

*For each: read the question, give the SQL example, then the tip. Don't over-explain, keep the pace.*

**Slide 13 — Completeness**
> "Is anything missing? The classic. Null in a NOT NULL column. Empty strings. Missing rows for the last hour. Everyone has this check."
> *Tip:* "Not always zero. Sometimes 5% nulls is fine. **Set a threshold, don't wing it.** A hard-coded 'zero' check on a column that's naturally 5% null is a check that cries wolf every day."

**Slide 14 — Uniqueness**
> "Any accidental duplicates? A primary key that isn't actually unique. A CDC job that double-inserted this morning. This one is boring until it isn't."
> *Tip:* "Always check natural keys AND composite keys. `(customer_id, day)` catches things `id` alone will miss."

**Slide 15 — Validity**
> "Does it fit the rules? Negative prices, ages of 250, postal codes that aren't, timestamps in 2099. Every column has an implicit contract. Write the contract down as a check — that's the whole game."

**Slide 16 — Consistency**
> "Same fact, same shape everywhere? BE vs be vs Belgium. USD in one table, EUR in another. This is where data contracts really earn their keep — you push one canonical shape upstream and stop paying the consistency tax downstream."

**Slide 17 — Accuracy**
> "Does it match reality? This is the hardest one. Your DB says 42 units in stock. The warehouse says 39. Which is right? Usually — neither, without going to look. Accuracy usually requires an external source of truth."
> *"How many of you would trust that a Google search result was correct without checking? Same reflex for data."*

**Slide 18 — Timeliness**
> "Is it fresh enough? Your dashboard says 'last updated 3 days ago'. Nobody noticed. The pipeline died on Friday. **Always have a freshness check.** It's the check that catches 'the pipeline is silently broken'. Silent failure is the worst kind."

---

### Slide 19 — Section 03  ·  ⏱ 30 sec

> "OK. You know what to check for. Next question: how do you know what to check on a table you've never seen?"

---

### Slide 20 — Manual vs automated profiling  ·  ⏱ 2 min

> "Two flavors. **Manual** — you plus SQL plus curiosity. Half a dozen `SELECT COUNT(*)` queries, a talk with whoever produces the data. Fastest for a new table. **Automated** — a tool profiles every column for you. Best when you have hundreds of tables or the schema changes weekly."

> "In practice: do a bit of both. Automated to get the lay of the land, manual to interrogate what looks off."

---

### Slide 21 — One line of code → a full report  ·  ⏱ 2 min

*Point at the code.*

> "`ydata-profiling` is the tool I use most often. One line, gives you an HTML report per column: type, missing percent, distribution, correlations, warnings. You can share the HTML with the person who produces the data and have an actual conversation about it. It's a small thing that changes the conversation."

*Warning box at bottom:*

> "One warning — profile a sample of very large tables. A full profile of 10 billion rows will eat your laptop and take 3 hours."

---

### Slide 22 — Can an LLM write your checks?  ·  ⏱ 2 min

*This is a topical slide — expect questions.*

> "Short answer: yes, for the first pass. No, for the last mile. LLMs are great at translating between formats and giving you the 80% you'd write anyway. They're bad at knowing which columns matter, setting thresholds, and understanding your team's on-call rules. **Use them as a co-pilot, not a driver.**"

*If someone asks about specific tools:* mention that most DQ tools now have LLM copilots (Soda has one, dbt Copilot exists) — they're useful but never accept-without-reading.

---

### Slide 23 — ☕ BREAK  ·  ⏱ 15 min (10:15 – 10:30)

> "OK. 15 minutes. Back at 10:30 sharp. Grab coffee, stretch, complain about me to your neighbor."

*(Actually leave the room. Don't stay and answer questions during the break — you need the break too.)*

---

### Slide 24 — Section 04  ·  ⏱ 30 sec

> "Welcome back. Now: where do we put all these checks?"

---

### Slide 25 — Shift-left: catch it early  ·  ⏱ 3 min

*The four-arrow diagram. Walk left to right.*

> "Same rule as slide 7 but bigger. The earlier you catch a bug, the cheaper it is to fix. A schema check at the source system costs one unit of work. Same bug caught by the dashboard downstream? A hundred units — because now three teams need to be paged, an incident report written, and someone has to explain to a director why the number moved."

*Point at each stage.*

> "Source system — the producer's contract. Ingestion — schema and row count, the shape of the thing. Transformation — where dbt tests and Soda scans live, the business rules. Serving — that's dashboards, and by then you're too late for anything but 'sorry'."

> "The rule of thumb: **every check should live at the earliest stage that can enforce it.** A schema check has no business being in the BI tool."

---

### Slide 26 — Who owns the check?  ·  ⏱ 2 min

> "Two columns. Producer-owned checks — schema, business rules the source enforces, freshness at the source. Consumer-owned — anomalies in your slice, reconciliation with your other sources, SLAs for your specific dashboard."

> "The mental model: **the check without an owner is the check that stops running on Tuesday.** Every check needs a name attached — a person or a team. If you can't name the owner, you don't own it, and it won't survive the next quarter's re-org."

---

### Slide 27 — Data contracts in one slide  ·  ⏱ 2 min

*Point at the YAML.*

> "This is a data contract. A YAML file — could be JSON, could be Protobuf — that the producer writes once and every consumer relies on. It says: 'here's the table I promise to give you, here are the columns, here are the rules each column obeys, here's how fresh it will be.'"

> "The point isn't the format. The point is that the promises are **written down and versioned**. When something breaks, it's not a fight about intent — it's a diff against the contract."

> "Not every project needs this. But every project that survives two years does."

---

### Slide 28 — Section 05  ·  ⏱ 30 sec

> "Which tool should you actually reach for? Let's do a quick tour."

---

### Slide 29 — Five tools you'll actually meet  ·  ⏱ 3 min

*The comparison table. Don't read the whole thing — pick a favorite and a "watch out".*

> "Five tools. I'll flag two things."

> "**Soda Core** — what we're about to use. YAML, one CLI command, works against any warehouse. My favorite because as a consultant you land in a new client's stack every 6 months and Soda works everywhere. Watch out: the Cloud UI is a separate product — Soda Cloud — with its own price tag."

> "**dbt tests** — if you're already using dbt for your transformations, use them! Zero extra tools, zero extra pipelines. Only limitation: they only test what dbt models — anything upstream of your dbt project needs a different tool."

> "**Great Expectations** — the OG. Rich, Python-based, notebook-friendly. Overkill if all you want is a YAML file to run in CI."

> "**Elementary and Monte Carlo** — these are data *observability* tools, one level up. They don't just run checks, they learn baselines and alert on anomalies. Elementary is open-source and tied to dbt; Monte Carlo is enterprise SaaS with a real price tag."

> "Today we use Soda Core because I want you to see all the plumbing yourself."

---

### Slide 30 — Section 06: Hands-on  ·  ⏱ 30 sec

> "OK. Laptops open. Let's actually do the thing."

---

### Slide 31 — Setup (5 min)  ·  ⏱ 5 min

*Read the commands slowly. Give them time to type.*

> "Everyone: git clone the repo, install with `uv sync` if you have `uv`, otherwise the venv+pip line. Generate the dirty dataset, then run the first scan. When you see the check results, close your terminal and wait."

*Walk around the room. Help people who are stuck. If someone can't install: pair them with a neighbor for the exercise.*

*Common failures:*
- Python too old → `python3` instead of `python`
- No `uv` → the pip line works
- Behind Talan proxy → they may need `pip install --proxy ...` — have a fallback plan (share your terminal on screen)

---

### Slide 32 — Exercise 1: Your first scan (10 min)  ·  ⏱ 10 min

> "Ten minutes. Run the starter scan, read the output. For each failed check, jot down: which DQ dimension does it cover? Then find the row(s) in the table that are causing it — a `SELECT * WHERE ...` is your friend."

*Circulate. Answer questions. The most likely misunderstanding: they'll think a "FAIL" means the check is broken. Clarify: **a fail means the check found bad data — that's the check doing its job.**"*

---

### Slide 33 — Exercise 2: Write your own checks (15 min)  ·  ⏱ 15 min

> "Fifteen minutes. Create your own checks file. Three checks: one completeness on a column that isn't region, one uniqueness on a combination, and one custom `failed rows` check with a SQL condition you invent. If you finish early, bonus: run the extended checks file and copy patterns you like."

*After 10 minutes, do a quick 'anyone stuck?' round.*

*Common mistakes to watch for:*
- Wrong metric name (`missing` vs `missing_count`)
- Forgetting the `name:` — the report becomes unreadable
- Writing a check that always passes (threshold too loose)

---

### Slide 34 — Exercise 3: Break it on purpose (15 min)  ·  ⏱ 15 min

> "Fifteen minutes. This one is different — you're going to inject bad data on purpose and confirm your checks catch it. Three incidents to simulate, described in the exercise. Discuss with your neighbor: which stage of the pipeline should each check live at?"

*This one has the discussion at the end. Bring the room back together for the last 2-3 minutes:*

**Ask:** *"Should a DQ check block the pipeline when it fails — fail loud — or just alert and let the data through — fail open? Show of hands: fail loud?"* (count) *"Fail open?"* (count) *"Both? Neither?"*

Then say:

> "There's no single right answer. Financial data with regulatory reporting? Fail loud. Marketing dashboards where late-but-correct data beats no data? Fail open. Know which one your team defaults to, and question it."

---

### Slide 35 — Section 07  ·  ⏱ 30 sec

> "OK. Let's land the plane."

---

### Slide 36 — If you remember three things  ·  ⏱ 2 min

> "If you remember only three things from this morning:"

> "**One — DQ is measurable.** The six dimensions give you a checklist. Use them to argue with people — and yourself — about which checks actually matter."

> "**Two — the earlier, the cheaper.** Every check should live at the earliest stage that can enforce it. Shift left whenever you can."

> "**Three — a check needs an owner.** Write it in code, version it, alert on it, and put a name on it. Otherwise it will silently stop running."

---

### Slide 37 — Adopt this on Monday  ·  ⏱ 2 min

> "One assignment for Monday. Pick ONE table on your current project — the one that hurts the most, the one you keep having to explain — and do these six things. Profile it. Write five checks. Run them. Fix or catalog every failure. Wire it into CI. Add your name in the YAML as the owner."

> "That's a morning's work. Do it next week on the next table. In three months you have real DQ coverage on your project and everyone else on the team learns from your PRs. That's how DQ actually shows up in the wild — one table at a time, one person at a time."

---

### Slide 38 — Where to go next  ·  ⏱ 1 min

> "Reading, listening, doing — some starters. The SodaCL reference is genuinely well-written; go there when you're writing your own checks and hit a wall. And come talk to me about the OpenMetadata pilot if that's interesting."

---

### Slide 39 — Q&A  ·  ⏱ 5-10 min

*Open the floor.*

> "Questions? Anything at all. Also — real talk: what surprised you this morning? What did you disagree with?"

**If nobody asks anything**, seed the conversation:
- *"What's the DQ story on the project you're on right now?"*
- *"Anyone here already had a production DQ incident? Tell us."*

See the Q&A prep at the bottom for likely questions.

---

### Slide 40 — Thank you  ·  ⏱ 30 sec

> "Thank you for the attention. Repo link is in the Slack channel. Go make bad data everyone else's problem. Enjoy lunch."

---

## 🆘 If something goes wrong

**Someone's install is failing:** don't try to debug live. Pair them with a working neighbor. Ping them after class.

**The projector dies:** open the deck on your laptop, walk them through it. The exercises don't need slides.

**Nobody's laughing at the jokes:** they're paying attention. Not the same thing. Keep going.

**You lose your place:** it's fine, look at the deck. Say "let me get back on the rail". They'll wait.

**Somebody asks something you don't know:** *"Great question. I don't know off the top of my head — let me get back to you after the session."* Then actually get back to them.

**A question turns into a debate that eats time:** *"I'd love to keep going on this — let's put it in the parking lot and come back after."* Actually keep a parking-lot list on the board.

---

## 🧠 Q&A prep — likely questions

**"Why Soda over Great Expectations?"**
> Both work. Soda's checks are more readable and the CLI is simpler for a first project. GX has a richer expectation library and better notebook workflows. If you're on Python-heavy ML work, GX. If you're on data engineering pipelines against a warehouse, Soda.

**"Can I use this with Databricks / Snowflake / BigQuery?"**
> Yes — Soda has connectors for all of them. The `data_source` block in `configuration.yml` changes, the checks file stays identical. That portability is the whole point.

**"How do I schedule this in production?"**
> Same as any other job. Airflow DAG, GitHub Actions cron, Databricks workflow — whatever your team uses to schedule Python. Soda Cloud does the scheduling for you if you don't want to run your own.

**"What about streaming data?"**
> Different problem. Soda Core is batch-oriented. For streaming DQ, look at things like Flink checkpoint validators, Kafka schema registries, or purpose-built tools like Bytewax. The 6 dimensions still apply, the tools change.

**"Where does this fit with a data catalog like OpenMetadata / Collibra / Alation?"**
> DQ tools produce results, catalogs consume them. Most modern catalogs have a DQ tab that pulls from Soda / GX / dbt tests. OpenMetadata specifically has a built-in DQ module too — I use it on my current project. Ask me about it after.

**"Isn't this just unit tests for data?"**
> Kind of, yes. That's actually the best mental model. Difference: unit tests run on code you wrote against fixed inputs. DQ checks run on data that changes every hour. The check is the same, the flakiness comes from a different place.

**"How do you set thresholds without arbitrary numbers?"**
> Two ways. First: profile historical data and use percentiles — "the check fails when today's null rate is above the 95th percentile of the last 30 days". Second: talk to the producer. Ask "what's the acceptable failure rate for this?" The number they give you is your threshold. If they say "zero", ask if they mean it — often they don't.

**"What if my company won't buy any DQ tool?"**
> Soda Core is free and open source. So is Great Expectations. So is dbt. So are their tests. You don't need to buy anything to start. If you want alerting, freshness detection, a UI — that's when tools like Soda Cloud or Monte Carlo start earning their price tag.

**"How do I convince my team we need this?"**
> Show them the cost of an incident that already happened. Every team has one. Then propose one week on one table. Nobody says no to "let me spend a week making our biggest headache table less painful."

**"How much test coverage is enough?"**
> Wrong question. Right question: "which tables would ruin our week if they broke, and are they covered?" 100% coverage on unimportant tables is worse than 20% coverage on the tables that matter.

**"What about data privacy — GDPR, PII?"**
> Related but different problem. DQ checks operate on the data as it is; PII detection is about *what* the data is (a phone number, a name). Some tools blend both — Great Expectations has PII expectations, Soda has some — but usually you want a dedicated tool (Amundsen, Immuta, a scanner in your catalog) for that.

**"How do we know a passing check means the data is actually good?"**
> You don't. A check tells you the data isn't broken *in the ways you thought to check for*. That's why profiling + fresh eyes + user feedback still matter — the checks catch known-unknowns, not unknown-unknowns.

---

## Timing budget check

| Block         | Target | Notes                              |
| ------------- | ------ | ---------------------------------- |
| Intro         | 6 min  | 5 slides at ~1 min each            |
| Why DQ        | 8 min  | 1 section header + 3 content       |
| 6 dimensions  | 15 min | 1 section + 1 overview + 6 × ~2min |
| Profiling     | 7 min  | 1 section + 3 content              |
| **Break**     | 15 min |                                    |
| Shift-left    | 8 min  | 1 section + 3 content              |
| Tool landscape| 4 min  | 1 section + 1 comparison           |
| Hands-on      | 45 min | 5 min setup + 40 min exercises     |
| Wrap          | 10 min | 5 slides + Q&A                     |
| **Total**     | 118 min | 2 min buffer                       |

You're targeting 118 minutes with a 180-minute window. That's ~1 hour of slack for tangents, laughter, questions, and reality being what it is.

---

**Good luck! You've got this. 🎉**

*If you want anything tweaked — a shorter script, a French translation, more detail on a specific block — just say.*
