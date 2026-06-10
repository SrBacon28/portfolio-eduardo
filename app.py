import streamlit as st
import os

# 1. Configuração da página - Premium Dark Mode
st.set_page_config(
    page_title="Eduardo Borges — Tech & Creative Portfolio",
    page_icon="⚡",
    layout="wide"
)

# 2. Design System Avançado (CSS Customizado)
st.markdown("""
    <style>
    /* Reset e fontes */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');
    
    /* Efeito de Gradiente Neon no Nome Principal */
    .title-gradient { 
        font-family: 'Outfit', sans-serif;
        font-size: 56px; 
        font-weight: 900; 
        background: linear-gradient(90deg, #00d1ff 0%, #00ffaa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px; 
        margin-top: 15px;
        margin-bottom: 2px;
    }
    
    .age-badge { font-family: 'Outfit', sans-serif; font-size: 16px; color: #a0aec0; margin-bottom: 15px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
    .subtitle { font-size: 18px; color: #8892b0; margin-bottom: 20px; font-weight: 400; }
    .section-title { font-size: 28px; font-weight: 700; color: #ffffff; border-left: 5px solid #00d1ff; padding-left: 15px; margin-top: 25px; margin-bottom: 20px; }
    
    /* Blocos de Conteúdo Estilizados */
    .box { background: linear-gradient(135deg, #161616 0%, #1c1c1c 100%); padding: 25px; border-radius: 16px; border: 1px solid #2d2d2d; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    .box h4 { font-size: 20px; color: #ffffff; margin-top: 0; font-weight: 700; display: flex; align-items: center; gap: 10px; }
    
    /* Badges e destaques */
    .badge-tech { background-color: rgba(0, 209, 255, 0.1); color: #00d1ff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; border: 1px solid rgba(0, 209, 255, 0.2); }
    .highlight { color: #00d1ff; font-weight: 700; }
    .mantra { font-style: italic; color: #00d1ff; font-size: 15px; margin-top: 10px; display: block; }
    
    /* Estilização das Redes Sociais / Contatos */
    .social-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: #8892b0;
        text-decoration: none;
        font-weight: 600;
        padding: 8px 16px;
        border-radius: 8px;
        border: 1px solid #2d2d2d;
        background: #111;
        transition: all 0.3s ease;
    }
    .social-link:hover {
        color: #00d1ff;
        border-color: #00d1ff;
        background: rgba(0, 209, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- CAPA DO SITE ---
if os.path.exists("imagens/capa.png"):
    st.image("imagens/capa.png", use_container_width=True)

# Cabeçalho de Alto Impacto com Gradiente e Idade Atualizada
st.markdown('<p class="title-gradient">EDUARDO CÉSAR CABRAL BORGES</p>', unsafe_allow_html=True)
st.markdown('<p class="age-badge">ブラジル • 22 ANOS</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🚀 Comunicação Pública Estratégica | 🎨 Identidade Visual, Branding Político e GenAI</p>', unsafe_allow_html=True)

# --- LINKS DE CONTATO REAIS CONFIGURADOS ---
NUMERO_WHATSAPP = "5534996987240"  
SEU_EMAIL = "edurochaborges@gmail.com"

link_whatsapp = f"https://wa.me/{NUMERO_WHATSAPP}"
link_email = f"mailto:{SEU_EMAIL}"

col_links, _ = st.columns([2, 1])
with col_links:
    st.markdown(f"""
        <div style="display: flex; gap: 12px; margin-bottom: 25px;">
            <a href="{link_whatsapp}" target="_blank" class="social-link">💬 WhatsApp</a>
            <a href="{link_email}" class="social-link">📧 E-mail</a>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# Abas Principais com Foco na Transição para o Design Gráfico Oficial
aba_perfil, aba_design, aba_skills, aba_projetos = st.tabs([
    "👤 Proposta & Manifesto", 
    "📐 Lab de Design Visual (Portfólio)", 
    "⚡ Arsenal Técnico", 
    "🎓 Engenharia & Projetos"
])

# ----------------- ABA 1: PROPOSTA & MANIFESTO -----------------
with aba_perfil:
    col_foto, col_espaco, col_texto = st.columns([1, 0.1, 2])
    with col_foto:
        if os.path.exists("imagens/eu.png"):
            st.image("imagens/eu.png", use_container_width=True)
        else:
            st.image("https://placehold.co/300x300?text=Sua+Foto", use_container_width=True)
        st.markdown('<p style="text-align:center; color:#666; font-size:13px; margin-top:10px;">Visual Designer & Estrategista de Comunicação</p>', unsafe_allow_html=True)
        
    with col_texto:
        st.markdown('<p class="section-title">Meu Objetivo Estratégico</p>', unsafe_allow_html=True)
        st.write("""
        Atuando na engrenagem interna do município, desenvolvi uma compreensão profunda de como a administração pública funciona. No entanto, minha verdadeira vocação e maior potencial de contribuição para a nossa cidade estão na **comunicação visual de alto impacto**.
        
        Minha meta é consolidar minha atuação como <span class="highlight">Designer Gráfico oficial da Prefeitura</span>, aplicando técnica acadêmica, velocidade de execução e inteligência artificial para elevar o padrão das campanhas institucionais e do branding político do Gabinete.
        """, unsafe_allow_html=True)

        st.markdown('<p class="section-title">Por que um Designer que conhece a Gestão Interna faz a diferença?</p>', unsafe_allow_html=True)
        
        # Cards de impacto direcionados ao Prefeito e Primeira Dama
        st.markdown("""
        <div class="box">
            <h4>🏛️ Alinhamento e Conexão Humana</h4>
            <p>Compreendo perfeitamente o tom de voz que o Gabinete e a Primeira Dama buscam. Minhas peças não são apenas bonitas; elas traduzem as conquistas da gestão em orgulho para o cidadão, usando psicologia das cores e grids limpos para gerar proximidade e engajamento real nas redes sociais.</p>
        </div>
        <div class="box">
            <h4>⚙️ Agilidade Institucional e Economia</h4>
            <p>Diferente de um designer externo, eu conheço a rotina das secretarias e a urgência dos prazos públicos. Sei o que uma campanha precisa para ser aprovada de forma rápida, eliminando refações desnecessárias e entregando layouts prontos para veiculação com foco em utilidade pública.</p>
        </div>
        <div class="box">
            <h4>🚀 Inovação Tecnológica com Inteligência Artificial</h4>
            <p>Domino ferramentas de IA generativa para a criação e direção de pílulas audiovisuais modernas. Isso garante que a comunicação do município esteja sempre na vanguarda tecnológica, gerando conteúdos disruptivos em tempo recorde.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<p class="section-title">Formação Acadêmica e Experiência</p>', unsafe_allow_html=True)
        st.write("""
        * **📐 Formação em Design Gráfico:** 6 períodos de bagagem densa na **ESAMC Uberlândia** (grade integrada com Publicidade). Domínio completo de direção de arte, tipografia comercial, grids estruturados e identidade de marca.
        * **💻 Ciência da Computação (UNITRI):** Graduando (1º Período). Desenvolvimento de raciocínio lógico avançado e arquitetura de dados aplicados à automação e otimização.
        * **⚡ Experiência de Campo:** Atuação direta na estrutura interna da Prefeitura de Tupaciguara, conhecendo de perto as demandas reais da população e as diretrizes do governo municipal.
        """, unsafe_allow_html=True)

# ----------------- ABA 2: LAB DE DESIGN VISUAL (PORTFÓLIO CORRIGIDO) -----------------
with aba_design:
    st.markdown('<p class="section-title">📐 Engenharia Visual Aplicada</p>', unsafe_allow_html=True)
    categoria = st.radio("Filtrar portfólio por ecossistema:", ["🏛️ Gabinete do Prefeito (Branding Político)", "📢 Campanhas Institucionais (Utilidade Pública)"], horizontal=True)
    st.write("---")

    if categoria == "🏛️ Gabinete do Prefeito (Branding Político)":
        st.caption("⚡ Foco: Conexão humana, quebra de formalidade rígida e comunicação direta da liderança municipal.")
        
        tab_pizza, tab_arraia, tab_pagou, tab_cinema, tab_videos = st.tabs([
            "🍕 Dia da Pizza", "🔥 Festa Junina", "💰 Salário na Conta", "🎬 Cinema Brasileiro", "🎬 Pílulas Audiovisuais"
        ])
        
        with tab_pizza:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/pizza.png"): c1.image("imagens/pizza.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🍕 Case: Dia Mundial da Pizza</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Romper a barreira séria do governo e criar um ponto de contato altamente instagramável e leve com a comunidade.
                * **A Solução:** Design lúdico, apostando em gatilhos visuais de apetite e tipografia descontraída para humanizar as redes do Prefeito.
                <span class="mantra">"Mantra: Nem toda comunicação institucional precisa ser cinza."</span>
                """, unsafe_allow_html=True)
        
        with tab_arraia:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/arraia.png"): c1.image("imagens/arraia.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🔥 Case: Arraiá do Município</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Divulgar um evento cultural gigantesco condensando informações mantendo a energia festiva sem poluir o layout.
                * **A Solução:** Criação de um grid temático rico em texturas e profundidade. Hierarquia rígida onde o olhar do cidadão bate primeiro na data.
                <span class="mantra">"Mantra: O ornamento serve ao layout, nunca o contrário."</span>
                """, unsafe_allow_html=True)
        
        with tab_pagou:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/pagou.png"): c1.image("imagens/pagou.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">💰 Case: Transparência Financeira (Tá na Conta)</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Comunicar o pagamento dos servidores públicos gerando sensação de segurança e compromisso.
                * **A Solução:** Design Bold (negrito), limpo e direto. Cores sólidas de contraste que entregam a informação principal de forma instantânea.
                <span class="mantra">"Mantra: Mensagem rápida para quem tem pressa."</span>
                """, unsafe_allow_html=True)

        with tab_cinema:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/netocinema.png"): c1.image("imagens/netocinema.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🎬 Case: Liderança & Cultura (Dia do Cinema)</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Associar a imagem do Prefeito ao fomento cultural de forma orgânica e robusta.
                * **A Solução:** Grid assimétrico moderno inspirado em posters de cinema contemporâneos, mesclando o elemento humano com grafismos sutis.
                """)

        with tab_videos:
            col_v1, col_v2 = st.columns([1.3, 1])
            
            with col_v1:
                video_selecionado = st.selectbox(
                    "Selecione a produção audiovisual:", 
                    ["cadeira.mp4", "lua.mp4"]
                )
                caminho_video = os.path.join("videos", video_selecionado)
                
                if os.path.exists(caminho_video):
                    with open(caminho_video, 'rb') as video_file:
                        video_bytes = video_file.read()
                    st.video(video_bytes)
                else:
                    st.warning(f"⚠️ O arquivo `{video_selecionado}` não foi encontrado na pasta `videos`.")
            
            with col_v2:
                st.markdown('<p class="destaque-arte">🎬 Amostras Técnicas: GenAI & Vídeos de Impacto</p>', unsafe_allow_html=True)
                st.write("""
                * **O Conceito:** Estas produções servem como **amostras práticas** que validam meu domínio completo e conhecimento avançado na criação e direção de vídeos gerados por meio de <span class="highlight">Inteligências Artificiais Generativas</span>.
                * **A Solução:** Aplicação prática de pipelines modernos de GenAI para criar narrativas fluidas de alto engajamento, dominando comandos e parâmetros complexos para garantir coerência de movimento, ritmo acelerado (Fast-paced cutting) e estética cinematográfica de altíssimo padrão.
                * **Destaque:** Demonstração real de controle de ferramentas de IA integradas à identidade visual do Gabinete para retenção rápida em Reels e Shorts.
                """)

    else:
        st.caption("⚡ Foco: Campanhas de impacto social massivo, onde clareza visual significa eficácia em saúde e civismo.")
        tab_dengue, tab_ind, tab_sangue, tab_serv = st.tabs(["🚫 Combate à Dengue", "🇧🇷 Independência", "🩸 Doador de Sangue", "💼 Servidor Público"])
        
        with tab_dengue:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/dengue.png"): c1.image("imagens/dengue.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🚫 Case: Alerta Vermelho — Guerra à Dengue</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Combater a negligência doméstica criando um senso de urgência real na população.
                * **A Solução:** Psicologia cromática de alto impacto (amarelo-alerta e preto). Ícones minimalistas para leitura universal rápida e foco nas ações preventivas.
                """)

        with tab_ind:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/indepen.png"): c1.image("imagens/indepen.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🇧🇷 Case: Solenidade e Identidade (7 de Setembro)</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Celebrar a data cívica fugindo dos layouts clichês do setor público tradicional.
                * **A Solução:** Limpeza heráldica. Cores nacionais aplicadas em tons sóbrios com uso elegante de espaços em branco (Negative Space), conferindo sofisticação à peça.
                """)

        with tab_sangue:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/sangue.png"): c1.image("imagens/sangue.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">🩸 Case: Junho Vermelho (Doação de Sangue)</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Sensibilizar o cidadão para o ato da doação através de um apelo emocional equilibrado e profissional.
                * **A Solução:** Domínio monocromático de alto contraste, direcionando o olhar do usuário diretamente para a chamada de ação.
                """)

        with tab_serv:
            c1, c2 = st.columns([1, 1.2])
            if os.path.exists("imagens/servidor.png"): c1.image("imagens/servidor.png", use_container_width=True)
            with c2:
                st.markdown('<p class="destaque-arte">💼 Case: Valorização do Funcionalismo Público</p>', unsafe_allow_html=True)
                st.write("""
                * **O Desafio:** Criar uma homenagem institucional que represente a relevância dos trabalhadores municipais.
                * **A Solução:** Layout corporativo moderno e geométrico, mesclando fotografia humanizada com linhas precisas do brasão municipal.
                """)

