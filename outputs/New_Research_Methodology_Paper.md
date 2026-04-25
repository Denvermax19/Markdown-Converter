Self-reported side effects of semaglutide and
tirzepatide in online communities

https://doi.org/10.1038/s44360-026-00108-y

Received: 11 October 2025

Accepted: 12 March 2026

Published online: xx xx xxxx

 Check for updates

Neil K. R. Sehgal
Sharath Chandra Guntuku1,2,4

1,2, Jena Shaw Tronieri3, Lyle Ungar1 &

Social media can reveal patient experiences with glucagon-like peptide-1
receptor agonists (GLP-1 RAs) that extend beyond clinical trial data.
We analysed 410,198 Reddit posts (May 2019–June 2025) mentioning
semaglutide or tirzepatide. A total of 67,008 users self-reported using these
medications, and 43.5% described at least one side effect. Gastrointestinal
symptoms predominated, including nausea (36.9%), fatigue (16.7%),
vomiting (16.3%), constipation (15.3%) and diarrhoea (12.6%). Notably,
reproductive symptoms (for example, menstrual irregularities) and
temperature-related complaints (for example, chills and hot flushes)
emerged as unrecognized potential effects. These findings highlight patient
concerns not well captured in current labelling or trials. Large-scale social
media analysis can complement traditional pharmacovigilance by detecting
emerging safety signals and expanding understanding of the real-world
safety profile of GLP-1 RAs.

Two glucagon-like peptide-1 receptor agonists (GLP-1 RAs), semaglutide
and tirzepatide, have rapidly gained popularity for type 2 diabetes
management and weight control. Clinical trials and regulatory docu-
ments have established gastrointestinal symptoms, such as nausea,
vomiting and diarrhoea, as common side effects of these medications.
Social media data provide the opportunity to capture a broader range
of patient experiences, including symptoms not formally recognized
in drug labelling1. Understanding these real-world reports can help
clinicians and regulators build a more comprehensive safety profile.
In this paper, we systematically characterize self-reported side
effects of semaglutide and tirzepatide shared on Reddit, a social media
platform with over 100 million daily active users anonymously post-
ing in topical forums (subreddits)2. Reddit was selected as the data
source for this study due to its large, publicly accessible, topic-specific
health communities and its long-form, context-rich user discussions.
Prior work has established Reddit as a valuable source for studying
health-related disclosures, including sensitive or stigmatized medi-
cal experiences, and as an important resource for public health and
computational social science research3,4. Unlike other major plat-
forms, which provide either restricted, unreliable or prohibitively

costly application programming interface access, publicly released
researcher-curated corpora have made Reddit data practically feasible
for large-scale public health research.

We conducted a cross-sectional study of self-reported side effects
of semaglutide and tirzepatide using Reddit data from May 2019
through June 2025. Posts and comments were collected from nine
large subreddits that discuss GLP-1 RAs or weight management. We
first identified posts where users disclosed taking semaglutide or
tirzepatide in any Food and Drug Administration-approved formula-
tion for type 2 diabetes or weight management using a generative
pre-trained transformer (GPT)-4o-mini-based classifier. This clas-
sifier also extracted the specific medications mentioned. Among
posts indicating self-use, we applied a GPT-4.1-mini-based classifier
to extract self-reported side effects and map them to Medical Diction-
ary for Regulatory Activities (MedDRA) Preferred Terms (PTs). Across
the May 2019–June 2025 period during which eligible posts appeared,
172,679 of 410,198 Reddit posts mentioning semaglutide or tirzepatide
indicated personal use by 67,008 users. Among them, 29,172 users
(43.5%) reported at least one side effect, with a mean of 2.7 (standard
deviation 2.4) PTs per user.

1Computer and Information Science Department, University of Pennsylvania, Philadelphia, PA, USA. 2Leonard Davis Institute of Health Economics,
University of Pennsylvania, Philadelphia, PA, USA. 3Department of Psychiatry, Perelman School of Medicine, University of Pennsylvania, Philadelphia,
PA, USA. 4Annenberg School for Communication, University of Pennsylvania, Philadelphia, PA, USA.

 e-mail: nsehgal@seas.upenn.edu

Nature Health

