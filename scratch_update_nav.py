import os
import glob

# HTML to insert (Journey to AI literacy nav link)
NAV_ITEM = """                <!-- Journey to AI Literacy -->
                <a href="literacy.html"
                    class="flex items-center gap-3 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm transition-all group hover:-translate-y-0.5 mt-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"
                        class="w-5 h-5 text-emerald-600 opacity-90 group-hover:scale-110 transition-transform">
                        <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"></path>
                    </svg>
                    <span class="text-sm">Journey to AI Literacy</span>
                </a>"""

html_files = glob.glob('/Users/mriley/Documents/Git-Repos/ai-assistant-library/*.html')

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # If already modified, skip
    if "Journey to AI Literacy" in content and 'literacy.html' in content:
        continue

    target = '<!-- Prompt Library -->'
    if target in content:
        # Find closing </a> of Prompt Library link block
        pos = content.find(target)
        end_a_pos = content.find('</a>', pos)
        if end_a_pos != -1:
            insert_pos = end_a_pos + 4
            new_content = content[:insert_pos] + "\n\n" + NAV_ITEM + content[insert_pos:]
            with open(filepath, 'w') as f:
                f.write(new_content)

print("Updated links!")
