import os
import re

INACTIVE_LINK = """<!-- Create Email Assistant -->
                <a href="email-guide.html"
                    class="flex items-center gap-3 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm transition-all hover:-translate-y-0.5 group mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 text-blue-600 opacity-90 group-hover:scale-110 transition-transform">
                        <rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                    </svg>
                    <span class="text-sm">Create Email Assistant</span>
                </a>

                """

ACTIVE_LINK = """<!-- Create Email Assistant (Active) -->
                <a href="email-guide.html"
                    class="flex items-center gap-3 bg-blue-600 text-white px-4 py-3 rounded-xl font-bold shadow-md shadow-blue-200 transition-all hover:-translate-y-0.5 group mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 opacity-90 group-hover:scale-110 transition-transform">
                        <rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                    </svg>
                    <span class="text-sm">Create Email Assistant</span>
                </a>

                """

INACTIVE_ADA = """<!-- Create ADA GPT -->
                <a href="guide.html"
                    class="flex items-center gap-3 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm transition-all hover:-translate-y-0.5 group mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 text-blue-600 opacity-90 group-hover:scale-110 transition-transform">
                        <circle cx="12" cy="11" r="3"/><path d="M12 2a9 9 0 1 0 9 9"/><path d="M15 2h6v6"/><path d="M8 17.6A7 7 0 0 0 17.6 8"/>
                    </svg>
                    <span class="text-sm">Create ADA GPT</span>
                </a>"""

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r') as f:
            content = f.read()

        # Check if already has the new link
        if 'Create Email Assistant' in content:
            print(f"Skipping {filename}, already updated.")
            continue

        if filename == 'email-guide.html':
            # Needs active email link and inactive ADA link
            # Replace active ADA link with active email link + inactive ADA link
            new_content = re.sub(
                r'<!-- Create ADA GPT \(Active\) -->.*?<span class="text-sm">Create ADA GPT</span>\n\s*</a>',
                ACTIVE_LINK + INACTIVE_ADA,
                content,
                flags=re.DOTALL
            )
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename} with Active Email, Inactive ADA.")
        else:
            # Add inactive email link before ADA link
            new_content = re.sub(
                r'(<!-- Create ADA GPT)',
                INACTIVE_LINK + r'\1',
                content
            )
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename} with Inactive Email before ADA.")

