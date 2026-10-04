---
id: software.seguranca.tranche08.000770
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

# OWASP Amass: Integração em Pipelines de Reconhecimento (**Amass -> `oam_subs` -> `httpx` -> `katana` -> `nuclei`**) e Execução Contêinerizada Docker

## Em uma frase
Em arquiteturas de automação de **DevSecOps e Bug Bounty / Red Team**, o OWASP Amass atua como a **fundação de descoberta de ativos (Camada de Grafo EASM)** que alimenta os scanners de protocolo e vulnerabilidade da ProjectDiscovery.

## Por que importa
O fluxo de trabalho canônico combina: **(1)** descoberta horizontal de ASNs e domínios raiz (`amass intel`); **(2)** enumeração profunda e persistência no banco de grafo (`amass enum -dir /cases/easm/amass_db -df roots.txt`); **(3)** extração limpa apenas dos FQDNs resolvidos (`oam_subs -names -dir /cases/easm/amass_db`); **(4)** sondagem HTTP/TLS ativa com **`httpx`**; e **(5)** varredura de vulnerabilidades e exposições com **`nuclei`**!

## Como funciona
Quando executado via container oficial Docker (`caffix/amass:latest`), conforme instrui o `doc/user_guide.md`, monte sempre o volume persistente **`-v /cases/easm/amass_db:/.config/amass/`** para que o banco de grafo e os arquivos `config.yaml`/`datasources.yaml` sobrevivam entre as execuções do container.

## Exemplo
```bash
# Pipeline completo de EASM: extrair todos os FQDNs validados do banco do Amass e alimentar o httpx e o nuclei
oam_subs -names -dir /cases/easm/amass_db -d exemplo.com.br \
  | httpx -silent -status-code -title -tech-detect -o /cases/easm/live_web_assets.txt
```

## Limites e trade-offs
Ao combinar `amass` e `subfinder` na mesma arquitetura de EASM, uma prática comum é usar o **`subfinder`** para varreduras rápidas de minutos em pipelines de CI/CD e rodar o **`amass enum`** em jobs agendados diários/semanais para manter o grafo completo OAM (incluindo ASNs, CIDRs, Reverse Whois e permutações recursivas) atualizado.

## Como verificar
Verifique que o volume Docker montado em `/.config/amass/` contém o banco de grafo atualizado após cada execução.

## Conexões
- [[amass-visualizacao-topologia-rede-oam-viz-d3-maltego-gexf]] — Veja também: OWASP Amass (`oam_viz` / `amass viz`): Exportação do Grafo de Superfície de Ataque para **D3.js HTML Interativo (`-d3`)**, **Gephi (`-gexf`)**, **Graphviz (`-dot`)** e **Maltego**.
- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — Referência cruzada direta com amass-arquitetura-easm-owasp-open-asset-model-oam-grafo.
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — Referência cruzada direta com amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db.

## Fontes
- [OWASP Amass Official GitHub — In-Depth Attack Surface Mapping & Asset Discovery](https://raw.githubusercontent.com/owasp-amass/amass/master/README.md) — documentação oficial do projeto OWASP Amass e sua arquitetura de grafo baseada no Open Asset Model (OAM); consultado em 2026-10-03.
- [OWASP Amass Official Users' Guide — intel, enum, db, Modes & Configuration](https://raw.githubusercontent.com/owasp-amass/amass/master/doc/user_guide.md) — guia completo do usuário do OWASP Amass cobrindo subcomandos intel/enum/db, força bruta recursiva, alterações e fontes de dados; consultado em 2026-10-03.
- [Go Package Documentation — github.com/owasp-amass/amass/v4](https://pkg.go.dev/github.com/owasp-amass/amass/v4) — documentação técnica da API e arquitetura do OWASP Amass v4; consultado em 2026-10-03.