nature healthBrief Communication
Table 1 presents the prevalence of PTs among users reporting
side effects. Nausea was most common (36.9%), followed by fatigue
(16.7%), vomiting (16.3%), constipation (15.3%) and diarrhoea (12.6%).
Other symptoms reported by ≥5% of users who disclosed side effects
included decreased appetite, abdominal pain, gastroesophageal reflux,
headache, abdominal distension and dizziness. The most frequent
co-occurring PTs were nausea and vomiting, with 2,917 users (10.0%)
self-reporting both (Supplementary Table 1).

Overall, 65.8% of semaglutide and/or tirzepatide users with side
effects reported at least one gastrointestinal symptom. Psychiatric
symptoms were noted by 12.9%, with anxiety (4.2%) and depression
(2.8%) being most common.

As a secondary analysis, we examined monthly frequencies of the
ten most commonly reported MedDRA PTs. Symptom counts increased
in parallel with overall discussion volume but did not show distinct or
interpretable temporal shifts (Supplementary Fig. 1).

As an exploratory analysis, we conducted a subanalysis of users
who exclusively mentioned one formulation to determine differential
side effect rates. Of the 29,172 users who self-disclosed at least one side
effect, 17,937 (61.5%) exclusively mentioned semaglutide formulations
and 7,125 (24.4%) exclusively mentioned tirzepatide formulations.

We then examined side effect frequencies separately for users
who mentioned semaglutide exclusively (n = 17,937) versus tirzepa-
tide (n = 7,125). Among semaglutide users reporting side effects, the
most commonly reported symptoms were nausea (39.4%), fatigue
(16.1%), vomiting (18.0%), constipation (14.9%) and diarrhoea (12.4%).
Among tirzepatide users reporting side effects, the most commonly
reported symptoms were nausea (28.6%), fatigue (14.7%), vomiting
(11.1%), constipation (12.9%) and diarrhoea (12.5%). Injection site reac-
tions, myalgia, insomnia and temperature-related symptoms (chills
and feeling cold) were each reported by 1–4% of tirzepatide users. A
complete descriptive summary for each formulation is provided in
Supplementary Table 2.

In this large-scale Reddit analysis, over 67,000 semaglutide or
tirzepatide users were identified, with 44% reporting side effects. Con-
sistent with the findings of clinical trials, gastrointestinal symptoms
were reported most commonly by these users5–8. The most frequently
reported gastrointestinal effects were nausea, vomiting, constipation,
diarrhoea and abdominal pain, which are the only adverse reactions
featured as occurring more commonly than with placebo in the Food
and Drug Administration-approved prescribing information for all five
versions of these medications. Additional symptoms reported by ≥5%
of users (for example, decreased appetite, eructation, distension and
dizziness) have similarly been noted in trials as more common than
placebo5–8. Headache, though common in trials, shows mixed placebo
comparisons, while fatigue, Reddit’s second most reported symptom,
has met reporting thresholds in relatively few trials5–8.

We also identified several side effects not previously reported
with semaglutide or tirzepatide. Nearly 4% of Reddit users with
side effects reported reproductive symptoms, notably menstrual
changes like intermenstrual bleeding (0.9%), heavy bleeding (0.9%)
and irregular cycles (0.7%). These rates would be higher in female-only
samples. While weight loss may alleviate some reproductive issues,
both weight gain and loss are linked to menstrual irregularities in
women with obesity9. Further, GLP-1 RAs are thought to impact food
intake, in part, by engaging receptors in the hypothalamus, a brain
region that also plays a central role in menstrual cycle regulation10.
Additionally, some users described symptoms possibly linked to
altered temperature regulation (for example, chills, hot flushes and
pyrexia), warranting further investigation in placebo-controlled trials
or post-market data, particularly due to glucagon’s associations with
increased thermogenesis10.

Strengths of our study include a large and contemporary sample,
the focus on unprompted, self-disclosed experiences, the systematic
classification of symptoms using MedDRA and the development of a

Nature Health

straightforward large language model-based pipeline to detect emerg-
ing, potentially under-reported signals in a timely manner.

