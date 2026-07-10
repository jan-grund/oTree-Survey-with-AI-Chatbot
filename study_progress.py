"""
Single source of truth for the study-wide progress bar.

oTree apps don't natively know about each other's page counts, so the
global page order/total below is hardcoded. If pages are added, removed,
or reordered in any app, update GLOBAL_PAGE_ORDER (and the per-page
global_progress(N) calls in each app's __init__.py) to match.

GLOBAL_PAGE_ORDER (app_sequence = ['intro', 'survey_pre', 'chat_simple',
'survey_post', 'outro']):

  1  intro/Welcome
  2  intro/Consent
  3  survey_pre/Demographics
  4  survey_pre/Experience
  5  survey_pre/Trust
  6  survey_pre/VerificationBehavior
  7  survey_pre/GIHS
  8  survey_pre/PriorAttitude
  9  survey_pre/KnowledgeSufficiency
  10 survey_pre/InteractionInstruction
  11 chat_simple/chat              <- single live-chat page, fixed step
  12 survey_post/KnowledgeSufficiencyPost
  13 survey_post/VerificationIntention
  14 survey_post/Credibility
  15 survey_post/PerceivedUncertainty
  16 survey_post/PerceivedCompleteness
  17 survey_post/PostAttitude
  18 survey_post/SIHS
  19 survey_post/GIHS_post
  20 survey_post/AIPerception
  21 survey_post/AIHumility
  22 survey_post/Naturality
  23 survey_post/DataQuality
  24 outro/Debriefing
"""

GLOBAL_TOTAL_PAGES = 24


def global_progress(step):
    """step = 1-indexed global page number (see table above)."""
    return dict(
        step=step,
        total=GLOBAL_TOTAL_PAGES,
        percent=round(100 * step / GLOBAL_TOTAL_PAGES),
    )
