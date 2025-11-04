from django.core.management.base import BaseCommand
from quiz.models import Course, Session, Question, Choice


class Command(BaseCommand):
    help = 'Load COMP3003 Software Engineering questions into the database'

    def handle(self, *args, **options):
        # Create or get course
        course, created = Course.objects.get_or_create(
            slug='COMP3003',
            defaults={
                'title': 'COMP3003 Software Engineering',
                'description': 'Software Engineering course questions covering software development methodologies, agile practices, and requirements engineering.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created course: {course.title}'))
        else:
            self.stdout.write(f'Course already exists: {course.title}')

        # Session 1: Software Engineering Fundamentals
        session1, created = Session.objects.get_or_create(
            course=course,
            slug='fundamentals',
            defaults={
                'title': 'Software Engineering Fundamentals',
                'is_published': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created session: {session1.title}'))
        else:
            self.stdout.write(f'Session already exists: {session1.title}')

        # Questions for Session 1
        questions1 = [
            {
                'text': 'Which statement about incremental delivery is accurate?',
                'choices': [
                    ('Users only see the system at the very end', False),
                    ('High-priority requirements are delivered early; current-increment requirements are frozen', True),
                    ('Each increment must include the full final feature set', False),
                    ('All requirements are finalized before any increment begins', False),
                ],
                'feedback': 'High-priority requirements are delivered first; requirements for the current increment are frozen.'
            },
            {
                'text': 'Which is a key benefit of incremental development?',
                'choices': [
                    ('No testing at early stages', False),
                    ('Earlier delivery of useful functionality with easier customer feedback', True),
                    ('Complete elimination of refactoring', False),
                    ('Full specification frozen before any coding', False),
                ],
                'feedback': 'It reduces the cost of accommodating change and enables earlier delivery and feedback.'
            },
            {
                'text': 'Which of the following is NOT typically considered an essential attribute of good software?',
                'choices': [
                    ('Maintainability', False),
                    ('Novelty', True),
                    ('Dependability and security', False),
                    ('Efficiency', False),
                ],
                'feedback': 'Maintainability, dependability/security, efficiency, and acceptability are classic essentials; novelty is not.'
            },
            {
                'text': 'When is the classic waterfall model generally most appropriate?',
                'choices': [
                    ('When no documentation is desired', False),
                    ('When rapid, continuous requirement changes are expected', False),
                    ('When only UI prototypes are required', False),
                    ('When requirements are stable and well understood', True),
                ],
                'feedback': 'It fits stable, well-understood requirements.'
            },
            {
                'text': 'Which is a potential disadvantage of a reuse-oriented (integration and configuration) approach?',
                'choices': [
                    ('Requirements compromises and less control over evolution', True),
                    ('Longer delivery time than building from scratch', False),
                    ('Higher risk than bespoke development', False),
                    ('Inability to use any COTS components', False),
                ],
                'feedback': 'Reuse reduces cost and risk but may require requirements compromises and less control over evolution.'
            },
            {
                'text': 'Software engineering is best described as an engineering discipline concerned with:',
                'choices': [
                    ('Only project management', False),
                    ('Only user interface design', False),
                    ('All aspects of software production from specification to maintenance', True),
                    ('Only programming and debugging', False),
                ],
                'feedback': 'It spans specification, development, validation, and evolution.'
            },
            {
                'text': 'The need for systems to work across diverse devices and platforms primarily highlights which issue?',
                'choices': [
                    ('Gamification', False),
                    ('Virtualization only', False),
                    ('Heterogeneity', True),
                    ('Monoculture', False),
                ],
                'feedback': 'Heterogeneity captures diversity in platforms, networks, and device types.'
            },
            {
                'text': 'Which is a common challenge in incremental development if quality work is deferred?',
                'choices': [
                    ('Impossible to gather user feedback', False),
                    ('Guaranteed alignment to all non-functional requirements', False),
                    ('Architecture/structure degradation unless time is invested in refactoring', True),
                    ('Over-documentation of every minor change', False),
                ],
                'feedback': 'Without periodic refactoring, structure degrades as increments accumulate.'
            },
            {
                'text': 'What is a well-known drawback of the waterfall model?',
                'choices': [
                    ('Difficulty accommodating change once phases progress', True),
                    ('Excessive customer involvement', False),
                    ('Absence of documentation', False),
                    ('No testing phase', False),
                ],
                'feedback': 'Accommodating change is difficult after the process is underway.'
            },
            {
                'text': 'In which product type does the customer typically own the specification and decide on changes?',
                'choices': [
                    ('Customized products', True),
                    ('Open-source community projects', False),
                    ('Generic products', False),
                    ('Commercial off-the-shelf tools', False),
                ],
                'feedback': 'Customized products are commissioned by a specific customer who owns the spec and change decisions.'
            },
        ]

        self._load_questions(session1, questions1, 'Session 1')

        # Session 2: Agile Development and Scrum
        session2, created = Session.objects.get_or_create(
            course=course,
            slug='agile-scrum',
            defaults={
                'title': 'Agile Development and Scrum',
                'is_published': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created session: {session2.title}'))
        else:
            self.stdout.write(f'Session already exists: {session2.title}')

        questions2 = [
            {
                'text': 'In Scrum, the primary responsibility of the **ScrumMaster** is to:',
                'choices': [
                    ('Be the technical lead responsible for the entire system architecture design', False),
                    ('Be the full-time representative of the end-user (the customer)', False),
                    ('Define product features and prioritize the Product Backlog', False),
                    ('Ensure the Scrum process is followed and protect the development team from external interference', True),
                ],
                'feedback': 'The ScrumMaster ensures the process is followed, guides the team, and protects them from outside interference.'
            },
            {
                'text': 'In the Scrum agile method, the fixed-length development iteration is called a:',
                'choices': [
                    ('Product Backlog', False),
                    ('Sprint', True),
                    ('Scrum of Scrums', False),
                    ('Velocity', False),
                ],
                'feedback': 'The core development cycle in Scrum is the Sprint, which is fixed in length, usually 2-4 weeks.'
            },
            {
                'text': 'Agile methods are most successful for small, co-located teams. Which factor makes scaling these methods to large systems difficult?',
                'choices': [
                    ('The requirement for only highly-skilled and experienced programmers', False),
                    ('The difficulty in maintaining documentation and development team continuity over a long system lifetime', True),
                    ('The lack of any tools to support continuous integration', False),
                    ('The inability to perform incremental delivery with large software products', False),
                ],
                'feedback': 'Agile\'s informality and reliance on tacit knowledge are difficult to maintain in large, long-lifetime systems where documentation and formal communication are often essential.'
            },
            {
                'text': 'In Extreme Programming (XP), how frequently are increments typically delivered to customers?',
                'choices': [
                    ('Every two weeks', True),
                    ('Twice per year', False),
                    ('Once every six months', False),
                    ('Several times per day', False),
                ],
                'feedback': 'XP is characterized by a high frequency of delivery to the customer.'
            },
            {
                'text': 'Unlike a plan-driven approach, the process outputs (deliverables) in agile development are:',
                'choices': [
                    ('Identical to those produced in a waterfall model', False),
                    ('Decided through a process of continuous negotiation during development', True),
                    ('Planned in detail before the project\'s implementation phase begins', False),
                    ('Completely undocumented and not formally reviewed by stakeholders', False),
                ],
                'feedback': 'Plan-driven approaches define outputs in advance, but in agile, outputs are decided throughout the process via negotiation.'
            },
            {
                'text': 'According to the Agile Manifesto, which of the following is valued *more*?',
                'choices': [
                    ('Contract negotiation', False),
                    ('Comprehensive documentation', False),
                    ('Working software', True),
                    ('Following a detailed plan', False),
                ],
                'feedback': 'The Agile Manifesto emphasizes working code delivered to the customer over extensive formal documentation.'
            },
            {
                'text': 'A defining characteristic of the agile development approach is that it often involves:',
                'choices': [
                    ('Strict adherence to a detailed, pre-planned sequence of separate development stages', False),
                    ('A single, monolithic deployment at the end of the project life cycle', False),
                    ('Producing a complete and stable set of requirements before any coding begins', False),
                    ('The frequent delivery of new software versions or increments', True),
                ],
                'feedback': 'Agile development involves frequent delivery of new versions or increments for evaluation by stakeholders.'
            },
            {
                'text': 'The Extreme Programming (XP) practice of **Refactoring** primarily involves:',
                'choices': [
                    ('Redeveloping the entire system architecture once a year to reflect new technologies', False),
                    ('Anticipating future changes and designing the system architecture to accommodate them', False),
                    ('Writing new unit tests after a new piece of functionality has been completely implemented', False),
                    ('Continuously restructuring and improving the software code to keep it simple and maintainable', True),
                ],
                'feedback': 'Refactoring is the continuous process of improving the code structure and clarity without changing its external behavior, making future changes easier.'
            },
            {
                'text': 'In Extreme Programming (XP), which of the following is a primary benefit of **Pair Programming**?',
                'choices': [
                    ('Spreading knowledge of the system across the development team', True),
                    ('Limiting the number of people who can change a specific part of the code', False),
                    ('Reducing the total working hours required for a software release', False),
                    ('Ensuring strict separation of duties between developers', False),
                ],
                'feedback': 'Pair programming helps spread system knowledge across the team and serves as an immediate, informal code review.'
            },
            {
                'text': 'A core benefit of **Test-first development** in agile methods is that it:',
                'choices': [
                    ('Eliminates the need for any further system-level or acceptance testing', False),
                    ('Allows the final user acceptance tests to be written by the development team alone', False),
                    ('Reduces the project\'s reliance on automated testing tools', False),
                    ('Clarifies the requirements that need to be implemented', True),
                ],
                'feedback': 'Writing tests before the code itself helps clarify exactly what the new functionality is intended to do, ensuring it meets the requirements.'
            },
        ]

        self._load_questions(session2, questions2, 'Session 2')

        # Session 3: Requirements Engineering
        session3, created = Session.objects.get_or_create(
            course=course,
            slug='requirements',
            defaults={
                'title': 'Requirements Engineering',
                'is_published': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created session: {session3.title}'))
        else:
            self.stdout.write(f'Session already exists: {session3.title}')

        questions3 = [
            {
                'text': 'Which of the following is a realistic problem encountered during requirements elicitation?',
                'choices': [
                    ('Elicitation is a one-time activity; requirements do not change thereafter.', False),
                    ('Stakeholders always provide complete and precise technical specifications on the first interview.', False),
                    ('Stakeholders may have conflicting priorities, may not be able to articulate needs clearly, or may change their minds as understanding evolves.', True),
                    ('Only automated questionnaires are necessary; observation and interviews are never needed.', False),
                ],
                'feedback': 'Stakeholders may have conflicting priorities, may not be able to articulate needs clearly, or may change their minds as understanding evolves.'
            },
            {
                'text': 'Which statement about scenarios or use cases is most accurate?',
                'choices': [
                    ('Scenarios (including use cases) describe typical and exceptional sequences of interactions between actors and the system and help reason about required behaviour.', True),
                    ('Scenarios are used only by testers after development is finished.', False),
                    ('Scenarios are complete low-level design documents describing internal algorithms only.', False),
                    ('Use cases replace the need for functional requirements entirely.', False),
                ],
                'feedback': 'Scenarios (including use cases) describe typical and exceptional sequences of interactions between actors and the system and help reason about required behaviour.'
            },
            {
                'text': 'Who should be considered a stakeholder during the requirements activity for a campus administration system?',
                'choices': [
                    ('Only end users who will directly operate the system.', False),
                    ('Anyone affected by or who can influence the system, including students, administrators, IT staff, faculty and external regulators.', True),
                    ('Only the project manager and developers.', False),
                    ('Only external auditors and vendors.', False),
                ],
                'feedback': 'Anyone affected by or who can influence the system, including students, administrators, IT staff, faculty and external regulators.'
            },
            {
                'text': 'How can a non-functional requirement such as a strict response-time constraint influence the project?',
                'choices': [
                    ('Non-functional requirements never affect architecture and can be deferred until after implementation.', False),
                    ('They always only concern the user-interface look-and-feel and nothing else.', False),
                    ('They are expressed only as absolute equations likeand have no role in design.', False),
                    ('It can affect architectural choices, hardware provisioning, and may generate additional functional or design constraints to meet the quality target.', True),
                ],
                'feedback': 'It can affect architectural choices, hardware provisioning, and may generate additional functional or design constraints to meet the quality target.'
            },
            {
                'text': 'Which property makes a non-functional requirement verifiable?',
                'choices': [
                    ('The requirement is written as a vague wish like "the system should be fast" without numbers.', False),
                    ('The requirement includes measurable criteria or an objective test (for example, a specific throughput, latency bound, or error rate) so it can be checked.', True),
                    ('Only functional requirements can be verified; non-functional ones cannot.', False),
                    ('Verifiability requires specifying the implementation language rather than measurable tests.', False),
                ],
                'feedback': 'The requirement includes measurable criteria or an objective test (for example, a specific throughput, latency bound, or error rate) so it can be checked.'
            },
            {
                'text': 'Which option correctly distinguishes functional requirements from non-functional requirements?',
                'choices': [
                    ('Functional requirements state corporate policies while non-functional requirements only list hardware components.', False),
                    ('Functional requirements are always measurable while non-functional requirements are always subjective.', False),
                    ('Functional requirements describe specific services or functions the system must provide; non-functional requirements constrain qualities like performance, reliability, security and usability.', True),
                    ('Functional requirements describe the user interface exclusively; non-functional requirements describe database tables exclusively.', False),
                ],
                'feedback': 'Functional requirements describe specific services or functions the system must provide; non-functional requirements constrain qualities like performance, reliability, security and usability.'
            },
            {
                'text': 'Which statement best captures the primary goal of requirements engineering?',
                'choices': [
                    ('A technique for modeling database schemas only.', False),
                    ('The phase where all system source code is written and integrated.', False),
                    ('The process of discovering, documenting and maintaining the services a system should provide and the constraints on its operation and development.', True),
                    ('An approach to performance tuning and deployment after release.', False),
                ],
                'feedback': 'The process of discovering, documenting and maintaining the services a system should provide and the constraints on its operation and development.'
            },
            {
                'text': 'Which action is NOT part of a sensible requirements change management process?',
                'choices': [
                    ('Prioritising and deciding which changes should be implemented based on business value and risk.', False),
                    ('Automatically accepting all requested changes without impact analysis.', True),
                    ('Assessing the impact, cost and schedule implications of a requested change using traceability links.', False),
                    ('Updating requirements artifacts and notifying affected stakeholders when a change is approved.', False),
                ],
                'feedback': 'Automatically accepting all requested changes without impact analysis.'
            },
            {
                'text': 'What is the main advantage of applying ethnographic observation when analysing user work practices?',
                'choices': [
                    ('It removes the need for validation and testing later in the project.', False),
                    ('It guarantees the final system will require no future changes.', False),
                    ('It is useful only for laboratory experiments and not for business systems.', False),
                    ('It uncovers actual practices, informal workarounds and organisational or social issues that stakeholders might not mention in interviews.', True),
                ],
                'feedback': 'It uncovers actual practices, informal workarounds and organisational or social issues that stakeholders might not mention in interviews.'
            },
            {
                'text': 'Which of the following is an example of a testable (verifiable) usability non-functional requirement?',
                'choices': [
                    ('Users should find the interface attractive and pleasant.', False),
                    ('The system should be easy to use for medical staff.', False),
                    ('Training shall be provided and usability will be determined informally.', False),
                    ('After four hours of training, medical staff shall be able to perform core tasks and the average number of errors by experienced users shall not exceed.', True),
                ],
                'feedback': 'After four hours of training, medical staff shall be able to perform core tasks and the average number of errors by experienced users shall not exceed.'
            },
        ]

        self._load_questions(session3, questions3, 'Session 3')

        self.stdout.write(self.style.SUCCESS('\n[SUCCESS] All questions loaded successfully!'))

    def _load_questions(self, session, questions_data, session_name):
        """Helper method to load questions into a session"""
        existing_count = session.questions.count()
        
        for idx, q_data in enumerate(questions_data, start=1):
            question, created = Question.objects.get_or_create(
                session=session,
                order=existing_count + idx,
                defaults={
                    'text': q_data['text'],
                    'is_active': True
                }
            )
            
            if created:
                # Create choices for this question
                for choice_text, is_correct in q_data['choices']:
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )
                self.stdout.write(f'  [+] Created question {idx}: {question.text[:50]}...')
            else:
                self.stdout.write(f'  [-] Question {idx} already exists, skipping: {question.text[:50]}...')