Several limitations should be noted. First, patients using weight
loss subreddits may differ from the overall population prescribed
GLP-1 RAs. Specifically, Reddit users tend to be younger, are more
likely to be male and are disproportionately located in the USA11,12.
The demographic composition of Reddit users and self-selection
into health-related discussions limit the generalizability of our find-
ings. Without cross-platform validation or comparison to structured
pharmacovigilance databases, we cannot quantify the magnitude or
direction of these biases. Although Reddit provides one of the largest
and most active online health communities and remains among the
few platforms with accessible, high-volume data, future work should
extend this approach to other sources—such as specialized patient
forums, clinical review platforms or any social media systems that
restore stable application programming interface access—to assess
the consistency of patient-reported symptom patterns across environ-
ments. Our results should be interpreted as hypothesis-generating
signals that require confirmation through traditional surveillance
systems and prospective studies in representative populations13.

Second, because users were not prompted to disclose all side
effects, we cannot estimate their true prevalence. Participation in
health-related subreddits is voluntary, and individuals who experi-
ence more severe, persistent or distressing symptoms may be more
likely to post about them than those with neutral or positive experi-
ences. Even those who reported side effects may not have disclosed
every symptom experienced, and individuals’ beliefs about which
symptoms are potentially attributable to the medication may have
influenced their report. Further, earlier work has found that, while
clinical trials often rely on self-reporting, gastrointestinal symptoms
are often under-reported and inconsistently reported compared with
validated measures for functional gastrointestinal disorders14,15. For
these reasons, self-reported experiences cannot be used to determine
true event frequency or causality. The symptoms discussed here may
be attributable to weight loss itself, changes in comorbidities or other
unrelated factors. Additionally, dosage, route of administration and
treatment duration were inconsistently reported in posts and were
not analysed. Our analysis prioritized breadth of symptom identifica-
tion over temporal granularity. While we examined monthly trends in
common symptoms (Supplementary Fig. 1), detailed assessment of
symptom onset timing or dose–response relationships would require
structured metadata (for example, prescription dates or dose titra-
tion schedules) rarely disclosed in social media posts. Examination of
these variables would require data sources with more complete and
structured medication histories, such as electronic health records or
prospective registries. We were unable to determine when or how fre-
quently these events occurred over the course of treatment or whether
event occurrence depended on patient characteristics, such as the
presence of type 2 diabetes. Results should be viewed as hypothesis-
generating signals about patient-perceived symptoms rather than
estimates of causal effects or true event rates.

Third, natural language processing can misclassify or overlook
nuanced context, and adverse drug event extraction from social media
texts remains an active area of research16. We validated the specific
models deployed in this study against manually annotated samples
and achieved high performance comparable to prior adverse event
extraction systems1,16. While systematic benchmarking across large
language model architectures represents an important direction for
future methods research, our validation approach ensured reliable
extraction for this application. Additionally, certain self-reported
effects may not fit neatly into existing MedDRA concepts or may have
been misclassified based on the user’s description. For example, some
events classified as ‘gastroesophageal reflux’ based on user terminol-
ogy might have instead been recorded as ‘dyspepsia’ in the context of
a clinical trial. In our exploratory subanalysis restricted to users whose

## TABLE IS MISSING(I DELETED FOR SEPARATE CONVERSION)

PTs are grouped by primary system organ classes (bold) in descending order. PTs reported by less
than 0.5% of users and system organ classes reported by less than 1.0% are omitted for brevity.
See Supplementary Table 3 for PTs ordered purely by frequency and Supplementary Tables 4 and
5 for frequencies of corresponding MedDRA high-level terms and high-level group terms.

Brief Communicationhttps://doi.org/10.1038/s44360-026-00108-y

posts exclusively mentioned one formulation, we present descriptive
comparisons of side effect frequencies but do not make formal statisti-
cal inferences about medication-specific effects. Without demographic
and clinical data to match or adjust for confounding between medica-
tion groups, we cannot determine whether observed differences in
complaint frequencies are attributable to the formulations themselves
or to differences in the populations using each formulation. Such analy-
ses would require data sources with detailed patient characteristics to
enable appropriate comparison groups. Future work should stratify
symptom patterns by medication using data sources with richer clinical
context and validated methods for establishing medication-specific
causal effects.

Despite these limitations, social media data provide important
insights into symptoms that are of concern to semaglutide and tirze-
patide users and may be helpful in identifying rarer or under-reported
effects that warrant further investigation. Online health communi-
ties are increasingly influential in shaping patient expectations and
treatment decisions, and a growing body of research examines these
platforms across a range of contexts17–21. Future work could extend
this framework by examining more detailed temporal dynamics in
symptom patterns and how they vary by medication type or for-
mulation; incorporating severity distinctions in patient-reported
symptoms; and evaluating multilingual or non-Reddit digital com-
munities to understand cross-platform and cross-cultural variation
in patient experiences.

