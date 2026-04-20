import os

index_path = '/Users/mriley/Documents/Git-Repos/ai-assistant-library/index.html'
lit_path = '/Users/mriley/Documents/Git-Repos/ai-assistant-library/literacy.html'

with open(index_path, 'r') as f:
    index_content = f.read()

# 1. Grab everything up to <main id="app"...>
main_start = index_content.find('<main id="app"')
pre_main = index_content[:main_start]

# 2. Add extra styles into <head>
style_block = """
        /* Custom Animation for the Progress Bar */
        @keyframes loadProgress {
            from { width: 0; }
            to { width: 49%; }
        }
        .animate-progress {
            animation: loadProgress 1.5s ease-out forwards;
        }

        /* Card Hover Effects */
        .phase-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .phase-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        .connector-arrow {
            position: absolute;
            right: -24px;
            top: 40%;
            z-index: 50;
            color: #94a3b8;
            font-size: 1.5rem;
        }
"""
# insert before </style>
style_end = pre_main.find('</style>')
pre_main = pre_main[:style_end] + style_block + pre_main[style_end:]

# update title
pre_main = pre_main.replace('<title>District AI Assistant Library</title>', '<title>Journey to AI Literacy - District AI</title>')

# add Font Awesome
head_end = pre_main.find('</head>')
pre_main = pre_main[:head_end] + '    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">\n' + pre_main[head_end:]

# add tailwind color config inside <head> before </head>
tw_config = """    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        district: {
                            blue: '#0F172A',
                            lightBlue: '#334155',
                            red: '#DC2626',
                            accent: '#991B1B',
                        }
                    }
                }
            }
        }
    </script>
"""
head_end = pre_main.find('</head>')
pre_main = pre_main[:head_end] + tw_config + pre_main[head_end:]

# make Assistant Library NOT active, and Literacy Active
# The Assistant Library active styling:
pre_main = pre_main.replace('bg-blue-600 text-white px-4 py-3 rounded-xl font-bold shadow-md shadow-blue-200', 'bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 px-4 py-3 rounded-xl font-bold shadow-sm')
pre_main = pre_main.replace('w-5 h-5 opacity-90 group-hover:scale-110', 'w-5 h-5 text-blue-600 opacity-90 group-hover:scale-110')
# Wait, let's find Assistant Library block and rewrite it:
def replace_class(html, find_str, target_cls, new_cls):
    # a bit hacky but it works string replace
    return html

