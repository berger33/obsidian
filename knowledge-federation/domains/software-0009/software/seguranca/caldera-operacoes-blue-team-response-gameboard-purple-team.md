---
id: software.seguranca.tranche12.001126
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Caldera para o **Blue Team e Purple Team**: Plugins **`response`**, **`gameboard`** e **`compass`** para Defesa Automatizada e Visualização Conjunta

## Em uma frase
Muitos profissionais pensam no **MITRE Caldera** apenas como uma ferramenta ofensiva de Red Team, mas ele foi projetado desde o início como uma plataforma **Red + Blue (Purple Team)** com um dashboard exclusivo para defensores e plugins de resposta automatizada a incidentes!

## Por que importa
O plugin **`response`** (`mitre/response`) equipa agentes do grupo `blue` com *Abilities* defensivas e de caça a ameaças (como coletar conexões de rede suspeitas, buscar processos órfãos, verificar entradas de persistência no Registro/WMI/Cron, matar processos maliciosos identificados e bloquear endereços IP no firewall local) que reagem automaticamente aos fatos descobertos no endpoint!

## Como funciona
Já o plugin **`gameboard`** (`mitre/gameboard`) cria um placar visual interativo que correlaciona lado a lado cada `link` executado pelo agente Red com as detecções e ações de resposta do time Blue, enquanto o plugin **`compass`** gera e importa camadas do **MITRE ATT&CK Navigator** diretamente na interface do Caldera!

## Exemplo
```bash
# Consultar via API REST v2 do Caldera os agentes registrados filtrando especificamente pelos agentes defensivos do grupo 'blue'
CALDERA_API_KEY="ADMIN123"
curl -sS -H "KEY: ${CALDERA_API_KEY}" http://127.0.0.1:8888/api/v2/agents | \
  jq '[.[] | select(.group == "blue") | {paw: .paw, host: .host, platform: .platform, trusted: .trusted}]'
```

## Limites e trade-offs
Outra joia do ecossistema do Caldera para laboratórios de treinamento de SOC é o plugin **`human`** (`mitre/human`): ele gera **ruído benigno realista de usuário** nos endpoints do laboratório (navegação web, criação de documentos, comandos normais de terminal, uso de e-mail) para que os analistas do SOC precisem separar os ataques reais do agente Sandcat em meio ao tráfego legítimo do dia a dia!

## Como verificar
Use o plugin `training` embutido no Caldera para capacitar novos engenheiros de segurança através de desafios práticos guiados estilo CTF.

## Conexões
- [[caldera-furtividade-ofuscadores-jitter-builder-evasao-edr]] — Veja também: Controles de Furtividade (*Stealth*) em Operações do Caldera: **Obfuscators** (`plain-text`, `base64`, `caesar`, `steganography`), **Jitter** e **Autonomous Mode**.
- [[caldera-relatorios-debrief-api-rest-automacao-cicd]] — Veja também: Automação via **API REST v2 (`/api/v2/operations`)** e Relatórios Executivos/Técnicos com o Plugin **`debrief`** do Caldera.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[caldera-plugins-stockpile-emu-atomic-planos-ctid]] — Referência cruzada direta com caldera-plugins-stockpile-emu-atomic-planos-ctid.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