Capturing these patient-reported experiences can alert clinicians
and researchers to emerging patient concerns related to GLP-1 RA use.
Our data suggest that clinicians may encounter patient inquiries about
menstrual irregularities and body temperature fluctuations in addition
to commonly reported gastrointestinal symptoms. We recommend
that future prospective trials and post-market surveillance studies
systematically assess fatigue and reproductive symptoms, particularly
menstrual changes in female participants, using validated instruments
rather than relying solely on passive adverse event reporting. These
findings may also inform updates to patient counselling materials
and regulatory labelling to address symptoms of concern better to
patients in real-world settings. We encourage researchers to examine
whether these patient-reported concerns occur more frequently with
semaglutide and/or tirzepatide than with placebo.

Methods
Posts  and  comments  were  collected  from  nine  large  subreddits
(forums) that discuss GLP-1 RAs or weight management. These sub-
reddits were selected to align with those analysed by prior researchers
who estimated real-world weight loss outcomes of these medications22.
Relevant posts and comments containing mentions of semaglutide or
tirzepatide were identified using a list of brand and generic names and
common misspellings. Data were collected for the period 1 January 2015
to 30 June 2025; in practice, all posts that met inclusion criteria were
dated May 2019–June 2025. All data were collected using Pushshift
and Arctic Shift (an extension of Pushshift)23,24. Please see the Supple-
mentary Methods for subreddits used and a full list of search terms.

We first identified posts in which users personally disclosed tak-
ing either semaglutide or tirzepatide in any formulation currently
approved by the Food and Drug Administration for the treatment of
type 2 diabetes or weight management using a GPT-4o-mini based
text classifier (prompt in Supplementary Methods). The classifier also
extracted the specific medications being taken. The classifier’s self-use
performance was evaluated against a manually annotated set of 100
randomly selected posts and had a sensitivity of 86% and specificity of
96%. Only posts that met the self-disclosure criterion were included in
subsequent analyses.

We evaluated the model’s medication extraction accuracy on a
random sample of 100 posts containing 109 medication mentions.
The model achieved a precision of 95% and recall of 98% (F1 = 96%) at

Nature Health

the medication level. Common errors included extracting a specific
medication when the post did not clearly state which drug was being
used, often inferring the medication from the subreddit name (for
example, assuming Ozempic for posts in r/Ozempic) rather than from
explicit mentions in the post content (n = 4), and missing secondary
(non-semaglutide or non-tirzepatide) medications (n = 2). At the post
level, 93.0% of posts had all medications correctly extracted.

Among posts indicating self-use, we applied a second classifier,
based on the GPT-4.1-mini model, to extract self-reported side effects.
Prior work has shown that both classical and transformer-based natu-
ral language processing systems can map free text to standardized
vocabularies such as MedDRA25–27. Our pipeline follows this normali-
zation paradigm but uses a large language model classifier to directly
map side effects mentioned in the user-generated text to standardized
MedDRA PTs using retrieval augmented generation (prompt in Sup-
plementary Methods). Manual evaluation of 100 randomly selected
posts indicated that the classifier had a sensitivity (recall) of 97%
and a positive predictive value (precision) of 87% for identifying the
presence or absence of individual side effects. Because true negatives
cannot be enumerated meaningfully for named entity recognition
models at the span level, specificity is undefined for this granularity.
The classifier extracted 2,013 unique side effect phrases, which were
matched to existing MedDRA PTs via exact matching and manual
review when needed.

Percentages were calculated based on the population of users who
disclosed at least one side effect. Because users were not prompted to
disclose side effects, we cannot estimate their true prevalence. Further,
uncontrolled self-reported experiences cannot be used to determine
causality. The symptoms discussed here may be attributable to weight
loss itself, changes in comorbidities or other unrelated factors.

For users mentioning one formulation exclusively (either semaglu-
tide or tirzepatide but not both), we conducted exploratory descrip-
tive comparisons of side effect frequencies. For each MedDRA PT, we
calculated proportions in each medication group to characterize the
distribution of reported symptoms. These comparisons are presented
descriptively without formal statistical testing, as we lack the demo-
graphic and clinical data necessary to adjust for potential confounding
factors that may differ between users of each medication.

