# oTree Survey with an Embedded AI Chat Task

An oTree application for online experiments that pair a questionnaire with a live
conversation with an AI chatbot. Participants answer a first set of questions,
then have an open-ended chat with a chatbot whose behaviour is set by the
experimental condition, then answer a second set of questions. The chat is the
experimental stimulus, not the object of study.

The repository was written for one specific study, which is included in full and
can serve as a template. That study — *Humble Answers, Humbler Users?
An Experiment on AI-mediated Intellectual Humility* (master's thesis, University of
Duisburg-Essen)—varied whether the chatbot expressed intellectual humility while
keeping the content of its answers the same, and measured how that affected
participants' own thinking. It was run with 563 participants recruited via
Prolific.

The chat itself builds on [clintmckenna/oTree_gpt](https://github.com/clintmckenna/oTree_gpt), from which this repository is forked. The questionnaires, the progress bar, the Prolific integration and the deployment setup are new.

## What is where

```
intro/            Welcome and consent
survey_pre/       Questions asked before the chat
chat_simple/      The chat task; prompts.py holds the condition prompts
survey_post/      Questions asked after the chat
outro/            Debriefing and return to the recruitment platform
study_progress.py Controls the progress bar shown on every page
```

All questionnaire items — wording, answer options, scale labels — are in the
`__init__.py` file of each survey app. To adapt this to a different study, change
the survey apps and `chat_simple/prompts.py`; the rest works independently of the
topic.

## The chat task

Participants write freely; no fixed questions are given. What distinguishes the
conditions is set entirely in `chat_simple/prompts.py`, which combines shared
instructions with one of two style descriptions and matching example answers.

Before participants can move on, they must spend at least three minutes on the
page and send at least three messages. Neither requirement is shown to them, and
reloading the page does not reset the timer. Model, response length and all three
thresholds are set as constants at the top of `chat_simple/__init__.py`.

## The included study

Two groups, randomly assigned: one chatbot expressed intellectual humility, the
other did not. Both gave comparable information; only the style differed. The
topic was social media bans for children and adolescents under 16. The model was
`gpt-4.1-mini`. Participants went through 24 pages in about 15 minutes.

Assignment happens when the session is created and is a simple coin flip per
participant, so the two groups end up roughly, not exactly, equal in size.

## Setup

Requires Python 3.11 and oTree 6.0.0b10.

```bash
git clone https://github.com/jan-grund/oTree-Survey-with-AI-Chatbot
cd oTree_gpt
pip install -r requirements.txt
cp .env.example .env      # then insert your OpenAI key
otree devserver
```

## Running it live

The study ran with Docker Compose on a single server behind nginx. Two settings
are not optional, and both cost data if you get them wrong.

**Start the app with `otree prodserver`, not `devserver`.** In this oTree version,
`devserver` keeps the whole database in memory and only writes it to disk when the
program shuts down cleanly. Inside a container that rarely happens, so a crash or
an abrupt restart can wipe everything collected so far. `prodserver` saves as it
goes.

**Keep the database file outside the container.** The volume line in
`docker-compose.yml` does this. Without it, the database only exists inside the
container and starts over empty on every rebuild. Create the file before the first
start, otherwise Docker creates a folder with that name instead:

```bash
touch db.sqlite3
docker compose up --build -d
```

One more thing worth knowing: oTree cannot change the shape of an existing
database. Once real participants have started, adding or renaming a question
breaks the running study and you have to start with an empty database. Finish all
changes to the questionnaires before you launch.

## Known limitations
**Code Quality.** This fork was created with Claude Code. As a psychology and computer science student I reviewed the functionality but not every line of code.

**Many participants at once.** The app handles one request at a time while
waiting several seconds for each chatbot reply. I recommend not exceeding 10 simultaneous active chatbot interactions.

**Name of the API key setting.** The code looks for `OPENAI_KEY`. Set that one, as
shown in `.env.example`.

## Citation

If you use this software, please cite oTree and the repositories it builds on:

> Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree — An open-source platform
> for laboratory, online and field experiments. *Journal of Behavioral and
> Experimental Finance, 9*, 88–97.

> Grund, J.-S. (2026). *oTree-Survey-with-AI-Chatbot* [Computer software].
> https://github.com/jan-grund/oTree-Survey-with-AI-Chatbot

> McKenna, C. (2023). *oTree_gpt* [Computer software].
> https://github.com/clintmckenna/oTree_gpt

## License

MIT, inherited from the original repository. See `LICENSE.txt`.