# 3. Literacy HTML Body Content
main_tag = '<main id="app" class="flex-grow max-w-6xl overflow-x-hidden relative w-full lg:px-6">'
literacy_content = """
        <!-- Hero Section -->
        <header class="bg-district-blue text-white pt-12 pb-20 mt-8 relative overflow-hidden rounded-3xl mx-4 sm:mx-6 lg:mx-8">
            <div class="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 rounded-full bg-district-red opacity-10 blur-3xl"></div>
            <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-72 h-72 rounded-full bg-blue-500 opacity-10 blur-3xl"></div>

            <div class="relative z-10 text-center px-4">
                <span class="inline-block py-1 px-3 rounded-full bg-blue-800/50 border border-blue-700 text-blue-100 text-xs font-semibold tracking-wider mb-4">FALL '25 UPDATE</span>
                <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4">
                    The Journey to <span class="text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400">AI Literacy</span>
                </h1>
                <p class="text-lg text-slate-300 max-w-2xl mx-auto">
                    Moving from basic awareness to innovation leadership.
                </p>
            </div>
        </header>

        <!-- Stats Dashboard -->
        <section id="stats" class="relative -mt-10 mb-16 mx-4 sm:mx-6 lg:mx-8 z-20">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Stat 1 -->
                <div class="bg-white p-6 md:p-8 rounded-xl shadow-lg border-t-4 border-district-red flex flex-col items-center text-center">
                    <div class="text-5xl font-extrabold text-district-blue mb-2">70%</div>
                    <p class="text-gray-600 font-medium text-sm md:text-base">Staff using AI <br>weekly or more</p>
                </div>

                <!-- Stat 2 -->
                <div class="bg-white p-6 md:p-8 rounded-xl shadow-lg border-t-4 border-district-blue flex flex-col items-center text-center">
                    <div class="text-5xl font-extrabold text-district-blue mb-2">70%</div>
                    <p class="text-gray-600 font-medium text-sm md:text-base">Reporting moderate to<br>significant productivity gains</p>
                </div>

                <!-- Stat 3 (The Goal) -->
                <div class="bg-district-blue p-6 md:p-8 rounded-xl shadow-lg border-t-4 border-blue-400 flex flex-col justify-center text-white relative overflow-hidden">
                    <div class="absolute top-0 right-0 opacity-10 text-9xl -mr-8 -mt-8 rotate-12">
                        <i class="fa-solid fa-bullseye"></i>
                    </div>
                    <h3 class="text-sm uppercase tracking-wide text-blue-300 mb-1">Current Status</h3>
                    <div class="flex items-end gap-2 mb-3 z-10">
                        <span class="text-5xl font-bold">49%</span>
                        <span class="text-blue-200 mb-2 font-medium">at Phase 3+</span>
                    </div>
                    <div class="w-full bg-slate-700 rounded-full h-3 mb-2 relative z-10">
                        <div class="absolute top-0 bottom-0 w-0.5 bg-white z-20 h-5 -mt-1" style="left: 75%"></div>
                        <div class="absolute -top-6 text-xs font-bold text-white z-20" style="left: 75%; transform: translateX(-50%);">GOAL: 75%</div>
                        <div class="bg-district-red h-3 rounded-full animate-progress relative z-10"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- The 5 Phases -->
        <section class="mb-24 mx-4 sm:mx-6 lg:mx-8 relative">
            <div class="mb-8 text-center xl:text-left">
                <h2 class="text-3xl font-bold text-district-blue">The Path of Progression</h2>
            </div>

            <div class="w-full pb-12 pt-6">
                <!-- Flex Container to prevent cut-offs -->
                <div class="flex flex-col xl:flex-row gap-8 xl:gap-4 w-full justify-between items-stretch">
                    
                    <!-- Phase 1 -->
                    <div class="phase-card relative flex-1 bg-white rounded-xl border-t-8 border-district-blue shadow-lg p-5 flex flex-col min-w-[180px]">
                        <div class="connector-arrow hidden xl:block z-50">
                             <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 10C5 10 15 10 22 10" stroke="#CBD5E1" stroke-width="2" marker-end="url(#arrowhead)"/>
                            </svg>
                        </div>
                        <div class="w-12 h-12 bg-blue-50 text-district-blue rounded-full flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-magnifying-glass"></i></div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Phase 1</h3>
                        <h4 class="text-lg font-bold text-district-blue mb-3">Awareness</h4>
                        <p class="text-sm text-gray-600 mb-4 flex-grow">Recognizing AI's existence & potential impact. Understanding basic terms.</p>
                        <div class="w-full bg-gray-100 rounded-full h-1.5 mt-auto"><div class="bg-district-blue w-1/5 h-1.5 rounded-full"></div></div>
                    </div>

                    <!-- Phase 2 -->
                    <div class="phase-card relative flex-1 bg-white rounded-xl border-t-8 border-blue-700 shadow-lg p-5 flex flex-col min-w-[180px]">
                        <div class="connector-arrow hidden xl:block z-50">
                             <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 10C5 10 15 10 22 10" stroke="#CBD5E1" stroke-width="2" marker-end="url(#arrowhead)"/>
                            </svg>
                        </div>
                        <div class="w-12 h-12 bg-blue-50 text-blue-700 rounded-full flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-hand-pointer"></i></div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Phase 2</h3>
                        <h4 class="text-lg font-bold text-district-blue mb-3">Basic Usage</h4>
                        <p class="text-sm text-gray-600 mb-4 flex-grow">Experimenting with simple AI tools & applications. Learning prompts.</p>
                        <div class="w-full bg-gray-100 rounded-full h-1.5 mt-auto"><div class="bg-blue-700 w-2/5 h-1.5 rounded-full"></div></div>
                    </div>

                    <!-- Phase 3 -->
                    <div class="phase-card relative flex-1 bg-blue-50 rounded-xl border-t-8 border-yellow-500 shadow-xl p-5 flex flex-col min-w-[180px] xl:-mt-2 xl:mb-2 border-2 border-x-blue-200 border-b-blue-200 z-10 scale-100 xl:scale-105">
                        <div class="connector-arrow hidden xl:block z-50" style="right: -24px;">
                             <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 10C5 10 15 10 22 10" stroke="#CBD5E1" stroke-width="2" marker-end="url(#arrowhead)"/>
                            </svg>
                        </div>
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-yellow-500 text-white px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase shadow-sm whitespace-nowrap z-20">Target Goal</div>
                        <div class="w-12 h-12 bg-yellow-100 text-yellow-600 rounded-full flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-arrows-spin"></i></div>
                        <h3 class="text-xs font-bold text-yellow-600 uppercase tracking-widest mb-1">Phase 3</h3>
                        <h4 class="text-lg font-bold text-district-blue mb-3">Routine Integration</h4>
                        <p class="text-sm text-gray-700 mb-4 flex-grow font-medium">Incorporating AI into daily tasks & workflows. Increasing efficiency.</p>
                        <div class="w-full bg-gray-200 rounded-full h-1.5 mt-auto"><div class="bg-yellow-500 w-3/5 h-1.5 rounded-full"></div></div>
                    </div>

                    <!-- Phase 4 -->
                    <div class="phase-card relative flex-1 bg-white rounded-xl border-t-8 border-red-400 shadow-lg p-5 flex flex-col min-w-[180px]">
                        <div class="connector-arrow hidden xl:block z-50">
                             <svg width="24" height="20" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 10C5 10 15 10 22 10" stroke="#CBD5E1" stroke-width="2" marker-end="url(#arrowhead)"/>
                            </svg>
                        </div>
                        <div class="w-12 h-12 bg-red-50 text-red-400 rounded-full flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-layer-group"></i></div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Phase 4</h3>
                        <h4 class="text-lg font-bold text-district-blue mb-3">Advanced App</h4>
                        <p class="text-sm text-gray-600 mb-4 flex-grow">Customizing AI solutions, solving complex problems. Analyzing data.</p>
                        <div class="w-full bg-gray-100 rounded-full h-1.5 mt-auto"><div class="bg-red-400 w-4/5 h-1.5 rounded-full"></div></div>
                    </div>

                    <!-- Phase 5 -->
                    <div class="phase-card relative flex-1 bg-white rounded-xl border-t-8 border-district-red shadow-lg p-5 flex flex-col min-w-[180px]">
                        <div class="w-12 h-12 bg-red-50 text-district-red rounded-full flex items-center justify-center text-xl mb-4"><i class="fa-solid fa-rocket"></i></div>
                        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-1">Phase 5</h3>
                        <h4 class="text-lg font-bold text-district-blue mb-3">Leadership</h4>
                        <p class="text-sm text-gray-600 mb-4 flex-grow">Creating new AI strategies, driving organizational change & ethical use.</p>
                        <div class="w-full bg-gray-100 rounded-full h-1.5 mt-auto"><div class="bg-district-red w-full h-1.5 rounded-full"></div></div>
                    </div>
                </div>
            </div>

            <!-- The "Progression & Growth" Bottom Arrow SVG -->
            <div class="mt-8 relative h-20 w-full hidden md:block">
                <svg viewBox="0 0 1200 100" class="w-full h-full overflow-visible" preserveAspectRatio="none">
                    <defs>
                        <linearGradient id="growthGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#0F172A;stop-opacity:1" />
                            <stop offset="50%" style="stop-color:#3B82F6;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#DC2626;stop-opacity:1" />
                        </linearGradient>
                         <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                            <polygon points="0 0, 10 3.5, 0 7" fill="#CBD5E1" />
                        </marker>
                    </defs>
                    <path d="M 20,60 Q 600,105 1180,20" stroke="url(#growthGradient)" stroke-width="8" fill="none" stroke-linecap="round" />
                    <path d="M 1180,20 L 1150,35 L 1155,20 L 1150,5 Z" fill="#DC2626" />
                </svg>
                <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-slate-50 px-4 text-xs font-bold tracking-[0.2em] text-gray-400 uppercase">
                    Progression & Growth
                </div>
            </div>
        </section>
        
        <!-- Footer -->
        <footer class="mt-12 text-center text-slate-400 text-sm pb-8 border-t border-slate-200 mx-8 pt-8">
            <p>© 2025 District AI Assistant Library <span class="opacity-30">| v1.0.6</span></p>
            <p class="mt-1">For updates, please contact mriley@aguafria.org.</p>
        </footer>
"""

footer_start = index_content.find('<footer')
footer_end = index_content.find('</footer>')

# 4. Write full file
with open(lit_path, 'w') as f:
    f.write(pre_main + main_tag + "\n" + literacy_content + "\n</main>\n</div>\n</body>\n</html>")

print("Created literacy.html!")
