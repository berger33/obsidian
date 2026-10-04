---
id: software.seguranca.tranche08.000768
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/owasp-amass/amass/master/README.md", "https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md", "https://pkg.go.dev/github.com/owasp-amass/amass/v4"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Amass (`oam_track` / `amass track`): Monitoramento Contínuo de **Drift da Superfície de Ataque** e Alertas de Novos Subdomínios e Mudanças de IP

## Em uma frase
Em um programa maduro de **Continuous Threat Exposure Management (CTEM) / EASM**, rodar o Amass uma única vez no ano é insuficiente: a cada semana, equipes de desenvolvimento e marketing criam novos subdomínios, apontam registros `CNAME` para serviços SaaS externos ou mudam endereços IP na nuvem.

## Por que importa
Como o banco de dados do Amass armazena cada execução (`Session` / timestamp) separadamente no grafo, a ferramenta **`oam_track`** (ou **`amass track`** no binário v3) compara automaticamente as sessões de enumeração ao longo do tempo para um domínio (`-d exemplo.com.br`) e exibe **apenas o diferencial (*diff / drift*)**: quais subdomínios surgiram hoje pela primeira vez, quais registros DNS mudaram de IP e quais novos blocos CIDR ou ASNs passaram a hospedar ativos da empresa!

## Como funciona
Colocar um cronjob / pipeline diário que roda `amass enum -d exemplo.com.br -dir /cases/easm/amass_db` seguido de `oam_track` e dispara o **Nuclei** apenas sobre os ativos recém-aparecidos cria um radar automático de superfície de ataque!

## Exemplo
```bash
# Comparar as duas ultimas enumeracoes gravadas no banco de grafo para detectar apenas ativos novos ou alterados
oam_track -dir /cases/easm/amass_db -d exemplo.com.br -last 2
```

## Limites e trade-offs
Você também pode usar a flag **`-since "2026/10/01 00:00:00"`** no `oam_track` / `amass track` para auditar todas as mudanças na superfície externa da organização ocorridas desde uma data específica (por exemplo, após uma janela de migração de nuvem).

## Como verificar
Integre a saída do diferencial diário a um webhook do Slack/Teams/Mattermost do SOC para que todo novo subdomínio criado na empresa seja revisado no mesmo dia.

## Conexões
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — Veja também: OWASP Amass & **`oam-tools` (`oam_subs` / `amass db`)**: Persistência em Banco de Grafo (`-dir` / PostgreSQL) e Extração de Relações OAM.
- [[amass-visualizacao-topologia-rede-oam-viz-d3-maltego-gexf]] — Veja também: OWASP Amass (`oam_viz` / `amass viz`): Exportação do Grafo de Superfície de Ataque para **D3.js HTML Interativo (`-d3`)**, **Gephi (`-gexf`)**, **Graphviz (`-dot`)** e **Maltego**.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
