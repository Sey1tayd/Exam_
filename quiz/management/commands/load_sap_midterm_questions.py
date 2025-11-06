from django.core.management.base import BaseCommand
from quiz.models import Course, Session, Question, Choice


class Command(BaseCommand):
    help = 'Load SAP Midterm questions into the database'

    def handle(self, *args, **options):
        # Create or get course
        course, created = Course.objects.get_or_create(
            slug='SAP',
            defaults={
                'title': 'SAP',
                'description': 'SAP ERP system questions covering MM, WM, SD, PP, FI, CO, and HR modules.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created course: {course.title}'))
        else:
            self.stdout.write(f'Course already exists: {course.title}')

        # Create Midterm session
        session, created = Session.objects.get_or_create(
            course=course,
            slug='midterm',
            defaults={
                'title': 'Midterm',
                'is_published': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created session: {session.title}'))
        else:
            self.stdout.write(f'Session already exists: {session.title}')

        # All questions for SAP Midterm (34 questions total: 30 multiple-choice + 4 True/False)
        questions = [
            # Multiple-Choice Questions (1-30)
            {
                'text': 'Why is MM the starting point of the supply chain in SAP?',
                'choices': [
                    ('It issues customer invoices', False),
                    ('It maintains employee skills', False),
                    ('It manages purchasing, inventory, and material availability', True),
                    ('It calculates profitability', False),
                ],
                'feedback': 'MM (Materials Management) is the starting point because it manages purchasing, inventory, and material availability, which are fundamental to the supply chain.'
            },
            {
                'text': 'In the cake factory, how does MM interact with PP?',
                'choices': [
                    ('PP buys ingredients; MM plans cakes', False),
                    ('PP plans production; MM ensures materials are available and posts withdrawals', True),
                    ('MM delivers cakes; PP updates stock', False),
                    ('PP sends invoices; MM records revenue', False),
                ],
                'feedback': 'PP (Production Planning) plans production, while MM ensures materials are available and posts withdrawals when materials are used in production.'
            },
            {
                'text': 'During purchasing, how does MM connect with FI?',
                'choices': [
                    ('Debit Vendor, Credit Inventory', False),
                    ('Debit Sales, Credit Customer', False),
                    ('Debit Inventory, Credit Vendor', True),
                    ('Debit Expense, Credit Cash', False),
                ],
                'feedback': 'When MM posts a goods receipt for purchases, FI records: Debit Inventory, Credit Vendor (accounts payable).'
            },
            {
                'text': 'Why is MM–WM integration important?',
                'choices': [
                    ('To schedule shifts', False),
                    ('MM knows *what* is used; WM knows *where* it is stored', True),
                    ('To print invoices', False),
                    ('To design product packaging', False),
                ],
                'feedback': 'MM–WM integration is important because MM knows what materials are used, while WM knows where they are stored (exact bin locations).'
            },
            {
                'text': 'How does MM support SD when an order arrives?',
                'choices': [
                    ('It negotiates prices with customers', False),
                    ('It assigns delivery trucks', False),
                    ('It provides availability info and triggers replenishment if needed', True),
                    ('It produces customer statements', False),
                ],
                'feedback': 'MM supports SD by providing availability information and triggering replenishment if needed when a sales order arrives.'
            },
            {
                'text': 'If MM data (stock/suppliers) is wrong, what can happen?',
                'choices': [
                    ('Faster deliveries', False),
                    ('Over/under-stock and possible production stoppage', True),
                    ('Higher staff morale', False),
                    ('Better profitability tracking', False),
                ],
                'feedback': 'If MM data is wrong, it can lead to over/under-stock situations and possible production stoppage.'
            },
            {
                'text': 'How does WM improve the material flow that starts in MM?',
                'choices': [
                    ('It creates sales orders', False),
                    ('It tracks exact storage bins and updates stock inside the warehouse', True),
                    ('It pays vendors', False),
                    ('It trains workers', False),
                ],
                'feedback': 'WM (Warehouse Management) improves material flow by tracking exact storage bins and updating stock inside the warehouse.'
            },
            {
                'text': 'How can WM improve customer satisfaction?',
                'choices': [
                    ('By reducing marketing costs', False),
                    ('By ensuring accurate, fast, on-time deliveries', True),
                    ('By raising prices', False),
                    ('By hiring more bakers', False),
                ],
                'feedback': 'WM improves customer satisfaction by ensuring accurate, fast, on-time deliveries through efficient warehouse operations.'
            },
            {
                'text': 'Why is the SD module important?',
                'choices': [
                    ('It handles machine maintenance', False),
                    ('It manages everything between company and customer (orders, stock check, delivery)', True),
                    ('It designs products', False),
                    ('It audits taxes', False),
                ],
                'feedback': 'SD (Sales and Distribution) is important because it manages everything between the company and customer: orders, stock check, and delivery.'
            },
            {
                'text': 'How does SD start the process for a cake order?',
                'choices': [
                    ('Posts payroll', False),
                    ('Creates production confirmations', False),
                    ('Records the sales order and checks availability', True),
                    ('Plans employee training', False),
                ],
                'feedback': 'SD starts the process by recording the sales order and checking availability of the requested items.'
            },
            {
                'text': 'How does SD communicate with MM?',
                'choices': [
                    ('"Do we have enough finished cakes/materials?"', True),
                    ('"Which bin stores sugar?"', False),
                    ('"How many shifts tomorrow?"', False),
                    ('"What is the tax rate?"', False),
                ],
                'feedback': 'SD communicates with MM to check if there are enough finished cakes/materials available for the order.'
            },
            {
                'text': 'How does SD work with WM during delivery?',
                'choices': [
                    ('SD books trucks; WM pays drivers', False),
                    ('SD creates delivery doc; WM finds, picks, and prepares cakes for shipment', True),
                    ('SD hires staff; WM trains them', False),
                    ('SD changes recipes; WM updates labels', False),
                ],
                'feedback': 'SD creates the delivery document, while WM finds, picks, and prepares the cakes for shipment.'
            },
            {
                'text': 'Why is SD–MM–WM communication important?',
                'choices': [
                    ('To increase ad revenue', False),
                    ('Without it, company could sell out-of-stock items or wrong quantities', True),
                    ('To reduce utilities', False),
                    ('To pass audits', False),
                ],
                'feedback': 'SD–MM–WM communication is critical because without it, the company could sell out-of-stock items or wrong quantities.'
            },
            {
                'text': 'Why is demand management important in PP?',
                'choices': [
                    ('It reduces taxes', False),
                    ('It balances customer orders with materials/capacity to avoid under/overproduction', True),
                    ('It assigns storage bins', False),
                    ('It handles billing', False),
                ],
                'feedback': 'Demand management in PP is important because it balances customer orders with materials and capacity to avoid under/overproduction.'
            },
            {
                'text': 'How does MRP support production?',
                'choices': [
                    ('Schedules vacations', False),
                    ('Automatically determines required materials and timing for orders/production', True),
                    ('Calculates depreciation', False),
                    ('Sends customer surveys', False),
                ],
                'feedback': 'MRP (Material Requirements Planning) automatically determines required materials and timing for orders and production.'
            },
            {
                'text': 'MRP vs. CRP — key difference?',
                'choices': [
                    ('MRP = capacity; CRP = materials', False),
                    ('MRP = materials; CRP = capacity (machines, labor)', True),
                    ('Both are payroll tools', False),
                    ('Both are tax modules', False),
                ],
                'feedback': 'The key difference: MRP focuses on materials, while CRP (Capacity Requirements Planning) focuses on capacity (machines, labor).'
            },
            {
                'text': 'How does PP integrate with MM and SD?',
                'choices': [
                    ('PP invoices customers directly', False),
                    ('PP takes orders from SD, requests ingredients from MM, returns output to MM/SD', True),
                    ('PP manages vendor payments', False),
                    ('PP assigns delivery trucks', False),
                ],
                'feedback': 'PP integrates by taking orders from SD, requesting ingredients from MM, and returning finished output to MM/SD.'
            },
            {
                'text': 'Why is production confirmation important?',
                'choices': [
                    ('It updates marketing budgets', False),
                    ('It updates material consumption, work completion, and costs in real time', True),
                    ('It creates vendor master data', False),
                    ('It closes fiscal years', False),
                ],
                'feedback': 'Production confirmation is important because it updates material consumption, work completion, and costs in real time.'
            },
            {
                'text': 'Why is FI the "heart of SAP ERP"?',
                'choices': [
                    ('It stores recipes', False),
                    ('All activities (MM, PP, SD, etc.) have financial impact recorded in real time', True),
                    ('It controls hiring', False),
                    ('It designs reports for auditors only', False),
                ],
                'feedback': 'FI is the "heart of SAP ERP" because all activities (MM, PP, SD, etc.) have financial impact that is recorded in real time.'
            },
            {
                'text': 'When MM posts a goods receipt for purchases, FI records:',
                'choices': [
                    ('Dr Vendor / Cr Inventory', False),
                    ('Dr Sales / Cr Customer', False),
                    ('Dr Inventory / Cr Vendor', True),
                    ('Dr Expense / Cr Revenue', False),
                ],
                'feedback': 'When MM posts a goods receipt, FI records: Debit Inventory, Credit Vendor (accounts payable).'
            },
            {
                'text': 'How do FI and SD work when cakes are sold?',
                'choices': [
                    ('SD posts invoice; FI records Dr Customer Receivable, Cr Sales Revenue', True),
                    ('SD records expense; FI credits Inventory', False),
                    ('SD pays vendor; FI debits Cash', False),
                    ('SD creates bins; FI posts payroll', False),
                ],
                'feedback': 'When cakes are sold, SD posts the invoice and FI records: Debit Customer Receivable, Credit Sales Revenue.'
            },
            {
                'text': 'FI vs. CO purpose:',
                'choices': [
                    ('FI external reporting; CO internal cost control', True),
                    ('FI HR planning; CO tax filing', False),
                    ('FI payroll; CO invoicing', False),
                    ('FI warehousing; CO shipping', False),
                ],
                'feedback': 'FI is for external reporting (financial statements), while CO (Controlling) is for internal cost control and analysis.'
            },
            {
                'text': 'Why is real-time integration with FI critical?',
                'choices': [
                    ('To improve taste of cakes', False),
                    ('Managers need up-to-date financials for quick, accurate decisions', True),
                    ('To hire auditors', False),
                    ('To reduce recipe changes', False),
                ],
                'feedback': 'Real-time integration with FI is critical because managers need up-to-date financials for quick, accurate decision-making.'
            },
            {
                'text': 'How does FI support overall financial health?',
                'choices': [
                    ('By consolidating module data into B/S, P&L, Cash Flow for real-time monitoring', True),
                    ('By managing forklifts', False),
                    ('By setting sales targets', False),
                    ('By recruiting bakers', False),
                ],
                'feedback': 'FI supports overall financial health by consolidating module data into Balance Sheet, P&L, and Cash Flow statements for real-time monitoring.'
            },
            {
                'text': 'Why is CO considered the "mirror" of FI?',
                'choices': [
                    ('CO prints tax forms', False),
                    ('FI records external results; CO analyzes internal cost performance (same data, different audience)', True),
                    ('CO stores customer addresses', False),
                    ('FI trains managers', False),
                ],
                'feedback': 'CO is the "mirror" of FI because FI records external results, while CO analyzes internal cost performance using the same data but for a different audience.'
            },
            {
                'text': 'How does CO support PP?',
                'choices': [
                    ('It hires machine operators', False),
                    ('PP sends planned/actual data; CO checks cost vs. plan', True),
                    ('It creates sales orders', False),
                    ('It updates storage bins', False),
                ],
                'feedback': 'CO supports PP by receiving planned/actual data from PP and checking actual costs versus the plan.'
            },
            {
                'text': 'When cakes are sold, how do CO, SD, and FI interact?',
                'choices': [
                    ('SD records sales → FI posts accounting → CO-PA uses revenue & cost to compute profitability', True),
                    ('CO pays customers', False),
                    ('FI assigns bins', False),
                    ('SD runs payroll', False),
                ],
                'feedback': 'When cakes are sold: SD records the sales, FI posts the accounting entries, and CO-PA (Profitability Analysis) uses revenue and cost data to compute profitability.'
            },
            {
                'text': 'If CO data is missing/outdated, what happens?',
                'choices': [
                    ('Better pricing decisions', False),
                    ('Managers miss inefficiencies/cost overruns → wrong pricing/production decisions', True),
                    ('Faster deliveries', False),
                    ('Higher morale', False),
                ],
                'feedback': 'If CO data is missing or outdated, managers miss inefficiencies and cost overruns, leading to wrong pricing and production decisions.'
            },
            {
                'text': 'Why is CO essential for decision-making?',
                'choices': [
                    ('It tracks recipes', False),
                    ('It gives real-time insight into where money is earned/lost by dept/product/customer', True),
                    ('It writes legal contracts', False),
                    ('It controls hiring', False),
                ],
                'feedback': 'CO is essential for decision-making because it provides real-time insight into where money is earned or lost by department, product, or customer.'
            },
            {
                'text': 'Why is HR the "backbone" of SAP modules?',
                'choices': [
                    ('It runs marketing', False),
                    ('Every process depends on people; HR provides accurate employee/time/cost data for other modules', True),
                    ('It manages trucks', False),
                    ('It inspects ovens', False),
                ],
                'feedback': 'HR is the "backbone" because every process depends on people, and HR provides accurate employee, time, and cost data for other modules.'
            },
            {
                'text': 'How does HR interact with FI and CO during payroll?',
                'choices': [
                    ('Sends wage & tax details to FI and CO for accounting and cost allocation', True),
                    ('Updates storage bins', False),
                    ('Creates delivery notes', False),
                    ('Closes customer invoices', False),
                ],
                'feedback': 'During payroll, HR sends wage and tax details to FI and CO for accounting and cost allocation purposes.'
            },
            {
                'text': 'How does HR support PP?',
                'choices': [
                    ('By posting invoices', False),
                    ('By providing shift schedules and available workers', True),
                    ('By ordering sugar', False),
                    ('By renting trucks', False),
                ],
                'feedback': 'HR supports PP by providing shift schedules and information about available workers for production planning.'
            },
            {
                'text': 'Why is Personnel Development important?',
                'choices': [
                    ('To cut all training costs', False),
                    ('Training/skill tracking retains employees, boosts productivity, prepares future leaders', True),
                    ('To avoid audits', False),
                    ('To reduce stock accuracy', False),
                ],
                'feedback': 'Personnel Development is important because training and skill tracking helps retain employees, boosts productivity, and prepares future leaders.'
            },
            {
                'text': 'If HR data is inaccurate/outdated, result is:',
                'choices': [
                    ('Perfect staffing', False),
                    ('Under-staffing, payroll errors, bad decisions → lower efficiency & morale', True),
                    ('Better pricing', False),
                    ('More inventory', False),
                ],
                'feedback': 'If HR data is inaccurate or outdated, it can lead to under-staffing, payroll errors, and bad decisions, resulting in lower efficiency and morale.'
            },
            {
                'text': 'In SAP, a Storage Location is:',
                'choices': [
                    ('A cost center for HR', False),
                    ('The physical area within a Plant where inventory is stored (lowest MM level)', True),
                    ('A sales region', False),
                    ('A vendor\'s office', False),
                ],
                'feedback': 'A Storage Location in SAP is the physical area within a Plant where inventory is stored - it is the lowest level in MM.'
            },
            # True/False Questions (T1-T4)
            {
                'text': 'MM is like the bakery\'s shopping basket and cupboard.',
                'choices': [
                    ('True', True),
                    ('False', False),
                ],
                'feedback': 'True. MM (Materials Management) is indeed like the bakery\'s shopping basket and cupboard - it manages purchasing and inventory.'
            },
            {
                'text': 'WM updates stock but does not know the exact location of ingredients.',
                'choices': [
                    ('True', False),
                    ('False', True),
                ],
                'feedback': 'False. WM (Warehouse Management) does know the exact location of ingredients - it tracks specific storage bins and shelves.'
            },
            {
                'text': 'SD is responsible for customer billing and delivery.',
                'choices': [
                    ('True', True),
                    ('False', False),
                ],
                'feedback': 'True. SD (Sales and Distribution) is responsible for customer billing and delivery processes.'
            },
            {
                'text': 'MM and SD can work completely independently without WM.',
                'choices': [
                    ('True', False),
                    ('False', True),
                ],
                'feedback': 'False. MM and SD cannot work completely independently without WM - WM provides critical warehouse management functionality that supports both modules.'
            },
        ]

        self._load_questions(session, questions)

        self.stdout.write(self.style.SUCCESS('\n[SUCCESS] All SAP Midterm questions loaded successfully!'))
        self.stdout.write(f'Total questions in Midterm: {session.questions.count()}')

    def _load_questions(self, session, questions_data):
        """Helper method to load questions into a session"""
        existing_count = session.questions.count()
        created_count = 0
        updated_count = 0
        
        for idx, q_data in enumerate(questions_data, start=1):
            # Check if question with same text already exists
            question = Question.objects.filter(
                session=session,
                text=q_data['text']
            ).first()
            
            if question:
                # Question exists, update order and ensure it's active
                question.order = idx
                question.is_active = True
                question.save(update_fields=['order', 'is_active'])
                
                # Update choices if they exist, otherwise create them
                existing_choices = list(question.choices.all())
                if len(existing_choices) == len(q_data['choices']):
                    # Update existing choices
                    for choice, (choice_text, is_correct) in zip(existing_choices, q_data['choices']):
                        choice.text = choice_text
                        choice.is_correct = is_correct
                        choice.save(update_fields=['text', 'is_correct'])
                else:
                    # Delete old choices and create new ones
                    question.choices.all().delete()
                    for choice_text, is_correct in q_data['choices']:
                        Choice.objects.create(
                            question=question,
                            text=choice_text,
                            is_correct=is_correct
                        )
                
                updated_count += 1
                self.stdout.write(f'  [~] Updated question {idx}: {question.text[:50]}...')
            else:
                # Create new question
                question = Question.objects.create(
                    session=session,
                    text=q_data['text'],
                    order=idx,
                    is_active=True
                )
                
                # Create choices for this question
                for choice_text, is_correct in q_data['choices']:
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )
                created_count += 1
                self.stdout.write(f'  [+] Created question {idx}: {question.text[:50]}...')
        
        self.stdout.write(f'\nSummary: Created {created_count} questions, updated {updated_count} questions.')