# ----------------- ABA 3: ARSENAL TÉCNICO -----------------
with aba_skills:
    st.markdown('<p class="section-title">Minhas Competências Técnicas</p>', unsafe_allow_html=True)
    col_sk1, col_sk2 = st.columns(2)
    with col_sk1:
        st.markdown("""
        <div class="box">
            <h4>🎨 Creative Intelligence & UI/UX</h4>
            <p>Arquitetura visual focada em marcas, governos e produtos digitais.</p>
            <ul>
                <li><strong>Adobe Illustrator & Photoshop:</strong> Vetorização avançada, tratamento de imagem e key visuals.</li>
                <li><strong>Figma:</strong> Criação de protótipos e Design Systems padronizados.</li>
                <li><strong>Branding Institucional:</strong> Traduzir a complexidade do setor público em layouts modernos para o ambiente digital.</li>
            </ul>
            <span class="badge-tech">UX/UI</span> <span class="badge-tech">Direção de Arte</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_sk2:
        st.markdown("""
        <div class="box">
            <h4>⚙️ Engenharia Reversa, Hardware & Code</h4>
            <p>Intervenções físicas em eletrônicos e lógica estruturada de software.</p>
            <ul>
                <li><strong>Hardware Hacking:</strong> Micro-soldagem, diagnóstico de trilhas, reparo de placas e reconstrução de setups de alta performance.</li>
                <li><strong>Console Modding:</strong> Modificações físicas e de software em plataformas de hardware.</li>
                <li><strong>Desenvolvimento Core:</strong> Algoritmos estruturados com foco em automação de tarefas cotidianas utilizando Python.</li>
            </ul>
            <span class="badge-tech">Micro-soldagem</span> <span class="badge-tech">Python / C</span> <span class="badge-tech">Hardware</span>
        </div>
        """, unsafe_allow_html=True)

# ----------------- ABA 4: PROJETOS DE FACULDADE -----------------
with aba_projetos:
    st.markdown('<p class="section-title">🎓 Projetos Acadêmicos & Engenharia de Software</p>', unsafe_allow_html=True)
    colp1, colp2 = st.columns(2)
    with colp1:
        st.markdown("""
        <div class="box">
            <h4>🎮 Pitch Acadêmico: Console Modular de Baixo Custo</h4>
            <p><strong>Conceito do Projeto:</strong> Apresentação e modelagem de arquitetura para um hardware modular totalmente acessível focado na democratização tecnológica. Trabalho desenvolvido em equipe aplicando conceitos de viabilidade técnica.</p>
            <span class="badge-tech">Academic Pitch</span> <span class="badge-tech">Hardware Design</span>
        </div>
        """, unsafe_allow_html=True)
        
    with colp2:
        st.markdown("""
        <div class="box">
            <h4>🖥️ Algoritmos de Otimização e Lógica Estruturada</h4>
            <p><strong>Desenvolvimento Core:</strong> Implementação de ferramentas lógicas, scripts utilitários e algoritmos acadêmicos em linguagens estruturadas (Python/C). Foco em automação avançada de processos.</p>
            <span class="badge-tech">Algoritmos</span> <span class="badge-tech">Python / C Core</span>
        </div>
        """, unsafe_allow_html=True)

st.write("---")
st.caption("Portfólio Interativo • Estruturado com precisão por Eduardo César Cabral Borges")