GPT-4o-mini was chosen for self-disclosure classification because,
at the time that component of the study was conducted, it was among
the most capable lightweight models available for large-scale process-
ing at feasible cost. Midway through the project, OpenAI released
GPT-4.1-mini with documented performance improvements over GPT-
4o-mini across a range of tasks including instruction following (https://
openai.com/index/gpt-4-1/), and we therefore used GPT-4.1-mini for
identifying mentions of side effects and mapping them to MedDRA
terms. Larger, reasoning and non-mini models (for example, GPT-4o
or GPT-4.1) were not employed for cost reasons.

All analyses were conducted in Python 3.11 using standard data
processing libraries. Data were collected from publicly accessible
Reddit posts and comments using Pushshift and Arctic Shift during the
study period. No attempts were made to access private or password-
protected content. As data were public and non-identifiable, institu-
tional review board review was not required. Human Ethics and Consent
to Participate declarations were not applicable.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability
All data used in this study are publicly available from Reddit.com or are
accessible via Pushshift and Arctic Shift. Due to Reddit’s Terms of Use,
we are unable to share the raw data. All Reddit data in this study were
used in accordance of Reddit’s Terms of Use.

Brief Communicationhttps://doi.org/10.1038/s44360-026-00108-yCode availability
Code to reproduce the analyses can be found at https://github.com/
sehgal-neil/glp1-side-effects-analysis.

References
1.  Saha, K. et al. A social media study on the effects of psychiatric

medication use. Proc. Int. AAAI Conf. Weblogs Soc. Media 13,
440–451 (2019).

2.  Ceci, L. Reddit: Quarterly Number of DAU 2021–2025, by Online
Status (Statista, accessed 6 August 2025); https://www.statista.
com/statistics/1453133/reddit-quarterly-dau-by-online-status/

3.  Proferes, N., Jones, N., Gilbert, S., Fiesler, C. & Zimmer, M.
Studying reddit: a systematic overview of disciplines,
approaches, methods, and ethics. Soc. Media Soc. https://doi.
org/10.1177/20563051211019004 (2021).

4.  Rai, S. et al. Cross-cultural differences in mental health
expressions on social media. In Proc. 3rd Workshop on
Cross-Cultural Considerations in NLP (C3NLP 2025)
(eds Prabhakaran, V. et al.) 132–142 (Association for
Computational Linguistics, 2025).

5.  Wadden, T. A. et al. Effect of subcutaneous semaglutide vs

17.  Record, R. A., Silberman, W. R., Santiago, J. E. & Ham, T. I sought
it, I Reddit: examining health information engagement behaviors
among Reddit users. J. Health Commun. 23, 470–476 (2018).
18.  Sehgal, N. K., Rader, B. & Brownstein, J. S. Examining the role

of physician characteristics in web-based verified primary care
physician reviews: observational study. J. Med. Internet Res. 26,
e51672 (2024).

19.  Sehgal, N. K. et al. Disparities by race and urbanicity in online

health care facility reviews. JAMA Netw. Open 7, e2446890
(2024).

20.  Sehgal, N. K., Guntuku, S. C., Southwick, L., Merchant, R. M. &

Agarwal, A. K. Online reviews of health care facilities. JAMA Netw.
Open 8, e2524505 (2025).

21.  Javaid, A. et al. Trends in glucagon-like peptide-1 receptor agonist
social media posts using artificial intelligence. JACC Adv. 3,
101182 (2024).

22.  Dhawan, N., Cotta, L., Ullrich, K., Krishnan, R. G. & Maddison, C.

J. End-to-end causal effect estimation from unstructured natural
language data. In Proc. 38th International Conference on Neural
Information Processing Systems 77165–77199 (Curran Associates
Inc., 2024).

placebo as an adjunct to intensive behavioral therapy on
body weight in adults with overweight or obesity: the STEP 3
randomized clinical trial. JAMA 325, 1403–1413 (2021).

23.  Baumgartner, J., Zannettou, S., Keegan, B., Squire, M. &

Blackburn, J. The pushshift reddit dataset. Proc. Int. AAAI Conf.
Web Soc. Media 14, 830–839 (2020).

