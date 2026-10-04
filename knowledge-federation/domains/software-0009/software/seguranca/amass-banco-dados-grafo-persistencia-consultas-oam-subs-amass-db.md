---
id: software.seguranca.tranche08.000767
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

# OWASP Amass & **`oam-tools` (`oam_subs` / `amass db`)**: Persistência em Banco de Grafo (`-dir` / PostgreSQL) e Extração de Relações OAM

## Em uma frase
O verdadeiro diferencial operacional do OWASP Amass em programas contínuos de EASM é que ele **não joga fora o conhecimento adquirido ao final da execução**: todos os ativos, registros DNS, certificados, ASNs, CIDRs e timestamps são gravados no banco de dados de grafo no diretório **`-dir /cases/easm/amass_db`** (SQLite local por padrão, ou um cluster **PostgreSQL** corporativo configurado em `config.yaml` / `datasources.yaml`).

## Por que importa
Para consultar o banco de dados sem disparar novo tráfego de rede, utiliza-se **`oam_subs`** (do repositório oficial `owasp-amass/oam-tools`, sucessor modular de `amass db`): **`oam_subs -names -d exemplo.com.br`** lista instantaneamente todos os FQDNs conhecidos, **`oam_subs -ip -d exemplo.com.br`** inclui os IPs e **`oam_subs -show -d exemplo.com.br`** imprime todas as triplas do grafo OAM (`nó_origem --> aresta --> nó_destino`) mais o resumo de ASNs e sub-redes CIDR!

## Como funciona
Centralizar o banco do Amass em um PostgreSQL permite que múltiplos coletores distribuídos alimentem o mesmo grafo de superfície de ataque da organização.

## Exemplo
```bash
# Consultar instantaneamente o banco de grafo persistido (-dir) exibindo as relacoes OAM, ASNs, CIDRs e enderecos IP
oam_subs -dir /cases/easm/amass_db -d exemplo.com.br -show -ip
```

## Limites e trade-offs
Em instalações que utilizam o binário integrado `amass` v3.x (presente em diversas distribuições Linux), os mesmos comandos de consulta ao banco de grafo são executados via **`amass db -dir /cases/easm/amass_db -d exemplo.com.br -show -ip`** ou `amass db -names -d exemplo.com.br`.

## Como verificar
Faça backup regular do diretório `-dir /cases/easm/amass_db` para preservar o histórico temporal de enumerações da organização.

## Conexões
- [[amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning]] — Veja também: OWASP Amass: Pool de **Resolvedores DNS Confiáveis (`-rf`, `-trf`)**, Limite de Taxa (`-dns-qps`, `-max-dns-queries`) e Detecção de **Wildcards / DNS Poisoning**.
- [[amass-monitoramento-continuo-drift-superficie-ataque-oam-track]] — Veja também: OWASP Amass (`oam_track` / `amass track`): Monitoramento Contínuo de **Drift da Superfície de Ataque** e Alertas de Novos Subdomínios e Mudanças de IP.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.
- [[amass-visualizacao-topologia-rede-oam-viz-d3-maltego-gexf]] — Referência cruzada direta com amass-visualizacao-topologia-rede-oam-viz-d3-maltego-gexf.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
