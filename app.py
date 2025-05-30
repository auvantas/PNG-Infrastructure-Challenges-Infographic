import streamlit as st

def get_streamlit_app_content(groq_api_key_js):
    """
    Generates the HTML, CSS, and JavaScript content for the Streamlit app.
    The Groq API key is injected into the JavaScript part.
    """
    
    style_content = """
        body {
            font-family: 'Inter', sans-serif;
            color: #073B4C;
            margin: 0;
            padding: 0;
        }
        .chart-container {
            position: relative;
            width: 100%; /* This percent is fine as it's not in the string being formatted by Python % op */
            max-width: 500px; 
            margin-left: auto;
            margin-right: auto;
            height: 300px; 
            max-height: 350px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 320px;
            }
        }
        .stat-card {
            background-color: white;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .stat-title {
            font-size: 1.125rem; 
            font-weight: 600; 
            margin-bottom: 0.5rem;
            color: #118AB2; 
        }
        .stat-value {
            font-size: 2.25rem; 
            font-weight: 700; 
            color: #FF6B6B; 
            line-height: 1.1;
        }
        .stat-context {
            font-size: 0.875rem; 
            color: #4A5568; 
            margin-top: 0.25rem;
        }
        .section-title {
            font-size: 1.875rem; 
            font-weight: 700; 
            color: #073B4C; 
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #118AB2; 
        }
        .nav-link {
            padding: 0.5rem 1rem;
            color: #073B4C;
            border-radius: 0.375rem;
            transition: background-color 0.3s ease;
        }
        .nav-link:hover {
            background-color: #E2E8F0; 
        }
        .flowchart-step {
            border: 2px solid #06D6A0; 
            padding: 0.75rem;
            border-radius: 0.375rem;
            text-align: center;
            background-color: #F0FDFA; 
            width: 100%; /* This percent is fine */
            max-width: 20rem; 
        }
        .flowchart-arrow {
            font-size: 1.5rem; 
            color: #073B4C;
            margin: 0.5rem 0;
        }
        .icon-placeholder {
            font-size: 1.5rem;
            margin-right: 0.5rem;
        }
        .gemini-button { 
            background-color: #FFD166; 
            color: #073B4C; 
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            font-weight: 500;
            margin-top: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
            border: 1px solid #E7B00B;
        }
        .gemini-button:hover {
            background-color: #FBC53E;
        }
        .gemini-response-area { 
            margin-top: 1rem;
            padding: 0.75rem;
            background-color: #F0FDFA; 
            border-radius: 0.375rem;
            font-size: 0.875rem;
            color: #073B4C;
            border: 1px solid #06D6A0; 
            white-space: pre-wrap; 
        }
        #geminiModal { 
            z-index: 1050; 
        }
    """

    body_content_html = """
    <div style="background-color: #F8F9FA;">
        <header class="bg-[#073B4C] text-white py-8 shadow-lg">
            <div class="container mx-auto px-4 text-center">
                <h1 class="text-4xl md:text-5xl font-bold mb-2">Papua New Guinea's Infrastructure</h1>
                <p class="text-xl md:text-2xl text-[#FFD166]">Challenges, Progress, and the Path to a Resilient Future</p>
            </div>
        </header>
        <nav class="bg-white shadow-md sticky top-0 z-50 hidden md:block">
            <div class="container mx-auto px-4 py-3 flex justify-center space-x-2 overflow-x-auto">
                <a href="#national-strategies" class="nav-link">National Strategies</a>
                <a href="#telecom" class="nav-link">Telecom</a>
                <a href="#transport" class="nav-link">Transport</a>
                <a href="#energy" class="nav-link">Energy</a>
                <a href="#wash" class="nav-link">WASH</a>
                <a href="#cross-cutting" class="nav-link">Enablers</a>
                <a href="#conclusion" class="nav-link">Conclusion</a>
            </div>
        </nav>
        <main class="container mx-auto p-4 md:p-8">
            <section class="mb-12 text-center">
                <p class="text-lg md:text-xl leading-relaxed max-w-3xl mx-auto text-gray-700">
                    Since 2015-2016, Papua New Guinea has faced significant infrastructure deficits across crucial sectors. This infographic provides an updated assessment of the evolving landscape, examining developments, persistent challenges, and strategic responses in transport, energy, ICT, and WASH, highlighting the nation's journey towards a more prosperous and resilient future. Explore AI-powered insights by clicking the ✨ buttons!
                </p>
            </section>
            <section id="national-strategies" class="mb-12">
                <h2 class="section-title">Overarching National Strategies</h2>
                <p class="mb-6 text-gray-700">PNG's infrastructure development is guided by ambitious national plans aiming for transformative economic and social growth. These strategies outline key priorities and targets to address long-standing deficits.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">MTDP IV Economic Goal</h3>
                        <p class="stat-value">K200 Billion</p>
                        <p class="stat-context">Target GDP by 2030 under Medium Term Development Plan IV.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Connect PNG: New Roads</h3>
                        <p class="stat-value">2,500 km</p>
                        <p class="stat-context">Target for new road construction by 2027 (Phase 1).</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Digital ID: GDP Impact</h3>
                        <p class="stat-value">3-5%%</p>
                        <p class="stat-context">Projected GDP increase in 3-5 years from SevisPass Digital ID.</p>
                    </div>
                </div>
            </section>
            <section id="telecom" class="mb-12">
                <h2 class="section-title">Telecommunications & ICT</h2>
                <p class="mb-6 text-gray-700">The ICT sector is crucial for PNG's development, with efforts focused on increasing connectivity, affordability, and leveraging digital transformation. However, significant gaps remain, particularly in rural access and cost.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Internet Penetration</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="internetPenetrationChart"></canvas></div>
                        <p class="stat-context text-center mt-2">~24.1%% of population (Early 2025, DataReportal)</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Mobile Connections</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="mobileConnectionsChart"></canvas></div>
                        <p class="stat-context text-center mt-2">~47.2%% of population (Early 2025, DataReportal/GSMA)</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Internet Affordability Challenge</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="internetAffordabilityChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Low-consumption basket vs. GNI per capita (2024).</p>
                    </div>
                    <div class="stat-card md:col-span-2 lg:col-span-3">
                        <h3 class="stat-title">Key ICT Infrastructure & Initiatives</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-2">
                            <li><span class="icon-placeholder">📡</span><strong>Submarine Cables (CSCS2, KSCN):</strong> Aiming to reduce costs and improve international/domestic bandwidth. KSCN repairs ongoing after 2022 earthquake.</li>
                            <li><span class="icon-placeholder">🗼</span><strong>National Transmission Network (NTN):</strong> Over 12,000 km of fibre by PNG DataCo, plus 500 new mobile towers planned by 2026.</li>
                            <li><span class="icon-placeholder">📱</span><strong>Market Competition:</strong> Three MNOs (Digicel, Vodafone, Telikom/Bmobile). Starlink licensed, but entry faced judicial review.</li>
                            <li><span class="icon-placeholder">💡</span><strong>Digital Government Plan 2023-2027:</strong> Includes SevisPass Digital ID, G2B Single Window, eProcurement.</li>
                        </ul>
                    </div>
                </div>
            </section>
            <section id="transport" class="mb-12">
                <h2 class="section-title">Transport Infrastructure</h2>
                <p class="mb-6 text-gray-700">Transport is vital for PNG's connectivity and economy. Ambitious programs like "Connect PNG" aim to address vast road network deficiencies, while ports and aviation sectors are also seeing significant upgrades.</p>
                <h3 class="text-2xl font-semibold mb-4 mt-8 text-[#118AB2]">Roads & Bridges</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Road Network Condition</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="roadConditionChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Estimated 85%% in poor condition.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Maintenance Backlog</h3>
                        <p class="stat-value">K45 Billion</p>
                        <p class="stat-context">Estimated cost to address deferred road maintenance.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Connect PNG: Strategic Highway Upgrades</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="connectPngProgressChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Progress on 16,200km strategic highways (Phase 1 target: 4,220km).</p>
                        <button class="gemini-button" onclick="fetchAIResponse('connectPNG', 'risksOpportunities', 'geminiResponseConnectPNG')">✨ Analyse Risks & Opportunities</button>
                        <div id="geminiResponseConnectPNG" class="gemini-response-area" style="display: none;"></div>
                    </div>
                </div>
                <h3 class="text-2xl font-semibold mb-4 mt-8 text-[#118AB2]">Ports & Maritime</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Kimbe Port Upgrade (AIFFP)</h3>
                        <p class="stat-value">$95 Million AUD</p>
                        <p class="stat-context">Australian funding for major upgrade, part of PNG Ports Infrastructure Investment Programme.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Port Modernisation</h3>
                         <p class="text-gray-700"><span class="icon-placeholder">🚢</span>Port Moresby (MIT) & Lae (SPICT) operated by ICTSI, showing improved performance and efficiency gains (e.g., 6x productivity at Lae with new cranes).</p>
                         <p class="text-gray-700 mt-2"><span class="icon-placeholder">🇪🇺</span>EU developing major investment for Rabaul port renovation and greening.</p>
                    </div>
                </div>
                <h3 class="text-2xl font-semibold mb-4 mt-8 text-[#118AB2]">Aviation</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Civil Aviation Development (CADIP)</h3>
                        <p class="stat-value">K1.67 Billion</p>
                        <p class="stat-context">Largest aviation investment, primarily ADB-funded, for airport infrastructure upgrades.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Air Niugini Re-fleeting</h3>
                        <p class="stat-value">NZ$2 Billion</p>
                        <p class="stat-context">Investment for 2025-2028, acquiring 11 Airbus A220s & 2 Boeing 787s (under review).</p>
                    </div>
                </div>
            </section>
            <section id="energy" class="mb-12">
                <h2 class="section-title">Energy Infrastructure</h2>
                <p class="mb-6 text-gray-700">Access to reliable and affordable electricity is a critical challenge. PNG aims to increase access significantly and shift towards renewable energy, but the state utility PPL faces major operational and financial hurdles.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">On-Grid Electricity Access</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="electricityAccessChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Below 15%% of population. Target: 70%% by 2030.</p>
                        <button class="gemini-button" onclick="fetchAIResponse('lowEnergyAccess', 'innovativeSolutions', 'geminiResponseEnergyAccess')">✨ Suggest Innovative Solutions</button>
                        <div id="geminiResponseEnergyAccess" class="gemini-response-area" style="display: none;"></div>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Generation Mix (On-Grid, ~580-600MW Total)</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="generationMixChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Dominated by Hydropower and Diesel. Aim: 78%% renewables by 2030.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">PNG Power Ltd (PPL) Loss</h3>
                        <p class="stat-value">K271.79 Million</p>
                        <p class="stat-context">Loss after tax in 2022, highlighting financial challenges.</p>
                    </div>
                     <div class="stat-card md:col-span-2 lg:col-span-3">
                        <h3 class="stat-title">Key Energy Initiatives & Projects</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-2">
                            <li><span class="icon-placeholder">💡</span><strong>World Bank NEAT Project (US$204m):</strong> To boost energy access, expand renewables, modernise infrastructure.</li>
                            <li><span class="icon-placeholder">💧</span><strong>ADB Support:</strong> Hydropower rehabilitation, mini-grids, Sustainable Energy Sector Development Programme.</li>
                            <li><span class="icon-placeholder">☀️</span><strong>Renewable Focus:</strong> Planned projects include Naoro Brown & Ramu 2 hydro, Edevu hydro, Markham Valley solar & biomass.</li>
                            <li><span class="icon-placeholder">🔧</span><strong>PPL Reforms:</strong> KCH planning restructure, NEA now regulatory body. Significant investment needed for plant/network upgrades.</li>
                        </ul>
                        <button class="gemini-button" onclick="fetchAIResponse('majorRenewableProject', 'risksOpportunities', 'geminiResponseRenewableProject')">✨ Analyse Major Renewable Project R&O</button>
                        <div id="geminiResponseRenewableProject" class="gemini-response-area" style="display: none;"></div>
                    </div>
                </div>
            </section>
            <section id="wash" class="mb-12">
                <h2 class="section-title">Water, Sanitation & Hygiene (WASH)</h2>
                <p class="mb-6 text-gray-700">Access to safe water and sanitation remains critically low, posing significant public health challenges. Efforts are underway to improve services, but issues like low investment, aging infrastructure, and cost recovery persist.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Access to Improved Drinking Water</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="waterAccessChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Less than 50%% of households (DHS 2016-18).</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Access to Improved Sanitation</h3>
                        <div class="chart-container h-64 md:h-72"><canvas id="sanitationAccessChart"></canvas></div>
                        <p class="stat-context text-center mt-2">Only 29%% of households (DHS 2016-18).</p>
                        <button class="gemini-button" onclick="fetchAIResponse('lowSanitationAccess', 'innovativeSolutions', 'geminiResponseSanitation')">✨ Suggest Innovative Solutions</button>
                        <div id="geminiResponseSanitation" class="gemini-response-area" style="display: none;"></div>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Water PNG: Non-Revenue Water</h3>
                         <p class="stat-value">~52%%</p>
                        <p class="stat-context">High NRW due to leaks, illegal connections, aging infrastructure.</p>
                    </div>
                    <div class="stat-card md:col-span-2 lg:col-span-3">
                        <h3 class="stat-title">Key WASH Initiatives & Challenges</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-2">
                            <li><span class="icon-placeholder">💧</span><strong>World Bank WSSDP (US$70m):</strong> Upgrading water supply in provincial/district towns (e.g., Bialla, Bulolo).</li>
                            <li><span class="icon-placeholder">📜</span><strong>National WaSH Policy (2015) & Roadmap for WASH in Healthcare (2023-2030):</strong> Guiding frameworks.</li>
                            <li><span class="icon-placeholder">💸</span><strong>Challenges:</strong> Low investment, aging infrastructure, culture of non-payment, land tenure disputes, governance issues, climate impacts.</li>
                            <li><span class="icon-placeholder">🏙️</span><strong>Water PNG Plans (2025):</strong> Improve Port Moresby supply, new clarifier, potential Edevu Treatment Plant (PPP).</li>
                        </ul>
                    </div>
                </div>
            </section>
            <section id="cross-cutting" class="mb-12">
                <h2 class="section-title">Cross-Cutting Enablers & Themes</h2>
                <p class="mb-6 text-gray-700">Several overarching factors influence PNG's ability to develop and maintain its infrastructure, including funding mechanisms, climate resilience, and the performance of state-owned enterprises.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="stat-card">
                        <h3 class="stat-title">Infrastructure Funding (2025 Budget)</h3>
                        <p class="stat-value">K7.6 Billion</p>
                        <p class="stat-context">Announced for infrastructure development, a 273%% increase from 2018.</p>
                         <p class="text-sm text-gray-700 mt-4">Significant international partnerships (ADB, World Bank, Australia/AIFFP, EU, China) are crucial for financing major projects.</p>
                    </div>
                    <div class="stat-card">
                        <h3 class="stat-title">Climate Change & Resilience</h3>
                        <p class="text-gray-700"><span class="icon-placeholder">🌍</span>PNG is acutely vulnerable. National Adaptation Plan (NAP) prioritises transport & infrastructure.</p>
                        <p class="text-gray-700 mt-2"><span class="icon-placeholder">🛣️</span>DoWH Corporate Plan & Connect PNG include climate-resilient road standards.</p>
                        <p class="text-gray-700 mt-2"><span class="icon-placeholder">💧</span>Focus on renewable energy and resilient port/WASH projects.</p>
                        <p class="stat-context mt-2">Challenge: Integrating resilience comprehensively and addressing data/capacity gaps.</p>
                    </div>
                </div>
                <div class="stat-card mt-6">
                    <h3 class="stat-title text-center">SOE Reform: Kumul Consolidated Holdings (KCH) Oversight</h3>
                    <div class="flex flex-col items-center space-y-2 md:space-y-0 md:flex-row md:justify-around md:items-start mt-4">
                        <div class="flex flex-col items-center text-center">
                            <div class="flowchart-step mb-2">SOE Ownership Policy (2020) & KCH Act Amendment (2021)</div>
                            <div class="flowchart-arrow hidden md:block transform rotate-90 md:rotate-0">→</div>
                            <div class="flowchart-arrow md:hidden">↓</div>
                        </div>
                        <div class="flex flex-col items-center text-center">
                            <div class="bg-[#FFD166] text-[#073B4C] p-4 rounded-lg shadow flowchart-step mb-2">
                                Kumul Consolidated Holdings (KCH)
                                <p class="text-xs">(Primary Oversight for SOEs)</p>
                            </div>
                            <div class="flowchart-arrow hidden md:block transform rotate-90 md:rotate-0">→</div>
                            <div class="flowchart-arrow md:hidden">↓</div>
                        </div>
                        <div class="flowchart-step">
                            SOEs (Air Niugini, Telikom, PPL, PNG Ports, Water PNG etc.)
                            <p class="text-xs">Develop 3-yr Corporate Plans, Restructuring Strategies</p>
                        </div>
                    </div>
                    <p class="stat-context text-center mt-4">Aim: Transform SOEs into profitable, efficient service providers with good governance.</p>
                </div>
            </section>
            <section id="conclusion" class="mb-12">
                <h2 class="section-title">Conclusion: Opportunities, Risks & The Path Forward</h2>
                <p class="mb-6 text-gray-700">PNG is at a critical juncture. Ambitious strategies and international support offer significant opportunities, but substantial risks related to funding, governance, capacity, and climate change must be managed to ensure sustainable infrastructure development and improve citizens' lives.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="stat-card bg-[#E6FFFA] border-l-4 border-[#06D6A0]">
                        <h3 class="stat-title text-[#047857]">Key Opportunities</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1 mt-2">
                            <li>Strategic National Programmes (Connect PNG, Digital Transformation).</li>
                            <li>SOE Reforms & strengthened PPP framework to attract private capital.</li>
                            <li>Abundant Renewable Energy Potential (hydro, solar, geothermal).</li>
                            <li>Strong International Partnerships providing finance & expertise.</li>
                        </ul>
                    </div>
                    <div class="stat-card bg-[#FFF5F5] border-l-4 border-[#FF6B6B]">
                        <h3 class="stat-title text-[#C53030]">Potential Risks</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1 mt-2">
                            <li>Funding Sustainability & immense maintenance backlogs.</li>
                            <li>Governance, transparency, and corruption concerns.</li>
                            <li>Institutional and human capacity constraints.</li>
                            <li>Complex land tenure issues delaying projects.</li>
                            <li>High vulnerability to climate change and natural disasters.</li>
                            <li>SOE underperformance and financial instability.</li>
                            <li>Macroeconomic volatility and security issues.</li>
                        </ul>
                    </div>
                </div>
                <p class="mt-8 text-lg text-center text-gray-800">
                    The path forward requires steadfast commitment to strategic frameworks, robust governance, transparent procurement, and a clear focus on long-term sustainability and equitable benefit distribution for all citizens.
                </p>
            </section>
        </main>
        <footer class="bg-[#073B4C] text-white py-6 mt-12">
            <div class="container mx-auto px-4 text-center">
                <p class="text-sm">© 2025 PNG Infrastructure Infographic. Data based on "INFRASTRUCTURE CHALLENGES FOR PAPUA NEW GUINEA’S FUTURE: AN UPDATED ASSESSMENT (Post-2015 Developments)".</p>
                <p class="text-xs mt-1">This is a visual representation and interpretation of complex data for illustrative purposes. AI-generated content requires verification.</p>
            </div>
        </footer>
        <div id="geminiModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center" style="display: none;">
            <div class="bg-white p-6 rounded-lg shadow-xl w-11/12 md:max-w-md mx-auto">
                <h3 id="geminiModalTitle" class="text-lg font-semibold mb-3 text-[#073B4C]">Loading...</h3>
                <div id="geminiModalContent" class="text-sm text-gray-700 max-h-60 overflow-y-auto"></div>
                <button id="geminiModalClose" class="mt-4 bg-[#118AB2] text-white px-4 py-2 rounded hover:bg-[#0F789D] w-full">Close</button>
            </div>
        </div>
    </div>
    """

    # Critical section: script_content_js_template
    # The error is likely in this string.
    # We need to ensure all literal '%' are '%%' and the API call part for Groq is correct.
    # The API key placeholder is '%s'.
    script_content_js_template = """
        function wrapLabel(label, maxWidth = 16) {
            if (typeof label !== 'string' || label.length <= maxWidth) { return label; }
            const words = label.split(' ');
            let currentLine = '';
            const lines = [];
            for (const word of words) {
                if ((currentLine + word).length > maxWidth && currentLine.length > 0) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            }
            if (currentLine.trim().length > 0) { lines.push(currentLine.trim()); }
            return lines.length > 0 ? lines : [label];
        }

        const defaultChartOptions = {
            responsive: true, maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom', labels: { color: '#073B4C', font: { size: 10 } } },
                tooltip: {
                    callbacks: {
                        title: function(tooltipItems) {
                            const item = tooltipItems[0];
                            if (!item || !item.chart || !item.chart.data || !item.chart.data.labels || typeof item.dataIndex === 'undefined') return '';
                            let label = item.chart.data.labels[item.dataIndex];
                            if (Array.isArray(label)) { return label.join(' '); }
                            return label;
                        }
                    }
                }
            },
            scales: {
                y: { ticks: { color: '#073B4C', font: { size: 10 } }, grid: { color: '#E2E8F0' } },
                x: { ticks: { color: '#073B4C', font: { size: 10 } }, grid: { display: false } }
            }
        };

        const energeticPlayfulPalette = {
            coralRed: '#FF6B6B', sunnyYellow: '#FFD166', tealishGreen: '#06D6A0',
            ceruleanBlue: '#118AB2', darkSlateBlue: '#073B4C', lightGray: '#F8F9FA'
        };
        
        function initializeCharts() {
            const internetCtx = document.getElementById('internetPenetrationChart')?.getContext('2d');
            if (internetCtx) {
                new Chart(internetCtx, { type: 'doughnut',
                    data: { labels: ['Internet Users', 'Offline Population'],
                        datasets: [{ label: 'Internet Penetration', data: [24.1, 100 - 24.1], backgroundColor: [energeticPlayfulPalette.ceruleanBlue, energeticPlayfulPalette.lightGray], borderColor: [energeticPlayfulPalette.ceruleanBlue, energeticPlayfulPalette.lightGray], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
            const mobileCtx = document.getElementById('mobileConnectionsChart')?.getContext('2d');
            if (mobileCtx) {
                new Chart(mobileCtx, { type: 'doughnut',
                    data: { labels: ['Mobile Connections', 'No Connection'],
                        datasets: [{ label: 'Mobile Connections', data: [47.2, 100 - 47.2], backgroundColor: [energeticPlayfulPalette.tealishGreen, energeticPlayfulPalette.lightGray], borderColor: [energeticPlayfulPalette.tealishGreen, energeticPlayfulPalette.lightGray], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
            const affordabilityCtx = document.getElementById('internetAffordabilityChart')?.getContext('2d');
            if (affordabilityCtx) {
                new Chart(affordabilityCtx, { type: 'bar',
                    data: { labels: [wrapLabel('PNG Cost (%% GNI per capita)'), wrapLabel('Target Cost (%% GNI per capita)')], 
                        datasets: [{ label: 'Internet Basket Cost', data: [12.04, 2], backgroundColor: [energeticPlayfulPalette.coralRed, energeticPlayfulPalette.sunnyYellow], borderColor: [energeticPlayfulPalette.coralRed, energeticPlayfulPalette.sunnyYellow], borderWidth: 1 }]
                    },
                    options: { ...defaultChartOptions, indexAxis: 'y',
                         scales: { x: { ticks: { color: '#073B4C', font: {size: 10}, callback: function(value) { return value + '%%' } }, grid: { color: '#E2E8F0' } }, 
                                   y: { ticks: { color: '#073B4C', font: {size: 10} }, grid: {display: false} } },
                        plugins: { ...defaultChartOptions.plugins, tooltip: { callbacks: {
                                     title: function(tooltipItems) { 
                                        const item = tooltipItems[0]; if (!item || !item.chart || !item.chart.data || !item.chart.data.labels || typeof item.dataIndex === 'undefined') return '';
                                        let label = item.chart.data.labels[item.dataIndex]; if (Array.isArray(label)) { return label.join(' '); } return label;
                                    },
                                    label: function(context) { return context.dataset.label + ': ' + context.raw + '%%'; } 
                        }}}
                    }
                });
            }
            const roadConditionCtx = document.getElementById('roadConditionChart')?.getContext('2d');
            if (roadConditionCtx) {
                new Chart(roadConditionCtx, { type: 'doughnut',
                    data: { labels: ['Poor Condition', 'Fair/Good Condition'],
                        datasets: [{ label: 'Road Network Condition', data: [85, 15], backgroundColor: [energeticPlayfulPalette.coralRed, energeticPlayfulPalette.tealishGreen], borderColor: [energeticPlayfulPalette.coralRed, energeticPlayfulPalette.tealishGreen], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
            const connectPngProgressCtx = document.getElementById('connectPngProgressChart')?.getContext('2d');
            if (connectPngProgressCtx) {
                new Chart(connectPngProgressCtx, { type: 'bar',
                    data: { labels: [wrapLabel('Upgraded Strategic Highways (km)')],
                        datasets: [ { label: 'Achieved', data: [3500], backgroundColor: energeticPlayfulPalette.ceruleanBlue, }, { label: 'Phase 1 Target Remaining', data: [4220 - 3500], backgroundColor: energeticPlayfulPalette.lightGray, } ]
                    },
                    options: { ...defaultChartOptions, indexAxis: 'y',
                        scales: { x: { stacked: true, ticks: { color: '#073B4C', font: {size: 10} }, grid: { color: '#E2E8F0' } },
                                  y: { stacked: true, ticks: { color: '#073B4C', font: {size: 10} }, grid: {display: false} } },
                        plugins: { ...defaultChartOptions.plugins, tooltip: { callbacks: {
                                    title: function(tooltipItems) { 
                                        const item = tooltipItems[0]; if (!item || !item.chart || !item.chart.data || !item.chart.data.labels || typeof item.dataIndex === 'undefined') return '';
                                        let label = item.chart.data.labels[item.dataIndex]; if (Array.isArray(label)) { return label.join(' '); } return label;
                                    },
                                    label: function(context) { return context.dataset.label + ': ' + context.raw.toLocaleString() + ' km'; }
                        }}}
                    }
                });
            }
            const electricityAccessCtx = document.getElementById('electricityAccessChart')?.getContext('2d');
            if (electricityAccessCtx) {
                new Chart(electricityAccessCtx, { type: 'doughnut',
                    data: { labels: ['On-Grid Access', 'No On-Grid Access'],
                        datasets: [{ label: 'Electricity Access', data: [15, 85], backgroundColor: [energeticPlayfulPalette.sunnyYellow, energeticPlayfulPalette.lightGray], borderColor: [energeticPlayfulPalette.sunnyYellow, energeticPlayfulPalette.lightGray], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
            const generationMixCtx = document.getElementById('generationMixChart')?.getContext('2d');
            if (generationMixCtx) {
                new Chart(generationMixCtx, { type: 'pie',
                    data: { labels: ['Hydropower (39.7%%)', 'Diesel (37.4%%)', 'Fossil Gas (14.1%%)', 'Geothermal (9.1%%)', 'Solar (~1%%)'], 
                        datasets: [{ label: 'On-Grid Generation Mix', data: [39.7, 37.4, 14.1, 9.1, 1], 
                            backgroundColor: [ energeticPlayfulPalette.ceruleanBlue, energeticPlayfulPalette.coralRed, energeticPlayfulPalette.darkSlateBlue, energeticPlayfulPalette.sunnyYellow, energeticPlayfulPalette.tealishGreen ], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, plugins: { ...defaultChartOptions.plugins, legend: { position: 'right', labels: {color: '#073B4C', font: {size:9}, boxWidth:15}}}}
                });
            }
            const waterAccessCtx = document.getElementById('waterAccessChart')?.getContext('2d');
            if (waterAccessCtx) {
                new Chart(waterAccessCtx, { type: 'doughnut',
                    data: { labels: ['Improved Water', 'Unimproved/Surface Water'],
                        datasets: [{ label: 'Access to Improved Drinking Water', data: [45, 55], backgroundColor: [energeticPlayfulPalette.ceruleanBlue, energeticPlayfulPalette.lightGray], borderColor: [energeticPlayfulPalette.ceruleanBlue, energeticPlayfulPalette.lightGray], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
            const sanitationAccessCtx = document.getElementById('sanitationAccessChart')?.getContext('2d');
            if (sanitationAccessCtx) {
                new Chart(sanitationAccessCtx, { type: 'doughnut',
                    data: { labels: ['Improved Sanitation', 'Unimproved/Open Defecation'],
                        datasets: [{ label: 'Access to Improved Sanitation', data: [29, 71], backgroundColor: [energeticPlayfulPalette.tealishGreen, energeticPlayfulPalette.lightGray], borderColor: [energeticPlayfulPalette.tealishGreen, energeticPlayfulPalette.lightGray], borderWidth: 1 }]
                    }, options: {...defaultChartOptions, cutout: '70%%'} 
                });
            }
        }

        if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', initializeCharts); } 
        else { initializeCharts(); }

        const aiModal = document.getElementById('geminiModal'); 
        const aiModalTitle = document.getElementById('geminiModalTitle');
        const aiModalContent = document.getElementById('geminiModalContent');
        const aiModalClose = document.getElementById('geminiModalClose');

        if (aiModalClose) { aiModalClose.addEventListener('click', () => { if (aiModal) aiModal.style.display = 'none'; }); }

        function showAIModal(title, content) { 
            if (aiModalTitle) aiModalTitle.textContent = title;
            if (aiModalContent) aiModalContent.innerHTML = content.replace(/\\n/g, '<br>'); 
            if (aiModal) aiModal.style.display = 'flex';
        }
        
        // Renamed from fetchGeminiData to fetchAIResponse
        window.fetchAIResponse = async function(context, type, responseElementId) { 
            const responseElement = document.getElementById(responseElementId);
            if (responseElement) { responseElement.style.display = 'none'; responseElement.innerHTML = ''; }
            showAIModal('✨ AI Assistant Loading...', 'Fetching insights from Llama 3.1 via Groq API. Please wait...');

            let prompt = "";
            if (type === 'risksOpportunities') {
                if (context === 'connectPNG') {
                    prompt = "You are an infrastructure development analyst. For a large-scale national road connectivity program like 'Connect PNG' in Papua New Guinea, which aims to connect various regions and stimulate economic activity, briefly list 3 potential key risks and 3 potential key opportunities. Focus on socio-economic and logistical aspects relevant to PNG's context. Present as bullet points under 'Risks:' and 'Opportunities:' headings.";
                } else if (context === 'majorRenewableProject') {
                    prompt = "You are an energy project analyst. For a major new renewable energy project (e.g., large hydropower or solar farm) in Papua New Guinea, briefly list 3 potential key risks and 3 potential key opportunities. Consider environmental, social, technical, and financial aspects relevant to PNG. Present as bullet points under 'Risks:' and 'Opportunities:' headings.";
                }
            } else if (type === 'innovativeSolutions') {
                if (context === 'lowEnergyAccess') {
                    prompt = "You are a sustainable development expert. For Papua New Guinea, where on-grid electricity access is below 15%%, suggest 3 innovative and context-appropriate solutions or strategies to significantly improve rural and remote electricity access, beyond traditional grid expansion. Focus on sustainability and community involvement. Present as a numbered list with brief explanations.";
                } else if (context === 'lowSanitationAccess') {
                    prompt = "You are a public health and WASH (Water, Sanitation, Hygiene) specialist. For Papua New Guinea, where access to improved sanitation is very low (around 29%%), suggest 3 innovative and culturally sensitive solutions or strategies to significantly improve sanitation coverage, particularly in rural and peri-urban areas. Focus on sustainability, community participation, and health impact. Present as a numbered list with brief explanations.";
                }
            }

            if (!prompt) { showAIModal('Error', 'Invalid context for AI API call.'); return; }
            
            const apiKey = "%s"; // API Key placeholder
            const modelName = "llama-3.1-70b-versatile"; 

            if (!apiKey || apiKey === "YOUR_GROQ_API_KEY_PLACEHOLDER" || apiKey === "") { 
                 showAIModal('API Key Error', 'Groq API key is not configured. Please ensure it is set up in Streamlit secrets (if deployed) or provided in the sidebar (for local use) and refresh the page.');
                 if (responseElement) responseElement.style.display = 'none';
                 return;
            }
            
            const apiUrl = `https://api.groq.com/openai/v1/chat/completions`; // No question mark here usually
            
            const payload = {
                messages: [{ "role": "user", "content": prompt }],
                model: modelName
            };

            try {
                const apiResponse = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 
                        'Authorization': `Bearer ${apiKey}`, // Corrected Bearer token format
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (!apiResponse.ok) {
                    const errorData = await apiResponse.json();
                    console.error('Groq API Error:', errorData);
                    let detailedMessage = (errorData.error && errorData.error.message) ? errorData.error.message : 'Unknown error. Check browser console for details.';
                    showAIModal('AI Assistant Error', `Could not fetch insights from Groq. Status: ${apiResponse.status}. Message: ${detailedMessage}`);
                    return;
                }

                const result = await apiResponse.json();
                
                let text = "No content generated or error in Groq response structure.";
                if (result.choices && result.choices.length > 0 &&
                    result.choices[0].message && result.choices[0].message.content) {
                    text = result.choices[0].message.content;
                } else if (result.choices && result.choices.length > 0 && result.choices[0].finish_reason && result.choices[0].finish_reason !== "stop") {
                     text = `Content generation stopped by Groq. Reason: ${result.choices[0].finish_reason}.`;
                } else {
                     showAIModal('AI Assistant Response', 'Received an empty or malformed response from Groq. Check console for details.');
                     console.log("Malformed Groq AI Response:", result);
                     return;
                }
                
                if (responseElement) {
                    responseElement.innerHTML = text.replace(/\\n/g, '<br>'); 
                    responseElement.style.display = 'block';
                }
                if (aiModal) aiModal.style.display = 'none';

            } catch (error) {
                console.error('Fetch error (Groq):', error);
                showAIModal('Network Error', 'Could not connect to the AI assistant (Groq). Please check your internet connection and API key. Error: ' + error.message);
            }
        }
    """

    # If the error is indeed from a '?', it's highly likely it's in the apiUrl construction, 
    # especially if it was trying to add a query parameter like "?key=" which we removed for Groq.
    # Let's ensure no stray '?' are near %s or in URL-like strings if they are not query params.
    # The error "unsupported format character '?' (0xa) at index 2679" means
    # at that specific index in the `script_content_js_template` string,
    # there is literally a single '%' followed by a '?'.

    # Count characters to find index 2679. This is hard to do manually.
    # A common place for '?' is in URLs. Let's re-check the apiUrl line carefully.
    # The previous Groq API URL was:
    # const apiUrl = `https://api.groq.com/openai/v1/chat/completions`;
    # This line itself doesn't have a '?' or a '%'.
    # The issue must be a literal '%?' sequence somewhere else in the JS template.

    # Let's assume for a moment the error character (0xa) might be misleading and it's a literal '%?'
    # I'll scan for '%?'
    # ... (manual scan of the JS code above) ...
    # I don't immediately see a '%?' sequence.

    # The error might be that a previously escaped '%%' was somehow reverted or a new '%' was introduced.
    # I've re-escaped all known % in the Chart.js options and labels like '70%%'.

    # One more check: Ensure the API key placeholder is truly the only single '%'.
    if script_content_js_template.count('%s') != 1:
        # This would be a problem with my template construction
        st.error("Developer Error: API key placeholder count is not 1 in JS template.")
        # For debugging, print how many %s it finds
        # print(f"Count of '%s': {script_content_js_template.count('%s')}")
        # print(f"Count of '%%': {script_content_js_template.count('%%')}")
        
        # To find single unescaped % not part of %s
        import re
        single_percent_errors = []
        for i, char_val in enumerate(script_content_js_template):
            if char_val == '%' and (i + 1 < len(script_content_js_template)):
                next_char = script_content_js_template[i+1]
                if next_char != '%' and next_char != 's': # if it's not '%%' and not '%s'
                    # Check if it's the start of a valid (but unwanted here) format specifier
                    if next_char in "diouxXeEfFgGcr": # common format specifiers
                         single_percent_errors.append(f"Potential unescaped format specifier '%{next_char}' at index {i}")
                    elif next_char == '?': # The specific error
                         single_percent_errors.append(f"Found offending '%?' at index {i}")


        if single_percent_errors:
            st.error("Found potential unescaped '%' characters in JS template that are not '%%' or the API key placeholder '%s':")
            for err in single_percent_errors:
                st.error(err)
            # This part is for debugging if the app is run locally by the developer
            # print("SINGLE PERCENT ERRORS:", single_percent_errors)
            # You'd then manually go to these indices in your editor.

    try:
        actual_script_content = script_content_js_template % (groq_api_key_js if groq_api_key_js is not None else "")
    except ValueError as e:
        st.error(f"Still encountered a ValueError during Python string formatting for JavaScript: {e}")
        st.error("This usually means a single '%' character is in the JavaScript template that is not part of the API key placeholder ('%s') and is not escaped as '%%'. Please meticulously review the script_content_js_template.")
        # For developer debugging:
        # print("----- ERROR DURING JS STRING FORMATTING -----")
        # print(e)
        # print("----- SCRIPT TEMPLATE causing error (first 3000 chars) -----")
        # print(script_content_js_template[:3000]) # Print a portion to help locate
        # print("----- END SCRIPT TEMPLATE -----")
        raise # re-raise the error to stop execution and see full Streamlit traceback

    full_html = f"""
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Papua New Guinea: Infrastructure Challenges & Future Outlook</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
            <style>{style_content}</style>
        </head>
        <body>
            {body_content_html}
            <script>{actual_script_content}</script>
        </body>
    """
    return full_html