6.  Aronne, L. J. et al. Tirzepatide as compared with semaglutide for
the treatment of obesity. N. Engl. J. Med. 393, 26–36 (2025).
7.  Garvey, W. T. et al. Tirzepatide once weekly for the treatment of
obesity in people with type 2 diabetes (SURMOUNT-2): a double-
blind, randomised, multicentre, placebo-controlled, phase 3 trial.
Lancet 402, 613–626 (2023).
Jastreboff, A. M. et al. Tirzepatide once weekly for the treatment of
obesity. N. Engl. J. Med. 387, 205–216 (2022).

8.

9.  Ko, K. M. et al. Association between body weight changes and
menstrual irregularity: the Korea National Health and Nutrition
Examination Survey 2010 to 2012. Endocrinol. Metab. 32, 248–256
(2017).

10.  Camilleri, M. & Acosta, A. Newer pharmacological interventions
directed at gut hormones for obesity. Br. J. Pharmacol. 181,
1153–1164 (2024).

11.  Backlinko Team. Reddit user and growth stats. Backlinko

(Internet). 24 September 2025 (cited 22 November 2025).
https://backlinko.com/reddit-users

12.  Statista. Distribution of Reddit.com traffic 2024, by country
(Internet). Statista GmbH (cited 22 November 2025). https://
www.statista.com/statistics/325144/reddit-global-active-user-
distribution/

13.  Golder, S., O’Connor, K., Wang, Y., Klein, A. & Gonzalez

Hernandez, G. The value of social media analysis for adverse
events detection and pharmacovigilance: scoping review.
JMIR Public Health Surveill. 10, e59167 (2024).

14.  Jalleh, R. J., Jones, K. L., Nauck, M. & Horowitz, M. Accurate
measurements of gastric emptying and gastrointestinal
symptoms in the evaluation of glucagon-like peptide-1 receptor
agonists. Ann. Intern. Med. 176, 1542–1543 (2023).

15.  Du, Y. T., Rayner, C. K., Jones, K. L., Talley, N. J. & Horowitz, M.

Gastrointestinal symptoms in diabetes: prevalence, assessment,
pathogenesis, and management. Diabetes Care 41, 627–637
(2018).

16.  Li, H., Zhang, Y., Zhang, Y., Jiang, S. & Dong, B. SRCB at #SMM4H
2024: Making full use of LLM-based data augmentation in
adverse drug event extraction and normalization. In Proc. 9th
Social Media Mining for Health Research and Applications
(SMM4H 2024) Workshop and Shared Tasks (eds Xu, D. &
Gonzalez-Hernandez, G.) 32–37 (Association for Computational
Linguistics, 2024).

Nature Health

24.  Heitmann, A. arctic_shift. GitHub https://github.com/

ArthurHeitmann/arctic_shift (2024).

25.  Chaichulee, S. et al. Multi-label classification of symptom terms
from free-text bilingual adverse drug reaction reports using
natural language processing. PLoS ONE 17, e0270595 (2022).

26.  Durand, J., Stassopoulou, A. & Katakis, I. Adverse drug reaction

classification in social media: a multi-label approach. In 2023
IEEE/WIC International Conference on Web Intelligence and
Intelligent Agent Technology (WI-IAT) 280–286 (IEEE Computer
Society, 2023).

27.  Murphy, R. M. et al. Adverse drug event detection using natural
language processing: a scoping review of supervised learning
methods. PLoS ONE 18, e0279842 (2023).

Acknowledgements
We have no funding to disclose.

Author contributions
N.K.R.S.: conceptualization, methodology, formal analysis,
investigation, data curation and writing—original draft. J.S.T.:
conceptualization, methodology and writing—review and editing. L.U.:
conceptualization, methodology and writing—review and editing.
S.C.G.: conceptualization, methodology, writing—review and editing,
and supervision.

Competing interests
J.S.T. reports receiving an investigator-initiated grant, on behalf of
the University of Pennsylvania, from Novo Nordisk and receiving
consulting fees from Currax Pharmaceuticals, LLC. The other authors
declare no competing interests.

Additional information
Supplementary information The online version
contains supplementary material available at
https://doi.org/10.1038/s44360-026-00108-y.

Correspondence and requests for materials should be addressed to
Neil K. R. Sehgal.

Peer review information Nature Health thanks Michael Horowitz, Eunil
Park and the other, anonymous, reviewer(s) for their contribution