import os
import re

# Read guide.html to get the shell
with open('guide.html', 'r', encoding='utf-8') as f:
    guide_html = f.read()

# Extract from start to <main
match = re.search(r'(<!DOCTYPE html>.*?)<main id="app"', guide_html, re.DOTALL)
if not match:
    print("Could not find <main> in guide.html")
    exit(1)

header_and_sidebar = match.group(1)

# New main content
main_content = """<main id="app" class="flex-grow p-4 md:p-8 lg:px-10 lg:py-8 max-w-6xl overflow-x-hidden">
            <header class="mb-8 flex flex-col md:flex-row md:items-start justify-between gap-4">
                <div>
                    <h1 class="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">
                        Create: My Email Writing Assistant
                    </h1>
                    <div class="mt-2 text-slate-600 max-w-2xl space-y-4">
                        <p>
                            On this page, we will walk you through how to create your <strong>Email Writing Assistant</strong> using a Custom GPT. This assistant helps you write clear, concise, and professional emails for any situation.
                        </p>
                    </div>
                </div>
            </header>

        <div id="content-gpt" class="gpt-theme">
            
            <h2 class="text-3xl font-bold text-slate-800 mb-8">Build Your Custom GPT Assistant</h2>

            <!-- Step 1 -->
            <div class="step-card">
                <div class="flex items-start space-x-5">
                    <div class="step-number-circle bg-teal-600 text-white">1</div>
                    <div class="flex-grow">
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Step 1 – Open GPT Editor</h3>
                        <p class="text-lg text-slate-600 mb-6 leading-relaxed">Click the button below to open the Custom GPT editor in a new tab to begin construction.</p>
                        <a href="https://chatgpt.com/gpts/editor" target="_blank" class="inline-block bg-blue-600 text-white px-10 py-3.5 rounded-xl font-bold hover:bg-blue-700 transition shadow-md">Open GPT Editor</a>
                    </div>
                </div>
            </div>

            <!-- Step 2 -->
            <div class="step-card">
                <div class="flex items-start space-x-5">
                    <div class="step-number-circle bg-teal-600 text-white">2</div>
                    <div class="flex-grow">
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Step 2 – Navigate to the Configure Tab</h3>
                        <p class="text-lg text-slate-600 mb-8 leading-relaxed">Once the editor opens, you will see two options at the top: <strong>Create</strong> and <strong>Configure</strong>. Ensure you select the <strong>Configure</strong> tab to access the fields needed for this setup guide.</p>
                        <div class="flex justify-center py-4">
                            <div class="bg-slate-100 rounded-xl p-1 inline-flex relative overflow-hidden">
                                <div id="gpt-tab-hl" class="tab-highlight absolute top-1 bottom-1 w-[100px] bg-white rounded-lg shadow-sm border border-slate-200 configure-active"></div>
                                <div class="px-6 py-2 text-sm font-bold z-10 w-[100px] text-center text-slate-400">Create</div>
                                <div class="px-6 py-2 text-sm font-bold z-10 w-[100px] text-center text-slate-900">Configure</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Step 3 -->
            <div class="step-card">
                <div class="flex items-start space-x-5">
                    <div class="step-number-circle bg-teal-600 text-white">3</div>
                    <div class="flex-grow space-y-8">
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Step 3 – Copy Paste Name, Description and Instructions</h3>
                        <div>
                            <div class="flex justify-between items-end mb-3">
                                <div>
                                    <label class="text-lg font-bold text-slate-900 block">Name</label>
                                </div>
                                <button onclick="copyText('gpt-name')" class="text-blue-600 text-xs font-bold hover:underline mb-1">Copy Name</button>
                            </div>
                            <div class="code-block rounded-lg p-3 text-sm bg-slate-50 text-slate-900 border border-slate-200" id="gpt-name">My Email Writing Assistant</div>
                        </div>
                        <div>
                            <div class="flex justify-between items-end mb-3">
                                <div>
                                    <label class="text-lg font-bold text-slate-900 block">Description</label>
                                </div>
                                <button onclick="copyText('gpt-desc')" class="text-blue-600 text-xs font-bold hover:underline mb-1">Copy Description</button>
                            </div>
                            <div class="code-block rounded-lg p-3 text-sm bg-slate-50 text-slate-900 border border-slate-200" id="gpt-desc">Helps you write clear, concise, and professional emails for any situation. Adjusts tone based on your needs and ensures your message is easy to understand and action-oriented.</div>
                        </div>
                        <div>
                            <div class="flex justify-between items-end mb-3">
                                <div>
                                    <label class="text-lg font-bold text-slate-900 block">Instructions / System Prompt</label>
                                </div>
                                <button onclick="copyText('gpt-instr')" class="text-blue-600 text-xs font-bold hover:underline mb-1">Copy Instructions</button>
                            </div>
                            <div class="code-block rounded-lg p-4 text-[13px] leading-relaxed max-h-64 overflow-y-auto bg-slate-50 text-slate-900 border border-slate-200 relative">
<pre id="gpt-instr">You are an assistant that helps users write clear, concise, and professional emails. Always prioritize clarity, tone, and readability. When the user clicks "Get Started," ask what tone they want: casual and friendly, professional but approachable, formal and polished, or persuasive and action-oriented. Use their selected tone to draft or improve emails.

I am the AI & Integration Specialist for the Agua Fria High School District in the West Valley, Arizona.
My phone number extension is: 7037

When the user clicks Get Started ask the following:
"What tone would you like for your email?"
a. Casual and friendly
b. Professional but approachable
c. Formal and polished
d. Persuasive and action-oriented</pre>
                                <button onclick="copyText('gpt-instr')" class="absolute top-2 right-2 text-blue-600 text-xs font-bold bg-white px-2 py-1 rounded shadow-sm border border-slate-200 hover:bg-slate-50">Copy</button>
                            </div>
                        </div>
                        
                        <div>
                            <div class="flex justify-between items-end mb-3">
                                <div>
                                    <label class="text-lg font-bold text-slate-900 block">Conversation Starters</label>
                                </div>
                                <button onclick="copyText('gpt-starter')" class="text-blue-600 text-xs font-bold hover:underline mb-1">Copy Starter</button>
                            </div>
                            <div class="code-block rounded-lg p-3 text-sm bg-slate-50 text-slate-900 border border-slate-200" id="gpt-starter">Get Started</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Step 4 -->
            <div class="step-card">
                <div class="flex items-start space-x-5">
                    <div class="step-number-circle bg-teal-600 text-white">4</div>
                    <div class="flex-grow">
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Step 4 – Add Knowledge Source</h3>
                        <p class="text-lg text-slate-600 mb-8 leading-relaxed">Upload the relevant knowledge document for email writing best practices.</p>
                        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 flex items-center shadow-sm">
                            <div class="mr-5 flex-shrink-0">
                                <svg class="w-10 h-10 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                            </div>
                            <div class="flex-grow">
                                <h4 class="font-bold text-sm text-slate-800 leading-tight">A Blueprint for Writing Effective Emails - Harvard Business School</h4>
                                <p class="text-[10px] text-slate-400 uppercase font-bold tracking-tighter mt-1">Knowledge Document</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Step 5 -->
            <div class="step-card">
                <div class="flex items-start space-x-5">
                    <div class="step-number-circle bg-teal-600 text-white">5</div>
                    <div class="flex-grow">
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Step 5 – Save & Create</h3>
                        <p class="text-lg text-slate-600 mb-4 leading-relaxed">Click the <strong>Create</strong> or <strong>Save</strong> button in the top-right to finalize.</p>
                        <div class="flex justify-center"><div id="gpt-save-btn" class="bg-slate-900 text-white px-10 py-3 rounded-full font-bold transition">Create</div></div>
                    </div>
                </div>
            </div>

            <!-- Customization Bank -->
            <div class="mt-16 mb-8 border-t-2 border-slate-200 pt-12">
                <div class="flex flex-col items-center text-center mb-10">
                    <div class="bg-emerald-100 text-emerald-800 px-4 py-1.5 rounded-full text-sm font-bold tracking-wide uppercase mb-4 inline-flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Level Up Your Assistant
                    </div>
                    <h2 class="text-3xl font-extrabold text-slate-900 mb-4">The Customization Bank</h2>
                    <p class="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
                        These snippets are not required — they’re just ways to teach your assistant how <strong>YOU</strong> communicate. The more context you give it, the more it sounds like you. Copy and paste these into your instructions to make iterative updates to your AI assistant.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    
                    <!-- Box 1 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>👤</span> Personal Identity & Context
                            </h4>
                            <button onclick="copyText('bank-1')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-1" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● Always sign emails with: [Your Full Name]
● Include my role in emails when appropriate: [Your Job Title]
● I work at: [Your Organization / District Name]
● My communication is typically with: [students / parents / staff / leadership / vendors]
● Include my contact info in signatures: [Phone Number] | [Email Address]</pre>
                        </div>
                    </div>

                    <!-- Box 2 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>🎯</span> Writing Style Preferences
                            </h4>
                            <button onclick="copyText('bank-2')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-2" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● Keep all emails short and concise (under [X] sentences when possible)
● Use bullet points when listing information
● Start emails with a clear purpose statement
● Avoid unnecessary words and get straight to the point
● Use simple, easy-to-understand language (avoid jargon unless needed)</pre>
                        </div>
                    </div>

                    <!-- Box 3 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>💬</span> Tone & Voice Controls
                            </h4>
                            <button onclick="copyText('bank-3')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-3" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● My default tone should be: [friendly / professional / formal / persuasive]
● When writing to leadership, sound: [more formal / concise / direct]
● When writing to coworkers, sound: [friendly but professional]
● Always be polite, respectful, and clear
● Avoid sounding robotic — write like a real person</pre>
                        </div>
                    </div>

                    <!-- Box 4 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>🧹</span> Quality & Clarity Rules
                            </h4>
                            <button onclick="copyText('bank-4')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-4" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● Always check grammar and spelling before finalizing
● Rewrite sentences that may be unclear or confusing
● Break up long paragraphs into short, readable sections
● Highlight important points using bold or formatting when helpful
● Remove filler phrases like "just checking in" unless necessary</pre>
                        </div>
                    </div>

                    <!-- Box 5 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>⚡</span> Behavior & Output Enhancements
                            </h4>
                            <button onclick="copyText('bank-5')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-5" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● Always include a suggested subject line
● Provide 2 versions when helpful: (1) concise, (2) more detailed
● Ask follow-up questions if the request is unclear
● If the email is complex, organize it into sections
● Suggest improvements if the message could be clearer or more effective</pre>
                        </div>
                    </div>

                    <!-- Box 6 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition border-l-4 border-l-blue-500">
                        <div class="bg-blue-50 border-b border-blue-100 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-blue-900 flex items-center gap-2">
                                <span>🏫</span> Workplace-Specific Context
                            </h4>
                            <button onclick="copyText('bank-6')" class="text-blue-700 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-6" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● I work at Agua Fria Union High School District — keep communication appropriate for a K–12 education environment
● Assume emails may involve students, parents, teachers, and administrators
● Prioritize clarity and professionalism when communicating with parents and guardians
● Be mindful of sensitive topics and maintain a respectful tone at all times</pre>
                        </div>
                    </div>

                    <!-- Box 7 -->
                    <div class="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden hover:shadow-md transition">
                        <div class="bg-slate-50 border-b border-slate-200 px-5 py-3 flex justify-between items-center">
                            <h4 class="font-bold text-slate-800 flex items-center gap-2">
                                <span>🧠</span> Advanced (Optional but Powerful)
                            </h4>
                            <button onclick="copyText('bank-7')" class="text-blue-600 text-xs font-bold hover:underline">Copy</button>
                        </div>
                        <div class="p-5">
<pre id="bank-7" class="code-block text-[13px] text-slate-700 whitespace-pre-wrap font-mono leading-relaxed">● Match my typical communication style: [describe your style in 1 sentence]
● Avoid using these phrases: [list phrases you don’t like]
● Prefer this type of closing: [Best, Thanks, Sincerely, etc.]
● When possible, make emails feel warm and approachable but still professional</pre>
                        </div>
                    </div>

                </div>
            </div>
            
        </div>
    </main>

    <div id="toast" class="notification">Copied to clipboard!</div>

    <script>
        function copyText(id) { performCopy(document.getElementById(id).innerText); }
        function copyValue(val) { performCopy(val); }
        function performCopy(text) {
            const textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2000);
        }
    </script>
</body>
</html>
"""

full_html = header_and_sidebar + main_content

with open('email-guide.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Created email-guide.html successfully.")
