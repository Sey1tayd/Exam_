from django.core.management.base import BaseCommand
from quiz.models import Course, Session, Question, Choice


class Command(BaseCommand):
    help = 'Load COMP3007 Modern Programming Languages Midterm questions into the database'

    def handle(self, *args, **options):
        # Create or get course
        course, created = Course.objects.get_or_create(
            slug='COMP3007',
            defaults={
                'title': 'COMP3007 Modern Programming Languages',
                'description': 'Comparative study of modern programming languages with emphasis on Rust and Go features, safety models, concurrency, and tooling.'
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

        questions = [
            {
                'text': 'Which statement best describes the ownership model in a systems programming language designed for memory safety?\n\nHint: At any time a value has exactly one owner, and the value is dropped when that owner leaves scope.',
                'choices': [
                    ('Each value has exactly one owner; when that owner\'s scope ends, the value is automatically dropped.', True),
                    ('Ownership is only tracked at runtime using reference counts for all values.', False),
                    ('Values can have multiple simultaneous owners by default, and a background collector frees memory later.', False),
                    ('Ownership only applies to stack-allocated values, not heap allocations.', False),
                ],
                'feedback': 'Ownership ensures each value has a single owner at a time; when the owner goes out of scope, the value is dropped. This enables memory safety without a garbage collector.'
            },
            {
                'text': 'Why does returning a reference to a local String fail to compile?\n\nfn bad_ref() -> &String {\n    let s = String::from("temp");\n    &s\n}',
                'choices': [
                    ('Returning references is never allowed, even to values that live longer.', False),
                    ('The problem is only that String cannot be referenced.', False),
                    ('The reference would outlive the local value, creating a dangling reference; the compiler rejects this.', True),
                    ('It compiles, but may segfault at runtime if used after return.', False),
                ],
                'feedback': 'A reference must not outlive the value it refers to. The local s is dropped at the end of the function, so returning &s would create a dangling reference.'
            },
            {
                'text': 'Which statement correctly characterizes the call stack versus the heap?\n\nHint: The stack is structured as a last-in, first-out region and typically stores fixed-size data known at compile time.',
                'choices': [
                    ('Stack: dynamic-size data; Heap: fixed-size compile-time-known data.', False),
                    ('Both stack and heap require manual frees in this language.', False),
                    ('Stack: fast, strictly ordered, fixed-size data; Heap: flexible, dynamic-size allocations with slower allocation/access.', True),
                    ('Heap allocations are always faster than stack allocation.', False),
                ],
                'feedback': 'The stack is fast, strictly ordered, and used for fixed-size, compile-time-known data. The heap is for dynamically sized or unknown-at-compile-time data and is generally slower to allocate.'
            },
            {
                'text': 'What is the primary distinction between concurrent programming and parallel programming?',
                'choices': [
                    ('There is no difference; they are synonymous terms.', False),
                    ('Concurrent programming involves managing multiple tasks at once, while parallel programming involves executing multiple tasks simultaneously.', True),
                    ('Concurrent programming focuses on resource utilization, while parallel programming improves performance.', False),
                    ('Concurrent programming executes tasks simultaneously, while parallel programming manages tasks at once.', False),
                ],
                'feedback': 'Concurrent programming coordinates multiple tasks, whereas parallel programming runs multiple tasks at the same time.'
            },
            {
                'text': 'What is a key advantage of using enums whose variants carry data?',
                'choices': [
                    ('Variants can carry different data, enabling a type-safe representation without a separate "kind" field.', True),
                    ('All variants must carry the same data type.', False),
                    ('Enums cannot implement methods, so data-carrying variants are rarely useful.', False),
                    ('Enums cannot be matched exhaustively with match.', False),
                ],
                'feedback': 'Enums can attach different data to different variants, preventing mismatches and enabling expressive, type-safe designs with pattern matching.'
            },
            {
                'text': 'Which Rust types are commonly used together for safe shared state concurrency across multiple threads?',
                'choices': [
                    ('Channel for sending and Receiver for receiving.', False),
                    ('Future for async computation and Await for blocking.', False),
                    ('Mutex for mutual exclusion and Arc for atomic reference counting.', True),
                    ('Send and Sync traits alone without wrappers.', False),
                ],
                'feedback': 'Arc<T> provides shared ownership across threads, and wrapping the inner T in a Mutex<T> ensures exclusive access while borrowing.'
            },
            {
                'text': 'Which statement best describes the ownership model in a systems programming language designed for memory safety?\n\nHint: At any time a value has exactly one owner, and the value is dropped when that owner leaves scope.',
                'choices': [
                    ('Each value has exactly one owner; when that owner\'s scope ends, the value is automatically dropped.', True),
                    ('Ownership is only tracked at runtime using reference counts for all values.', False),
                    ('Ownership only applies to stack-allocated values, not heap allocations.', False),
                    ('Values can have multiple simultaneous owners by default, and a background collector frees memory later.', False),
                ],
                'feedback': 'Ownership ensures each value has a single owner at a time; when the owner goes out of scope, the value is dropped. This enables memory safety without a garbage collector.'
            },
            {
                'text': 'As highlighted in the slides, which statement about binary size is generally true?',
                'choices': [
                    ('Rust binaries are larger because they always embed a garbage collector.', False),
                    ('Go binaries are always smaller because they are statically linked.', False),
                    ('They are identical in size after link-time optimization.', False),
                    ('Rust release binaries are often smaller than Go binaries, which include a runtime.', True),
                ],
                'feedback': 'Go runtime support code tends to produce larger statically linked binaries, whereas optimized Rust release binaries can be smaller.'
            },
            {
                'text': 'Which statement correctly contrasts Rust and Go error handling?',
                'choices': [
                    ('Rust uses Result<T, E> and the ? operator; Go returns an error value checked with if err != nil.', True),
                    ('Go uses Result<T, E>; Rust returns an error interface.', False),
                    ('Rust ignores errors by default; Go panics on all errors.', False),
                    ('Both rely on exceptions and try/catch blocks by default.', False),
                ],
                'feedback': 'Rust propagates errors with Result and ?, while Go conventions use explicit error results and if err != nil checks.'
            },
            {
                'text': 'What happens when you pass a String by value into a function?\n\nfn takes_ownership(s: String) {\n    println!("{}", s);\n}\n\nConsider the caller\'s ability to use the variable afterward.',
                'choices': [
                    ('The value is implicitly cloned before the call to preserve the caller\'s access.', False),
                    ('The behavior is undefined and depends on optimization level.', False),
                    ('The function receives a reference automatically; the caller still owns and can always use the value.', False),
                    ('Ownership moves into the function; the caller cannot use the original variable afterward unless ownership is returned.', True),
                ],
                'feedback': 'Passing a non-Copy type by value transfers ownership to the callee. The caller must receive ownership back or avoid using the moved binding.'
            },
            {
                'text': 'Which statement about string slices is correct?\n\nlet s = String::from("hello world");\nlet hello: &str = &s[0..5];\n\nNote that a slice is a non-owning view.',
                'choices': [
                    ('Taking a slice moves ownership of the sliced bytes to the slice.', False),
                    ('A string slice is a non-owning reference to a portion of a string; it borrows and does not move or copy the data.', True),
                    ('Slices are only valid for arrays, not for strings.', False),
                    ('A slice always copies the underlying bytes into a new buffer.', False),
                ],
                'feedback': 'A string slice (&str) borrows a view into existing UTF-8 data without copying or taking ownership.'
            },
            {
                'text': 'When does a value get deallocated in this ownership model, assuming normal control flow and no leaks?\n\nThink about the point at which the language calls the destructor automatically.',
                'choices': [
                    ('Only if manually freed by an explicit free()-style call from the programmer.', False),
                    ('At some unspecified later time chosen by a background garbage collector.', False),
                    ('Exactly when the owner variable goes out of scope; the destructor is called automatically.', True),
                    ('Only when the whole program exits.', False),
                ],
                'feedback': 'Values are deterministically dropped when their owner goes out of scope, following RAII-style resource management.'
            },
            {
                'text': 'Which borrowing rule prevents data races and enforces safe aliasing?\n\nRemember: either many read-only aliases or exactly one writable alias at a time.',
                'choices': [
                    ('Only one immutable reference is allowed at a time.', False),
                    ('You may freely mix immutable and mutable references to the same value at any time.', False),
                    ('At any time, you may have any number of immutable references or exactly one mutable reference, but not both.', True),
                    ('Multiple mutable references are always allowed if they are in different functions.', False),
                ],
                'feedback': 'The aliasing XOR mutability rule allows either multiple immutable references or one mutable reference, never both simultaneously.'
            },
            {
                'text': 'When is the if let syntax preferred over a full match?',
                'choices': [
                    ('Only when working with numeric types, not enums.', False),
                    ('It automatically covers all unmatched patterns.', False),
                    ('When exhaustive handling of multiple patterns is required.', False),
                    ('When only one specific pattern matters and other cases can be ignored or handled by else.', True),
                ],
                'feedback': 'Use if let for succinctly handling a single pattern of interest; match shines when exhaustive pattern coverage is needed.'
            },
            {
                'text': 'Which Rust traits are used to ensure types can be safely transferred and shared between threads?',
                'choices': [
                    ('Borrow for references and Own for ownership.', False),
                    ('Send for transferring between threads and Sync for sharing between threads.', True),
                    ('Clone for copying data and Drop for cleanup.', False),
                    ('Mutex for locking and Arc for reference counting.', False),
                ],
                'feedback': 'Send indicates ownership transfer across threads is safe; Sync means shared references may be accessed from multiple threads safely.'
            },
            {
                'text': 'According to Rust\'s orphan rule (part of its coherence rules), which of the following trait implementations is permitted?',
                'choices': [
                    ('In your crate, implementing a trait from crate A for a type from crate B.', False),
                    ('Any implementation is allowed as long as you use the unsafe keyword.', False),
                    ('In your crate, implementing an external trait (Display) for an external type (Vec<T>).', False),
                    ('In your crate, implementing a trait you defined (MyTrait) for an external type (String).', True),
                ],
                'feedback': 'The orphan rule allows an implementation when either the trait or the type is local to your crate; defining your trait and implementing it for String is allowed.'
            },
            {
                'text': 'When does a value get deallocated in this ownership model, assuming normal control flow and no leaks?\n\nThink about the point at which the language calls the destructor automatically.',
                'choices': [
                    ('Only when the whole program exits.', False),
                    ('At some unspecified later time chosen by a background garbage collector.', False),
                    ('Only if manually freed by an explicit free()-style call from the programmer.', False),
                    ('Exactly when the owner variable goes out of scope; the destructor is called automatically.', True),
                ],
                'feedback': 'Values are deterministically dropped when their owner goes out of scope, following RAII-style resource management.'
            },
            {
                'text': 'In Rust\'s error handling philosophy, what is the fundamental distinction between using panic! and returning a Result<T, E>?',
                'choices': [
                    ('panic! is used in applications, while Result is used in libraries.', False),
                    ('panic! is for runtime errors, while Result is for compile-time errors.', False),
                    ('panic! throws an exception, while Result is an error code.', False),
                    ('panic! is for unrecoverable errors, while Result is for recoverable errors.', True),
                ],
                'feedback': 'panic! indicates an unrecoverable situation and unwinds or aborts; Result<T, E> models recoverable errors to be handled by the caller.'
            },
            {
                'text': 'Which describes Go\'s cross-compilation experience?',
                'choices': [
                    ('Limited to the host OS and CPU architecture.', False),
                    ('Only works for WebAssembly targets out of the box.', False),
                    ('Built-in: set GOOS/GOARCH and run go build.', True),
                    ('Requires external toolchains and custom linkers for every target.', False),
                ],
                'feedback': 'Go\'s toolchain includes first-class cross-compilation support via GOOS and GOARCH environment variables.'
            },
            {
                'text': 'Which statement about associated functions is true?',
                'choices': [
                    ('They have no self parameter and are called with Type::function(...).', True),
                    ('They must be pub to be callable.', False),
                    ('They can only return Self by value.', False),
                    ('They require &self and are called with instance.method(...).', False),
                ],
                'feedback': 'Associated functions omit a self receiver and are invoked with the type name, like Type::new().'
            },
            {
                'text': 'What is the idiomatic way to count word frequencies using a HashMap?',
                'choices': [
                    ('Rebuild the entire HashMap for each word seen.', False),
                    ('Insert every key unconditionally, then read and increment a copy.', False),
                    ('Use get to read a value and increment without writing it back.', False),
                    ('Use entry(key).or_insert(0) to get a mutable reference and increment it.', True),
                ],
                'feedback': 'Using the entry API avoids double lookups: let count = map.entry(word).or_insert(0); *count += 1;.'
            },
            {
                'text': 'What is a race condition in concurrent programming?',
                'choices': [
                    ('A buffer overflow caused by concurrent writes.', False),
                    ('An invalid memory access occurring after data is freed.', False),
                    ('A situation where multiple threads access shared data and the outcome depends on the timing of thread execution.', True),
                    ('When threads wait for each other indefinitely, causing a deadlock.', False),
                ],
                'feedback': 'Race conditions arise when scheduling order affects shared state, leading to unpredictable results.'
            },
            {
                'text': 'What happens when you pass a String by value into a function?\n\nfn takes_ownership(s: String) {\n    println!("{}", s);\n}',
                'choices': [
                    ('Ownership moves into the function; the caller cannot use the original variable afterward unless ownership is returned.', True),
                    ('The value is implicitly cloned before the call to preserve the caller\'s access.', False),
                    ('The behavior is undefined and depends on optimization level.', False),
                    ('The function receives a reference automatically; the caller still owns and can always use the value.', False),
                ],
                'feedback': 'Moving a String into the function transfers ownership; the caller must not use the moved variable unless ownership is returned.'
            },
            {
                'text': 'What is a deadlock in concurrent programming?',
                'choices': [
                    ('A scenario where threads wait for each other indefinitely, each holding resources the other needs.', True),
                    ('A race condition where timing affects shared data access.', False),
                    ('Use of memory after it has been freed in multiple threads.', False),
                    ('When threads share state without proper synchronization.', False),
                ],
                'feedback': 'Deadlocks occur when cyclical waits on resources prevent any thread from making progress.'
            },
            {
                'text': 'What is the key performance and flexibility difference between using a generic trait bound (e.g., fn foo<T: Draw>(item: &T)) and a trait object (e.g., fn foo(item: &dyn Draw))?',
                'choices': [
                    ('Trait bounds only work on structs, while trait objects work on enums.', False),
                    ('Trait bounds use static dispatch (compile-time), while trait objects use dynamic dispatch (runtime).', True),
                    ('Trait bounds require heap allocation, while trait objects work on the stack.', False),
                    ('Trait bounds allow heterogeneous collections, while trait objects do not.', False),
                ],
                'feedback': 'Generics are monomorphized for static dispatch; trait objects erase type information and dispatch through a vtable at runtime.'
            },
            {
                'text': 'Given a borrowed string reference, which statement is true about mutating the underlying data?\n\nfn change(s: &String) { /* ??? */ }',
                'choices': [
                    ('You can always mutate through any reference if the original binding was declared mut.', False),
                    ('You must borrow as &mut String to mutate; &String does not allow mutation.', True),
                    ('Mutation is never allowed through references in this language.', False),
                    ('Mutation is allowed if there are also other immutable references alive.', False),
                ],
                'feedback': 'Immutable borrows (&String) forbid mutation; you need a unique mutable borrow (&mut String) to modify the data.'
            },
            {
                'text': 'In many cases, Rust\'s lifetime elision rules allow you to omit explicit lifetime annotations. Which of the following is a primary rule of lifetime elision?',
                'choices': [
                    ('A lifetime is never required for structs.', False),
                    ('If there is exactly one input reference, its lifetime is assigned to all output references.', True),
                    ('All output references are automatically given the \'static lifetime.', False),
                    ('If a function returns a reference, it must be created inside that function.', False),
                ],
                'feedback': 'With exactly one input reference, the compiler assumes the output reference uses that lifetime, avoiding explicit annotations.'
            },
            {
                'text': 'Which construct is generally most appropriate when modeling long-lived domain data that benefits from named fields and self-documenting code?',
                'choices': [
                    ('A struct, because it offers named fields and clarity for long-lived domain data.', True),
                    ('A struct, but only if it will never have methods associated with it.', False),
                    ('A tuple, because field order does not matter when constructing it.', False),
                    ('A tuple, because it supports named fields for readability.', False),
                ],
                'feedback': 'Structs provide descriptive field names and are ideal for modeling complex, persistent data structures.'
            },
            {
                'text': 'In Rust, behavior abstraction (similar to Go\'s interfaces) is provided by:',
                'choices': [
                    ('Mixins', False),
                    ('Traits', True),
                    ('Classes', False),
                    ('Prototypes', False),
                ],
                'feedback': 'Traits define shared behavior that types can implement, analogous to Go interfaces.'
            },
            {
                'text': 'Despite compile-time ownership checks, which situation can still lead to a memory leak?\n\nConsider reference-counted pointers forming cycles.',
                'choices': [
                    ('Creating cyclic structures with reference-counted smart pointers so their counts never reach zero.', True),
                    ('Assigning small integers between variables repeatedly.', False),
                    ('Returning references to local variables from functions.', False),
                    ('Dropping a value twice due to multiple owners of the same raw pointer.', False),
                ],
                'feedback': 'Reference cycles with Rc or Arc can prevent counts from reaching zero, leaking memory despite safety guarantees.'
            },
            {
                'text': 'Consider the following code:\n\nlet s1 = String::from("hello");\nlet s2 = s1;\n// println!("{}", s1);\n\nWhat is the effect of the move from s1 to s2?',
                'choices': [
                    ('Both s1 and s2 remain valid aliases to the same heap buffer.', False),
                    ('The assignment performs an implicit deep copy of the heap data.', False),
                    ('The code compiles, but s1 prints an empty string.', False),
                    ('s1 is moved into s2, and using s1 afterward is a compile-time error.', True),
                ],
                'feedback': 'Moving a String transfers ownership and invalidates the source binding to prevent double free or use-after-free.'
            },
            {
                'text': 'Which statement best reflects Rust\'s design philosophy as discussed in Week 2?',
                'choices': [
                    ('Dynamic typing with runtime checks for safety.', False),
                    ('Automatic memory management with a concurrent garbage collector.', False),
                    ('Memory safety without a garbage collector via ownership and borrowing.', True),
                    ('Primarily an interpreted scripting language for fast iteration.', False),
                ],
                'feedback': 'Rust emphasizes compile-time guarantees for memory safety without relying on a garbage collector.'
            },
            {
                'text': 'Which statement correctly characterizes the call stack versus the heap?\n\nHint: The stack is structured as a last-in, first-out region and typically stores fixed-size data known at compile time.',
                'choices': [
                    ('Both stack and heap require manual frees in this language.', False),
                    ('Heap allocations are always faster than stack allocation.', False),
                    ('Stack: fast, strictly ordered, fixed-size data; Heap: flexible, dynamic-size allocations with slower allocation/access.', True),
                    ('Stack: dynamic-size data; Heap: fixed-size compile-time-known data.', False),
                ],
                'feedback': 'The stack is fast, strictly ordered, and used for fixed-size, compile-time-known data. The heap is for dynamically sized or unknown-at-compile-time data and is generally slower to allocate.'
            },
            {
                'text': 'What is the primary function of the ? operator when used on a Result value in a Rust function?',
                'choices': [
                    ('It unwraps the Ok value, or returns the Err value from the current function.', True),
                    ('It converts the Result to an Option, discarding the error message.', False),
                    ('It prints the error to stderr but continues execution.', False),
                    ('It forces a panic! if the value is Err.', False),
                ],
                'feedback': 'The ? operator is sugar for propagating errors: Ok values unwrap, Err values are returned early.'
            },
            {
                'text': 'Which construct provides pattern matching in Rust?',
                'choices': [
                    ('select statement.', False),
                    ('switch statement identical to C.', False),
                    ('case blocks on labels without patterns.', False),
                    ('match expression.', True),
                ],
                'feedback': 'The match expression enables exhaustive pattern matching across Rust types.'
            },
            {
                'text': 'What concurrency model is Go known for?',
                'choices': [
                    ('Greenlets with implicit cooperative scheduling only.', False),
                    ('Actor model with mailboxes and supervisors.', False),
                    ('Fork/join via POSIX processes by default.', False),
                    ('CSP-style concurrency with goroutines and channels.', True),
                ],
                'feedback': 'Go embraces Communicating Sequential Processes (CSP) with lightweight goroutines and channel-based communication.'
            },
            {
                'text': 'What happens when you assign a small, fixed-size integer to another variable?\n\nlet x: i32 = 5;\nlet y = x;',
                'choices': [
                    ('The assignment performs a deep heap allocation and copy.', False),
                    ('The value is copied; both variables are usable because the type implements Copy.', True),
                    ('The value is moved; the original variable becomes invalid.', False),
                    ('It is undefined which variable holds the value after assignment.', False),
                ],
                'feedback': 'Copy types like i32 are trivially duplicated on assignment, leaving both bindings valid.'
            },
            {
                'text': 'Which of the following method signatures, if added to a trait, would make that trait not object-safe, preventing it from being used as a trait object (e.g., Box<dyn MyTrait>)?',
                'choices': [
                    ('fn new_instance() -> Self;', True),
                    ('fn get_name(&self) -> String;', False),
                    ('fn default_behavior(&self) -> &str { "default" }', False),
                    ('fn do_something(&self);', False),
                ],
                'feedback': 'Returning Self makes the trait unsuitable for trait objects because the concrete type is unknown at compile time.'
            },
            {
                'text': 'How does Rust achieve "zero-cost abstractions" for generic code (e.g., functions or structs defined with <T>)?',
                'choices': [
                    ('Through monomorphization, where the compiler generates specialized code for each concrete type used.', True),
                    ('By using dynamic dispatch (v-tables) for all generic types.', False),
                    ('By requiring all generic types to be boxed on the heap.', False),
                    ('By type-erasing all generic parameters at runtime.', False),
                ],
                'feedback': 'Monomorphization clones generic code per concrete type, enabling compile-time specialization without runtime overhead.'
            },
            {
                'text': 'Which domain is more commonly Go-dominated per the Week 2 slides?',
                'choices': [
                    ('AAA game engine inner loops.', False),
                    ('Cloud-native microservices and DevOps tooling.', True),
                    ('Bare-metal firmware for tiny MCUs exclusively.', False),
                    ('Kernel drivers and hard real-time control loops.', False),
                ],
                'feedback': 'Go thrives in cloud-native services, DevOps tooling, and infrastructure automation.'
            },
            {
                'text': 'Which approach is idiomatic for transforming an Option and providing a default in case it is None?',
                'choices': [
                    ('Treat Option like null; no explicit handling is needed.', False),
                    ('Use a match for every case; there are no helper methods for Option.', False),
                    ('Use .map(...) to transform and .unwrap_or(...) (or .unwrap_or_else(...)) to supply a default.', True),
                    ('Always call .unwrap(), which is safe even if the value is None.', False),
                ],
                'feedback': 'Combinators like map and unwrap_or enable concise Option handling without panicking on None.'
            },
            {
                'text': 'Consider the following code:\n\nlet s1 = String::from("hello");\nlet s2 = s1;\n// println!("{}", s1);\n\nWhat is the effect of the move from s1 to s2?',
                'choices': [
                    ('The assignment performs an implicit deep copy of the heap data.', False),
                    ('s1 is moved into s2, and using s1 afterward is a compile-time error.', True),
                    ('The code compiles, but s1 prints an empty string.', False),
                    ('Both s1 and s2 remain valid aliases to the same heap buffer.', False),
                ],
                'feedback': 'Once s1 is moved, it cannot be used; s2 now owns the String.'
            },
            {
                'text': 'Despite compile-time ownership checks, which situation can still lead to a memory leak?\n\nConsider reference-counted pointers forming cycles.',
                'choices': [
                    ('Dropping a value twice due to multiple owners of the same raw pointer.', False),
                    ('Assigning small integers between variables repeatedly.', False),
                    ('Creating cyclic structures with reference-counted smart pointers so their counts never reach zero.', True),
                    ('Returning references to local variables from functions.', False),
                ],
                'feedback': 'Strong reference cycles with Rc or Arc keep counts above zero, preventing automatic cleanup.'
            },
            {
                'text': 'What happens when you assign a small, fixed-size integer to another variable?\n\nlet x: i32 = 5;\nlet y = x;',
                'choices': [
                    ('The value is copied; both variables are usable because the type implements Copy.', True),
                    ('It is undefined which variable holds the value after assignment.', False),
                    ('The value is moved; the original variable becomes invalid.', False),
                    ('The assignment performs a deep heap allocation and copy.', False),
                ],
                'feedback': 'Copy types duplicate their bits on assignment, leaving the original binding intact.'
            },
            {
                'text': 'Which borrowing rule prevents data races and enforces safe aliasing?\n\nRemember: either many read-only aliases or exactly one writable alias at a time.',
                'choices': [
                    ('You may freely mix immutable and mutable references to the same value at any time.', False),
                    ('At any time, you may have any number of immutable references or exactly one mutable reference, but not both.', True),
                    ('Only one immutable reference is allowed at a time.', False),
                    ('Multiple mutable references are always allowed if they are in different functions.', False),
                ],
                'feedback': 'You may hold many immutable references or one mutable reference, but never both simultaneously.'
            },
            {
                'text': 'What is the safest way to access a vector element when the index might be out of bounds?',
                'choices': [
                    ('Rely on compiler checks; panics cannot occur on vector indexing.', False),
                    ('Clone the vector first, then index it.', False),
                    ('Call v.get(index) and handle the returned Option.', True),
                    ('Use v[index] because it returns Option and will not panic.', False),
                ],
                'feedback': 'Vec::get returns Option<&T>, allowing graceful handling of missing elements without a panic.'
            },
            {
                'text': 'Which statement about string slices is correct?\n\nlet s = String::from("hello world");\nlet hello: &str = &s[0..5];\n\nNote that a slice is a non-owning view.',
                'choices': [
                    ('A slice always copies the underlying bytes into a new buffer.', False),
                    ('Taking a slice moves ownership of the sliced bytes to the slice.', False),
                    ('A string slice is a non-owning reference to a portion of a string; it borrows and does not move or copy the data.', True),
                    ('Slices are only valid for arrays, not for strings.', False),
                ],
                'feedback': 'A string slice (&str) borrows a view into existing UTF-8 data without copying or taking ownership.'
            },
            {
                'text': 'What does the move keyword do when used with a closure in a Rust thread spawn?',
                'choices': [
                    ('It synchronizes access to shared data between threads.', False),
                    ('It converts the closure into an asynchronous future.', False),
                    ('It allows the closure to borrow values mutably across threads.', False),
                    ('It forces the closure to take ownership of the values it captures from the environment.', True),
                ],
                'feedback': 'move captures referenced variables by value, making ownership explicit for thread-safe transfer.'
            },
            {
                'text': 'What does calling .clone() on a heap-backed string value do?\n\nlet s1 = String::from("hello");\nlet s2 = s1.clone();',
                'choices': [
                    ('It moves ownership and invalidates the original.', False),
                    ('It creates another alias to the same buffer with shared ownership by default.', False),
                    ('It copies only the pointer, leaving both to deallocate the same buffer.', False),
                    ('It creates a deep copy of the heap data so both variables own independent copies.', True),
                ],
                'feedback': '.clone() duplicates the heap allocation, giving s1 and s2 separate owned buffers.'
            },
            {
                'text': 'What does the \'static lifetime annotation signify in Rust?',
                'choices': [
                    ('The data is mutable and can be changed by any thread.', False),
                    ('The data can only be accessed from the main function.', False),
                    ('The data is allocated on the stack instead of the heap.', False),
                    ('The reference is valid for the entire duration of the program.', True),
                ],
                'feedback': '\'static references remain valid for the program\'s lifetime; string literals are common examples.'
            },
            {
                'text': 'What is the primary purpose of lifetime annotations (like &\'a T) in Rust?',
                'choices': [
                    ('To manage the memory allocation and deallocation of heap data.', False),
                    ('To specify how long a variable should be kept in the CPU cache.', False),
                    ('To help the borrow checker prove that references will always be valid and not outlive the data they point to.', True),
                    ('To control which thread a piece of data can be accessed from.', False),
                ],
                'feedback': 'Lifetimes let the compiler reason about how long references must remain valid, preventing dangling references.'
            },
            {
                'text': 'According to the slides, which language typically has faster compilation times?',
                'choices': [
                    ('Go', True),
                    ('Rust', False),
                    ('They are roughly the same', False),
                    ('Depends only on LLVM version', False),
                ],
                'feedback': 'Go prioritizes fast compilation to accelerate the edit-build-run cycle.'
            },
            {
                'text': 'In Rust, how can you ensure a spawned thread completes its execution before the main thread continues?',
                'choices': [
                    ('By sending a message through a channel.', False),
                    ('By calling the join method on the thread handle.', True),
                    ('By using a Mutex to lock shared state.', False),
                    ('By applying the move keyword to the closure.', False),
                ],
                'feedback': 'Calling join blocks until the spawned thread finishes execution.'
            },
            {
                'text': 'In Rust, what prevents data races and enforces memory safety at compile time?',
                'choices': [
                    ('Automatic reference counting across the entire program.', False),
                    ('A global garbage collector that pauses all threads.', False),
                    ('Runtime insertion of locks by the compiler.', False),
                    ('The borrow checker (ownership and borrowing rules).', True),
                ],
                'feedback': 'The borrow checker enforces the ownership and borrowing rules, preventing data races statically.'
            },
            {
                'text': 'What does calling .clone() on a heap-backed string value do?\n\nlet s1 = String::from("hello");\nlet s2 = s1.clone();',
                'choices': [
                    ('It creates another alias to the same buffer with shared ownership by default.', False),
                    ('It copies only the pointer, leaving both to deallocate the same buffer.', False),
                    ('It creates a deep copy of the heap data so both variables own independent copies.', True),
                    ('It moves ownership and invalidates the original.', False),
                ],
                'feedback': '.clone() duplicates the owned allocation, producing independent Strings.'
            },
            {
                'text': 'Which receiver allows a method to mutate the instance without taking ownership?',
                'choices': [
                    ('`self` (by value) always prevents mutation.', False),
                    ('Any of the above; they are equivalent.', False),
                    ('`&self`', False),
                    ('`&mut self`', True),
                ],
                'feedback': 'Methods that take `&mut self` borrow the instance mutably, allowing in-place mutation without taking ownership.'
            },
            {
                'text': 'Which trait is used by the `{:?}` formatter in `println!` for printing values?',
                'choices': [
                    ('`Debug`', True),
                    ('`Display`', False),
                    ('Both `Debug` and `Display` simultaneously.', False),
                    ('Neither; `{:?}` is a special-case formatter.', False),
                ],
                'feedback': 'The `{:?}` and `{:#?}` formatters invoke the `Debug` implementation, while `{}` relies on `Display`.'
            },
            {
                'text': 'When can Rust’s field initialization shorthand be used when constructing a struct?',
                'choices': [
                    ('Whenever the compiler can infer the types, regardless of names.', False),
                    ('Only inside trait implementations.', False),
                    ('Only when the type implements `Debug`.', False),
                    ('When local variable names exactly match the struct field names.', True),
                ],
                'feedback': 'Shorthand like `Point { x, y }` works when local bindings share the same names as the struct fields.'
            },
            {
                'text': 'What is the purpose of async/await syntax in Rust?',
                'choices': [
                    ('To enforce ownership rules in concurrent access.', False),
                    ('To write asynchronous code that resembles synchronous code, built on top of futures.', True),
                    ('To create OS threads for parallel execution.', False),
                    ('To pass messages between threads using channels.', False),
                ],
                'feedback': 'Async/await is syntax sugar over futures, enabling asynchronous workflows with familiar sequential-looking code.'
            },
            {
                'text': 'Which threading model does Rust primarily use for concurrency?',
                'choices': [
                    ('M:N model, also known as green threads.', False),
                    ('1:1 model, where one OS thread maps to one language thread.', True),
                    ('Async/await model exclusively for all concurrency.', False),
                    ('A hybrid model combining OS threads and futures.', False),
                ],
                'feedback': 'The standard library’s `std::thread` spawns native OS threads in a 1:1 mapping.'
            },
            {
                'text': 'What are the typical average-case time complexities for lookup and insertion in a hash map implementation?',
                'choices': [
                    ('Both lookup and insertion are O(1) on average.', True),
                    ('Lookup is O(log n) and insertion is O(1) on average.', False),
                    ('Lookup is O(1) and insertion is O(log n) on average.', False),
                    ('Lookup is O(n) but deletion is always O(1) on average.', False),
                ],
                'feedback': 'With a well-distributed hash function, both lookups and insertions run in expected constant time.'
            },
        ]

        self._load_questions(session, questions)

        self.stdout.write(self.style.SUCCESS('\n[SUCCESS] All COMP3007 Midterm questions loaded successfully!'))
        self.stdout.write(f'Total questions in Midterm: {session.questions.count()}')

    def _load_questions(self, session, questions_data):
        """Helper method to load questions into a session"""
        existing_count = session.questions.count()
        created_count = 0
        updated_count = 0

        for idx, q_data in enumerate(questions_data, start=1):
            question = Question.objects.filter(
                session=session,
                text=q_data['text']
            ).first()

            if question:
                question.order = idx
                question.is_active = True
                question.save(update_fields=['order', 'is_active'])

                existing_choices = list(question.choices.all())
                if len(existing_choices) == len(q_data['choices']):
                    for choice, (choice_text, is_correct) in zip(existing_choices, q_data['choices']):
                        choice.text = choice_text
                        choice.is_correct = is_correct
                        choice.save(update_fields=['text', 'is_correct'])
                else:
                    question.choices.all().delete()
                    for choice_text, is_correct in q_data['choices']:
                        Choice.objects.create(
                            question=question,
                            text=choice_text,
                            is_correct=is_correct
                        )

                updated_count += 1
                self.stdout.write(f'  [~] Updated question {idx}')
            else:
                question = Question.objects.create(
                    session=session,
                    text=q_data['text'],
                    order=idx,
                    is_active=True
                )

                for choice_text, is_correct in q_data['choices']:
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )
                created_count += 1
                self.stdout.write(f'  [+] Created question {idx}')

        self.stdout.write(f'\nSummary: Created {created_count} questions, updated {updated_count} questions.')