def main():
    st.set_page_config(page_title="PNG Infrastructure Infographic", layout="wide")

    groq_api_key = "" 
    try:
        groq_api_key = st.secrets.get("GROQ_API_KEY", "")
    except FileNotFoundError:
         st.sidebar.info("Local secrets.toml not found. Use sidebar input for Groq API key if needed.")
         groq_api_key = ""
    except Exception: # Catch any other secrets-related errors
        st.sidebar.warning("Could not read secrets. Ensure `secrets.toml` is correctly formatted if used locally, or secrets are set on the server.")
        groq_api_key = ""


    st.sidebar.header("API Configuration (Groq Llama 3.1)")
    if not groq_api_key: # If not found in secrets (or secrets failed to load)
        # Try to access directly, st.secrets acts like a dict
        if "GROQ_API_KEY" in st.secrets and st.secrets["GROQ_API_KEY"]:
             groq_api_key = st.secrets.GROQ_API_KEY # Use .get or direct access
             st.sidebar.success("Groq API Key loaded from secrets.")
        else:
            st.sidebar.warning("Groq API Key not found in Streamlit secrets.")
            groq_api_key_input = st.sidebar.text_input(
                "Enter Groq API Key for Llama 3.1 features:", 
                type="password", 
                value="", # Ensure default is empty
                help="Your Groq API key is used to fetch live insights via Llama 3.1."
            )
            if groq_api_key_input:
                groq_api_key = groq_api_key_input
            else: # Still no key
                st.sidebar.info("AI-powered insights (✨ buttons) will be disabled or show an error until a valid Groq API key is provided and the page is re-run.")
    else: # Key was successfully loaded from st.secrets.get initially
        st.sidebar.success("Groq API Key loaded from secrets.")


    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "**Important for GitHub & Deployment:**\n"
        "1.  **Do NOT commit your API key directly into your `app.py` or any other file in your GitHub repository if it's public.**\n"
        "2.  Store your `GROQ_API_KEY` in the Streamlit app's secrets configuration on the deployment platform.\n\n"
        "**For local development, you can:**\n"
        "1. Use the input field above (key is not saved beyond the session).\n"
        "2. Or, create a `.streamlit/secrets.toml` file in your project's root directory with your key:\n"
        "   ```toml\n"
        "   GROQ_API_KEY = \"YOUR_ACTUAL_GROQ_API_KEY\"\n"
        "   ```"
    )
    st.sidebar.markdown("---")
    st.sidebar.info("Using Groq API with Llama-3.1-70b-versatile model for AI insights.")

    # Ensure groq_api_key is a string before passing
    html_content = get_streamlit_app_content(groq_api_key_js=str(groq_api_key) if groq_api_key is not None else "")
    st.markdown(html_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
